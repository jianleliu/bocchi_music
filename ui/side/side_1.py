from PySide6.QtCore import (QSize, Qt)
from PySide6.QtGui import (QCursor, QIcon, QPixmap)
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout)
import os
from config.style_manager import STYLE_SIDE_SHRINKED
from config.image_manager import (IMAGE_LOGO, IMAGE_HOME_BTN_1, IMAGE_LIBRARY_BTN_1,
                                  IMAGE_PLAYLIST_BTN_1, IMAGE_DOWNLOAD_BTN_1,
                                  IMAGE_SETTING_BTN_1)

IMAGE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/images')
STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class SideShrinked(QFrame):
    def __init__(self, centralWidget):
        super().__init__(centralWidget)
        self.setObjectName(u'side_shrinked')

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
        self.home_btn_1 = QPushButton(self)
        self.home_btn_1.setObjectName(u'home_btn_shrinked')
        self.home_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_HOME_BTN_1)
        icon1.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_1.setIcon(icon1)
        self.home_btn_1.setIconSize(QSize(18, 18))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.home_btn_1)

        # library button
        self.library_btn_1 = QPushButton(self)
        self.library_btn_1.setObjectName(u'library_btn_shrinked')
        self.library_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_LIBRARY_BTN_1)
        icon2.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.library_btn_1.setIcon(icon2)
        self.library_btn_1.setIconSize(QSize(18, 18))
        self.library_btn_1.setCheckable(True)
        self.library_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.library_btn_1)

        # playlist button
        self.playlist_btn_1 = QPushButton(self)
        self.playlist_btn_1.setObjectName(u'playlist_btn_shrinked')
        self.playlist_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_PLAYLIST_BTN_1)
        icon3.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.playlist_btn_1.setIcon(icon3)
        self.playlist_btn_1.setIcon(icon3)
        self.playlist_btn_1.setIconSize(QSize(18, 18))
        self.playlist_btn_1.setCheckable(True)
        self.playlist_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.playlist_btn_1)

        # download button
        self.download_btn_1 = QPushButton(self)
        self.download_btn_1.setObjectName(u'download_btn_shrinked')
        self.download_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_DOWNLOAD_BTN_1)
        icon4.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.download_btn_1.setIcon(icon4)
        self.download_btn_1.setIconSize(QSize(18, 18))
        self.download_btn_1.setCheckable(True)
        self.download_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.download_btn_1)

        # add a spacer for style
        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 188, QSizePolicy.Policy.Minimum,
                                            QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        # setting button
        self.setting_btn_1 = QPushButton(self)
        self.setting_btn_1.setObjectName(u'setting_btn_shrinked')
        icon5 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_SETTING_BTN_1)
        icon5.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.setting_btn_1.setIcon(icon5)
        self.setting_btn_1.setIconSize(QSize(18, 18))
        self.setting_btn_1.setCheckable(True)
        self.setting_btn_1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.setting_btn_1)

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_SIDE_SHRINKED)

        with open(stylesheet_path, "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
