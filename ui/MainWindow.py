"""MainWinodw GUI file."""
import logging
from random import randint

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QMainWindow,
                               QSizePolicy, QVBoxLayout)

from config.default_parameters import (DEFAULT_PAGE_DOWNLOAD_NAME,
                                       DEFAULT_PAGE_LIBRARY_NAME,
                                       DEFAULT_ENCODING)
from config.image_manager import IMAGE_LOGO
from config.keys import KEY_DICT_PLAYER_STATES_ROW
from config.style_manager import STYLE_MAIN_WINDOW
from handler.handler_main import (handle_backward, handle_btn_library_populate,
                                  handle_end_of_media, handle_forward,
                                  handle_mute, handle_next, handle_page_switch,
                                  handle_play_order, handle_player,
                                  handle_populate_table_song, handle_prev,
                                  handle_slider_progress_pressed,
                                  handle_slider_progress_released,
                                  handle_slider_volume_changed,
                                  handle_spinning_bocchi_clicked,
                                  handle_toggle_menu, handle_track_played,
                                  handle_track_position_changed)
from session.session_data import session_data
from ui.media.media_player import VideoWidget
from ui.media.play_bar import PlayBar
from ui.menu.menu_bar import MenuBar
from ui.menu.status_bar import StatusBar
from ui.page.page_manager import PageManager
from ui.side.side_1 import SideShrinked
from ui.side.Side_2 import SideExpanded
from ui.top.top_bar import TopBar

from .central import CentralWidget

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """main gui instance MainWindow.

    Args:
        QMainWindow (QMainWindow): PySide6.QtWidgets
    """

    def __init__(self) -> None:
        logger.info('initializing')
        # initialization
        super().__init__()

        self.setObjectName('main_window')
        self.setWindowTitle('Bocchi Music')

        logger.info('initializing widgets')
        self.widget_centralWidget = CentralWidget(self)

        # initialize widgets
        self.widget_playBar = PlayBar(self.widget_centralWidget)
        self.widget_pageManager = PageManager(self.widget_centralWidget)
        self.widget_sideShrinked = SideShrinked(self.widget_centralWidget)
        self.widget_sideExpanded = SideExpanded(self.widget_centralWidget)
        self.widget_topBar = TopBar(self.widget_centralWidget)
        self.widget_videoWidget = VideoWidget(self.widget_centralWidget)

        # menu bar
        self.setCentralWidget(self.widget_centralWidget)
        self.menuBar_menu_bar = MenuBar(self)
        self.statusBar_status_bar = StatusBar(self)
        self.setMenuBar(self.menuBar_menu_bar)
        self.setStatusBar(self.statusBar_status_bar)

        logger.info('initializing layouts')
        # configure widget layouts
        self._initialize_layout()

        logger.info('initializing default values')
        self._configure_default_value()

        logger.info('initializing stylesheet')
        # apply stylesheet
        self._apply_stylesheet()

        # handle widget signal
        self._handle_signal()

    def _handle_signal(self) -> None:
        """_handle_signal"""
        self._handle_playBar_signal()
        self._handle_PageManager_signal()
        self._handle_sideExpanded_signal()
        self._handle_sideShrinked_signal()
        self._handle_topBar_signal()
        self._handle_videoWidget_signal()

    def _handle_playBar_signal(self) -> None:
        """_handle_playBar_signal"""
        self.widget_playBar.signal_btn_spinning_bocchi_clicked.connect(
            lambda: handle_spinning_bocchi_clicked(self.widget_pageManager,
                                                   self.widget_videoWidget))
        self.widget_playBar.signal_btn_play_pause_clicked.connect(lambda: handle_player(
            self, session_data.dict_player_states.get(KEY_DICT_PLAYER_STATES_ROW, 0)))
        self.widget_playBar.signal_btn_backward_clicked.connect(
            lambda: handle_backward(self.widget_videoWidget.player))
        self.widget_playBar.signal_btn_forward_clicked.connect(
            lambda: handle_forward(self.widget_videoWidget.player))
        self.widget_playBar.signal_btn_next_clicked.connect(lambda: handle_next(
            self, session_data.dict_song_entity, session_data.dict_player_states))
        self.widget_playBar.signal_btn_prev_clicked.connect(lambda: handle_prev(
            self, session_data.dict_song_entity, session_data.dict_player_states))
        self.widget_playBar.signal_btn_volume_clicked.connect(lambda: handle_mute(
            self.widget_videoWidget.player, self.widget_playBar.btn_volume))
        self.widget_playBar.signal_slider_volume_changed.connect(
            lambda value: handle_slider_volume_changed(self.widget_videoWidget.player, value))
        self.widget_playBar.signal_slider_progress_pressed.connect(
            lambda: handle_slider_progress_pressed(self.widget_videoWidget))
        self.widget_playBar.signal_slider_progress_released.connect(
            lambda value: handle_slider_progress_released(self.widget_videoWidget,
                                                          self.widget_playBar, value))
        self.widget_playBar.signal_btn_play_order_clicked.connect(lambda: handle_play_order(
            self.widget_playBar.btn_play_order, session_data.dict_player_states))

    def _handle_PageManager_signal(self) -> None:
        """_handle_PageManager_signal
        """
        self._handle_page_library_signal()
        self._handle_page_download_signal()

    def _handle_page_download_signal(self):
        """_handle_page_download_signal
        """
        self.widget_page_download = self.widget_pageManager.get_page(
            DEFAULT_PAGE_DOWNLOAD_NAME)
        self.widget_page_download.signal_repopulate_table_song.connect(lambda:
            handle_populate_table_song(self.widget_page_library.table_song,
                                       session_data.dict_song_entity))

    def _handle_page_library_signal(self) -> None:
        """_handle_page_library_signal"""
        self.widget_page_library = self.widget_pageManager.get_page(
            DEFAULT_PAGE_LIBRARY_NAME)

        self.widget_page_library.signal_populate_table_song.connect(lambda:
            handle_populate_table_song(self.widget_page_library.table_song,
                                       session_data.dict_song_entity))

        self.widget_page_library.signal_play_pause_clicked.connect(
            lambda row: handle_player(self, row))

        self.widget_page_library.signal_btn_library_populate_clicked.connect(
            lambda: handle_btn_library_populate(self.widget_page_library.table_song))

        self.widget_page_library.signal_btn_shuffle_clicked.connect(
            lambda: handle_player(self, randint(0, len(session_data.dict_song_entity) - 1)))

    def _handle_sideShrinked_signal(self) -> None:
        """_handle_sideShrinked_signal"""
        self.widget_sideShrinked.signal_page_switch.connect(
            lambda page_num: handle_page_switch(self, page_num))

    def _handle_sideExpanded_signal(self) -> None:
        """_handle_sideExpanded_signal"""
        self.widget_sideExpanded.signal_page_switch.connect(
            lambda page_num: handle_page_switch(self, page_num))

    def _handle_topBar_signal(self) -> None:
        """_handle_topBar_signal"""
        self.widget_topBar.signal_menu_toggle.connect(
            lambda checked: handle_toggle_menu(self, checked))

    def _handle_videoWidget_signal(self) -> None:
        """_handle_videoWidget_signal"""
        # self.widget_videoWidget.signal_track_paused.connect(
        #     handle_track_paused)
        self.widget_videoWidget.signal_track_played.connect(lambda position_current, duration:
            handle_track_played(self.widget_playBar, position_current, duration,
                                session_data.dict_player_states, session_data.dict_song_entity))
        # self.widget_videoWidget.signal_track_stopped.connect(
        #     handle_track_stopped)
        self.widget_videoWidget.signal_position_changed.connect(
            lambda
            position_current: handle_track_position_changed(
                self.widget_playBar, position_current))
        self.widget_videoWidget.signal_end_of_media.connect(
            lambda:
            handle_end_of_media(
                self.widget_page_library.table_song,
                self.widget_playBar, self.
                widget_videoWidget.player,
                session_data.dict_player_states,
                session_data.dict_song_entity))

    def _initialize_layout(self) -> None:
        """_initialize_layout"""
        self.grid_layout_2 = QGridLayout(self.widget_centralWidget)
        self.grid_layout_2.setObjectName('Outer_most_layout')
        self.vertical_layout_9 = QVBoxLayout()
        self.vertical_layout_9.setObjectName('vertical_layout_9')
        self.horizontal_layout_12 = QHBoxLayout()
        self.vertical_layout_10 = QVBoxLayout()
        self.vertical_layout_10.setObjectName('top_and_center')
        self.horizontal_layout_12.setObjectName('horizontal_layout_12')
        self.horizontal_layout_11 = QHBoxLayout()
        self.horizontal_layout_11.setObjectName('side_bars')

        self.horizontal_layout_11.addWidget(self.widget_sideShrinked)
        self.horizontal_layout_11.addWidget(self.widget_sideExpanded)

        self.vertical_layout_10.addWidget(self.widget_topBar)
        self.vertical_layout_10.addWidget(self.widget_pageManager)
        self.vertical_layout_10.addWidget(self.widget_videoWidget)

        self.horizontal_layout_12.addLayout(self.horizontal_layout_11)
        self.horizontal_layout_12.addLayout(self.vertical_layout_10)

        self.vertical_layout_9.addLayout(self.horizontal_layout_12)

        self.vertical_layout_9.addWidget(self.widget_playBar)

        self.grid_layout_2.addLayout(self.vertical_layout_9, 1, 0, 1, 1)

    def _configure_default_value(self) -> None:
        """_configure_default_value
        """
        self.setEnabled(True)
        self.resize(749, 643)
        size_policy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(size_policy.hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(IMAGE_LOGO, QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

    def _apply_stylesheet(self) -> None:
        """_apply_stylesheet
        """
        with open(STYLE_MAIN_WINDOW, 'r', encoding=DEFAULT_ENCODING) as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
