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
    _read_config_ini()
    is_song = findall(r'watch\?v=', url)
    is_playlist = findall(r'list=', url)
    print(f'song: {is_song}, playlist: {is_playlist}')

    if is_song and is_playlist:
        # ask user if want to download song or playlist
        msg_box = QMessageBox(page_download.window())
        msg_box.setWindowTitle('Choose an option')
        msg_box.setText(
            'This url contains a song inside a playlist, would you like to download the playlist or the song.')
        btn_song = msg_box.addButton('Song', QMessageBox.AcceptRole)
        btn_playlist = msg_box.addButton('Playlist', QMessageBox.AcceptRole)
        btn_cancel = msg_box.addButton('Cancel', QMessageBox.RejectRole)
        msg_box.exec_()
        print(f'dir_song: {dir_song} audio only: {check_audio_only}')
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
            print(dir_playlist)
        return
    # if url is a song, download it
    elif is_song:
        file_path = _download_mp4(
            url, directory=dir_song, audio_only=check_audio_only)
        session_data.dict_song_entity.setdefault(len(session_data.dict_song_entity), {
            KEY_DICT_SONG_ENTITY_BASENAME: os.path.basename(file_path),
            KEY_DICT_SONG_ENTITY_TITLE: os.path.splitext(
                os.path.basename(file_path))[0]
        })
    # if its a playlist, download all of it.
    elif is_playlist:
        _download_playlist(page_download, url, dir_playlist,
                           audio_only=check_audio_only)
        print(dir_playlist)
    else:
        page_download.update_status_box(f'Invalid URL: {url}')

    # emit signal to update table_song
    signal_repopulate_table_song.emit()


def handle_check_audio_only(is_checked):
    config[SECTION_PAGE_DOWNLOAD][KEY_CHECK_AUDIO_ONLY] = str(is_checked)
    with open(INI_FILE_PATH, 'w') as f:
        config.write(f)


def handle_check_use_default_path(is_checked):
    config[SECTION_PAGE_DOWNLOAD][KEY_CHECK_USE_DEFAULT_PATH] = str(is_checked)
    with open(INI_FILE_PATH, 'w') as f:
        config.write(f)


def handle_check_include_thumbnail(is_checked):
    config[SECTION_PAGE_DOWNLOAD][KEY_CHECK_INCLUDE_THUMBNAIL] = str(
        is_checked)
    with open(INI_FILE_PATH, 'w') as f:
        config.write(f)


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
    page_download.update_status_box(f'URL: {video_url} Found')
    yt = YouTube(video_url)
    # download audio only or highest resolution video
    stream = yt.streams.filter(
        only_audio=audio_only) if audio_only else yt.streams.get_highest_resolution()
    file_name = f'{safe_filename(yt.title)}.{DEFAULT_DOWNLOAD_FORMAT}'
    stream.download(output_path=directory, filename=file_name)

    file_path = stream.get_file_path()

    page_download.update_status_box(f'Downloaded at {file_path}')
    
    print(f'Downloaded at {file_path}')
    
    return file_path


def _download_playlist(page_download, playlist_url, directory=os.getcwd(), audio_only=DEFAULT_CHECK_AUDIO_ONLY):
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
        
        print(f'exists: {song_exists} title: {cleaned_video_title}')
        if song_exists:
            page_download.update_status_box(
                f'Skipping: file {video_title} found as {song_path}')
            continue
        
        print('downloading', video_title)
        if i == 5:
            break
        _download_mp4(page_download, url, directory=dir_new_song, audio_only=audio_only)

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