from PySide6.QtCore import (QSize, Qt, Signal)
from PySide6.QtGui import (QCursor, QIcon, QPixmap)
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout)
import os
from config.style_manager import STYLE_SIDE_SHRINKED
from config.image_manager import (IMAGE_LOGO, IMAGE_HOME_BTN_1, IMAGE_LIBRARY_BTN_1,
                                  IMAGE_PLAYLIST_BTN_1, IMAGE_DOWNLOAD_BTN_1,
                                  IMAGE_SETTINGS_BTN_1)

IMAGE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/images')
STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class SideShrinked(QFrame):
    signal_home_btn = Signal(int)
    signal_library_btn = Signal(int)
    signal_playlist_btn = Signal(int)
    signal_download_btn = Signal(int)
    signal_settings_btn = Signal(int)
    signal_page_switch = Signal(int)

    def __init__(self, centralWidget):
        super().__init__(centralWidget)
        self.setObjectName(u'side_shrinked')
        self.setHidden(True)

        # widget expansion policies
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed,
                                  QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy1)
        self.setMouseTracking(False)

        self.verticalLayout_3 = QVBoxLayout(self)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        # sidebar logo
        self.initialize_logo()

        # list of side buttons
        self.initialize_buttons()

        # apply stylesheet
        self.apply_stylesheet()

        # signals
        self.emit_signal()

    def emit_signal(self):
        self.btn_home_1.clicked.connect(
            lambda: self.signal_page_switch.emit(0))
        self.btn_library_1.clicked.connect(
            lambda: self.signal_page_switch.emit(1))
        self.btn_playlist_1.clicked.connect(
            lambda: self.signal_page_switch.emit(2))
        self.btn_download_1.clicked.connect(
            lambda: self.signal_page_switch.emit(3))
        self.btn_settings_1.clicked.connect(
            lambda: self.signal_page_switch.emit(4))

    def initialize_logo(self):
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u'logo_horizontal_alignment')
        self.logo_5 = QLabel(self)
        self.logo_5.setObjectName(u'logo_5')
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred,
                                  QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.logo_5.sizePolicy().hasHeightForWidth())
        self.logo_5.setSizePolicy(sizePolicy2)
        self.logo_5.setMinimumSize(QSize(0, 0))
        self.logo_5.setMaximumSize(QSize(40, 40))
        self.logo_5.setAutoFillBackground(False)
        image_path = os.path.join(IMAGE_DIR, IMAGE_LOGO)
        self.logo_5.setPixmap(QPixmap(image_path))
        self.logo_5.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

    def initialize_buttons(self):
        # home button
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u'buttons_vertical_alignment')
        self.btn_home_1 = QPushButton(self)
        self.btn_home_1.setObjectName(u'home_btn_shrinked')
        self.btn_home_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_HOME_BTN_1)
        icon1.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home_1.setIcon(icon1)
        self.btn_home_1.setIconSize(QSize(18, 18))
        self.btn_home_1.setCheckable(True)
        self.btn_home_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.btn_home_1)

        # library button
        self.btn_library_1 = QPushButton(self)
        self.btn_library_1.setObjectName(u'library_btn_shrinked')
        self.btn_library_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_LIBRARY_BTN_1)
        icon2.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_library_1.setIcon(icon2)
        self.btn_library_1.setIconSize(QSize(18, 18))
        self.btn_library_1.setCheckable(True)
        self.btn_library_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.btn_library_1)

        # playlist button
        self.btn_playlist_1 = QPushButton(self)
        self.btn_playlist_1.setObjectName(u'playlist_btn_shrinked')
        self.btn_playlist_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_PLAYLIST_BTN_1)
        icon3.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_playlist_1.setIcon(icon3)
        self.btn_playlist_1.setIcon(icon3)
        self.btn_playlist_1.setIconSize(QSize(18, 18))
        self.btn_playlist_1.setCheckable(True)
        self.btn_playlist_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.btn_playlist_1)

        # download button
        self.btn_download_1 = QPushButton(self)
        self.btn_download_1.setObjectName(u'download_btn_shrinked')
        self.btn_download_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_DOWNLOAD_BTN_1)
        icon4.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_download_1.setIcon(icon4)
        self.btn_download_1.setIconSize(QSize(18, 18))
        self.btn_download_1.setCheckable(True)
        self.btn_download_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.btn_download_1)

        # add a spacer for style
        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 188, QSizePolicy.Policy.Minimum,
                                            QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        # setting button
        self.btn_settings_1 = QPushButton(self)
        self.btn_settings_1.setObjectName(u'setting_btn_shrinked')
        icon5 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_SETTINGS_BTN_1)
        icon5.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings_1.setIcon(icon5)
        self.btn_settings_1.setIconSize(QSize(18, 18))
        self.btn_settings_1.setCheckable(True)
        self.btn_settings_1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_settings_1)

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_SIDE_SHRINKED)

        with open(stylesheet_path, "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
