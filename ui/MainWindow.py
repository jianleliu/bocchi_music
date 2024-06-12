from handler.handler_topBar import handle_toggle_menu
from handler.handler_side1 import handle_page_switch
from handler.handler_main import *
from initialization.initialization_external import initialize_external
from initialization.initialization_internal import generate_dict_song_entity
from ui.menu.status_bar import StatusBar
from ui.menu.menu_bar import MenuBar
from config.style_manager import STYLE_MAIN_WINDOW
from config.image_manager import IMAGE_LOGO
from .central import CentralWidget
from ui.top.top_bar import TopBar
from ui.side.Side_2 import SideExpanded
from ui.side.side_1 import SideShrinked
from ui.page.page_manager import PageManager
from ui.media.play_bar import PlayBar
from ui.media.media_player import VideoWidget
from PySide6.QtCore import (
    QSize)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QSizePolicy,
                               QGridLayout, QHBoxLayout, QMainWindow, QVBoxLayout)
import os

IMAGE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../resource/images')
STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../resource/style')


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        # initialization
        super().__init__()
        initialize_external()
        self.initialize_variables()

        self.setObjectName('main_window')
        self.setWindowTitle('Bocchi Music')

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

        # configure widget layouts
        self.initialize_layout()
        self.configure_default_value()

        # apply stylesheet
        self.apply_stylesheet()

        # handle widget signal
        self.handle_signal()

    def handle_signal(self):
        self.handle_playBar_signal()
        self.handle_PageManager_signal()
        self.handle_sideExpanded_signal()
        self.handle_sideShrinked_signal()
        self.handle_topBar_signal()
        self.handle_videoWidget_signal()

    def handle_playBar_signal(self):
        self.widget_playBar.signal_btn_spinning_bocchi_clicked.connect(
            lambda: handle_spinning_bocchi_clicked(self.widget_pageManager, self.widget_videoWidget))
        self.widget_playBar.signal_btn_play_pause_clicked.connect(
            lambda: handle_player(self, self.dict_player_states.get(KEY_DICT_PLAYER_STATES_ROW, 0)))
        self.widget_playBar.signal_btn_backward_clicked.connect(
            lambda: handle_backward(self.widget_videoWidget.player))
        self.widget_playBar.signal_btn_forward_clicked.connect(
            lambda: handle_forward(self.widget_videoWidget.player))
        self.widget_playBar.signal_btn_next_clicked.connect(lambda: handle_next(
            self, self.dict_song_entity, self.dict_player_states))
        self.widget_playBar.signal_btn_prev_clicked.connect(
            lambda: handle_prev(self, self.dict_song_entity, self.dict_player_states))
        self.widget_playBar.signal_btn_volume_clicked.connect(lambda: handle_mute(
            self.widget_videoWidget.player, self.widget_playBar.btn_volume))
        self.widget_playBar.signal_slider_volume_changed.connect(
            lambda value: handle_slider_volume_changed(self.widget_videoWidget.player, value))
        self.widget_playBar.signal_slider_progress_changed.connect(
            lambda value: handle_slider_progress_changed(self.widget_videoWidget.player, value))
        self.widget_playBar.signal_btn_play_order_clicked.connect(lambda: handle_play_order(
            self.widget_playBar.btn_play_order, self.dict_player_states))

    def handle_PageManager_signal(self):
        self.handle_page_library_signal()

    def handle_page_library_signal(self):
        self.widget_page_library = self.widget_pageManager.get_page(
            'page_library')

        self.widget_page_library.signal_populate_table_song.connect(
            lambda: handle_populate_table_song(self.widget_page_library.table_song, self.dict_song_entity))

        self.widget_page_library.signal_play_pause_clicked.connect(
            lambda row: handle_player(self, row))

    def handle_sideShrinked_signal(self):
        self.widget_sideShrinked.signal_page_switch.connect(
            lambda page_num: handle_page_switch(self, page_num))

    def handle_sideExpanded_signal(self):
        self.widget_sideExpanded.signal_page_switch.connect(
            lambda page_num: handle_page_switch(self, page_num))

    def handle_topBar_signal(self):
        self.widget_topBar.signal_menu_toggle.connect(
            lambda checked: handle_toggle_menu(self, checked))

    def handle_videoWidget_signal(self):
        # self.widget_videoWidget.signal_track_paused.connect(
        #     handle_track_paused)
        self.widget_videoWidget.signal_track_played.connect(lambda position_current, duration: handle_track_played(
            self.widget_playBar, position_current, duration, self.dict_player_states, self.dict_song_entity))
        # self.widget_videoWidget.signal_track_stopped.connect(
        #     handle_track_stopped)
        self.widget_videoWidget.signal_position_changed.connect(
            lambda position_current: handle_track_position_changed(self.widget_playBar, position_current))
        self.widget_videoWidget.signal_end_of_media.connect(lambda: handle_end_of_media(
            self.widget_page_library.table_song, self.widget_playBar, self.widget_videoWidget.player, self.dict_player_states, self.dict_song_entity))

    def initialize_layout(self):
        self.gridLayout_2 = QGridLayout(self.widget_centralWidget)
        self.gridLayout_2.setObjectName('Outer_most_layout')
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_12 = QHBoxLayout()
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"top_and_center")
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"side_bars")

        self.horizontalLayout_11.addWidget(self.widget_sideShrinked)
        self.horizontalLayout_11.addWidget(self.widget_sideExpanded)

        self.verticalLayout_10.addWidget(self.widget_topBar)
        self.verticalLayout_10.addWidget(self.widget_pageManager)
        self.verticalLayout_10.addWidget(self.widget_videoWidget)

        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.verticalLayout_9.addWidget(self.widget_playBar)

        self.gridLayout_2.addLayout(self.verticalLayout_9, 1, 0, 1, 1)

    def configure_default_value(self):
        self.setEnabled(True)
        self.resize(749, 643)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(IMAGE_LOGO, QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

    def initialize_variables(self):
        self.dict_song_entity = generate_dict_song_entity()
        self.dict_player_states = {
            KEY_DICT_PLAYER_STATES_PLAY_ORDER: DEFAULT_PLAY_ORDER,

        }

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_MAIN_WINDOW)

        with open(stylesheet_path, "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
