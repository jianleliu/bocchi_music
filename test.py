from os import path, walk, listdir
from config.keys import *
from config.default_parameters import *


def populate_song_entity_all(root_dir: str, extensions: list):
    """
    Recursively find songs with specified extensions starting from root_dir.

    Args:
    - root_dir (str): Root directory path to start searching.
    - extensions (list): List of file extensions (e.g., ['.mp3', '.mp4']).

    Returns:
    - dict: A dictionary containing information about found files.
      Keys are 'row', where each value is a dictionary with KEY_DICT_SONG_ENTITY_BASENAME 
      and KEY_DICT_SONG_ENTITY_TITLE.
    """
    result = {}
    seen_files = []
    # Validate root directory
    if not path.isdir(root_dir):
        raise ValueError(f"Root directory '{
                         root_dir}' does not exist or is not a valid directory.")

    index = 0  # Start index for results

    for root, _, files in walk(root_dir):
        for file in files:
            
            _, ext = path.splitext(file)
            if ext.lower() in extensions:
                full_path = path.join(root, file)
                relative_path = path.relpath(full_path, start=root_dir)
                filename_without_ext = path.splitext(file)[0]
                print(relative_path)
                # Check if the filename has already been added
                if filename_without_ext not in seen_files:
                    result.setdefault(index, {
                        KEY_DICT_SONG_ENTITY_BASENAME: relative_path,
                        KEY_DICT_SONG_ENTITY_TITLE: filename_without_ext,
                    })
                    seen_files.append(filename_without_ext)
                    index += 1

    return result
