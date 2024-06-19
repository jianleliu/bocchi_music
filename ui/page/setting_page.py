from PySide6.QtCore import (QRect, Qt, Signal)
from PySide6.QtGui import (QCursor, QFont)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QTabWidget, QVBoxLayout, QWidget)

from config.default_parameters import DEFAULT_PLAYLIST_DOWNLOAD_DIR, DEFAULT_TRACK_DOWNLOAD_DIR, INI_FILE_PATH
from handler.handler_page_settings import handle_browse_path
from config.sections import *
from config.keys import *
from configparser import ConfigParser
from os import path
import logging

logger = logging.getLogger(__name__)

class SettingPage(QFrame):

    def __init__(self):
        logger.info('initializing')
        super().__init__()
        self.setObjectName('setting_page')
        self.verticalLayout_26 = QVBoxLayout(self)
        self.verticalLayout_26.setObjectName('verticalLayout_26')
        
        logger.info('initializing tab widget')
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setObjectName('tabWidget')

        # initialize tabs
        logger.info('initializing tabs')
        self.parameter_tab()
        self.second_tab()

        # self.btn_browse_song_path.clicked.connect(switch_tab(self.le_song_dir))

        # configure display text
        logger.info('configure parameters')
        self.configure_parameter()

        # handle signal/events
        logger.info('handle events')
        self.handle_event()

    def handle_event(self):
        # update display text and update config file.
        self.btn_browse_song_path.clicked.connect(
            lambda: handle_browse_path(self.le_song_dir, KEY_DIR_TRACK_DOWNLOAD))
        self.btn_browse_playlist_path.clicked.connect(
            lambda: handle_browse_path(self.le_playlist_dir, KEY_DIR_PLAYLIST_DOWNLOAD))

    def parameter_tab(self):
        self.parameters_tab = QWidget()
        self.parameters_tab.setObjectName('parameters_tab')
        self.label_download_title = QLabel(self.parameters_tab)
        self.label_download_title.setObjectName('label_download_title')
        self.label_download_title.setGeometry(QRect(20, 20, 131, 21))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_download_title.setFont(font1)

        # widget stores components below
        self.widget_2 = QWidget(self.parameters_tab)
        self.widget_2.setObjectName('widget_2')
        self.widget_2.setGeometry(QRect(20, 50, 421, 121))
        self.layoutWidget = QWidget(self.widget_2)
        self.layoutWidget.setObjectName('layoutWidget')
        self.layoutWidget.setGeometry(QRect(20, 60, 251, 40))

        # default playlist download path
        self.verticalLayout_28 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_28.setObjectName('verticalLayout_28')
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_default_playlist_download_dir = QLabel(self.layoutWidget)
        self.label_default_playlist_download_dir.setObjectName(
            'label_default_playlist_download_dir')
        font = QFont()
        font.setPointSize(10)
        self.label_default_playlist_download_dir.setFont(font)

        self.verticalLayout_28.addWidget(
            self.label_default_playlist_download_dir)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName('horizontalLayout_13')
        self.le_playlist_dir = QLineEdit(self.layoutWidget)
        self.le_playlist_dir.setObjectName('le_playlist_dir')

        self.horizontalLayout_13.addWidget(self.le_playlist_dir)

        self.btn_browse_playlist_path = QPushButton(self.layoutWidget)
        self.btn_browse_playlist_path.setObjectName('btn_browse_playlist_path')
        self.btn_browse_playlist_path.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.btn_browse_playlist_path)

        self.verticalLayout_28.addLayout(self.horizontalLayout_13)

        # default track download path
        self.layoutWidget1 = QWidget(self.widget_2)
        self.layoutWidget1.setObjectName('layoutWidget1')
        self.layoutWidget1.setGeometry(QRect(20, 10, 251, 40))
        self.verticalLayout_27 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_27.setObjectName('verticalLayout_27')
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_default_track_download_dir = QLabel(self.layoutWidget1)
        self.label_default_track_download_dir.setObjectName(
            'label_default_track_download_dir')
        self.label_default_track_download_dir.setFont(font)

        self.verticalLayout_27.addWidget(self.label_default_track_download_dir)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName('horizontalLayout_10')
        self.le_song_dir = QLineEdit(self.layoutWidget1)
        self.le_song_dir.setObjectName('le_song_dir')

        self.horizontalLayout_10.addWidget(self.le_song_dir)

        self.btn_browse_song_path = QPushButton(self.layoutWidget1)
        self.btn_browse_song_path.setObjectName('btn_browse_song_path')
        self.btn_browse_song_path.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.btn_browse_song_path)

        self.verticalLayout_27.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.parameters_tab, 'Parameters')

    def second_tab(self):
        self.tab_2 = QWidget()
        self.tab_2.setObjectName('tab_2')
        self.tabWidget.addTab(self.tab_2, 'Other')

        self.verticalLayout_26.addWidget(self.tabWidget)

    def configure_parameter(self):
        self.label_download_title.setText('Download')
        self.label_default_track_download_dir.setText(
            'Default track download directiory:')
        self.label_default_playlist_download_dir.setText(
            'Default playlist download directory:')
        self.btn_browse_song_path.setText('Browse')
        self.btn_browse_playlist_path.setText('Browse')

        # Download page
        dir_track_download = DEFAULT_TRACK_DOWNLOAD_DIR
        dir_playlist_download = DEFAULT_PLAYLIST_DOWNLOAD_DIR
        if path.exists(INI_FILE_PATH):
            config = ConfigParser()
            config.read(INI_FILE_PATH)

            dir_track_download = config[SECTION_SETTINGS_TAB_1][KEY_DIR_TRACK_DOWNLOAD]
            dir_playlist_download = config[SECTION_SETTINGS_TAB_1][KEY_DIR_PLAYLIST_DOWNLOAD]

        self.le_song_dir.setText(dir_track_download)
        self.le_playlist_dir.setText(dir_playlist_download)
