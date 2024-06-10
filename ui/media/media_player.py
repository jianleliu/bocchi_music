from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from config.default_parameters import DIR_ROOT
import sys
import os

class VideoWidget(QVideoWidget):
    def __init__(self, centralWidget):
        super().__init__(centralWidget)
        file_path = os.path.join(os.path.join(DIR_ROOT, 'song'), 'Baka to Test to Shoukanjuu OP 「 Perfect-area Complete! 」 Full HQ.mp4')
                
        # Create a media player
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self)
        
        # Create an audio output
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        # Set the media source
        media_url = QUrl.fromLocalFile(file_path)
        self.player.setSource(media_url)
        
        # Play the video
        self.player.setLoops(-1)
        self.hide()
        
        # self.player.play()
