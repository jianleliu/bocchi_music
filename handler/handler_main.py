from PySide6.QtCore import (QUrl, QTime)
from PySide6.QtGui import (QPixmap)
from PySide6.QtWidgets import (QFrame, QGridLayout,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QTableWidget,
                               QTableWidgetItem, QStackedWidget)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer
from os import path
import time
import math
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
           f'{row}. { song_entity.get(KEY_DICT_SONG_ENTITY_TITLE, '')}'))
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
        print('play initial song')
        _play_song(main_window.widget_page_library.table_song,
                   state, main_window.dict_song_entity, row, player)
        return
    elif (state[KEY_DICT_PLAYER_STATES_STATE] == STATE_PAUSE) and (state[KEY_DICT_PLAYER_STATES_ROW] == row):
        print('continue song')
        _continue_song(main_window.widget_page_library.table_song,
                       state, main_window.dict_song_entity, row, player)
        return
    # pause current song
    if (state[KEY_DICT_PLAYER_STATES_STATE] == STATE_PLAY) and (state[KEY_DICT_PLAYER_STATES_ROW] == row):
        print('pause song')
        _pause_song(main_window.widget_page_library.table_song,
                    state, main_window.dict_song_entity, row, player)
    else:
        print('switch song')
        _switch_song(main_window.widget_page_library.table_song,
                     state, main_window.dict_song_entity, row, player)
    main_window.widget_page_library.btn_shuffle.setText(
        f'{state[KEY_DICT_PLAYER_STATES_STATE]}')


def handle_spinning_bocchi_clicked(widget_pageManger: QStackedWidget, widget_videoWidget: QVideoWidget):
    widget_pageManger.setHidden(not widget_pageManger.isHidden())
    widget_videoWidget.setHidden(not widget_videoWidget.isHidden())


def handle_track_paused(widget_playBar):
    # stop the spinning bocchi
    pass


def handle_track_played(widget_playBar: QFrame, position_current: int, duration: int, states: dict, song_entity: dict):
    # start the spinning bocchi
    # set label title
    
    duration_in_seconds = math.floor(duration/1000)
    position_current_in_seconds = math.floor(position_current/1000)
    formatted_current_time = QTime(0, 0, 0).addSecs(position_current_in_seconds).toString('mm:ss')
    formatted_end_time = QTime(0, 0, 0).addSecs(duration_in_seconds).toString('mm:ss')

    widget_playBar.slider_progress.setRange(0, duration_in_seconds)
    widget_playBar.slider_progress.setValue(position_current_in_seconds)
    widget_playBar.label_play_title.setText(
        song_entity[states[KEY_DICT_PLAYER_STATES_ROW]][KEY_DICT_SONG_ENTITY_TITLE])
    widget_playBar.label_current_timestamp.setText(formatted_current_time)
    widget_playBar.label_end_timestamp.setText(formatted_end_time)
    
    
def handle_track_position_changed(widget_playBar, position_current):
    position_current_in_seconds = math.floor(position_current/1000)
    formatted_current_time = QTime(0, 0, 0).addSecs(position_current_in_seconds).toString('mm:ss')
    
    widget_playBar.slider_progress.setValue(position_current_in_seconds)
    widget_playBar.label_current_timestamp.setText(formatted_current_time)
    
def handle_track_stopped():
    # pause the spinning bocchi
    #
    pass


def _play_song(table_song: QTableWidget, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PAUSE))
    table_song.setVerticalHeaderItem(row, icon)
    state[KEY_DICT_PLAYER_STATES_ROW] = row
    config.read(INI_FILE_PATH)

    # start audio player
    dir_song = config[SECTION_SETTINGS_TAB_1][KEY_DIR_TRACK_DOWNLOAD]
    file_path = path.join(
        dir_song, song_entity[row][KEY_DICT_SONG_ENTITY_BASENAME])
    player.setSource(QUrl.fromLocalFile(file_path))
    player.play()
    state[KEY_DICT_PLAYER_STATES_PATH] = file_path
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_PLAY


def _continue_song(table_song: QTableWidget, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    print('resume song')
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PAUSE))
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_PLAY
    table_song.setVerticalHeaderItem(row, icon)
    state[KEY_DICT_PLAYER_STATES_ROW] = row

    player.play()


def _pause_song(table_song: QTableWidget, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PLAY))
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_PAUSE
    table_song.setVerticalHeaderItem(row, icon)
    state[KEY_DICT_PLAYER_STATES_ROW] = row
    player.pause()
# will run IF a new song is going to be played WHILE there is a ongoing song.


def _switch_song(table_song: QTableWidget, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    #  current song
    print('switch song')
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PLAY))
    table_song.setVerticalHeaderItem(state[KEY_DICT_PLAYER_STATES_ROW], icon)
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_STOP
    # stop the current song
    player.stop()
    time.sleep(0.01)

    _play_song(table_song, state, song_entity, row, player)
