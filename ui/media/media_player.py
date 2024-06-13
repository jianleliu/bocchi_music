from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QUrl, Signal, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from config.default_parameters import *
import sys
import os


class VideoWidget(QVideoWidget):
    signal_track_stopped = Signal()
    signal_track_paused = Signal()
    signal_track_played = Signal(int, int)
    signal_position_changed = Signal(int)
    signal_source_changed = Signal()
    signal_end_of_media = Signal()

    def __init__(self, centralWidget):
        super().__init__(centralWidget)
        # Create a media player
        self.position_current = 0
        self.current_volume = 100
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self)

        # craete a seconds timer
        self.timer_seconds = QTimer()

        # Create an audio output
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.hide()
        self.emit_signal()
        self.signal_internal()        

    def emit_signal(self):
        self.player.playbackStateChanged.connect(
            self.send_signal_playback_state)
        self.timer_seconds.timeout.connect(self.emit_position_changed)
        self.timer_seconds.start(1000)
        self.player.mediaStatusChanged.connect(self.emit_end_of_media)
        
    def signal_internal(self):
        self.player.audioOutput().volumeChanged.connect(self.update_current_volume)

    def send_signal_playback_state(self):
        state_playing = self.player.playbackState().PlayingState
        state_stopped = self.player.playbackState().StoppedState
        state_paused = self.player.playbackState().PausedState
        playback_state = self.player.playbackState()
        print(self.player.duration())
        if playback_state == state_playing:
            self.player.setPosition(self.position_current)
            self.signal_track_played.emit(
                self.position_current, self.player.duration())
        elif playback_state == state_stopped:
            self.position_current = 0
            self.signal_track_stopped.emit()
        else:
            self.position_current = self.player.position()
            self.signal_track_paused.emit()

    def emit_position_changed(self):
        self.player.positionChanged.connect(
            lambda position: self.signal_position_changed.emit(self.player.position()))
        
    def emit_end_of_media(self, status):
        status_end_of_media = self.player.mediaStatus().EndOfMedia
        
        if status == status_end_of_media:
            self.signal_end_of_media.emit()

    def update_current_volume(self, volume):
        self.current_volume = volume
