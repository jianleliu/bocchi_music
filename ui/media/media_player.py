from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QUrl, Signal
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from config.default_parameters import DIR_ROOT
import sys
import os


class VideoWidget(QVideoWidget):
    signal_track_stopped = Signal()
    signal_track_paused = Signal()
    signal_track_played = Signal()

    def __init__(self, centralWidget):
        super().__init__(centralWidget)
        # Create a media player
        self.position_current = 0
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self)

        # Create an audio output
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        # Play the video
        self.player.setLoops(-1)
        self.hide()
        self.emit_signal()
        
        # self.player.play()

    def emit_signal(self):
        self.player.playbackStateChanged.connect(self.send_signal_playback_state)
        
    def send_signal_playback_state(self):
        state_playing = self.player.playbackState().PlayingState
        state_stopped = self.player.playbackState().StoppedState
        state_paused = self.player.playbackState().PausedState
        playback_state = self.player.playbackState()
        
        if playback_state == state_playing:
            self.player.setPosition(self.position_current)
            self.signal_track_played.emit()
        elif playback_state == state_stopped:
            self.position_current = 0
            self.signal_track_stopped.emit()
        else:
            self.position_current = self.player.position()
            self.signal_track_paused.emit()