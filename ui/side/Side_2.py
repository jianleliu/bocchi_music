from PySide6.QtCore import (
    QSize, Qt, Signal)
from PySide6.QtGui import (QCursor, QIcon, QPixmap)
from PySide6.QtWidgets import (
    QSizePolicy, QFrame, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QVBoxLayout)
import os
from config.style_manager import STYLE_SIDE_EXPANDED
from config.image_manager import (IMAGE_LOGO, IMAGE_HOME_BTN_2, IMAGE_LIBRARY_BTN_2,
                                  IMAGE_PLAYLIST_BTN_2, IMAGE_DOWNLOAD_BTN_2,
                                  IMAGE_SETTINGS_BTN_2)

IMAGE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/images')
STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class SideExpanded(QFrame):
    signal_page_switch = Signal(int)

    def __init__(self, centralWidget):
        super().__init__(centralWidget)
        self.setObjectName('side_expanded')
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy3)

        # layouts
        self.verticalLayout_5 = QVBoxLayout(self)
        self.verticalLayout_5.setObjectName('verticalLayout_5')
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName('verticalLayout_expanded')

        # logo
        self.initialize_logo()

        # buttons
        self.initialize_buttons()

        # apply stylesheet
        self.apply_stylesheet()

        # configure display text
        self.configure_parameters()

        # signal
        self.emit_signal()

    def emit_signal(self):
        self.btn_home_2.clicked.connect(
            lambda: self.signal_page_switch.emit(0))
        self.btn_library_2.clicked.connect(
            lambda: self.signal_page_switch.emit(1))
        self.btn_playlist_2.clicked.connect(
            lambda: self.signal_page_switch.emit(2))
        self.btn_download_2.clicked.connect(
            lambda: self.signal_page_switch.emit(3))
        self.btn_settings_2.clicked.connect(
            lambda: self.signal_page_switch.emit(4))

    def initialize_logo(self):
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.logo_3 = QLabel(self)
        self.logo_3.setObjectName('logo_3')
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred,
                                  QSizePolicy.Policy.Preferred)
        sizePolicy2.setHeightForWidth(
            self.logo_3.sizePolicy().hasHeightForWidth())
        self.logo_3.setSizePolicy(sizePolicy2)
        self.logo_3.setMinimumSize(QSize(0, 0))
        self.logo_3.setMaximumSize(QSize(40, 40))
        self.logo_3.setAutoFillBackground(False)
        self.logo_3.setPixmap(QPixmap(IMAGE_LOGO))
        self.logo_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

    def initialize_buttons(self):
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName('verticalLayout')

        # home button
        self.btn_home_2 = QPushButton(self)
        self.btn_home_2.setObjectName('home_btn_expanded')
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.btn_home_2.sizePolicy().hasHeightForWidth())
        self.btn_home_2.setSizePolicy(sizePolicy4)
        self.btn_home_2.setSizeIncrement(QSize(0, 0))
        self.btn_home_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(IMAGE_HOME_BTN_2, QSize(), QIcon.Normal, QIcon.Off)

        self.btn_home_2.setIcon(icon1)
        self.btn_home_2.setIconSize(QSize(18, 18))
        self.btn_home_2.setCheckable(True)
        self.btn_home_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_home_2)

        # library button
        self.btn_library_2 = QPushButton(self)
        self.btn_library_2.setObjectName('library_btn_expanded')
        self.btn_library_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(IMAGE_LIBRARY_BTN_2, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_library_2.setIcon(icon2)
        self.btn_library_2.setIconSize(QSize(18, 18))
        self.btn_library_2.setCheckable(True)
        self.btn_library_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_library_2)

        # playlist button
        self.btn_playlist_2 = QPushButton(self)
        self.btn_playlist_2.setObjectName('playlist_btn_expanded')
        self.btn_playlist_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(IMAGE_PLAYLIST_BTN_2, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_playlist_2.setIcon(icon3)
        self.btn_playlist_2.setIconSize(QSize(18, 18))
        self.btn_playlist_2.setCheckable(True)
        self.btn_playlist_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_playlist_2)

        self.btn_download_2 = QPushButton(self)
        self.btn_download_2.setObjectName('download_btn_expanded')
        self.btn_download_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(IMAGE_DOWNLOAD_BTN_2, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_download_2.setIcon(icon4)
        self.btn_download_2.setIconSize(QSize(18, 18))
        self.btn_download_2.setCheckable(True)
        self.btn_download_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_download_2)

        # veritical spacer
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.spacer_2 = QSpacerItem(
            17, 238, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.spacer_2)

        # setting button
        self.btn_settings_2 = QPushButton(self)
        self.btn_settings_2.setObjectName('setting_btn_expanded')
        icon5 = QIcon()
        icon5.addFile(IMAGE_SETTINGS_BTN_2, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings_2.setIcon(icon5)
        self.btn_settings_2.setIconSize(QSize(18, 18))
        self.btn_settings_2.setCheckable(True)
        self.btn_settings_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_settings_2)

        self.verticalLayout_5.addLayout(self.verticalLayout_2)

    def apply_stylesheet(self):
        with open(STYLE_SIDE_EXPANDED, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def configure_parameters(self):
        self.btn_home_2.setText('Home')
        self.btn_library_2.setText('Library')
        self.btn_playlist_2.setText('Playlist')
        self.btn_download_2.setText('Download')
        self.btn_settings_2.setText('Settings')
