from PySide6.QtCore import (QUrl)
from PySide6.QtGui import (QPixmap)
from PySide6.QtWidgets import (QFrame, QGridLayout,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QTableWidget,
                               QTableWidgetItem)
from PySide6.QtMultimedia import QMediaPlayer
from os import path
import time
from config.keys import *
from config.image_manager import *
from config.states import *
from config.sections import *
from config.default_parameters import *
from configparser import ConfigParser

config = ConfigParser()

def handle_populate_table_song(table_song: QTableWidgetItem, dict_song: dict) -> None:
    table_song.setRowCount(0)
    # prev_entities = len(table_song_entities)
    # table_song_entities = init_table_song(song_path, ['.mp4', '.mp3'])
    table_song.setRowCount(len(dict_song))

    index_row = 0
    for row, song_entity in dict_song.items():
        table_song.setItem(index_row, 0, QTableWidgetItem(
            song_entity.get(KEY_DICT_SONG_ENTITY_TITLE, '')))
        table_song.setItem(index_row, 1, QTableWidgetItem(
            song_entity.get(KEY_DICT_SONG_ENTITY_ARTIST, '')))
        table_song.setItem(index_row, 2, QTableWidgetItem(
            song_entity.get(KEY_DICT_SONG_ENTITY_LAST_PLAYED, '')))
        table_song.setItem(index_row, 3, QTableWidgetItem(
            song_entity.get(KEY_DICT_SONG_ENTITY_DATE_ADDED, '')))
        table_song.setItem(index_row, 4, QTableWidgetItem(
            song_entity.get(KEY_DICT_SONG_ENTITY_TIMES_PLAYED, '')))
        icon = QPixmap(path.join(DIR_IMAGE, IMAGE_PLAY))
        item = QTableWidgetItem()
        item.setIcon(icon)
        table_song.setVerticalHeaderItem(index_row, item)
        index_row += 1


def handle_player(main_window, row):
    state = main_window.dict_player_states
    player = main_window.widget_videoWidget.player
    # play a new song when no song is playing
    if not len(state):
        play_song(main_window.widget_page_library.table_song,
                  state, main_window.dict_song_entity, row, player)
        return
    elif (state[KEY_DICT_PLAYER_STATES_STATE] == STATE_PAUSE) and (state[KEY_DICT_PLAYER_STATES_ROW] == row):
        continue_song(main_window.widget_page_library.table_song,
                  state, main_window.dict_song_entity, row, player)
        return
    # pause current song
    if (state[KEY_DICT_PLAYER_STATES_STATE] == STATE_PLAY) and (state[KEY_DICT_PLAYER_STATES_ROW] == row):
        pause_song(main_window.widget_page_library.table_song,
                  state, main_window.dict_song_entity, row, player)
    else:
        switch_song(main_window.widget_page_library.table_song,
                  state, main_window.dict_song_entity, row, player)

# def stop_song(self, row, state):
#     self.audio_player.stop()
#     self.song_stopped.emit(row, state)
# play song
# continue song
# puase song
# switch song


def play_song(table_song: QTableWidget, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PAUSE))
    table_song.setVerticalHeaderItem(row, icon)
    state[KEY_DICT_PLAYER_STATES_ROW] = row
    config.read(INI_FILE_PATH)

    # start audio player
    dir_song = config[SECTION_SETTINGS_TAB_1][KEY_DIR_TRACK_DOWNLOAD]
    file_path = path.join(dir_song, song_entity[row][KEY_DICT_SONG_ENTITY_BASENAME])
    player.setSource(QUrl.fromLocalFile(file_path))
    player.play()
    state[KEY_DICT_PLAYER_STATES_PATH] = file_path
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_PLAY


def continue_song(table_song: QTableWidget, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PAUSE))
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_PLAY
    table_song.setVerticalHeaderItem(row, icon)
    state[KEY_DICT_PLAYER_STATES_ROW] = row
    player.play()


def pause_song(table_song: QTableWidget, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PLAY))
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_PAUSE
    table_song.setVerticalHeaderItem(row, icon)
    state[KEY_DICT_PLAYER_STATES_ROW] = -1
    player.pause()
# will run IF a new song is going to be played WHILE there is a ongoing song.


def switch_song(table_song: QTableWidget, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    #  current song
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PLAY))
    table_song.setVerticalHeaderItem(state[KEY_DICT_PLAYER_STATES_ROW], icon)
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_STOP
    # stop the current song
    player.stop()
    time.sleep(0.01)

    play_song(table_song, state, song_entity, row, player)