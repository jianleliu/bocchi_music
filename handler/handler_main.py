"""handler for events that require going through MainWindow."""
import logging
import math
import time
from configparser import ConfigParser
from os import path
from random import randint

from PySide6.QtCore import QTime, QUrl
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QFrame, QStackedWidget, QTableWidget,
                               QTableWidgetItem, QMainWindow, QPushButton)

from config.default_parameters import (DEAFULT_PLAY_ORDER_LOOPS,
                                       DEFAULT_BACKWARD_LENGTH,
                                       DEFAULT_DOWNLOAD_FORMAT,
                                       DEFAULT_FORWARD_LENGTH,
                                       DEFAULT_PLAY_ORDER_CYCLE,
                                       DEFAULT_PLAY_ORDER_SHUFFLE,
                                       INI_FILE_PATH)
from config.image_manager import (IMAGE_CYCLE, IMAGE_LOOP, IMAGE_MUTED,
                                  IMAGE_PAUSE, IMAGE_PLAY, IMAGE_SHUFFLE,
                                  IMAGE_VOLUME)
from config.keys import (KEY_DICT_PLAYER_STATES_PATH,
                         KEY_DICT_PLAYER_STATES_PLAY_ORDER,
                         KEY_DICT_PLAYER_STATES_ROW,
                         KEY_DICT_PLAYER_STATES_STATE,
                         KEY_DICT_SONG_ENTITY_ARTIST,
                         KEY_DICT_SONG_ENTITY_BASENAME,
                         KEY_DICT_SONG_ENTITY_DATE_ADDED,
                         KEY_DICT_SONG_ENTITY_LAST_PLAYED,
                         KEY_DICT_SONG_ENTITY_TIMES_PLAYED,
                         KEY_DICT_SONG_ENTITY_TITLE, KEY_DIR_PLAYLIST_DOWNLOAD,
                         KEY_DIR_TRACK_DOWNLOAD)
from config.sections import SECTION_SETTINGS_TAB_1
from config.states import STATE_PAUSE, STATE_PLAY, STATE_STOP
from initialization.initialization_internal import populate_song_entity_all
from session.session_data import session_data

config = ConfigParser()
logger = logging.getLogger(__name__)


def handle_populate_table_song(table_song: QTableWidget, dict_song: dict) -> None:
    """populate the song table in the library page with songs in dict_song.

    Args:
        table_song (QTableWidget): table widget from LibraryPage.
        dict_song (dict): a dict containing songs in the table, stored in Session_data.
    """
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
        icon = QPixmap(IMAGE_PLAY)
        item = QTableWidgetItem()
        item.setIcon(icon)
        table_song.setVerticalHeaderItem(index_row, item)
        index_row += 1


def handle_btn_library_populate(table_song:  QTableWidget) -> None:
    """populate dict_song_entity then populate song table.

    Args:
        table_song (QTableWidget): song table widget in Librarypage.
    """
    config.read(INI_FILE_PATH)
    dir_song_root = config[SECTION_SETTINGS_TAB_1][KEY_DIR_TRACK_DOWNLOAD]
    dir_playlist_root = config[SECTION_SETTINGS_TAB_1][KEY_DIR_PLAYLIST_DOWNLOAD]

    session_data.dict_song_entity = populate_song_entity_all(
        dir_song_root, dir_playlist_root, [DEFAULT_DOWNLOAD_FORMAT])

    handle_populate_table_song(table_song, session_data.dict_song_entity)


def handle_player(main_window: QMainWindow, row: int) -> None:
    """play/pause/continue/switch song based on the state variable in session_data.

    Args:
        main_window (QMainWindow): MainWindow of the GUI.
        row (int): the row the target song is in on song table.
    """
    state = session_data.dict_player_states
    player = main_window.widget_videoWidget.player

    if 'row' not in state:
        logger.info('play song')
        _play_song(main_window.widget_page_library.table_song, main_window.widget_playBar,
                   state, session_data.dict_song_entity, row, player)
        return

    elif ((state[KEY_DICT_PLAYER_STATES_STATE] == STATE_PAUSE) and (state[KEY_DICT_PLAYER_STATES_ROW] == row)):
        logger.info('continue song')
        _continue_song(main_window.widget_page_library.table_song, main_window.widget_playBar,
                       state, row, player)
        return

    if (state[KEY_DICT_PLAYER_STATES_STATE] == STATE_PLAY) and (state[KEY_DICT_PLAYER_STATES_ROW] == row):
        logger.info('pause song')
        _pause_song(main_window.widget_page_library.table_song, main_window.widget_playBar,
                    state, row, player)
    else:
        logger.info('switch song')
        _switch_song(main_window.widget_page_library.table_song, main_window.widget_playBar,
                     state, session_data.dict_song_entity, row, player)


def handle_spinning_bocchi_clicked(widget_pageManger: QStackedWidget,
                                   widget_videoWidget: QVideoWidget) -> None:
    """toggle video player / page widget.

    Args:
        widget_pageManger (QStackedWidget): page manager instance, ui.
        widget_videoWidget (QVideoWidget): videowidget instance, ui.
    """
    widget_pageManger.setHidden(not widget_pageManger.isHidden())
    widget_videoWidget.setHidden(not widget_videoWidget.isHidden())


def handle_page_switch(window: object, page_num: int):
    """switch page widget page index.

    Args:
        window (object): MainWindow GUI.
        page_num (int): page num.
    """
    window.widget_pageManager.setCurrentIndex(page_num)
    window.widget_pageManager.show()
    window.widget_videoWidget.hide()

def handle_toggle_menu(main_window: QMainWindow, isChecked: bool):
    """toggle expanded/shrinked side bars.

    Args:
        main_window (QMainWindow): MainWindow GUI.
        isChecked (bool): should always be true.
    """
    main_window.widget_sideExpanded.setHidden(isChecked)
    main_window.widget_sideShrinked.setVisible(isChecked)

# pylint: disable=unnecessary-pass, invalid-name, unused-argument


def handle_track_paused(widget_playBar: QFrame) -> None:
    """for spinning bocchi animation, currently not used.

    Args:
        widget_playBar (QFrame): playBar instance, ui.
    """
    # stop the spinning bocchi
    # logger.info('handler called')
    pass
    # logger.info('handler ended')
# pylint: enable=unnecessary-pass, invalid-name, unused-argument


def handle_track_played(widget_playBar: QFrame, position_current: int, duration: int, states: dict,
                        song_entity: dict) -> None:
    """update playbar with new song info.

    Args:
        widget_playBar (QFrame): playBar instance, ui.
        position_current (int): position of the playing song in ms, returned by video player.
        duration (int): total duration returned by video player.
        states (dict): play state, stored in session_data.
        song_entity (dict):  a dict containing songs in the table, stored in Session_data.
    """
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


def handle_track_position_changed(widget_playBar: QFrame, position_current: int) -> None:
    """update slider as the song plays.

    Args:
        widget_playBar (QFrame): playBar instance, ui.
        position_current (int): position of the playing song in ms, returned by video player.
    """
    # # logger.info('handler called')
    position_current_in_seconds = math.floor(position_current/1000)
    formatted_current_time = QTime(0, 0, 0).addSecs(
        position_current_in_seconds).toString('mm:ss')

    # logger.info('update slider_progress value')
    widget_playBar.slider_progress.setValue(position_current_in_seconds)
    widget_playBar.label_current_timestamp.setText(formatted_current_time)
    # # logger.info('handler ended')


def handle_track_stopped() -> None:
    """for spinning bocchi, not used.
    """
    # pause the spinning bocchi
    # pylint: disable=unnecessary-pass
    pass
    # pylint: enable=unnecessary-pass


def handle_backward(player: QMediaPlayer) -> None:
    """the song position minus DEFAULT_BACKWARD_LENGTH.

    Args:
        player (QMediaPlayer): music player.
    """
    player.setPosition(player.position() - DEFAULT_BACKWARD_LENGTH)


def handle_forward(player: QMediaPlayer) -> None:
    """the song position plus DEFAULT_FORWARD_LENGTH.

    Args:
        player (QMediaPlayer): music player.
    """
    player.setPosition(player.position() + DEFAULT_FORWARD_LENGTH)


def handle_next(main_window: QMainWindow, song_entity: dict, state: dict) -> None:
    """when next btn is clicked, update state dict and play the next song.

    Args:
        main_window (QMainWindow): GUI MainWindow.
        song_entity (dict):  a dict containing songs in the table, stored in Session_data.
        state (dict): a dict containing the state of the current song, stored in Session_data.
    """
    config.read(INI_FILE_PATH)
    row_next = (state[KEY_DICT_PLAYER_STATES_ROW] + 1) % len(song_entity)
    if state[KEY_DICT_PLAYER_STATES_PLAY_ORDER] == DEFAULT_PLAY_ORDER_SHUFFLE:
        row_next = randint(0, len(song_entity) - 1)

    handle_player(main_window, row_next)


def handle_prev(main_window: QMainWindow, song_entity: dict, state: dict) -> None:
    """when prev btn is clicked, update state dict and play the prev song.

    Args:
        main_window (QMainWindow): GUI MainWindow.
        song_entity (dict):  a dict containing songs in the table, stored in Session_data.
        state (dict): a dict containing the state of the current song, stored in Session_data.
    """
    config.read(INI_FILE_PATH)
    row_prev = (state[KEY_DICT_PLAYER_STATES_ROW] - 1) % len(song_entity)
    if state[KEY_DICT_PLAYER_STATES_PLAY_ORDER] == DEFAULT_PLAY_ORDER_SHUFFLE:
        row_prev = randint(0, len(song_entity) - 1)
    handle_player(main_window, row_prev)


def handle_mute(player: QMediaPlayer, btn_volume: QPushButton) -> None:
    """when mute btn is clicked, setMute() to true/false and change icon.

    Args:
        player (QMediaPlayer): music player.
        btn_volume (QPushButton): one of playbar btn.
    """
    is_muted = player.audioOutput().isMuted()
    player.audioOutput().setMuted(not is_muted)
    btn_volume.setIcon(QIcon(IMAGE_VOLUME if is_muted else IMAGE_MUTED))


def handle_slider_volume_changed(player: QMediaPlayer, value: int) -> None:
    """when slider is dragged and dropped, update the volume of media player.

    Args:
        player (QMediaPlayer): music player.
        value (int): new volume of the slider.
    """
    logger.info('update volume')
    player.audioOutput().setVolume(value/100)


def handle_slider_progress_released(widget_videoWidget: QVideoWidget,
                                    widget_playBar: QFrame, value: int) -> None:
    """when slider is dragged and dropped, update the position of playing song.

    Args:
        widget_videoWidget (QVideoWidget): video player instance, ui.
        widget_playBar (QFrame): playBar instance, ui.
        value (int): new position value.
    """
    widget_videoWidget.player.setPosition(value * 1000)
    widget_videoWidget.signal_position_changed.connect(
        lambda position_current: handle_track_position_changed(widget_playBar, position_current))


def handle_slider_progress_pressed(widget_videoWidget: QVideoWidget) -> None:
    """when user pressed the slider, temporarily disconnect the
    update slider signal to allow user to drag and drop.

    Args:
        widget_videoWidget (QVideoWidget): video player instance, ui.
    """
    widget_videoWidget.signal_position_changed.disconnect()


def handle_play_order(btn_play_order: QPushButton, state: dict) -> None:
    """when play order btn is clicked, update icon and play state to either 
    cycle, loop, or shuffle.

    Args:
        btn_play_order (QPushButton): one of playbar btn.
        state (dict): play state dict, stored in session data.
    """
    PLAY_ORDERS = [
        (DEAFULT_PLAY_ORDER_LOOPS, IMAGE_LOOP),
        (DEFAULT_PLAY_ORDER_CYCLE, IMAGE_CYCLE),
        (DEFAULT_PLAY_ORDER_SHUFFLE, IMAGE_SHUFFLE)
    ]

    # Get the current play order and find its index in the PLAY_ORDERS list
    current_play_order = state[KEY_DICT_PLAYER_STATES_PLAY_ORDER]
    current_index = [order[0]
                     for order in PLAY_ORDERS].index(current_play_order)

    next_index = (current_index + 1) % len(PLAY_ORDERS)

    next_play_order, image_path = PLAY_ORDERS[next_index]

    state[KEY_DICT_PLAYER_STATES_PLAY_ORDER] = next_play_order

    btn_play_order.setIcon(QIcon(image_path))


def handle_end_of_media(table_song: QTableWidget, widget_playBar: QFrame,
                        player: QMediaPlayer, state: dict, song_entity: dict) -> None:
    """when the song is finished playing, switch song based on its state (play order and row order).

    Args:
        table_song (QTableWidget): song table ui instance, in library page.
        widget_playBar (QFrame): playbar instance, ui.
        player (QMediaPlayer): music player.
        state (dict): play state dict, stored in session data. 
        song_entity (dict): a dict containing songs in the table, stored in Session_data.
    """
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


def _play_song(
        table_song: QTableWidget, widget_playBar: QFrame, state: dict, song_entity: dict, row: int,
        player: QMediaPlayer) -> None:
    """update song table icon, playbar, start audio player and
    update state dict value to the new song.

    Args:
        table_song (QTableWidget): song table ui instance, in library page.
        widget_playBar (QFrame):  playbar instance, ui.
        state (dict): play state dict, stored in session data. 
        song_entity (dict):  play state dict, stored in session data. 
        row (int): row order of the song in song table.
        player (QMediaPlayer): music player.
    """
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


def _continue_song(
        table_song: QTableWidget, widget_playBar: QFrame, state: dict, row: int,
        player: QMediaPlayer) -> None:
    """update song table icon, update playbar, and start player and update state value.

    Args:
        table_song (QTableWidget): song table ui instance, in library page.
        widget_playBar (QFrame):  playbar instance, ui.
        state (dict): play state dict, stored in session data. 
        row (int): row order of the song in song table.
        player (QMediaPlayer): music player.
    """
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


def _pause_song(
        table_song: QTableWidget, widget_playBar: QFrame, state: dict, row: int,
        player: QMediaPlayer) -> None:
    """update song table icon, update playbar, pause player and update state dict.

    Args:
        table_song (QTableWidget): song table ui instance, in library page.
        widget_playBar (QFrame):  playbar instance, ui.
        state (dict): play state dict, stored in session data. 
        row (int): row order of the song in song table.
        player (QMediaPlayer): music player.
    """
    # update table_song
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PLAY))
    table_song.setVerticalHeaderItem(row, icon)

    # update playbar
    widget_playBar.btn_play_pause.setIcon(QIcon(IMAGE_PLAY))

    # pause player and update value
    logger.info('pause player')
    player.pause()
    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_PAUSE
    state[KEY_DICT_PLAYER_STATES_ROW] = row

#


def _switch_song(
        table_song: QTableWidget, widget_playBar, state: dict, song_entity: dict, row: int,
        player: QMediaPlayer) -> None:
    """will run IF a new song is going to be played WHILE there is a ongoing song.
    update song table icon, stop current song, update state dict, and play a new song.

    Args:
        table_song (QTableWidget): _description_
        widget_playBar (_type_): _description_
        state (dict): _description_
        song_entity (dict): _description_
        row (int): _description_
        player (QMediaPlayer): _description_
    """
    # update table_song
    icon = QTableWidgetItem()
    icon.setIcon(QPixmap(IMAGE_PLAY))
    table_song.setVerticalHeaderItem(state[KEY_DICT_PLAYER_STATES_ROW], icon)

    widget_playBar.btn_play_pause.setIcon(QIcon(IMAGE_PLAY))
    widget_playBar.angle = 0

    # stop the current song
    logger.info('stop song')
    player.stop()
    # sleep is neccessary or it will crash.
    time.sleep(0.01)

    state[KEY_DICT_PLAYER_STATES_STATE] = STATE_STOP
    _play_song(table_song, widget_playBar, state, song_entity, row, player)
