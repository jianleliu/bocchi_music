from PySide6.QtCore import (QUrl, QTime)
from PySide6.QtGui import (QPixmap, QIcon)
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
from random import randint

config = ConfigParser()


def handle_populate_table_song(table_song: QTableWidgetItem, dict_song: dict) -> None:
    table_song.setRowCount(0)
    # prev_entities = len(table_song_entities)
    # table_song_entities = init_table_song(song_path, ['.mp4', '.mp3'])
    table_song.setRowCount(len(dict_song))

    index_row = 0
    for row, song_entity in dict_song.items():
        table_song.setItem(index_row, 0, QTableWidgetItem(
            f'{row}. {song_entity.get(KEY_DICT_SONG_ENTITY_TITLE, '')}'))
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
    if 'row' not in state:
        _play_song(main_window.widget_page_library.table_song, main_window.widget_playBar,
                   state, main_window.dict_song_entity, row, player)
        return
    elif (state[KEY_DICT_PLAYER_STATES_STATE] == STATE_PAUSE) and (state[KEY_DICT_PLAYER_STATES_ROW] == row):
        print('continue song')
        _continue_song(main_window.widget_page_library.table_song, main_window.widget_playBar,
                       state, main_window.dict_song_entity, row, player)
        return
    # pause current song
    if (state[KEY_DICT_PLAYER_STATES_STATE] == STATE_PLAY) and (state[KEY_DICT_PLAYER_STATES_ROW] == row):
        print('pause song')
        _pause_song(main_window.widget_page_library.table_song, main_window.widget_playBar,
                    state, main_window.dict_song_entity, row, player)
    else:
        print('switch song')
        _switch_song(main_window.widget_page_library.table_song, main_window.widget_playBar,
                     state, main_window.dict_song_entity, row, player)


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
    formatted_current_time = QTime(0, 0, 0).addSecs(
        position_current_in_seconds).toString('mm:ss')
    formatted_end_time = QTime(0, 0, 0).addSecs(
        duration_in_seconds).toString('mm:ss')

    widget_playBar.slider_progress.setRange(0, duration_in_seconds)
    widget_playBar.slider_progress.setValue(position_current_in_seconds)
    widget_playBar.label_play_title.setText(
        song_entity[states[KEY_DICT_PLAYER_STATES_ROW]][KEY_DICT_SONG_ENTITY_TITLE])
    widget_playBar.label_current_timestamp.setText(formatted_current_time)
    widget_playBar.label_end_timestamp.setText(formatted_end_time)


def handle_track_position_changed(widget_playBar, position_current):
    position_current_in_seconds = math.floor(position_current/1000)
    formatted_current_time = QTime(0, 0, 0).addSecs(
        position_current_in_seconds).toString('mm:ss')

    widget_playBar.slider_progress.setValue(position_current_in_seconds)
    widget_playBar.label_current_timestamp.setText(formatted_current_time)


def handle_track_stopped():
    # pause the spinning bocchi
    #
    pass


def handle_backward(player):
    player.setPosition(player.position() - DEFAULT_BACKWARD_LENGTH)


def handle_forward(player):
    player.setPosition(player.position() + DEFAULT_FORWARD_LENGTH)


def handle_next(main_window, song_entity, state):
    config.read(INI_FILE_PATH)
    row_next = (state[KEY_DICT_PLAYER_STATES_ROW] + 1) % len(song_entity)
    if state[KEY_DICT_PLAYER_STATES_PLAY_ORDER] == DEFAULT_PLAY_ORDER_SHUFFLE:
        row_next = randint(0, len(song_entity) - 1)

    handle_player(main_window, row_next)


def handle_prev(main_window, song_entity, state):
    config.read(INI_FILE_PATH)
    row_prev = (state[KEY_DICT_PLAYER_STATES_ROW] - 1) % len(song_entity)
    if state[KEY_DICT_PLAYER_STATES_PLAY_ORDER] == DEFAULT_PLAY_ORDER_SHUFFLE:
        row_prev = randint(0, len(song_entity) - 1)
    handle_player(main_window, row_prev)


def handle_mute(player, btn_volume):
    is_muted = player.audioOutput().isMuted()
    player.audioOutput().setMuted(not is_muted)
    btn_volume.setIcon(QIcon(IMAGE_VOLUME if is_muted else IMAGE_MUTED))


def handle_slider_volume_changed(player, value):
    player.audioOutput().setVolume(value/100)


def handle_slider_progress_released(widget_videoWidget, widget_playBar, value):
    widget_videoWidget.player.setPosition(value * 1000)
    widget_videoWidget.signal_position_changed.connect(
        lambda position_current: handle_track_position_changed(widget_playBar, position_current))


def handle_slider_progress_pressed(widget_videoWidget):
    widget_videoWidget.signal_position_changed.disconnect()


def handle_play_order(btn_play_order, state):
    PLAY_ORDERS = [
        (DEAFULT_PLAY_ORDER_LOOPS, IMAGE_LOOP),
        (DEFAULT_PLAY_ORDER_CYCLE, IMAGE_CYCLE),
        (DEFAULT_PLAY_ORDER_SHUFFLE, IMAGE_SHUFFLE)
    ]

    # Get the current play order and find its index in the PLAY_ORDERS list
    current_play_order = state[KEY_DICT_PLAYER_STATES_PLAY_ORDER]
    current_index = [order[0]
                     for order in PLAY_ORDERS].index(current_play_order)

    # Calculate the index of the next play order
    next_index = (current_index + 1) % len(PLAY_ORDERS)

    # Get the next play order and its corresponding image path
    next_play_order, image_path = PLAY_ORDERS[next_index]

    # Update the state with the next play order
    state[KEY_DICT_PLAYER_STATES_PLAY_ORDER] = next_play_order

    # Set the icon of the button to the corresponding image path
    btn_play_order.setIcon(QIcon(image_path))


def handle_end_of_media(table_song, widget_playBar, player, state, song_entity):
    if state[KEY_DICT_PLAYER_STATES_PLAY_ORDER] == DEAFULT_PLAY_ORDER_LOOPS:
        _switch_song(table_song, widget_playBar, state, song_entity,
                     state[KEY_DICT_PLAYER_STATES_ROW], player)
    elif state[KEY_DICT_PLAYER_STATES_PLAY_ORDER] == DEFAULT_PLAY_ORDER_CYCLE:
        new_row = (state[KEY_DICT_PLAYER_STATES_ROW] + 1) % len(song_entity)
        _switch_song(table_song, widget_playBar, state, song_entity,
                     new_row, player)
    elif state[KEY_DICT_PLAYER_STATES_PLAY_ORDER] == DEFAULT_PLAY_ORDER_SHUFFLE:
        new_row = randint(0, len(song_entity) - 1)
        _switch_song(table_song, widget_playBar, state, song_entity,
                     new_row, player)


def _play_song(table_song: QTableWidget, widget_playBar, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PAUSE))
    widget_playBar.btn_play_pause.setIcon(QIcon(IMAGE_PAUSE))
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


def _continue_song(table_song: QTableWidget, widget_playBar, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    print('resume song')
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PAUSE))
    widget_playBar.btn_play_pause.setIcon(QIcon(IMAGE_PAUSE))
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_PLAY
    table_song.setVerticalHeaderItem(row, icon)
    state[KEY_DICT_PLAYER_STATES_ROW] = row

    player.play()


def _pause_song(table_song: QTableWidget, widget_playBar, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PLAY))
    widget_playBar.btn_play_pause.setIcon(QIcon(IMAGE_PLAY))
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_PAUSE
    table_song.setVerticalHeaderItem(row, icon)
    state[KEY_DICT_PLAYER_STATES_ROW] = row
    player.pause()
# will run IF a new song is going to be played WHILE there is a ongoing song.


def _switch_song(table_song: QTableWidget, widget_playBar, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    #  current song
    print('switch song')
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PLAY))
    widget_playBar.btn_play_pause.setIcon(QIcon(IMAGE_PLAY))
    table_song.setVerticalHeaderItem(state[KEY_DICT_PLAYER_STATES_ROW], icon)
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_STOP
    # stop the current song
    player.stop()
    time.sleep(0.01)

    _play_song(table_song, widget_playBar, state, song_entity, row, player)
