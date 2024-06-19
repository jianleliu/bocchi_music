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
from config.sections import *
from config.default_parameters import *
from config.states import *
from session.session_data import session_data
from configparser import ConfigParser
from random import randint
from initialization.initialization_internal import *

config = ConfigParser()


def handle_populate_table_song(table_song: QTableWidget, dict_song: dict) -> None:
    # logger.info('handler called')
    table_song.setRowCount(0)
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
    # logger.info('handler ended')


def handle_btn_library_populate(table_song:  QTableWidget):
    # logger.info('handler called')
    config.read(INI_FILE_PATH)
    # read dirs
    dir_song_root = config[SECTION_SETTINGS_TAB_1][KEY_DIR_TRACK_DOWNLOAD]
    dir_playlist_root = config[SECTION_SETTINGS_TAB_1][KEY_DIR_PLAYLIST_DOWNLOAD]

    # recursively append songs
    session_data.dict_song_entity = populate_song_entity_all(
        dir_song_root, dir_playlist_root, [DEFAULT_DOWNLOAD_FORMAT])

    # populate table
    handle_populate_table_song(table_song, session_data.dict_song_entity)
    # logger.info('handler ended')


def handle_player(main_window, row):
    # logger.info('handler called')
    state = session_data.dict_player_states
    player = main_window.widget_videoWidget.player
    # play a new song when no song is playing
    if 'row' not in state:
        logger.info('play song')
        _play_song(main_window.widget_page_library.table_song, main_window.widget_playBar,
                   state, session_data.dict_song_entity, row, player)
        return
    elif (state[KEY_DICT_PLAYER_STATES_STATE] == STATE_PAUSE) and (state[KEY_DICT_PLAYER_STATES_ROW] == row):
        logger.info('continue song')
        _continue_song(main_window.widget_page_library.table_song, main_window.widget_playBar,
                       state, session_data.dict_song_entity, row, player)
        return
    # pause current song
    if (state[KEY_DICT_PLAYER_STATES_STATE] == STATE_PLAY) and (state[KEY_DICT_PLAYER_STATES_ROW] == row):
        logger.info('pause song')
        _pause_song(main_window.widget_page_library.table_song, main_window.widget_playBar,
                    state, session_data.dict_song_entity, row, player)
    else:
        logger.info('switch song')
        _switch_song(main_window.widget_page_library.table_song, main_window.widget_playBar,
                     state, session_data.dict_song_entity, row, player)
    # logger.info('handler ended')


def handle_spinning_bocchi_clicked(widget_pageManger: QStackedWidget, widget_videoWidget: QVideoWidget):
    # logger.info('handler called')
    widget_pageManger.setHidden(not widget_pageManger.isHidden())
    widget_videoWidget.setHidden(not widget_videoWidget.isHidden())
    # logger.info('handler ended')


def handle_track_paused(widget_playBar):
    # stop the spinning bocchi
    # logger.info('handler called')
    pass
    # logger.info('handler ended')


def handle_track_played(widget_playBar: QFrame, position_current: int, duration: int, states: dict, song_entity: dict):
    # logger.info('handler called')
    duration_in_seconds = math.floor(duration/1000)
    position_current_in_seconds = math.floor(position_current/1000)
    formatted_current_time = QTime(0, 0, 0).addSecs(
        position_current_in_seconds).toString('mm:ss')
    formatted_end_time = QTime(0, 0, 0).addSecs(
        duration_in_seconds).toString('mm:ss')

    logger.info('slider_progress set new range')
    widget_playBar.slider_progress.setRange(0, duration_in_seconds)
    widget_playBar.slider_progress.setValue(position_current_in_seconds)
    widget_playBar.label_play_title.setText(
        song_entity[states[KEY_DICT_PLAYER_STATES_ROW]][KEY_DICT_SONG_ENTITY_TITLE])
    widget_playBar.label_current_timestamp.setText(formatted_current_time)
    widget_playBar.label_end_timestamp.setText(formatted_end_time)
    # logger.info('handler ended')


def handle_track_position_changed(widget_playBar, position_current):
    # # logger.info('handler called')
    position_current_in_seconds = math.floor(position_current/1000)
    formatted_current_time = QTime(0, 0, 0).addSecs(
        position_current_in_seconds).toString('mm:ss')

    # logger.info('update slider_progress value')
    widget_playBar.slider_progress.setValue(position_current_in_seconds)
    widget_playBar.label_current_timestamp.setText(formatted_current_time)
    # # logger.info('handler ended')


def handle_track_stopped():
    # logger.info('handler called')
    # pause the spinning bocchi
    pass
    # logger.info('handler ended')


def handle_backward(player):
    # logger.info('handler called')
    player.setPosition(player.position() - DEFAULT_BACKWARD_LENGTH)
    # logger.info('handler ended')


def handle_forward(player):
    # logger.info('handler called')
    player.setPosition(player.position() + DEFAULT_FORWARD_LENGTH)
    # logger.info('handler ended')


def handle_next(main_window, song_entity, state):
    # logger.info('handler called')
    config.read(INI_FILE_PATH)
    row_next = (state[KEY_DICT_PLAYER_STATES_ROW] + 1) % len(song_entity)
    if state[KEY_DICT_PLAYER_STATES_PLAY_ORDER] == DEFAULT_PLAY_ORDER_SHUFFLE:
        row_next = randint(0, len(song_entity) - 1)

    handle_player(main_window, row_next)
    # logger.info('handler ended')


def handle_prev(main_window, song_entity, state):
    # logger.info('handler called')
    config.read(INI_FILE_PATH)
    row_prev = (state[KEY_DICT_PLAYER_STATES_ROW] - 1) % len(song_entity)
    if state[KEY_DICT_PLAYER_STATES_PLAY_ORDER] == DEFAULT_PLAY_ORDER_SHUFFLE:
        row_prev = randint(0, len(song_entity) - 1)
    handle_player(main_window, row_prev)
    # logger.info('handler ended')


def handle_mute(player, btn_volume):
    # logger.info('handler called')
    is_muted = player.audioOutput().isMuted()
    player.audioOutput().setMuted(not is_muted)
    btn_volume.setIcon(QIcon(IMAGE_VOLUME if is_muted else IMAGE_MUTED))
    # logger.info('handler ended')


def handle_slider_volume_changed(player, value):
    # logger.info('handler called')
    logger.info('update volume')
    player.audioOutput().setVolume(value/100)
    # logger.info('handler ended')


def handle_slider_progress_released(widget_videoWidget, widget_playBar, value):
    # logger.info('handler called')
    widget_videoWidget.player.setPosition(value * 1000)
    widget_videoWidget.signal_position_changed.connect(
        lambda position_current: handle_track_position_changed(widget_playBar, position_current))
    # logger.info('handler ended')


def handle_slider_progress_pressed(widget_videoWidget):
    # logger.info('handler called')
    widget_videoWidget.signal_position_changed.disconnect()
    # logger.info('handler ended')


def handle_play_order(btn_play_order, state):
    # logger.info('handler called')
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
    # logger.info('handler ended')


def handle_end_of_media(table_song, widget_playBar, player, state, song_entity):
    # logger.info('handler called')
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
    # logger.info('handler ended')


def _play_song(table_song: QTableWidget, widget_playBar, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    # update table_song icon
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PAUSE))
    table_song.setVerticalHeaderItem(row, icon)

    # update playbar
    widget_playBar.btn_play_pause.setIcon(QIcon(IMAGE_PAUSE))

    # read value
    state[KEY_DICT_PLAYER_STATES_ROW] = row
    config.read(INI_FILE_PATH)

    # start audio player
    dir_song = config[SECTION_SETTINGS_TAB_1][KEY_DIR_TRACK_DOWNLOAD]
    file_path = path.join(
        dir_song, song_entity[row][KEY_DICT_SONG_ENTITY_BASENAME])
    logger.info('set source')
    player.setSource(QUrl.fromLocalFile(file_path))
    logger.info('play from source')
    player.play()

    # update state values
    state[KEY_DICT_PLAYER_STATES_PATH] = file_path
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_PLAY


def _continue_song(table_song: QTableWidget, widget_playBar, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    # update table_song icon
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PAUSE))
    table_song.setVerticalHeaderItem(row, icon)

    # update playbar
    widget_playBar.btn_play_pause.setIcon(QIcon(IMAGE_PAUSE))

    # start player and update value
    logger.info('play from source')
    player.play()
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_PLAY
    state[KEY_DICT_PLAYER_STATES_ROW] = row


def _pause_song(table_song: QTableWidget, widget_playBar, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    # update table_song
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PLAY))
    table_song.setVerticalHeaderItem(row, icon)

    # update playbar
    widget_playBar.btn_play_pause.setIcon(QIcon(IMAGE_PLAY))

    # start player and update value
    logger.info('pause player')
    player.pause()
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_PAUSE
    state[KEY_DICT_PLAYER_STATES_ROW] = row
# will run IF a new song is going to be played WHILE there is a ongoing song.


def _switch_song(table_song: QTableWidget, widget_playBar, state: dict, song_entity: dict, row: int, player: QMediaPlayer):
    #  current song
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PLAY))
    table_song.setVerticalHeaderItem(state[KEY_DICT_PLAYER_STATES_ROW], icon)

    widget_playBar.btn_play_pause.setIcon(QIcon(IMAGE_PLAY))
    widget_playBar.angle = 0

    # stop the current song
    logger.info('stop song')
    player.stop()
    time.sleep(0.01)

    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_STOP
    _play_song(table_song, widget_playBar, state, song_entity, row, player)
