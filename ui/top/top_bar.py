from PySide6.QtCore import (QSize, Qt)
from PySide6.QtGui import (QCursor, QIcon)
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QLineEdit, QPushButton, QSizePolicy, QSpacerItem)
import os
from config.style_manager import STYLE_TOP_BAR
from config.image_manager import IMAGE_SEARCH, IMAGE_MENU


IMAGE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/images')
STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class TopBar(QFrame):
    def __init__(self, centralWidget):
        super().__init__(centralWidget)
        self.setObjectName(u"top_bar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy5)

        # initialize components
        self.initialize_components()
        # stylesheet
        self.apply_stylesheet()

    def initialize_components(self):
        self.horizontalLayout_4 = QHBoxLayout(self)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menu_btn = QPushButton(self)
        self.menu_btn.setObjectName(u"menu_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy6)
        self.menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_MENU)
        icon6.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon6)
        self.menu_btn.setCheckable(True)
        self.menu_btn.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.menu_btn)

        self.horizontalSpacer_5 = QSpacerItem(
            138, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.search_bar = QLineEdit(self)
        self.search_bar.setObjectName(u"search_bar")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(
            self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy7)
        self.horizontalLayout_3.addWidget(self.search_bar)

        self.search_btn = QPushButton(self)
        self.search_btn.setObjectName(u"search_btn")
        sizePolicy6.setHeightForWidth(
            self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy6)
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_SEARCH)
        icon7.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.search_btn)

        self.horizontalSpacer_6 = QSpacerItem(185, 20,
                                              QSizePolicy.Policy.Expanding,
                                              QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_TOP_BAR)

        with open(stylesheet_path, "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
