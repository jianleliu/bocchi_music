"""side bar shrinked."""
import logging

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QCursor, QIcon, QPixmap
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout)

from config.image_manager import (IMAGE_DOWNLOAD_BTN_1, IMAGE_HOME_BTN_1,
                                  IMAGE_LIBRARY_BTN_1, IMAGE_LOGO,
                                  IMAGE_PLAYLIST_BTN_1, IMAGE_SETTINGS_BTN_1)
from config.style_manager import STYLE_SIDE_SHRINKED
from config.default_parameters import DEFAULT_ENCODING

logger = logging.getLogger(__name__)


class SideShrinked(QFrame):
    """shrinked ver of side bar, inherit QFrame.

    Args:
        QFrame (QFrame): PySide6.QtWidgets
    """
    signal_home_btn = Signal(int)
    signal_library_btn = Signal(int)
    signal_playlist_btn = Signal(int)
    signal_download_btn = Signal(int)
    signal_settings_btn = Signal(int)
    signal_page_switch = Signal(int)

    def __init__(self, centralWidget):
        """child of centralWidget.

        Args:
            centralWidget (QFrame): PySide6.QtWidgets
        """
        logger.info('initializing')
        super().__init__(centralWidget)
        self.setObjectName('side_shrinked')
        self.setHidden(True)

        # widget expansion policies
        size_policy_1 = QSizePolicy(QSizePolicy.Policy.Fixed,
                                    QSizePolicy.Policy.Expanding)
        size_policy_1.setHorizontalStretch(0)
        size_policy_1.setVerticalStretch(0)
        size_policy_1.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy_1)
        self.setMouseTracking(False)

        self.vertical_layout_3 = QVBoxLayout(self)
        self.vertical_layout_3.setObjectName('vertical_layout_3')

        # sidebar logo
        logger.info('initializing components')
        self._initialize_logo()

        # list of side buttons
        self._initialize_buttons()

        # apply stylesheet
        logger.info('initializing stylesheet')
        self._apply_stylesheet()

        # signals
        logger.info('emit signal')
        self._emit_signal()

    def _emit_signal(self) -> None:
        """_emit_signal.
        """
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

    def _initialize_logo(self) -> None:
        """_initialize_logo.
        """
        self.horizontal_layout_2 = QHBoxLayout()
        self.horizontal_layout_2.setObjectName('logo_horizontal_alignment')
        self.logo_5 = QLabel(self)
        self.logo_5.setObjectName('logo_5')
        size_policy_2 = QSizePolicy(QSizePolicy.Policy.Preferred,
                                    QSizePolicy.Policy.Preferred)
        size_policy_2.setHorizontalStretch(0)
        size_policy_2.setVerticalStretch(0)
        size_policy_2.setHeightForWidth(
            self.logo_5.sizePolicy().hasHeightForWidth())
        self.logo_5.setSizePolicy(size_policy_2)
        self.logo_5.setMinimumSize(QSize(0, 0))
        self.logo_5.setMaximumSize(QSize(40, 40))
        self.logo_5.setAutoFillBackground(False)
        self.logo_5.setPixmap(QPixmap(IMAGE_LOGO))
        self.logo_5.setScaledContents(True)

        self.horizontal_layout_2.addWidget(self.logo_5)
        self.vertical_layout_3.addLayout(self.horizontal_layout_2)

    def _initialize_buttons(self) -> None:
        """initalize_buttons.
        """
        # home button
        self.vertical_layout_4 = QVBoxLayout()
        self.vertical_layout_4.setObjectName('buttons_vertical_alignment')
        self.btn_home_1 = QPushButton(self)
        self.btn_home_1.setObjectName('home_btn_shrinked')
        self.btn_home_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(IMAGE_HOME_BTN_1, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home_1.setIcon(icon1)
        self.btn_home_1.setIconSize(QSize(18, 18))
        self.btn_home_1.setCheckable(True)
        self.btn_home_1.setAutoExclusive(True)

        self.vertical_layout_4.addWidget(self.btn_home_1)

        # library button
        self.btn_library_1 = QPushButton(self)
        self.btn_library_1.setObjectName('library_btn_shrinked')
        self.btn_library_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(IMAGE_LIBRARY_BTN_1, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_library_1.setIcon(icon2)
        self.btn_library_1.setIconSize(QSize(18, 18))
        self.btn_library_1.setCheckable(True)
        self.btn_library_1.setAutoExclusive(True)

        self.vertical_layout_4.addWidget(self.btn_library_1)

        # playlist button
        self.btn_playlist_1 = QPushButton(self)
        self.btn_playlist_1.setObjectName('playlist_btn_shrinked')
        self.btn_playlist_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(IMAGE_PLAYLIST_BTN_1, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_playlist_1.setIcon(icon3)
        self.btn_playlist_1.setIcon(icon3)
        self.btn_playlist_1.setIconSize(QSize(18, 18))
        self.btn_playlist_1.setCheckable(True)
        self.btn_playlist_1.setAutoExclusive(True)

        self.vertical_layout_4.addWidget(self.btn_playlist_1)

        # download button
        self.btn_download_1 = QPushButton(self)
        self.btn_download_1.setObjectName('download_btn_shrinked')
        self.btn_download_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(IMAGE_DOWNLOAD_BTN_1, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_download_1.setIcon(icon4)
        self.btn_download_1.setIconSize(QSize(18, 18))
        self.btn_download_1.setCheckable(True)
        self.btn_download_1.setAutoExclusive(True)

        self.vertical_layout_4.addWidget(self.btn_download_1)

        # add a spacer for style
        self.vertical_layout_3.addLayout(self.vertical_layout_4)

        self.vertical_spacer_3 = QSpacerItem(20, 188, QSizePolicy.Policy.Minimum,
                                             QSizePolicy.Policy.Expanding)

        self.vertical_layout_3.addItem(self.vertical_spacer_3)

        # setting button
        self.btn_settings_1 = QPushButton(self)
        self.btn_settings_1.setObjectName('setting_btn_shrinked')
        icon5 = QIcon()
        icon5.addFile(IMAGE_SETTINGS_BTN_1, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings_1.setIcon(icon5)
        self.btn_settings_1.setIconSize(QSize(18, 18))
        self.btn_settings_1.setCheckable(True)
        self.btn_settings_1.setAutoExclusive(True)

        self.vertical_layout_3.addWidget(self.btn_settings_1)

    def _apply_stylesheet(self) -> None:
        """_apply_stylesheet
        """
        with open(STYLE_SIDE_SHRINKED, "r", encoding=DEFAULT_ENCODING) as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
