from config.default_parameters import INI_FILE_PATH, DIR_ROOT
from config.sections import SECTION_SETTINGS_TAB_1
from config.keys import *
from os import path, listdir
from configparser import ConfigParser

config = ConfigParser()

def generate_dict_song_entity() -> dict:
  config.read(INI_FILE_PATH)
  dict_song_entity = {}
  dir_song = config[SECTION_SETTINGS_TAB_1][KEY_DIR_TRACK_DOWNLOAD]

  if path.isdir(dir_song):
    for i, file in enumerate(listdir(dir_song)):
      if path.isfile(path.join(dir_song, file)):
        basename = path.basename(file)
        dict_song_entity.setdefault(i, {
          KEY_DICT_SONG_ENTITY_BASENAME: basename,
          KEY_DICT_SONG_ENTITY_TITLE: path.splitext(basename)[0],
        })
  return dict_song_entity