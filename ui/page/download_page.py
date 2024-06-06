from PySide6.QtCore import (QSize, Qt)
from PySide6.QtGui import (QCursor, QFont, QIcon)
from PySide6.QtWidgets import (QCheckBox, QFrame, QGridLayout,
                               QHBoxLayout, QLineEdit,
                               QPushButton, QRadioButton,
                               QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)
import os
from config.style_manager import STYLE_DOWNLOAD_PAGE
from config.image_manager import IMAGE_DOWNLOAD_BTN_2

IMAGE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/images')
STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class DownloadPage(QFrame):
    def __init__(self):
        print('download page 1')
        super().__init__()
        print('download page 3')
        self.setObjectName(u"download_page")
        print('download page 2')
        self.verticalLayout_24 = QVBoxLayout(self)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        # search bar and options
        self.initialize_search_bar()

        # advanced tab
        self.initialize_advanced_tab()

        # status box
        self.initialize_status_box()

        # apply stylesheet
        self.apply_stylesheet()

    def initialize_status_box(self):
        self.status_box = QTextBrowser(self)
        self.status_box.setObjectName(u"status_box")

        self.verticalLayout_24.addWidget(self.status_box)

    def initialize_advanced_tab(self):
        self.advanced_btn = QPushButton(self)
        self.advanced_btn.setObjectName(u"advanced_btn")
        self.advanced_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_24.addWidget(self.advanced_btn)

        # advanced widget tab
        self.advanced_widget = QWidget(self)
        self.advanced_widget.setObjectName(u"advanced_widget")
        self.advanced_widget.setMinimumSize(QSize(0, 50))
        self.gridLayout = QGridLayout(self.advanced_widget)
        self.gridLayout.setObjectName(u"gridLayout")

        # audio only check
        self.audio_only_check = QCheckBox(self.advanced_widget)
        self.audio_only_check.setObjectName(u"audio_only_check")
        font = QFont()
        font.setPointSize(10)
        self.audio_only_check.setFont(font)
        self.audio_only_check.setChecked(True)

        self.gridLayout.addWidget(self.audio_only_check, 0, 0, 1, 1)

        # default path check
        self.use_default_path_check = QCheckBox(self.advanced_widget)
        self.use_default_path_check.setObjectName(u"use_default_path_check")
        self.use_default_path_check.setFont(font)
        self.use_default_path_check.setChecked(True)

        self.gridLayout.addWidget(self.use_default_path_check, 1, 0, 1, 1)

        # thumbnail check
        self.thumbnail_check = QCheckBox(self.advanced_widget)
        self.thumbnail_check.setObjectName(u"thumbnail_check")
        self.thumbnail_check.setEnabled(False)
        self.thumbnail_check.setChecked(True)

        self.gridLayout.addWidget(self.thumbnail_check, 0, 1, 1, 1)

        self.verticalLayout_24.addWidget(self.advanced_widget)

    def initialize_search_bar(self):
        # search bar
        self.url_search_bar = QLineEdit(self)
        self.url_search_bar.setObjectName(u"url_search_bar")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy7.setHeightForWidth(
            self.url_search_bar.sizePolicy().hasHeightForWidth())
        self.url_search_bar.setSizePolicy(sizePolicy7)
        # self.url_search_bar.setStyleSheet(u"border-bottom: 1px solid;")

        self.horizontalLayout_7.addWidget(self.url_search_bar)

        # radio options
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.radio_song = QRadioButton(self)
        self.radio_song.setObjectName(u"radio_song")
        self.radio_song.setMinimumSize(QSize(0, 15))
        self.radio_song.setChecked(True)

        self.verticalLayout_23.addWidget(self.radio_song)

        self.radio_playlist = QRadioButton(self)
        self.radio_playlist.setObjectName(u"radio_playlist")
        self.radio_playlist.setMinimumSize(QSize(0, 15))

        self.verticalLayout_23.addWidget(self.radio_playlist)

        self.horizontalLayout_7.addLayout(self.verticalLayout_23)

        # download button
        self.download_btn = QPushButton(self)
        self.download_btn.setObjectName(u"download_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy6.setHeightForWidth(
            self.download_btn.sizePolicy().hasHeightForWidth())
        self.download_btn.setSizePolicy(sizePolicy6)
        self.download_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_DOWNLOAD_BTN_2)
        icon4.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.download_btn.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.download_btn)

        self.verticalLayout_24.addLayout(self.horizontalLayout_7)

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_DOWNLOAD_PAGE)

        with open(stylesheet_path, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
