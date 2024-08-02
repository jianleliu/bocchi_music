"""side bar expanded."""
import logging

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QCursor, QIcon, QPixmap
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout)

from config.default_parameters import DEFAULT_ENCODING
from config.image_manager import (IMAGE_DOWNLOAD_BTN_2, IMAGE_HOME_BTN_2,
                                  IMAGE_LIBRARY_BTN_2, IMAGE_LOGO,
                                  IMAGE_PLAYLIST_BTN_2, IMAGE_SETTINGS_BTN_2)
from config.style_manager import STYLE_SIDE_EXPANDED

logger = logging.getLogger(__name__)


class SideExpanded(QFrame):
    """expanded ver of side bar, inherit QFrame.

    Args:
        QFrame (QFrame): PySide6.QtWidgets
    """
    signal_page_switch = Signal(int)

    def __init__(self, centralWidget):
        """child of centralWidget.

        Args:
            centralWidget (QFrame): PySide6.QtWidgets
        """
        logger.info('initializing')
        super().__init__(centralWidget)
        self.setObjectName('side_expanded')
        size_policy_3 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        size_policy_3.setHorizontalStretch(0)
        size_policy_3.setVerticalStretch(0)
        size_policy_3.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy_3)

        # layouts
        self.vertical_layout_5 = QVBoxLayout(self)
        self.vertical_layout_5.setObjectName('vertical_layout_5')
        self.vertical_layout_2 = QVBoxLayout()
        self.vertical_layout_2.setObjectName('vertical_layout_expanded')

        # logo
        logger.info('initializing components')
        self._initialize_logo()

        # buttons
        self._initialize_buttons()

        # apply stylesheet
        logger.info('initializing stylesheet')
        self._apply_stylesheet()

        # configure display text
        logger.info('configure parameters')
        self._configure_parameters()

        # signal
        logger.info('emit signal')
        self.emit_signal()

    def emit_signal(self):
        """emit_signal.
        """
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

    def _initialize_logo(self) -> None:
        """_initialize_logo.
        """
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setObjectName('horizontal_layout')
        self.logo_3 = QLabel(self)
        self.logo_3.setObjectName('logo_3')
        size_policy2 = QSizePolicy(QSizePolicy.Policy.Preferred,
                                   QSizePolicy.Policy.Preferred)
        size_policy2.setHeightForWidth(
            self.logo_3.sizePolicy().hasHeightForWidth())
        self.logo_3.setSizePolicy(size_policy2)
        self.logo_3.setMinimumSize(QSize(0, 0))
        self.logo_3.setMaximumSize(QSize(40, 40))
        self.logo_3.setAutoFillBackground(False)
        self.logo_3.setPixmap(QPixmap(IMAGE_LOGO))
        self.logo_3.setScaledContents(True)

        self.horizontal_layout.addWidget(self.logo_3)
        self.vertical_layout_2.addLayout(self.horizontal_layout)

    def _initialize_buttons(self) -> None:
        """initalize_buttons.
        """
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setObjectName('vertical_layout')

        # home button
        self.btn_home_2 = QPushButton(self)
        self.btn_home_2.setObjectName('home_btn_expanded')
        size_policy_4 = QSizePolicy(QSizePolicy.Policy.Minimum,
                                    QSizePolicy.Policy.Fixed)
        size_policy_4.setHorizontalStretch(0)
        size_policy_4.setVerticalStretch(0)
        size_policy_4.setHeightForWidth(
            self.btn_home_2.sizePolicy().hasHeightForWidth())
        self.btn_home_2.setSizePolicy(size_policy_4)
        self.btn_home_2.setSizeIncrement(QSize(0, 0))
        self.btn_home_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(IMAGE_HOME_BTN_2, QSize(), QIcon.Normal, QIcon.Off)

        self.btn_home_2.setIcon(icon1)
        self.btn_home_2.setIconSize(QSize(18, 18))
        self.btn_home_2.setCheckable(True)
        self.btn_home_2.setAutoExclusive(True)

        self.vertical_layout.addWidget(self.btn_home_2)

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

        self.vertical_layout.addWidget(self.btn_library_2)

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

        self.vertical_layout.addWidget(self.btn_playlist_2)

        self.btn_download_2 = QPushButton(self)
        self.btn_download_2.setObjectName('download_btn_expanded')
        self.btn_download_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(IMAGE_DOWNLOAD_BTN_2, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_download_2.setIcon(icon4)
        self.btn_download_2.setIconSize(QSize(18, 18))
        self.btn_download_2.setCheckable(True)
        self.btn_download_2.setAutoExclusive(True)

        self.vertical_layout.addWidget(self.btn_download_2)

        # veritical spacer
        self.vertical_layout_2.addLayout(self.vertical_layout)

        self.spacer_2 = QSpacerItem(
            17, 238, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout_2.addItem(self.spacer_2)

        # setting button
        self.btn_settings_2 = QPushButton(self)
        self.btn_settings_2.setObjectName('setting_btn_expanded')
        icon5 = QIcon()
        icon5.addFile(IMAGE_SETTINGS_BTN_2, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings_2.setIcon(icon5)
        self.btn_settings_2.setIconSize(QSize(18, 18))
        self.btn_settings_2.setCheckable(True)
        self.btn_settings_2.setAutoExclusive(True)

        self.vertical_layout_2.addWidget(self.btn_settings_2)

        self.vertical_layout_5.addLayout(self.vertical_layout_2)

    def _apply_stylesheet(self) -> None:
        """_apply_stylesheet.
        """
        with open(STYLE_SIDE_EXPANDED, 'r', encoding=DEFAULT_ENCODING) as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def _configure_parameters(self) -> None:
        """_configure_parameters.
        """
        self.btn_home_2.setText('Home')
        self.btn_library_2.setText('Library')
        self.btn_playlist_2.setText('Playlist')
        self.btn_download_2.setText('Download')
        self.btn_settings_2.setText('Settings')
