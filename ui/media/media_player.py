"""Ui file for VideoWidget containing video and audio player."""
import logging

from PySide6.QtCore import QTimer, Signal
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QFrame

logger = logging.getLogger(__name__)


class VideoWidget(QVideoWidget):
    """ui instance video widget.

    Args:
        QVideoWidget (QVideoWidget): PySide6.QtMultimediaWidgets.
    """
    signal_track_stopped = Signal()
    signal_track_paused = Signal()
    signal_track_played = Signal(int, int)
    signal_position_changed = Signal(int)
    signal_source_changed = Signal()
    signal_end_of_media = Signal()

    def __init__(self, centralWidget: QFrame):
        """child of centralWidget.

        Args:
            centralWidget (QFrame): PySide6.QtWidgets.
        """
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
        self._emit_signal()
        self._signal_internal()

    def _emit_signal(self) -> None:
        """helper function containing signals to be emitted.
        """
        self.player.playbackStateChanged.connect(
            self._send_signal_playback_state)
        self.timer_seconds.timeout.connect(self._emit_position_changed)
        self.player.mediaStatusChanged.connect(self._emit_end_of_media)

    def _signal_internal(self) -> None:
        """signal to be handled internally.
        """
        self.player.audioOutput().volumeChanged.connect(self._update_current_volume)

    def _send_signal_playback_state(self) -> None:
        """emit signal based on the current playback state.
        """
        playback_state = self.player.playbackState()

        state_playing = self.player.playbackState().PlayingState
        state_stopped = self.player.playbackState().StoppedState
        # state_paused = self.player.playbackState().PausedState
        logger.info('playbackStateChanged: %s', playback_state)

        if playback_state == state_playing:
            self.player.setPosition(self.position_current)
            logger.info('current position: %s', self.position_current)
            self.signal_track_played.emit(
                self.position_current, self.player.duration())
        elif playback_state == state_stopped:
            self.position_current = 0
            logger.info('current position: %s', self.position_current)
            self.signal_track_stopped.emit()
        else:
            self.position_current = self.player.position()
            logger.info('current position: %s', self.position_current)
            self.signal_track_paused.emit()

    def _emit_position_changed(self) -> None:
        """emit signal when position changed. 
        need it's own function because it's triggered by QTimer.
        """
        self.signal_position_changed.emit(self.player.position())

    def _emit_end_of_media(self, status) -> None:
        """_emit_end_of_media

        Args:
            status (_type_): self.player.mediaStatus().EndOfMedia
        """
        status_end_of_media = self.player.mediaStatus().EndOfMedia

        if status == status_end_of_media:
            self.signal_end_of_media.emit()

    def _update_current_volume(self, volume: int) -> None:
        """update volume of player.

        Args:
            volume (int): between 0 - 1.
        """
        logger.info('updating volume, current: %s, new: %s', self.current_volume, volume)
        self.current_volume = volume
