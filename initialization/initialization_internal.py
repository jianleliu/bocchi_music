from config.default_parameters import INI_FILE_PATH, DIR_ROOT
from config.sections import SECTION_SETTINGS_TAB_1
from config.keys import *
from os import path, listdir, walk
from configparser import ConfigParser
import logging

logger = logging.getLogger(__name__)
config = ConfigParser()


def generate_dict_song_entity() -> dict:
    logger.info('generating dict_song_entity...')
    config.read(INI_FILE_PATH)
    dict_song_entity = {}
    dir_song = config[SECTION_SETTINGS_TAB_1][KEY_DIR_TRACK_DOWNLOAD]

    count = 0
    if path.isdir(dir_song):
        for file in listdir(dir_song):
            if path.isfile(path.join(dir_song, file)):
                basename = path.basename(file)
                dict_song_entity.setdefault(count, {
                    KEY_DICT_SONG_ENTITY_BASENAME: basename,
                    KEY_DICT_SONG_ENTITY_TITLE: path.splitext(basename)[0],
                })
                count += 1
    logger.info(f'total songs found: {len(dict_song_entity)}')
    return dict_song_entity


def populate_song_entity_all(dir_song_root: str, dir_playlist_root: str, extensions: list):
    logger.info('populate dict_song_entity from library and all playlist...')
    '''
    Recursively find songs with specified extensions starting from root_dir.

    Args:
    - root_dir (str): Root directory path to start searching.
    - extensions (list): List of file extensions (e.g., ['.mp3', '.mp4']).

    Returns:
    - dict: A dictionary containing information about found files.
      Keys are 'row', where each value is a dictionary with KEY_DICT_SONG_ENTITY_BASENAME 
      and KEY_DICT_SONG_ENTITY_TITLE.
    '''
    result = {}
    seen_files = []
    # Validate root directory
    if not path.isdir(dir_song_root):
        raise ValueError(f'Root directory {
                         dir_song_root} does not exist or is not a valid directory.')

    index = 0  # Start index for results

    for root, _, files in walk(dir_song_root):
        for file in files:
            
            _, ext = path.splitext(file)
            if ext.lower() in extensions:
                full_path = path.join(root, file)
                relative_path = path.relpath(full_path, start=dir_song_root)
                filename_without_ext = path.splitext(file)[0]
                # Check if the filename has already been added
                if filename_without_ext not in seen_files:
                    result.setdefault(index, {
                        KEY_DICT_SONG_ENTITY_BASENAME: relative_path,
                        KEY_DICT_SONG_ENTITY_TITLE: filename_without_ext,
                    })
                    seen_files.append(filename_without_ext)
                    index += 1

    for root, _, files in walk(dir_playlist_root):
        for file in files:
            
            _, ext = path.splitext(file)
            if ext.lower() in extensions:
                full_path = path.join(root, file)
                relative_path = path.relpath(full_path, start=dir_playlist_root)
                filename_without_ext = path.splitext(file)[0]
                # Check if the filename has already been added
                if filename_without_ext not in seen_files:
                    result.setdefault(index, {
                        KEY_DICT_SONG_ENTITY_BASENAME: relative_path,
                        KEY_DICT_SONG_ENTITY_TITLE: filename_without_ext,
                    })
                    seen_files.append(filename_without_ext)
                    index += 1
    
    logger.info(f'total songs found: {len(result)}')
    return result

