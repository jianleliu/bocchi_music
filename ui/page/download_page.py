"""ui file for download page"""

import logging

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QCursor, QFont, QIcon
from PySide6.QtWidgets import (QCheckBox, QFrame, QGridLayout, QHBoxLayout,
                               QLineEdit, QProgressBar, QPushButton,
                               QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

from config.default_parameters import (DEFAULT_CHECK_AUDIO_ONLY,
                                       DEFAULT_CHECK_USE_DEFAULT_PATH,
                                       DEFAULT_ENCODING,
                                       DEFAULT_PAGE_DOWNLOAD_NAME)
from config.image_manager import IMAGE_DOWNLOAD_BTN_2
from config.style_manager import STYLE_DOWNLOAD_PAGE
from handler.handler_page_download import (handle_check_audio_only,
                                           handle_check_use_default_path,
                                           handle_download_track)

logger = logging.getLogger(__name__)


class DownloadPage(QFrame):
    """download page with QFrame inheritance

    Args:
        QFrame (QFrame): QFrame
    """
    signal_download = Signal()
    signal_repopulate_table_song = Signal()
    # signal_check_audio_only = Signal(bool)
    # signal_check_use_default_path = Signal(bool)
    # signal_check_include_thumbnail = Signal(bool)

    def __init__(self):
        logger.info('initializing')
        super().__init__()
        self.setObjectName(DEFAULT_PAGE_DOWNLOAD_NAME)
        self.vertical_layout_24 = QVBoxLayout(self)
        self.vertical_layout_24.setObjectName('vertical_layout_24')
        self.horizontal_layout_7 = QHBoxLayout()
        self.horizontal_layout_7.setObjectName('horizontal_layout_7')

        # search bar and options
        logger.info('initializing components')
        self._initialize_search_bar()

        # advanced tab
        self._initialize_advanced_tab()

        # status box
        self._initialize_status_box()

        # progress bar
        self._initialize_progress_bar()

        # apply stylesheet
        logger.info('initializing stylesheet')
        self._apply_stylesheet()

        # configure display text
        logger.info('configure parameters')
        self._configure_parameters()

        # # handle event
        logger.info('handle events')
        self.handle_event()

        # emit signal
        logger.info('emit signal')
        self.emit_signal()

    def handle_event(self) -> None:
        """event listener function.
        """
        self.btn_advanced.toggled.connect(
            lambda: self.advanced_widget.setHidden(not self.advanced_widget.isHidden()))
        self.btn_download.clicked.connect(lambda: handle_download_track(
            self, self.url_search_bar.text(), self.signal_repopulate_table_song))
        self.check_audio_only.stateChanged.connect(
            lambda: handle_check_audio_only(self.check_audio_only.isChecked()))
        self.check_use_default_path.stateChanged.connect(
            lambda: handle_check_use_default_path(self.check_use_default_path.isChecked()))

    def emit_signal(self) -> None:
        """signal to be emitted to MainWindow.
        """
        return

    def _initialize_status_box(self) -> None:
        """Initialize status box component.
        """
        self.status_box = QTextBrowser(self)
        self.status_box.setObjectName('status_box')

        self.vertical_layout_24.addWidget(self.status_box)

    def _initialize_advanced_tab(self) -> None:
        """Initialize advanced tab.
        """
        self.btn_advanced = QPushButton(self)
        self.btn_advanced.setObjectName('btn_advanced')
        self.btn_advanced.setCheckable(True)
        self.btn_advanced.setCursor(QCursor(Qt.PointingHandCursor))

        self.vertical_layout_24.addWidget(self.btn_advanced)

        # advanced widget tab
        self.advanced_widget = QWidget(self)
        self.advanced_widget.setObjectName('advanced_widget')
        self.advanced_widget.setMinimumSize(QSize(0, 50))
        self.grid_layout = QGridLayout(self.advanced_widget)
        self.grid_layout.setObjectName('grid_layout')

        # audio only check
        self.check_audio_only = QCheckBox(self.advanced_widget)
        self.check_audio_only.setObjectName('check_audio_only')
        font = QFont()
        font.setPointSize(10)
        self.check_audio_only.setFont(font)
        self.check_audio_only.setChecked(DEFAULT_CHECK_AUDIO_ONLY)

        self.grid_layout.addWidget(self.check_audio_only, 0, 0, 1, 1)

        # default path check
        self.check_use_default_path = QCheckBox(self.advanced_widget)
        self.check_use_default_path.setObjectName('check_use_default_path')
        self.check_use_default_path.setFont(font)
        self.check_use_default_path.setChecked(DEFAULT_CHECK_USE_DEFAULT_PATH)

        self.grid_layout.addWidget(self.check_use_default_path, 1, 0, 1, 1)

        self.vertical_layout_24.addWidget(self.advanced_widget)

    def _initialize_search_bar(self) -> None:
        """Initialize url search bar.
        """
        # search bar
        self.url_search_bar = QLineEdit(self)
        self.url_search_bar.setObjectName('url_search_bar')
        size_policy_7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding,
                                    QSizePolicy.Policy.Fixed)
        size_policy_7.setHeightForWidth(
            self.url_search_bar.sizePolicy().hasHeightForWidth())
        self.url_search_bar.setSizePolicy(size_policy_7)
        # self.url_search_bar.setStyleSheet('border-bottom: 1px solid;')

        self.horizontal_layout_7.addWidget(self.url_search_bar)

        # download button
        self.btn_download = QPushButton(self)
        self.btn_download.setObjectName('btn_download')
        size_policy_6 = QSizePolicy(QSizePolicy.Policy.Fixed,
                                    QSizePolicy.Policy.Fixed)
        size_policy_6.setHeightForWidth(
            self.btn_download.sizePolicy().hasHeightForWidth())
        self.btn_download.setSizePolicy(size_policy_6)
        self.btn_download.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_download.setIcon(QIcon(IMAGE_DOWNLOAD_BTN_2))

        self.horizontal_layout_7.addWidget(self.btn_download)

        self.vertical_layout_24.addLayout(self.horizontal_layout_7)

    def _initialize_progress_bar(self) -> None:
        """Initialize progress bar.
        """
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setObjectName('progress_bar')
        self.progress_bar.setValue(100)

        self.vertical_layout_24.addWidget(self.progress_bar)

    def _apply_stylesheet(self) -> None:
        """Apply stylesheet
        """
        with open(STYLE_DOWNLOAD_PAGE, 'r', encoding=DEFAULT_ENCODING) as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def _configure_parameters(self) -> None:
        """Configure ui component default parameters.
        """
        self.url_search_bar.setPlaceholderText('YouTube URL: song or playlist')
        self.btn_advanced.setText('Advanced')
        self.check_audio_only.setText('Audio Only')
        self.check_use_default_path.setText('Use Default Path')
        self.status_box.setText('...')
        self.progress_bar.setFormat('0')
