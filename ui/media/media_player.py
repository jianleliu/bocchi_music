from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QUrl, Signal, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from config.default_parameters import *
import sys
import os
import logging

logger = logging.getLogger(__name__)


class VideoWidget(QVideoWidget):
    signal_track_stopped = Signal()
    signal_track_paused = Signal()
    signal_track_played = Signal(int, int)
    signal_position_changed = Signal(int)
    signal_source_changed = Signal()
    signal_end_of_media = Signal()

    def __init__(self, centralWidget):
        logger.info('initializing')
        super().__init__(centralWidget)
        # Create a media player
        logger.info('configure parameters')
        self.position_current = 0
        self.current_volume = 100
        
        logger.info('initializing components')
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self)
        self.audio_output = QAudioOutput()
        self.timer_seconds = QTimer()
        self.timer_seconds.start(1000)
        
        
        # Create an audio output
        logger.info('set audio_output for media player')
        self.player.setAudioOutput(self.audio_output)

        self.hide()
        logger.info('emit signal')
        self.emit_signal()
        self.signal_internal()        

    def emit_signal(self):
        self.player.playbackStateChanged.connect(
            self.send_signal_playback_state)
        self.timer_seconds.timeout.connect(self.emit_position_changed)
        self.player.mediaStatusChanged.connect(self.emit_end_of_media)
        
    def signal_internal(self):
        self.player.audioOutput().volumeChanged.connect(self.update_current_volume)

    def send_signal_playback_state(self):
        playback_state = self.player.playbackState()
        
        state_playing = self.player.playbackState().PlayingState
        state_stopped = self.player.playbackState().StoppedState
        state_paused = self.player.playbackState().PausedState
        logger.info(f'playbackStateChanged: {playback_state}')

        if playback_state == state_playing:
            self.player.setPosition(self.position_current)
            logger.info(f'current position: {self.position_current}')
            self.signal_track_played.emit(
                self.position_current, self.player.duration())
        elif playback_state == state_stopped:
            self.position_current = 0
            logger.info(f'current position: {self.position_current}')
            self.signal_track_stopped.emit()
        else:
            self.position_current = self.player.position()
            logger.info(f'current position: {self.position_current}')
            self.signal_track_paused.emit()

    def emit_position_changed(self):
        self.signal_position_changed.emit(self.player.position())
        
    def emit_end_of_media(self, status):
        status_end_of_media = self.player.mediaStatus().EndOfMedia
        
        if status == status_end_of_media:
            self.signal_end_of_media.emit()

    def update_current_volume(self, volume):
        logger.info(f'updating volume, current: {self.current_volume}, new: {volume}')
        self.current_volume = volume
