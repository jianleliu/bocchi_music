from PySide6.QtCore import (QSize, Qt, Signal)
from PySide6.QtGui import (QCursor, QFont, QIcon)
from PySide6.QtWidgets import (QCheckBox, QFrame, QGridLayout,
                               QHBoxLayout, QLineEdit,
                               QPushButton, QRadioButton,
                               QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)
import os
from config.style_manager import STYLE_DOWNLOAD_PAGE
from config.image_manager import IMAGE_DOWNLOAD_BTN_2
from handler.handler_page_download import handle_download_track

IMAGE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/images')
STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class DownloadPage(QFrame):
    signal_download = Signal

    def __init__(self):
        super().__init__()
        self.setObjectName(u"download_page")
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

        # configure display text
        self.configure_parameters()

        # handle event
        self.handle_event()

        # emit signal
        self.emit_signal()

    def handle_event(self):
        self.btn_advanced.toggled.connect(
            lambda: self.advanced_widget.setHidden(not self.advanced_widget.isHidden()))
        self.btn_download.clicked.connect(
            lambda: handle_download_track(self, self.url_search_bar.text()))

    def emit_signal(self):
        pass

    def initialize_status_box(self):
        self.status_box = QTextBrowser(self)
        self.status_box.setObjectName(u"status_box")

        self.verticalLayout_24.addWidget(self.status_box)

    def initialize_advanced_tab(self):
        self.btn_advanced = QPushButton(self)
        self.btn_advanced.setObjectName(u"btn_advanced")
        self.btn_advanced.setCheckable(True)
        self.btn_advanced.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_24.addWidget(self.btn_advanced)

        # advanced widget tab
        self.advanced_widget = QWidget(self)
        self.advanced_widget.setObjectName(u"advanced_widget")
        self.advanced_widget.setMinimumSize(QSize(0, 50))
        self.gridLayout = QGridLayout(self.advanced_widget)
        self.gridLayout.setObjectName(u"gridLayout")

        # audio only check
        self.check_audio_only = QCheckBox(self.advanced_widget)
        self.check_audio_only.setObjectName(u"check_audio_only")
        font = QFont()
        font.setPointSize(10)
        self.check_audio_only.setFont(font)
        self.check_audio_only.setChecked(True)

        self.gridLayout.addWidget(self.check_audio_only, 0, 0, 1, 1)

        # default path check
        self.check_use_default_path = QCheckBox(self.advanced_widget)
        self.check_use_default_path.setObjectName(u"check_use_default_path")
        self.check_use_default_path.setFont(font)
        self.check_use_default_path.setChecked(True)

        self.gridLayout.addWidget(self.check_use_default_path, 1, 0, 1, 1)

        # thumbnail check
        self.check_include_thumbnail = QCheckBox(self.advanced_widget)
        self.check_include_thumbnail.setObjectName(u"check_include_thumbnail")
        self.check_include_thumbnail.setEnabled(False)
        self.check_include_thumbnail.setChecked(True)

        self.gridLayout.addWidget(self.check_include_thumbnail, 0, 1, 1, 1)

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
        self.btn_download = QPushButton(self)
        self.btn_download.setObjectName(u"btn_download")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy6.setHeightForWidth(
            self.btn_download.sizePolicy().hasHeightForWidth())
        self.btn_download.setSizePolicy(sizePolicy6)
        self.btn_download.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_DOWNLOAD_BTN_2)
        icon4.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_download.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.btn_download)

        self.verticalLayout_24.addLayout(self.horizontalLayout_7)

    def apply_stylesheet(self):
        with open(STYLE_DOWNLOAD_PAGE, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def configure_parameters(self):
        self.url_search_bar.setPlaceholderText('URL')
        self.radio_song.setText('Song')
        self.radio_playlist.setText('Playlist')
        self.btn_advanced.setText('Advanced')
        self.check_audio_only.setText('Audio Only')
        self.check_use_default_path.setText('Use Default Path')
        self.check_include_thumbnail.setText('Include Thumbnail')
        self.status_box.setText('...')
