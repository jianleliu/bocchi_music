from PySide6.QtWidgets import QMessageBox
from pytube import YouTube, Playlist
from re import findall, compile
from configparser import ConfigParser
from config.default_parameters import INI_FILE_PATH
from config.sections import SECTION_PAGE_DOWNLOAD, SECTION_SETTINGS_TAB_1
from config.keys import (KEY_CHECK_AUDIO_ONLY, KEY_CHECK_INCLUDE_THUMBNAIL,
                         KEY_CHECK_USE_DEFAULT_PATH, KEY_DIR_PLAYLIST_DOWNLOAD, KEY_DIR_TRACK_DOWNLOAD)
import os

config = ConfigParser()
config.read(INI_FILE_PATH)

dir_song = None
dir_playlist = None
check_audio_only = None
check_use_default_path = None
check_include_thumnnail = None


def handle_download_track(window, url):
    # find if it's a playlist, song, or song in a playlist
    read_config_ini()
    is_song = findall(r'watch\?v=', url)
    is_playlist = findall(r'list=', url)
    print(f'song: {is_song}, playlist: {is_playlist}')

    if is_song and is_playlist:
        # ask user if want to download song or playlist
        msg_box = QMessageBox(window.window())
        msg_box.setWindowTitle('Choose an option')
        msg_box.setText(
            'This url contains a song inside a playlist, would you like to download the playlist or the song.')
        btn_song = msg_box.addButton('Song', QMessageBox.AcceptRole)
        btn_playlist = msg_box.addButton('Playlist', QMessageBox.AcceptRole)
        btn_cancel = msg_box.addButton('Cancel', QMessageBox.RejectRole)
        msg_box.exec_()
        print(f'dir_song: {dir_song} audio only: {check_audio_only}')
        if msg_box.clickedButton() == btn_song:
            print('btn_song')
            download_mp4(url, directory=dir_song, audio_only=check_audio_only)
        elif msg_box.clickedButton() == btn_playlist:
            download_playlist()
        
        return
    else:
        download_mp4(url, directory=dir_song, audio_only=check_audio_only)


def read_config_ini():
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


def download_mp4(video_url, directory=os.getcwd(), audio_only=True):
    print(f'url: {video_url} directory: {directory}')
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=audio_only).first()
    stream.download(output_path=directory)

    file_path = stream.get_file_path()
    return file_path


def download_playlist(url, directory=os.getcwd()):
    pass
