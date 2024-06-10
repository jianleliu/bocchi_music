# library page
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtGui import QPixmap
import time
import os

def populate_table_song(window) -> None:
    window.table_song.setRowCount(0)
    # prev_entities = len(self.table_song_entities)
    # self.table_song_entities = init_table_song(self.song_path, ['.mp4', '.mp3'])
    if self.table_song_entities:
        row = 0
        for filename in self.table_song_entities:
            
            self.table_song.insertRow(row)
            self.table_song.setItem(row, 1, QTableWidgetItem(filename))
            self.table_song.setItem(row, 0, QTableWidgetItem('not playing'))
            icon = QPixmap(self.row_header_icon['play'])
            item = QTableWidgetItem()
            item.setIcon(icon)
            self.table_song.setVerticalHeaderItem(row, item)
    

def update_vertical_header(columnIndex):
    # reset back to default
    if self.row_ongoing_song != -1:
        # set back to default icon pause
        icon = QTableWidgetItem()
        icon.setIcon(QPixmap(self.row_header_icon['play']))
        self.table_song.setVerticalHeaderItem(self.row_ongoing_song, icon)
        # locate the row after sorting, update its new location
        for row in range(self.table_song.rowCount()):
            if self.table_song.item(row, 0).text() == 'playing':
                # update 
                self.row_ongoing_song = row
                # set it back to playing icon
                icon = QTableWidgetItem()
                icon.setIcon(QPixmap(self.row_header_icon['pause']))
                self.table_song.setVerticalHeaderItem(row, icon)
        
