from PySide6.QtCore import (Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QFrame, QGridLayout,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QTableWidget,
                               QTableWidgetItem)
import os
from config.style_manager import STYLE_LIBRARY_PAGE

STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class LibraryPage(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName('library_page')

        # apply stylesheet
        self.apply_stylesheet()

    def initilize_song_table(self):
        self.gridLayout_3 = QGridLayout(self)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(494, 20,
                                            QSizePolicy.Policy.Expanding,
                                            QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.play_random_btn = QPushButton(self)
        self.play_random_btn.setObjectName(u"play_random_btn")
        self.play_random_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.play_random_btn, 0, 1, 1, 1)

        self.song_table = QTableWidget(self)
        if (self.song_table.columnCount() < 6):
            self.song_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.song_table.setObjectName(u"song_table")
        self.song_table.viewport().setProperty("cursor",
                                               QCursor(Qt.PointingHandCursor))
        self.song_table.setLineWidth(1)
        self.song_table.setDragDropOverwriteMode(False)
        self.song_table.setAlternatingRowColors(True)
        self.song_table.setSortingEnabled(True)
        self.song_table.setWordWrap(True)
        self.song_table.setRowCount(0)
        self.song_table.setColumnCount(6)

        self.gridLayout_3.addWidget(self.song_table, 1, 0, 1, 2)

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_LIBRARY_PAGE)

        with open(stylesheet_path, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
