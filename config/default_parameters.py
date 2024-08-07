"""Constant file for default parameters."""
import os

from .keys import (KEY_CHECK_AUDIO_ONLY, KEY_CHECK_INCLUDE_THUMBNAIL,
                   KEY_CHECK_USE_DEFAULT_PATH, KEY_DIR_PLAYLIST_DOWNLOAD,
                   KEY_DIR_TRACK_DOWNLOAD)
from .sections import SECTION_PAGE_DOWNLOAD, SECTION_SETTINGS_TAB_1

DIR_ROOT = os.path.dirname(os.path.dirname(__file__))

# settings page
DEFAULT_TRACK_DOWNLOAD_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'song')
DEFAULT_PLAYLIST_DOWNLOAD_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'song')

# download page
DEFAULT_CHECK_AUDIO_ONLY = False
DEFAULT_CHECK_USE_DEFAULT_PATH = True
DEFAULT_CHECK_INCLUDE_THUMBNAIL = True
DEFAULT_DOWNLOAD_FORMAT = '.mp4'
# ini file
INI_FILE_PATH = os.path.join(os.path.join(DIR_ROOT, 'config'), 'config.ini')
DEFAULT_INI_DICT = {
    SECTION_SETTINGS_TAB_1: {
        KEY_DIR_TRACK_DOWNLOAD: DEFAULT_TRACK_DOWNLOAD_DIR,
        KEY_DIR_PLAYLIST_DOWNLOAD: DEFAULT_PLAYLIST_DOWNLOAD_DIR,
    },
    SECTION_PAGE_DOWNLOAD: {
        KEY_CHECK_AUDIO_ONLY: DEFAULT_CHECK_AUDIO_ONLY,
        KEY_CHECK_USE_DEFAULT_PATH: DEFAULT_CHECK_USE_DEFAULT_PATH,
        KEY_CHECK_INCLUDE_THUMBNAIL: DEFAULT_CHECK_INCLUDE_THUMBNAIL,
    },
}
DEFAULT_ENCODING = 'utf-8'

# dict_song_entity

SONG_ENTITY_ARTIST = 'Artist'


# playBar
DEFAULT_BACKWARD_LENGTH = 10 * 1000  # in ms
DEFAULT_FORWARD_LENGTH = 10 * 1000  # in ms
DEFAULT_SPEED_BOCCHI_ROTATION = 2 # angle degree
DEFAULT_INTERVAL_BOCCHI_ROTATION = 50 # in ms

# media player
DEFAULT_LOOPS = - 1  # loops

# other
DEFAULT_PLAY_ORDER = -1  # index of DEFAULT_LIST_PLAY_ORDER
DEAFULT_PLAY_ORDER_LOOPS = -1
DEFAULT_PLAY_ORDER_CYCLE = 0
DEFAULT_PLAY_ORDER_SHUFFLE = 1
DEFAULT_LIST_PLAY_ORDER = [DEAFULT_PLAY_ORDER_LOOPS, DEFAULT_PLAY_ORDER_CYCLE,
                           DEFAULT_PLAY_ORDER_SHUFFLE]  # -1: loops, 0: cycle, 1: shuffle

# pages object name

DEFAULT_PAGE_DOWNLOAD_NAME = 'page_download'
DEFAULT_PAGE_HOME_NAME = 'page_home'
DEFAULT_PAGE_LIBRARY_NAME = 'page_library'
DEFAULT_PAGE_PLAYLIST_NAME = 'page_playlist'
DEFAULT_PAGE_SETTINGS_NAME =  'page_settings'
