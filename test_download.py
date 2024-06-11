from pytube import YouTube, Playlist
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

def download_mp4(video_url, directory=os.getcwd(), audio_only=True):
    print(f'url: {video_url} directory: {directory}')
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=audio_only).first()
    stream.download(output_path=directory)

    file_path = stream.get_file_path()
    return file_path

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
    
download_mp4( url, directory=dir_song, audio_only=False)