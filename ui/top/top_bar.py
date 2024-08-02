"""ui file for top bar."""
import logging

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLineEdit, QPushButton,
                               QSizePolicy, QSpacerItem)

from config.image_manager import IMAGE_MENU, IMAGE_SEARCH
from config.style_manager import STYLE_TOP_BAR
from config.default_parameters import DEFAULT_ENCODING

logger = logging.getLogger(__name__)


class TopBar(QFrame):
    """top bar, inherit QFrame.

    Args:
        QFrame (QFrame): PySide6.QtWidgets
    """
    signal_menu_toggle = Signal(bool)

    def __init__(self, centralWidget):
        """child of centralWidget.

        Args:
            centralWidget (QFrame): PySide6.QtWidgets
        """
        logger.info('initializing')
        super().__init__(centralWidget)
        self.setObjectName('top_bar')
        size_policy_5 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                    QSizePolicy.Policy.Fixed)
        size_policy_5.setHorizontalStretch(0)
        size_policy_5.setVerticalStretch(0)
        size_policy_5.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy_5)

        # initialize components
        logger.info('initializing components')
        self._initialize_components()

        # stylesheet
        logger.info('initializing stylesheet')
        self._apply_stylesheet()

        # configure display text
        logger.info('configure parameters')
        self._configure_parameters()

        # emit signal
        logger.info('emit signal')
        self._emit_signal()

    def _emit_signal(self) -> None:
        """_emit_signal
        """
        self.btn_menu.toggled.connect(self.signal_menu_toggle.emit)

    def _initialize_components(self) -> None:
        """_initialize_components
        """
        self.horizontal_layout_4 = QHBoxLayout(self)
        self.horizontal_layout_4.setObjectName('horizontal_layout_4')
        self.horizontal_layout_3 = QHBoxLayout()
        self.horizontal_layout_3.setObjectName('horizontal_layout_3')
        self.btn_menu = QPushButton(self)
        self.btn_menu.setObjectName('btn_men')
        size_policy_6 = QSizePolicy(QSizePolicy.Policy.Fixed,
                                    QSizePolicy.Policy.Fixed)
        size_policy_6.setHorizontalStretch(0)
        size_policy_6.setVerticalStretch(0)
        size_policy_6.setHeightForWidth(
            self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(size_policy_6)
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(IMAGE_MENU, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon6)
        self.btn_menu.setCheckable(True)
        self.btn_menu.setAutoExclusive(True)

        self.horizontal_layout_3.addWidget(self.btn_menu)

        self.horizontal_spacer_5 = QSpacerItem(
            138, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_3.addItem(self.horizontal_spacer_5)

        self.search_bar = QLineEdit(self)
        self.search_bar.setObjectName('search_bar')
        size_policy_7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding,
                                    QSizePolicy.Policy.Fixed)
        size_policy_7.setHorizontalStretch(0)
        size_policy_7.setVerticalStretch(0)
        size_policy_7.setHeightForWidth(
            self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(size_policy_7)
        self.horizontal_layout_3.addWidget(self.search_bar)

        self.search_btn = QPushButton(self)
        self.search_btn.setObjectName('search_btn')
        size_policy_6.setHeightForWidth(
            self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(size_policy_6)
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(IMAGE_SEARCH, QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon7)

        self.horizontal_layout_3.addWidget(self.search_btn)

        self.horizontal_spacer_6 = QSpacerItem(185, 20,
                                               QSizePolicy.Policy.Expanding,
                                               QSizePolicy.Policy.Minimum)

        self.horizontal_layout_3.addItem(self.horizontal_spacer_6)

        self.horizontal_layout_4.addLayout(self.horizontal_layout_3)

    def _apply_stylesheet(self) -> None:
        """_apply_stylesheet
        """
        with open(STYLE_TOP_BAR, "r", encoding=DEFAULT_ENCODING) as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def _configure_parameters(self) -> None:
        """_configure_parameters
        """
        self.search_bar.setPlaceholderText('Search')
