from PySide6.QtCore import (QSize, Qt, Signal)
from PySide6.QtGui import (QCursor, QIcon)
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QLineEdit, QPushButton, QSizePolicy, QSpacerItem)
import os
import logging
from config.style_manager import STYLE_TOP_BAR
from config.image_manager import IMAGE_SEARCH, IMAGE_MENU

logger = logging.getLogger(__name__)

class TopBar(QFrame):
    signal_menu_toggle = Signal(bool)
    
    def __init__(self, centralWidget):
        logger.info('initializing')
        super().__init__(centralWidget)
        self.setObjectName(u"top_bar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy5)

        # initialize components
        logger.info('initializing components')
        self.initialize_components()
        
        # stylesheet
        logger.info('initializing stylesheet')
        self.apply_stylesheet()
        
        # configure display text
        logger.info('configure parameters')
        self.configure_parameters()
        
        # emit signal
        logger.info('emit signal')
        self.emit_signal()
        
    def emit_signal(self):
        self.btn_menu.toggled.connect(self.signal_menu_toggle.emit)

    def initialize_components(self):
        self.horizontalLayout_4 = QHBoxLayout(self)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_menu = QPushButton(self)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy6)
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(IMAGE_MENU, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon6)
        self.btn_menu.setCheckable(True)
        self.btn_menu.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_menu)

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
        icon7.addFile(IMAGE_SEARCH, QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.search_btn)

        self.horizontalSpacer_6 = QSpacerItem(185, 20,
                                              QSizePolicy.Policy.Expanding,
                                              QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

    def apply_stylesheet(self):
        with open(STYLE_TOP_BAR, "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
    
    def configure_parameters(self):
        self.search_bar.setPlaceholderText('Search')