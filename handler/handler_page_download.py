"""handler for download page."""

import logging
import os
import re
from configparser import ConfigParser
from pathlib import Path
from re import findall

from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal
from PySide6.QtWidgets import QMessageBox, QFrame
from pytube import Playlist, YouTube
from pytube.innertube import _default_clients

from config.default_parameters import (DEFAULT_CHECK_AUDIO_ONLY,
                                       DEFAULT_DOWNLOAD_FORMAT,
                                       DEFAULT_ENCODING, INI_FILE_PATH)
from config.keys import (KEY_CHECK_AUDIO_ONLY, KEY_CHECK_INCLUDE_THUMBNAIL,
                         KEY_CHECK_USE_DEFAULT_PATH,
                         KEY_DICT_SONG_ENTITY_BASENAME,
                         KEY_DICT_SONG_ENTITY_TITLE, KEY_DIR_PLAYLIST_DOWNLOAD,
                         KEY_DIR_TRACK_DOWNLOAD)
from config.sections import SECTION_PAGE_DOWNLOAD, SECTION_SETTINGS_TAB_1
from session.session_data import session_data

logger = logging.getLogger(__name__)

# needed to bypass age restriction
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

config = ConfigParser()
config.read(INI_FILE_PATH)

DIR_SONG = None
DIR_PLAYLIST = None
CHECK_AUDIO_ONLY = None
CHECK_USE_DEFAULT_PATH = None
CHECK_INCLUDE_THUMBNAIL = None

# thread
thread = QThreadPool()
num_total_track = 0
num_track_downloaded = 0
connect_to_result_slot = None

class SignalWorkerDownload(QObject):
    """signal for download track worker instance (thread) to
    communicate with handler in main thread.
    """
    signal_result_ready = Signal(str)


class _WorkerDownload(QRunnable):
    """worker thread to download track.

    Args:
        QRunnable (_type_): inheritance.
    """
    signal_manager = SignalWorkerDownload()

    def __init__(self, video_url: str, directory: str = os.getcwd(),
                 audio_only: bool = DEFAULT_CHECK_AUDIO_ONLY) -> None:
        """initialize variables.

        Args:
            video_url (str): youtube url
            directory (str, optional): absolute path, Defaults to os.getcwd().
            audio_only (bool, optional): boolean,
                Defaults to DEFAULT_CHECK_AUDIO_ONLY.
        """
        super().__init__()
        # self.callback = callback
        self.video_url = video_url
        self.directory = directory
        self.audio_only = audio_only

    def run(self) -> None:
        """entry point of worker thread
        """
        file_path = self._download_mp4(
            self.video_url, self.directory, self.audio_only)
        # emit signal to update status box
        self.signal_manager.signal_result_ready.emit(file_path)

    def _download_mp4(self, video_url: str, directory: str = os.getcwd(),
                      audio_only: bool = DEFAULT_CHECK_AUDIO_ONLY) -> str:
        """download from youtube using pytube library.

        Args:
            video_url (str): youtube url
            directory (str, optional): absolute path. Defaults to os.getcwd().
            audio_only (bool, optional): bool. Defaults to DEFAULT_CHECK_AUDIO_ONLY.

        Returns:
            str: absolute path of the downloaded file.
        """
        logger.info('downloading song')

        yt = YouTube(video_url)
        # download audio only or highest resolution video
        stream = yt.streams.filter(only_audio=audio_only).first(
        ) if audio_only else yt.streams.get_highest_resolution()

        file_name = f'{safe_filename(yt.title)}{DEFAULT_DOWNLOAD_FORMAT}'
        stream.download(output_path=directory, filename=file_name)

        file_path = stream.get_file_path()

        logger.info('Downloaded at %s', file_path)

        return file_path


def handle_download_track(page_download: QFrame, url: str,
                          signal_repopulate_table_song: Signal) -> None:
    """handler when the download button in the download page is clicked.

    Args:
        page_download (DownloadPage): DownloadPage instance, initialized in MainWindow.
        url (str): youtube url.
        signal_repopulate_table_song (Signal): Signal used to repopulate song table
            in page_library.
    """

    global num_total_track, connect_to_result_slot
    # _handle_btn_download_accessibility(page_download)

    # find if it's a playlist, song, or song in a playlist
    logger.info('handler called')
    _read_config_ini()
    is_song = findall(r'watch\?v=', url)
    is_playlist = findall(r'list=', url)
    logger.info('song: %s, playlist: %s', is_song, is_playlist)

    # msg box will show either download thread exits or there's an error.
    msg_box = QMessageBox(page_download.window())
    msg_box.setWindowTitle('Choose an option')
    msg_box_finish = QMessageBox(page_download.window())
    msg_box_finish.setWindowTitle('Done')
    msg_box_finish.addButton('Done', QMessageBox.AcceptRole)

    if is_song and is_playlist:
        msg_box.setText(
            'This url contains a song inside a playlist,'
            'would you like to download the playlist or the song.')
        btn_song = msg_box.addButton('Song', QMessageBox.AcceptRole)
        btn_playlist = msg_box.addButton('Playlist', QMessageBox.AcceptRole)
        btn_cancel = msg_box.addButton('Cancel', QMessageBox.RejectRole)
        msg_box.exec_()

        logger.info('DIR_SONG: %s audio only: %s', DIR_SONG, CHECK_AUDIO_ONLY)

        if msg_box.clickedButton() == btn_song:
            try:
                handle_update_status_box(page_download, f'URL: {url} Found')
                worker = _WorkerDownload(
                    url, directory=DIR_SONG, audio_only=CHECK_AUDIO_ONLY)
                worker.signal_manager.signal_result_ready.disconnect()
                worker.signal_manager.signal_result_ready.connect(
                    lambda file_path: _handle_worker_download_result(page_download, file_path, msg_box_finish=msg_box_finish))
                thread.start(worker)
                num_total_track += 1
                _handle_update_progress_bar(page_download)
            except Exception as error:
                msg_box_finish.setText(f'An error has occurred: {error}')
                logger.error('Occurred while downloading song: %s', error)
                msg_box_finish.exec_()

        # else download the entire playlist
        elif msg_box.clickedButton() == btn_playlist:
            try:
                _download_playlist(page_download, url, DIR_PLAYLIST,
                                   audio_only=CHECK_AUDIO_ONLY)
                logger.info(DIR_PLAYLIST)
            except Exception as error:
                msg_box_finish.setText(f'An error has occurred: {error}')
                logger.error('Occurred while downloading song: %s', error)
                msg_box_finish.exec_()
        return

    # if url is a song, download it
    elif is_song:
        msg_box.setText('Download this song?')
        btn_confirm = msg_box.addButton('Confirm', QMessageBox.AcceptRole)
        btn_cancel = msg_box.addButton('Cancel', QMessageBox.RejectRole)
        msg_box.exec_()

        if msg_box.clickedButton() == btn_confirm:
            try:
                handle_update_status_box(page_download, f'{num_total_track} URL: {url} Found')

                worker = _WorkerDownload(
                    url, directory=DIR_SONG, audio_only=CHECK_AUDIO_ONLY)
                worker.signal_manager.signal_result_ready.disconnect()
                worker.signal_manager.signal_result_ready.connect(lambda file_path: _handle_worker_download_result(
                    page_download, file_path, msg_box_finish=msg_box_finish))
                thread.start(worker)
                num_total_track += 1
                _handle_update_progress_bar(page_download)
            except Exception as error:
                msg_box_finish.setText(f'An error has occurred: {error}')
                logger.error('Occurred while downloading song: %s', error)
                msg_box_finish.exec_()

    # if its a playlist, download all of it.
    elif is_playlist:
        msg_box.setText('Download this playlist?')
        btn_confirm = msg_box.addButton('Confirm', QMessageBox.AcceptRole)
        msg_box.exec_()

        if msg_box.clickedButton() == btn_confirm:
            try:
                _download_playlist(page_download, url, DIR_PLAYLIST,
                                   audio_only=CHECK_AUDIO_ONLY)
                msg_box_finish.setText('Successful!')
                msg_box_finish.exec_()
            except Exception as error:
                msg_box_finish.setText(f'An error has occurred: {error}')
                logger.error('Occurred while downloading playlist: %s', error)
                msg_box_finish.exec_()

        logger.info(DIR_PLAYLIST)

    else:
        handle_update_status_box(page_download, f'Invalid URL: {url}')
        msg_box_finish.setText(f'Invalid URL: {url}')
        msg_box_finish.exec_()

    # emit signal to update table_song
    signal_repopulate_table_song.emit()
    logger.info('handler ended')


def _handle_btn_download_accessibility(page_download: QFrame) -> None:
    """disable download btn when downloading.

    Args:
        page_download (QFrame): DownloadPage instance, initialized in MainWindow.
    """
    page_download.btn_download.setEnabled(not page_download.btn_download.isEnabled)


def _handle_update_progress_bar(page_download: QFrame) -> None:
    """update progress bar value.

    Args:
        page_download (QFrame): DownloadPage instance, initialized in MainWindow.
    """
    logger.info('%s/%s', num_track_downloaded, num_total_track)
    page_download.progress_bar.setRange(0, num_total_track)
    page_download.progress_bar.setValue(num_track_downloaded)
    page_download.progress_bar.setFormat(f'{num_track_downloaded}/{num_total_track}')


def handle_check_audio_only(is_checked: bool) -> None:
    """when audio_only checkbox is clicked in download page.

    Args:
        is_checked (bool): status
    """
    logger.info('handler called')
    config[SECTION_PAGE_DOWNLOAD][KEY_CHECK_AUDIO_ONLY] = str(is_checked)
    with open(INI_FILE_PATH, 'w', encoding=DEFAULT_ENCODING) as f:
        config.write(f)
    logger.info('handler ended')


def handle_check_use_default_path(is_checked: bool) -> None:
    """when default_path checkbox is clicked in download page.

    Args:
        is_checked (bool): status.
    """
    logger.info('handler called')
    config[SECTION_PAGE_DOWNLOAD][KEY_CHECK_USE_DEFAULT_PATH] = str(is_checked)
    with open(INI_FILE_PATH, 'w', encoding=DEFAULT_ENCODING) as f:
        config.write(f)
    logger.info('handler ended')


def handle_check_include_thumbnail(is_checked: bool) -> None:
    """when include thumbnail checkbox is clicked in download page.

    Args:
        is_checked (bool): status.
    """
    logger.info('handler called')
    config[SECTION_PAGE_DOWNLOAD][KEY_CHECK_INCLUDE_THUMBNAIL] = str(
        is_checked)
    with open(INI_FILE_PATH, 'w', encoding='utf-8') as f:
        config.write(f)
    logger.info('handler ended')


def handle_update_status_box(page_download: QFrame, message: str) -> None:
    """append message to status box in download page.

    Args:
        page_download (QFrame): ui, download page.
        message (str): message to be appended.
    """
    page_download.status_box.append(f'{message}\n')


def _read_config_ini() -> None:
    """read config.ini file and update global variables.
    """
    global DIR_SONG, DIR_PLAYLIST, CHECK_AUDIO_ONLY, CHECK_INCLUDE_THUMBNAIL, CHECK_USE_DEFAULT_PATH
    config.read(INI_FILE_PATH)

    DIR_SONG = config[SECTION_SETTINGS_TAB_1][KEY_DIR_TRACK_DOWNLOAD]
    DIR_PLAYLIST = config[SECTION_SETTINGS_TAB_1][KEY_DIR_PLAYLIST_DOWNLOAD]
    CHECK_AUDIO_ONLY = config[SECTION_PAGE_DOWNLOAD].getboolean(
        KEY_CHECK_AUDIO_ONLY)
    CHECK_USE_DEFAULT_PATH = config[SECTION_PAGE_DOWNLOAD].getboolean(
        KEY_CHECK_USE_DEFAULT_PATH)
    CHECK_INCLUDE_THUMBNAIL = config[SECTION_PAGE_DOWNLOAD].getboolean(
        KEY_CHECK_INCLUDE_THUMBNAIL)


def _handle_worker_download_result(page_download: QFrame,
                                   file_path: str, msg_box_finish: QMessageBox = None) -> None:
    """handle when worker thread for downloading track finished.
    Will update dict_song_entity and append status_box in download page.

    Args:
        page_download (DownloadPage Instance): download page, ui instance, declared in MainWindow.
        file_path (str): absolute path of the file downloaded, emitted through the finished signal.
        msg_box_finish (QMessageBox, optional): popup to show finished downloading,
        Defaults to None.
    """

    global num_track_downloaded
    session_data.dict_song_entity.setdefault(len(session_data.dict_song_entity), {
        KEY_DICT_SONG_ENTITY_BASENAME: os.path.basename(file_path),
        KEY_DICT_SONG_ENTITY_TITLE: os.path.splitext(
            os.path.basename(file_path))[0]
    })
    handle_update_status_box(page_download, f'Downloaded at {file_path}')
    if msg_box_finish is not None:
        msg_box_finish.setText('Successful!')
        msg_box_finish.exec_()

    num_track_downloaded += 1
    logger.info('thread count: %s', thread.activeThreadCount())
    _handle_update_progress_bar(page_download)


def _download_playlist(
        page_download: QFrame, playlist_url: str, directory: str = os.getcwd(),
        audio_only: bool = DEFAULT_CHECK_AUDIO_ONLY) -> None:
    """download the entire youtube playlist

    Args:
        page_download (QFrame): download page, ui instance, declared in MainWindow.
        playlist_url (str): _description_
        directory (str, optional): _description_. Defaults to os.getcwd().
        audio_only (bool, optional): _description_. Defaults to DEFAULT_CHECK_AUDIO_ONLY.
    """
    logger.info('downloading playlist')
    playlist = Playlist(playlist_url)

    cleaned_playlist_title = None
    # bare except because playlist.title will throw error if
    # the playlist is a generated mix (temp playlist for a user only)
    try:
        cleaned_playlist_title = safe_filename(playlist.title)
    except:
        index = 0
        while True:
            dir_name = str(index)
            full_path = os.path.join(directory, dir_name)

            if not os.path.exists(full_path):
                break
            index += 1
        cleaned_playlist_title = str(index)

    dir_new_song = Path(directory).joinpath(cleaned_playlist_title)
    count = len(playlist.video_urls)

    handle_update_status_box(page_download, f'URLs Found: {count} in playlist {
        cleaned_playlist_title}')

    cleaned_list_filename = []

    # create a list of clenaed filenames within the playlist dir
    if not os.path.isdir(dir_new_song):
        os.mkdir(dir_new_song)

    for filename in os.listdir(dir_new_song):
        cleaned_list_filename.append(
            os.path.splitext(filename)[0])

    # check if the video already exists within the dir(cleaned filenames), download if not.
    for _, url in enumerate(playlist.video_urls):
        video_title = YouTube(url).title
        cleaned_video_title = safe_filename(video_title)
        song_path = Path(dir_new_song).joinpath(
            f'{cleaned_video_title}.{DEFAULT_DOWNLOAD_FORMAT}')
        song_exists = cleaned_video_title in cleaned_list_filename

        if song_exists:
            logger.info('exists: %s title: %s', song_exists, cleaned_video_title)
            handle_update_status_box(page_download,
                                     f'Skipping: file {video_title} found as {song_path}')
            continue

        worker = _WorkerDownload(
            url, directory=dir_new_song, audio_only=audio_only)
        worker.signal_manager.signal_result_ready.disconnect()
        worker.signal_manager.signal_result_ready.connect(
            lambda file_path: _handle_worker_download_result(page_download, file_path))
        thread.start(worker)
        global num_total_track
        num_total_track += 1
        _handle_update_progress_bar(page_download)
        # _download_mp4(page_download, url, directory=dir_new_song, audio_only=audio_only)


def safe_filename(s: str, max_length: int = 255) -> str:
    """Sanitize a string making it safe to use as a filename.

    This function was based off the limitations outlined here:
    https://en.wikipedia.org/wiki/Filename.

    :param str s:
        A string to make safe for use as a file name.
    :param int max_length:
        The maximum filename character length.
    :rtype: str
    :returns:
        A sanitized string.
    """
    logger.info('sanitize filename')
    # Characters in range 0-31 (0x00-0x1F) are not allowed in ntfs filenames.
    ntfs_characters = [chr(i) for i in range(0, 31)]
    characters = [
        r'"',
        r"\#",
        r"\$",
        r"\%",
        r"'",
        r"\*",
        r"\,",
        r"\.",
        r"\/",
        r"\:",
        r'"',
        r"\;",
        r"\<",
        r"\>",
        r"\?",
        r"\\",
        r"\^",
        r"\|",
        r"\~",
        r"\\\\",
    ]
    pattern = "|".join(ntfs_characters + characters)
    regex = re.compile(pattern, re.UNICODE)
    filename = regex.sub("", s)
    return filename[:max_length].rsplit(" ", 0)[0]
