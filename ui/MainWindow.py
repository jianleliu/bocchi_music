from handler.handler_topBar import handle_toggle_menu
from handler.handler_side1 import handle_page_switch
from handler.handler_main import handle_populate_table_song, handle_player
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
from ui.bottom.play_bar import PlayBar
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
        self.initializae_variables()

        self.setObjectName('main_window')
        self.setWindowTitle('Bocchi Music')

        self.widget_centralWidget = CentralWidget(self)

        # initialize widgets
        self.widget_playBar = PlayBar(self.widget_centralWidget)
        self.widget_PageManager = PageManager(self.widget_centralWidget)
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
        self.configure_layout()
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

    def handle_playBar_signal(self):
        pass

    def handle_PageManager_signal(self):
        self.handle_page_library_signal()

    def handle_page_library_signal(self):
        self.widget_page_library = self.widget_PageManager.get_page('page_library')

        self.widget_page_library.signal_populate_table_song.connect(
            lambda: handle_populate_table_song(self.widget_page_library.table_song, self.dict_song_entity))

        self.widget_page_library.signal_play_pause_clicked.connect(lambda row: handle_player(self, row))

    def handle_sideShrinked_signal(self):
        self.widget_sideShrinked.signal_page_switch.connect(
            lambda page_num: handle_page_switch(self, page_num))

    def handle_sideExpanded_signal(self):
        self.widget_sideExpanded.signal_page_switch.connect(
            lambda page_num: handle_page_switch(self, page_num))

    def handle_topBar_signal(self):
        self.widget_topBar.signal_menu_toggle.connect(
            lambda checked: handle_toggle_menu(self, checked))

    def configure_layout(self):
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
        self.verticalLayout_10.addWidget(self.widget_PageManager)
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

    def initializae_variables(self):
        self.dict_song_entity = generate_dict_song_entity()
        self.dict_player_states = {}

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_MAIN_WINDOW)

        with open(stylesheet_path, "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
