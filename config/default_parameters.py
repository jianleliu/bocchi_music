import os
from .sections import SECTION_SETTINGS_TAB_1, SECTION_PAGE_DOWNLOAD
from .keys import (KEY_CHECK_AUDIO_ONLY, KEY_CHECK_INCLUDE_THUMBNAIL,
                  KEY_CHECK_USE_DEFAULT_PATH, KEY_DIR_PLAYLIST_DOWNLOAD, KEY_DIR_TRACK_DOWNLOAD)

dir_root = os.path.dirname(os.path.dirname(__file__))

# settings page
DEFAULT_TRACK_DOWNLOAD_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'song')
DEFAULT_PLAYLIST_DOWNLOAD_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'song')

# download page
DEFAULT_CHECK_AUDIO_ONLY = True
DEFAULT_CHECK_USE_DEFAULT_PATH = True
DEFAULT_CHECK_INCLUDE_THUMBNAIL = True

# ini file
INI_FILE_PATH = os.path.join(os.path.join(dir_root, 'config'), 'config.ini')
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