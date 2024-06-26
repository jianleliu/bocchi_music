from PySide6.QtWidgets import QMessageBox
from pytube import YouTube, Playlist
from pytube.innertube import _default_clients
from moviepy.editor import VideoFileClip, concatenate_videoclips, ImageClip
from re import findall, compile
import requests
from configparser import ConfigParser
from config.default_parameters import *
from config.sections import SECTION_PAGE_DOWNLOAD, SECTION_SETTINGS_TAB_1
from config.keys import *
from session.session_data import session_data
import os
from pathlib import Path
import re
import logging

logger = logging.getLogger(__name__)

# needed to bypass age restriction
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

config = ConfigParser()
config.read(INI_FILE_PATH)

dir_song = None
dir_playlist = None
check_audio_only = None
check_use_default_path = None


def handle_download_track(page_download, url, signal_repopulate_table_song):
    # find if it's a playlist, song, or song in a playlist
    logger.info('handler called')
    _read_config_ini()
    is_song = findall(r'watch\?v=', url)
    is_playlist = findall(r'list=', url)
    logger.info(f'song: {is_song}, playlist: {is_playlist}')

    msg_box = QMessageBox(page_download.window())
    msg_box.setWindowTitle('Choose an option')
    msg_box_finish = QMessageBox(page_download.window())
    msg_box_finish.setWindowTitle('Done')
    msg_box_finish.addButton('Done', QMessageBox.AcceptRole)

    if is_song and is_playlist:
        # ask user if want to download song or playlist
        # configure msg box
        msg_box.setText(
            'This url contains a song inside a playlist, would you like to download the playlist or the song.')
        btn_song = msg_box.addButton('Song', QMessageBox.AcceptRole)
        btn_playlist = msg_box.addButton('Playlist', QMessageBox.AcceptRole)
        btn_cancel = msg_box.addButton('Cancel', QMessageBox.RejectRole)
        msg_box.exec_()
        
        # log
        logger.info(f'dir_song: {dir_song} audio only: {check_audio_only}')
        
        # download signle file if user clicked btn_song
        if msg_box.clickedButton() == btn_song:
            file_path = _download_mp4(
                page_download, url, directory=dir_song, audio_only=check_audio_only)
            session_data.dict_song_entity.setdefault(len(session_data.dict_song_entity), {
                KEY_DICT_SONG_ENTITY_BASENAME: os.path.basename(file_path),
                KEY_DICT_SONG_ENTITY_TITLE: os.path.splitext(
                    os.path.basename(file_path))[0]
            })
            
        # else download the entire playlist
        elif msg_box.clickedButton() == btn_playlist:
            _download_playlist(page_download, url, dir_playlist,
                               audio_only=check_audio_only)
            logger.info(dir_playlist)
        return
    
    # if url is a song, download it
    elif is_song:
        msg_box.setText('Download this song?')
        btn_confirm = msg_box.addButton('Confirm', QMessageBox.AcceptRole)
        btn_cancel = msg_box.addButton('Cancel', QMessageBox.RejectRole)
        msg_box.exec_()

        if msg_box.clickedButton() == btn_confirm:
            try:
                file_path = _download_mp4(page_download, url, directory=dir_song, audio_only=check_audio_only) 
                session_data.dict_song_entity.setdefault(len(session_data.dict_song_entity), {
                        KEY_DICT_SONG_ENTITY_BASENAME: os.path.basename(file_path),
                        KEY_DICT_SONG_ENTITY_TITLE: os.path.splitext(
                            os.path.basename(file_path))[0]
                    })
                msg_box_finish.setText('Successful!')
                msg_box_finish.exec_()
                
            except Exception as error:
                msg_box_finish.setText(f'An error has occurred: {error}')
                logger.error(f'Occurred while downloading song: {error}')
                msg_box_finish.exec_()
                
    # if its a playlist, download all of it.
    elif is_playlist:
        msg_box.setText('Download this playlist?')
        btn_confirm = msg_box.addButton('Confirm', QMessageBox.AcceptRole)
        btn_cancel = msg_box.addButton('Cancel', QMessageBox.RejectRole)
        msg_box.exec_()
        
        if msg_box.clickedButton() == btn_confirm:
            try:
                _download_playlist(page_download, url, dir_playlist,
                               audio_only=check_audio_only)
                msg_box_finish.setText('Successful!')
                msg_box_finish.exec_()
            except Exception as error:
                msg_box_finish.setText(f'An error has occurred: {error}')
                logger.error(f'Occurred while downloading playlist: {error}')
                msg_box_finish.exec_()
                
        logger.info(dir_playlist)
        
    else:
        page_download.update_status_box(f'Invalid URL: {url}')
        msg_box_finish.setText(f'Invalid URL: {url}')
        msg_box_finish.exec_()

    # emit signal to update table_song
    signal_repopulate_table_song.emit()
    logger.info('handler ended')


def handle_check_audio_only(is_checked):
    logger.info('handler called')
    config[SECTION_PAGE_DOWNLOAD][KEY_CHECK_AUDIO_ONLY] = str(is_checked)
    with open(INI_FILE_PATH, 'w') as f:
        config.write(f)
    logger.info('handler ended')


def handle_check_use_default_path(is_checked):
    logger.info('handler called')
    config[SECTION_PAGE_DOWNLOAD][KEY_CHECK_USE_DEFAULT_PATH] = str(is_checked)
    with open(INI_FILE_PATH, 'w') as f:
        config.write(f)
    logger.info('handler ended')


def handle_check_include_thumbnail(is_checked):
    logger.info('handler called')
    config[SECTION_PAGE_DOWNLOAD][KEY_CHECK_INCLUDE_THUMBNAIL] = str(
        is_checked)
    with open(INI_FILE_PATH, 'w') as f:
        config.write(f)
    logger.info('handler ended')


def _read_config_ini():
    global dir_song, dir_playlist, check_audio_only, check_use_default_path, check_include_thumnnail
    config.read(INI_FILE_PATH)

    dir_song = config[SECTION_SETTINGS_TAB_1][KEY_DIR_TRACK_DOWNLOAD]
    dir_playlist = config[SECTION_SETTINGS_TAB_1][KEY_DIR_PLAYLIST_DOWNLOAD]
    check_audio_only = config[SECTION_PAGE_DOWNLOAD].getboolean(
        KEY_CHECK_AUDIO_ONLY)
    check_use_default_path = config[SECTION_PAGE_DOWNLOAD].getboolean(
        KEY_CHECK_USE_DEFAULT_PATH)
    check_include_thumnnail = config[SECTION_PAGE_DOWNLOAD].getboolean(
        KEY_CHECK_INCLUDE_THUMBNAIL)


def _download_mp4(page_download, video_url, directory=os.getcwd(), audio_only=DEFAULT_CHECK_AUDIO_ONLY):
    logger.info('downloading song')
    page_download.update_status_box(f'URL: {video_url} Found')
    yt = YouTube(video_url)
    # download audio only or highest resolution video
    stream = yt.streams.filter(
        only_audio=audio_only) if audio_only else yt.streams.get_highest_resolution()
    file_name = f'{safe_filename(yt.title)}{DEFAULT_DOWNLOAD_FORMAT}'
    stream.download(output_path=directory, filename=file_name)

    file_path = stream.get_file_path()

    page_download.update_status_box(f'Downloaded at {file_path}')

    logger.info(f'Downloaded at {file_path}')

    return file_path


def _download_playlist(page_download, playlist_url, directory=os.getcwd(), audio_only=DEFAULT_CHECK_AUDIO_ONLY):
    logger.info('downloading playlist')
    playlist = Playlist(playlist_url)
    cleaned_playlist_title = safe_filename(playlist.title)
    dir_new_song = Path(directory).joinpath(cleaned_playlist_title)
    count = len(playlist.video_urls)

    page_download.update_status_box(f'URLs Found: {count} in playlist {
                                    cleaned_playlist_title}')

    cleaned_list_filename = []

    # create a list of clenaed filenames within the playlist dir
    for filename in os.listdir(dir_new_song):
        cleaned_list_filename.append(
            os.path.splitext(filename)[0])

    # check if the video already exists within the dir(cleaned filenames), download if not.
    for i, url in enumerate(playlist.video_urls):
        video_title = YouTube(url).title
        cleaned_video_title = safe_filename(video_title)
        song_path = Path(dir_new_song).joinpath(
            f'{cleaned_video_title}.{DEFAULT_DOWNLOAD_FORMAT}')
        song_exists = cleaned_video_title in cleaned_list_filename

        if song_exists:
            logger.info(f'exists: {song_exists} title: {cleaned_video_title}')
            page_download.update_status_box(
                f'Skipping: file {video_title} found as {song_path}')
            continue

        _download_mp4(page_download, url, directory=dir_new_song,
                      audio_only=audio_only)


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
