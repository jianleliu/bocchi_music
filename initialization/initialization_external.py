"""helper function: stores functions that will run when the app start."""
from configparser import ConfigParser
from os import mkdir, path

from config.default_parameters import (DEFAULT_ENCODING, DEFAULT_INI_DICT,
                                       DEFAULT_TRACK_DOWNLOAD_DIR,
                                       INI_FILE_PATH)

DIR_ROOT = path.dirname(path.dirname(__file__))


def initialize_external() -> None:
    """This is the api for all other initialization functions in the module.
    """
    initialize_dir_song()
    initialize_config_ini()


def initialize_config_ini() -> None:
    """create config/config.ini if not exists.
    """
    path_config = path.join(DIR_ROOT, 'config')
    if not path.exists(path_config):
        mkdir(path_config)
    path_ini = path.join(path_config, 'config.ini')

    if not path.exists(path_ini):
        config = ConfigParser()
        config.read_dict(DEFAULT_INI_DICT)
        with open(INI_FILE_PATH, 'w', encoding=DEFAULT_ENCODING) as f:
            config.write(f)


def initialize_dir_song():
    """create song/ if not exists.
    """
    if not path.exists(DEFAULT_TRACK_DOWNLOAD_DIR):
        mkdir(DEFAULT_TRACK_DOWNLOAD_DIR)
