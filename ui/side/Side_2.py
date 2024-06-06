from PySide6.QtCore import (
    QSize, Qt)
from PySide6.QtGui import (QCursor, QIcon, QPixmap)
from PySide6.QtWidgets import (
    QSizePolicy, QFrame, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QVBoxLayout)
import os
from config.style_manager import STYLE_SIDE_EXPANDED
from config.image_manager import (IMAGE_LOGO, IMAGE_HOME_BTN_2, IMAGE_LIBRARY_BTN_2,
                                  IMAGE_PLAYLIST_BTN_2, IMAGE_DOWNLOAD_BTN_2,
                                  IMAGE_SETTING_BTN_2)

IMAGE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/images')
STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class SideExpanded(QFrame):
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
        image_path = os.path.join(IMAGE_DIR, IMAGE_LOGO)
        self.logo_3.setPixmap(QPixmap(image_path))
        self.logo_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

    def initialize_buttons(self):
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName('verticalLayout')

        # home button
        self.home_btn_2 = QPushButton(self)
        self.home_btn_2.setObjectName('home_btn_expanded')
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.home_btn_2.sizePolicy().hasHeightForWidth())
        self.home_btn_2.setSizePolicy(sizePolicy4)
        self.home_btn_2.setSizeIncrement(QSize(0, 0))
        self.home_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_HOME_BTN_2)
        icon1.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)

        self.home_btn_2.setIcon(icon1)
        self.home_btn_2.setIconSize(QSize(18, 18))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_btn_2)

        # library button
        self.library_btn_2 = QPushButton(self)
        self.library_btn_2.setObjectName('library_btn_expanded')
        self.library_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_LIBRARY_BTN_2)
        icon2.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.library_btn_2.setIcon(icon2)
        self.library_btn_2.setIconSize(QSize(18, 18))
        self.library_btn_2.setCheckable(True)
        self.library_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.library_btn_2)

        # playlist button
        self.playlist_btn_2 = QPushButton(self)
        self.playlist_btn_2.setObjectName('playlist_btn_expanded')
        self.playlist_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_PLAYLIST_BTN_2)
        icon3.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.playlist_btn_2.setIcon(icon3)
        self.playlist_btn_2.setIconSize(QSize(18, 18))
        self.playlist_btn_2.setCheckable(True)
        self.playlist_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.playlist_btn_2)

        self.download_btn_2 = QPushButton(self)
        self.download_btn_2.setObjectName('download_btn_expanded')
        self.download_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_DOWNLOAD_BTN_2)
        icon4.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.download_btn_2.setIcon(icon4)
        self.download_btn_2.setIconSize(QSize(18, 18))
        self.download_btn_2.setCheckable(True)
        self.download_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.download_btn_2)

        # veritical spacer
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.spacer_2 = QSpacerItem(
            17, 238, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.spacer_2)

        # setting button
        self.setting_btn_2 = QPushButton(self)
        self.setting_btn_2.setObjectName('setting_btn_expanded')
        icon5 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_SETTING_BTN_2)
        icon5.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.setting_btn_2.setIcon(icon5)
        self.setting_btn_2.setIconSize(QSize(18, 18))
        self.setting_btn_2.setCheckable(True)
        self.setting_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.setting_btn_2)

        self.verticalLayout_5.addLayout(self.verticalLayout_2)

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_SIDE_EXPANDED)

        with open(stylesheet_path, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
