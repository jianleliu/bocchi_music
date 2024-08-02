"""library page."""
import logging

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLineEdit, QPushButton,
                               QSizePolicy, QTableWidget, QTableWidgetItem,
                               QVBoxLayout)

from config.default_parameters import (DEFAULT_ENCODING,
                                       DEFAULT_PAGE_LIBRARY_NAME)
from config.style_manager import STYLE_LIBRARY_PAGE
from handler.handler_page_library import *

logger = logging.getLogger(__name__)


class LibraryPage(QFrame):
    """home page ui, currently blank.

    Args:
        QFrame (QFrame): PySide6.QtWidgets
    """
    signal_populate_table_song = Signal()
    signal_play_pause_clicked = Signal(int)
    signal_btn_shuffle_clicked = Signal()
    signal_btn_library_populate_clicked = Signal()

    def __init__(self):
        logger.info('initializing')
        super().__init__()
        self.setObjectName(DEFAULT_PAGE_LIBRARY_NAME)
        self.first_show = True

        # initialize song table
        logger.info('initializing table_song')
        self._initilize_table_song()

        # layout
        self._initialize_layout()

        # apply stylesheet
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
        self.table_song.verticalHeader().sectionClicked.connect(
            lambda row: self.signal_play_pause_clicked.emit(row))
        self.btn_shuffle.clicked.connect(self.signal_btn_shuffle_clicked)
        self.btn_library_populate.clicked.connect(
            self.signal_btn_library_populate_clicked)
        self.le_search_bar.textChanged.connect(
            lambda: handle_le_search_bar(self.table_song, self.le_search_bar.text()))

    def showEvent(self, event) -> None:
        """override default showEvent

        Args:
            event (_type_): default parameter
        """
        super().showEvent(event)

        if self.first_show:
            self.signal_populate_table_song.emit()
            self.first_show = False

    def _initilize_table_song(self) -> None:
        """_initilize_table_song
        """
        self.le_search_bar = QLineEdit(self)
        self.le_search_bar.setObjectName('le_search_bar')
        self.le_search_bar.setCursor(QCursor(Qt.IBeamCursor))
        self.le_search_bar.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)

        self.btn_library_populate = QPushButton(self)
        self.btn_library_populate.setObjectName('btn_library_populate')
        self.btn_library_populate.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_shuffle = QPushButton(self)
        self.btn_shuffle.setObjectName('btn_shuffle')
        self.btn_shuffle.setCursor(QCursor(Qt.PointingHandCursor))

        self.table_song = QTableWidget(self)
        if self.table_song.columnCount() < 6:
            self.table_song.setColumnCount(6)
        self.table_song_header0 = QTableWidgetItem()
        self.table_song.setHorizontalHeaderItem(0, self.table_song_header0)
        self.table_song_header1 = QTableWidgetItem()
        self.table_song.setHorizontalHeaderItem(1, self.table_song_header1)
        self.table_song_header2 = QTableWidgetItem()
        self.table_song.setHorizontalHeaderItem(2, self.table_song_header2)
        self.table_song_header3 = QTableWidgetItem()
        self.table_song.setHorizontalHeaderItem(3, self.table_song_header3)
        self.table_song_header4 = QTableWidgetItem()
        self.table_song.setHorizontalHeaderItem(4, self.table_song_header4)
        self.table_song_header5 = QTableWidgetItem()
        self.table_song.setHorizontalHeaderItem(5, self.table_song_header5)
        self.table_song.setObjectName('table_song')
        self.table_song.viewport().setProperty("cursor",
                                               QCursor(Qt.PointingHandCursor))

        self.table_song.setLineWidth(1)
        self.table_song.setDragDropOverwriteMode(False)
        self.table_song.setAlternatingRowColors(True)
        self.table_song.setSortingEnabled(False)
        self.table_song.setWordWrap(True)
        self.table_song.setRowCount(0)
        self.table_song.setColumnCount(6)

    def _initialize_layout(self) -> None:
        """_initialize_layout
        """
        self.vertical = QVBoxLayout(self)
        self.horizontal = QHBoxLayout()

        self.horizontal.addWidget(self.le_search_bar)
        self.horizontal.addWidget(self.btn_library_populate)
        self.horizontal.addWidget(self.btn_shuffle)

        self.vertical.addLayout(self.horizontal)
        self.vertical.addWidget(self.table_song)

    def _apply_stylesheet(self):
        """_apply_stylesheet
        """
        with open(STYLE_LIBRARY_PAGE, 'r', encoding=DEFAULT_ENCODING) as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def _configure_parameters(self) -> None:
        """_configure_parameters
        """
        self.table_song_header0.setText('Title')
        self.table_song_header1.setText('Artist')
        self.table_song_header2.setText('Last Played')
        self.table_song_header3.setText('Date Added')
        self.table_song_header4.setText('Times Played')
        self.btn_shuffle.setText('Shuffle')
        self.btn_library_populate.setText('Show all songs')
        self.le_search_bar.setPlaceholderText('Search table')
