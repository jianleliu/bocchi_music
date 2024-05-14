from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFileDialog, QErrorMessage, QTableWidgetItem
from PySide6.QtCore import Qt, QUrl, Signal
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtGui import QIcon, QPixmap
import time
import sys
import os
from SideBar import SideBar
from util import download_mp3, download_playlist, init_config_file, init_song_table
from error import ErrorPopup
from resources_rc import qInitResources

app = QApplication(sys.argv)

class Main(SideBar):
    def __init__(self) -> None:
        init_config_file()
        super().__init__()
        # Setting page
        self.song_dir_le.setText(self.set_default_song_path())
        self.playlist_dir_le.setText(self.set_default_song_path())
        self.song_path_browse.clicked.connect(self.browse_song_path)
        self.playlist_path_browse.clicked.connect(self.browse_playlist_path)
        
        # audio player
        self.audio_output = QAudioOutput()
        self.audio_player = QMediaPlayer()
        self.audio_player.setAudioOutput(self.audio_output)
        self.audio_player.errorOccurred.connect(lambda error: print("QMediaPlayer Error:", error))
        self.audio_player.setLoops(-1)
        
        # Library page
        self.song_table.hideColumn(0)

        self.song_path = self.song_dir_le.displayText()
        self.song_table_entities = {}
        if self.song_path:
            self.song_table_entities = init_song_table(self.song_path, ['.mp4', '.mp3'])
        self.library_btn_1.clicked.connect(lambda: self.populate_song_table() if self.song_table.rowCount() == 0 else None)
        self.library_btn_2.clicked.connect(lambda: self.populate_song_table() if self.song_table.rowCount() == 0 else None)
        
            ## keep track of the song currently playing
        self.row_ongoing_song = -1
        self.row_header_icon = {
            'play': u':/newPrefix/images/playpng.png',
            'pause': u':/newPrefix/images/pause.png'
        }
        self.song_table.verticalHeader().sectionClicked.connect(self.toggle_play)
        self.song_table.horizontalHeader().sectionClicked.connect(self.update_vertical_header)
        self.song_table.setCornerButtonEnabled(False)
        
        # Download page
        self.download_btn.clicked.connect(self.download_track)
        self.advanced_btn.clicked.connect(self.toggle_advanced_tab)
        
        # Signals
        # self.song_stopped = Signal()
        # self.song_stopped.connect(self.play_song)
        

        

        
        
        
    
    # library page
    def populate_song_table(self) -> None:
        self.song_table.setRowCount(0)
        # prev_entities = len(self.song_table_entities)
        # self.song_table_entities = init_song_table(self.song_path, ['.mp4', '.mp3'])
        if self.song_table_entities:
            row = 0
            for filename in self.song_table_entities:
                
                self.song_table.insertRow(row)
                self.song_table.setItem(row, 1, QTableWidgetItem(filename))
                self.song_table.setItem(row, 0, QTableWidgetItem('not playing'))
                icon = QPixmap(self.row_header_icon['play'])
                item = QTableWidgetItem()
                item.setIcon(icon)
                self.song_table.setVerticalHeaderItem(row, item)
        
    
    def update_vertical_header(self, columnIndex):
        # reset back to default
        if self.row_ongoing_song != -1:
            # set back to default icon pause
            icon = QTableWidgetItem()
            icon.setIcon(QPixmap(self.row_header_icon['play']))
            self.song_table.setVerticalHeaderItem(self.row_ongoing_song, icon)
            # locate the row after sorting, update its new location
            for row in range(self.song_table.rowCount()):
                if self.song_table.item(row, 0).text() == 'playing':
                    # update 
                    self.row_ongoing_song = row
                    # set it back to playing icon
                    icon = QTableWidgetItem()
                    icon.setIcon(QPixmap(self.row_header_icon['pause']))
                    self.song_table.setVerticalHeaderItem(row, icon)
            
    # def stop_song(self, row, state):
    #     self.audio_player.stop()
    #     self.song_stopped.emit(row, state)
    # play song
    # continue song
    # puase song
    # switch song
    def play_song(self, row, state):
        icon = QTableWidgetItem()
        icon.setIcon(QPixmap(self.row_header_icon['pause']))
        self.song_table.setVerticalHeaderItem(row, icon)
        self.song_table.setItem(row, 0, QTableWidgetItem('playing'))
        self.row_ongoing_song = row
        
        # start audio player
        path = self.song_table_entities.get(self.song_table.item(row, 1).text(), None)
        self.audio_player.setSource(QUrl.fromLocalFile(path))
        self.audio_player.play()
        print(path)
        print('exists: ', os.path.exists(path))
        print(self.audio_player.playbackState())
    
    def continue_song(self, row, state):
        icon = QTableWidgetItem()
        icon.setIcon(QPixmap(self.row_header_icon['pause']))
        self.song_table.setItem(row, 0, QTableWidgetItem('playing'))
        self.song_table.setVerticalHeaderItem(row, icon)
        self.row_ongoing_song = row
        self.audio_player.play()
    
    def pause_song(self, row, state):
        icon = QTableWidgetItem()
        icon.setIcon(QPixmap(self.row_header_icon['play']))
        self.song_table.setItem(row, 0, QTableWidgetItem('not playing'))
        self.song_table.setVerticalHeaderItem(row, icon)
        self.row_ongoing_song = -1
        self.audio_player.pause()
    
    # will run IF a new song is going to be played WHILE there is a ongoing song.
    def switch_song(self, row, state):
        #  current song
        icon = QTableWidgetItem()
        icon.setIcon(QPixmap(self.row_header_icon['play']))
        self.song_table.setItem(self.row_ongoing_song, 0, QTableWidgetItem('not playing'))
        self.song_table.setVerticalHeaderItem(self.row_ongoing_song, icon)
        # stop the current song
        self.audio_player.stop()
        time.sleep(0.01)
        
        self.play_song(row, state)
    
    def toggle_play(self, item):
        row = item
        state = self.song_table.item(row, 0).text()
        self.audio_output.device()
        # play a new song when no song is playing
        if (state == 'not playing') and (self.row_ongoing_song == -1):
            print('play new song')
            self.play_song(row, state)
            return
        elif (state == 'not playing') and (self.row_ongoing_song == row): 
            print('continue current song')
            self.continue_song(row, state)
            return
        # pause current song
        if (state == 'playing') and (row == self.row_ongoing_song):
            print('pause current song')
            self.pause_song(row, state)
        else:
            print('switch to new song')
            self.switch_song(row, state)


    # Download page
    def download_track(self) -> None:
        if self.radio_song.isChecked():
            directory = self.song_dir_le.displayText()
            if not os.path.exists(directory):
                popup = ErrorPopup("The default path does not exists. It's likely the default download path in setting not setup properly.")
                popup.exec()
                return
            download_mp3(self.url_search_bar.displayText(), directory=directory)
        else:
            download_playlist(self.url_search_bar.displayText())

    def toggle_advanced_tab(self) -> None:
        if self.advanced_widget.isVisible():
            self.advanced_widget.setVisible(False)
        else:
            self.advanced_widget.setVisible(True)

    # Setting page
    def set_default_song_path(self):
        songs_path = os.path.join(os.getcwd(), 'songs')
        if not os.path.isdir(songs_path):
            os.mkdir('songs')
        return songs_path
        
    def browse_song_path(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select default song directory')
        if directory:
            self.song_dir_le.setText(directory)
    
    def browse_playlist_path(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select default playlist directory')
        if directory:
            self.playlist_dir_le.setText(directory)

window = Main()
window.show()
sys.exit(app.exec())
