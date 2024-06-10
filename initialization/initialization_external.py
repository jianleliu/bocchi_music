from os import path, mkdir
from configparser import ConfigParser
from config.default_parameters import INI_FILE_PATH, DEFAULT_INI_DICT, DEFAULT_TRACK_DOWNLOAD_DIR

DIR_ROOT = path.dirname(path.dirname(__file__))


def initialize_external():
    """This is the api for all other initialization functions.
    """
    initialize_dir_song()
    initialize_config_ini()


def initialize_config_ini():
    path_ini = path.join(path.join(DIR_ROOT, 'config'), 'config.ini')

    if not path.exists(path_ini):
        config = ConfigParser()
        config.read_dict(DEFAULT_INI_DICT)
        with open(INI_FILE_PATH, 'w') as f:
            config.write(f)


def initialize_dir_song():
    if not path.exists(DEFAULT_TRACK_DOWNLOAD_DIR):
        mkdir(DEFAULT_TRACK_DOWNLOAD_DIR)
