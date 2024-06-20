from PySide6.QtCore import (Qt, Signal, QSortFilterProxyModel)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QFrame, QGridLayout, QTableView,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QTableWidget, QLineEdit, QVBoxLayout, QHBoxLayout,
                               QTableWidgetItem)
import os
import logging
from configparser import ConfigParser
from config.style_manager import STYLE_LIBRARY_PAGE
from config.default_parameters import INI_FILE_PATH
from config.sections import SECTION_SETTINGS_TAB_1
from config.keys import KEY_DIR_TRACK_DOWNLOAD
from handler.handler_page_library import *

logger = logging.getLogger(__name__)


class LibraryPage(QFrame):
    signal_populate_table_song = Signal()
    signal_play_pause_clicked = Signal(int)
    signal_btn_shuffle_clicked = Signal()
    signal_btn_library_populate_clicked = Signal()

    def __init__(self):
        logger.info('initializing')
        super().__init__()
        self.setObjectName('library_page')
        self.first_show = True

        # initialize song table
        logger.info('initializing table_song')
        self.initilize_table_song()

        # layout
        self.initialize_layout()

        # apply stylesheet
        logger.info('initializing stylesheet')
        self.apply_stylesheet()

        # configure display text
        logger.info('configure parameters')
        self.configure_parameters()

        # emit signal
        logger.info('emit signal')
        self.emit_signal()

    def emit_signal(self):
        self.table_song.verticalHeader().sectionClicked.connect(
            lambda row: self.signal_play_pause_clicked.emit(row))
        self.btn_shuffle.clicked.connect(self.signal_btn_shuffle_clicked)
        self.btn_library_populate.clicked.connect(
            self.signal_btn_library_populate_clicked)

        self.le_search_bar.textChanged.connect(
            lambda: handle_le_search_bar(self.table_song, self.le_search_bar.text()))

    def showEvent(self, event):
        super().showEvent(event)

        if self.first_show:
            self.signal_populate_table_song.emit()
            self.first_show = False

    def initilize_table_song(self):
        self.le_search_bar = QLineEdit(self)
        self.le_search_bar.setObjectName('le_search_bar')
        self.le_search_bar.setCursor(QCursor(Qt.IBeamCursor))
        self.le_search_bar.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)

        self.btn_library_populate = QPushButton(self)
        self.btn_library_populate.setObjectName('btn_library_populate')
        self.btn_library_populate.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_shuffle = QPushButton(self)
        self.btn_shuffle.setObjectName(u"btn_shuffle")
        self.btn_shuffle.setCursor(QCursor(Qt.PointingHandCursor))

        self.table_song = QTableWidget(self)
        if (self.table_song.columnCount() < 6):
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
        self.table_song.setObjectName(u"table_song")
        self.table_song.viewport().setProperty("cursor",
                                               QCursor(Qt.PointingHandCursor))

        self.table_song.setLineWidth(1)
        self.table_song.setDragDropOverwriteMode(False)
        self.table_song.setAlternatingRowColors(True)
        self.table_song.setSortingEnabled(False)
        self.table_song.setWordWrap(True)
        self.table_song.setRowCount(0)
        self.table_song.setColumnCount(6)
        

    def initialize_layout(self):
        self.vertical = QVBoxLayout(self)
        self.horizontal = QHBoxLayout()

        self.horizontal.addWidget(self.le_search_bar)
        self.horizontal.addWidget(self.btn_library_populate)
        self.horizontal.addWidget(self.btn_shuffle)

        self.vertical.addLayout(self.horizontal)
        self.vertical.addWidget(self.table_song)

    def apply_stylesheet(self):
        with open(STYLE_LIBRARY_PAGE, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def configure_parameters(self):
        self.table_song_header0.setText('Title')
        self.table_song_header1.setText('Artist')
        self.table_song_header2.setText('Last Played')
        self.table_song_header3.setText('Date Added')
        self.table_song_header4.setText('Times Played')
        self.btn_shuffle.setText('Shuffle')
        self.btn_library_populate.setText('Show all songs')
        self.le_search_bar.setPlaceholderText('Search table')
