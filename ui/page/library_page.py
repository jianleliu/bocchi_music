from PySide6.QtCore import (Qt, Signal)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QFrame, QGridLayout,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QTableWidget,
                               QTableWidgetItem)
import os
from configparser import ConfigParser
from config.style_manager import STYLE_LIBRARY_PAGE
from config.default_parameters import INI_FILE_PATH
from config.sections import SECTION_SETTINGS_TAB_1
from config.keys import KEY_DIR_TRACK_DOWNLOAD

STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class LibraryPage(QFrame):
    signal_populate_table_song = Signal()
    signal_play_pause_clicked = Signal(int)

    def __init__(self):
        super().__init__()
        self.setObjectName('library_page')
        self.first_show = True

        # initialize song table
        self.initilize_table_song()

        # populate song table

        # apply stylesheet
        self.apply_stylesheet()

        # configure display text
        self.configure_parameters()

        # emit signal
        self.emit_signal()

    def emit_signal(self):
        self.table_song.verticalHeader().sectionClicked.connect(
            lambda row: self.signal_play_pause_clicked.emit(row))

    def showEvent(self, event):
        super().showEvent(event)

        if self.first_show:
            self.signal_populate_table_song.emit()
            self.first_show = False

    def initilize_table_song(self):
        self.gridLayout_3 = QGridLayout(self)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(494, 20,
                                            QSizePolicy.Policy.Expanding,
                                            QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.btn_shuffle = QPushButton(self)
        self.btn_shuffle.setObjectName(u"btn_shuffle")
        self.btn_shuffle.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.btn_shuffle, 0, 1, 1, 1)

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
        self.table_song.setSortingEnabled(True)
        self.table_song.setWordWrap(True)
        self.table_song.setRowCount(0)
        self.table_song.setColumnCount(6)

        self.gridLayout_3.addWidget(self.table_song, 1, 0, 1, 2)

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_LIBRARY_PAGE)

        with open(stylesheet_path, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def configure_parameters(self):
        self.table_song_header0.setText('Title')
        self.table_song_header1.setText('Artist')
        self.table_song_header2.setText('Last Played')
        self.table_song_header3.setText('Date Added')
        self.table_song_header4.setText('Times Played')
        self.btn_shuffle.setText('Shuffle')
