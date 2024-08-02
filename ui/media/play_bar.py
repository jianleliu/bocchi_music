"""playBar ui file."""
import logging

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QCursor, QIcon, QPixmap
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QSlider, QSpacerItem, QVBoxLayout)

from config.default_parameters import (DEAFULT_PLAY_ORDER_LOOPS,
                                       DEFAULT_PLAY_ORDER,
                                       DEFAULT_PLAY_ORDER_CYCLE,
                                       DEFAULT_PLAY_ORDER_SHUFFLE,
                                       DEFAULT_ENCODING)
from config.image_manager import (IMAGE_BACKWARD, IMAGE_CYCLE, IMAGE_FORWARD,
                                  IMAGE_LOGO, IMAGE_LOOP,
                                  IMAGE_NEXT, IMAGE_PLAY, IMAGE_PREV,
                                  IMAGE_SHUFFLE, IMAGE_VOLUME)
from config.style_manager import STYLE_PLAY_BAR

logger = logging.getLogger(__name__)


class PlayBar(QFrame):
    """Inherit QFrame.

    Args:
        QFrame (QFrame): PySide6.QtWidgets.
    """
    signal_btn_spinning_bocchi_clicked = Signal()
    signal_btn_backward_clicked = Signal()
    signal_btn_prev_clicked = Signal()
    signal_btn_play_pause_clicked = Signal()
    signal_btn_next_clicked = Signal()
    signal_btn_forward_clicked = Signal()
    signal_slider_progress_released = Signal(int)
    signal_slider_progress_pressed = Signal()
    signal_btn_play_order_clicked = Signal()
    signal_btn_volume_clicked = Signal()
    signal_slider_volume_changed = Signal(int)

    def __init__(self, centralWidget):
        """child of centralWidget.

        Args:
            centralWidget (QFrame): PySide6.QtWidgets
        """
        logger.info('initializing')
        super().__init__(centralWidget)
        self.setObjectName('play_bar')
        size_policy_5 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                    QSizePolicy.Policy.Fixed)
        size_policy_5.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy_5)
        self.setMinimumSize(QSize(0, 85))
        self.setMaximumSize(QSize(16777215, 85))

        # layouts
        logger.info('initializing layouts')
        self._initialize_layout()

        # components
        logger.info('initializing components')
        self._initalize_components()

        # apply stylesheet
        logger.info('initializing stylesheet')
        self._apply_stylesheet()
        # self.setStyleSheet(TEMP_STYLE)

        # configure display text
        logger.info('configure parameters')
        self._configure_parameters()

        # emit signals
        logger.info('emit signals')
        self._emit_signal()

    def _emit_signal(self) -> None:
        """emit signals to MainWindow.
        """
        self.btn_spinning_bocchi.clicked.connect(
            self.signal_btn_spinning_bocchi_clicked)
        self.btn_play_pause.clicked.connect(self.signal_btn_play_pause_clicked)
        self.btn_backward.clicked.connect(self.signal_btn_backward_clicked)
        self.btn_forward.clicked.connect(self.signal_btn_forward_clicked)
        self.btn_prev.clicked.connect(self.signal_btn_prev_clicked)
        self.btn_next.clicked.connect(self.signal_btn_next_clicked)
        self.btn_volume.clicked.connect(self.signal_btn_volume_clicked)
        self.btn_play_order.clicked.connect(self.signal_btn_play_order_clicked)
        self.slider_progress.sliderPressed.connect(
            self.signal_slider_progress_pressed)
        self.slider_progress.sliderReleased.connect(
            lambda: self.signal_slider_progress_released.emit(self.slider_progress.value()))
        self.slider_volume.valueChanged.connect(
            lambda: self.signal_slider_volume_changed.emit(self.slider_volume.value()))

    def _initalize_components(self) -> None:
        """initialize components.
        """
        self._initialize_button_thumbnail()
        self._initialize_horizontal_spacer_left()
        self._initialize_label_current_timestamp()
        self._initialize_label_track_title()
        self._initialize_slider_progress()
        # self.initialize_lcd_current_timestamp()
        self._initalize_horizontal_spacer_center_bottom_left()
        self._initialize_buttons()
        self._initialize_horizontal_spacer_center_bottom_right()
        self._initialize_label_end_timestamp()
        self._initialize_horizontal_spacer_right()
        self._initialize_button_play_order()
        self._initialize_button_volume()
        self._initialize_slider_volume()

    def _initialize_layout(self) -> None:
        """initialize layouts.
        """
        self.horizontal_layout_whole = QHBoxLayout(self)
        self.horizontal_layout_whole.setObjectName(
            'horizontal_layout_whole')

        self.vertical_layout_center_section = QVBoxLayout()
        self.vertical_layout_center_section.setSpacing(4)
        self.vertical_layout_center_section.setObjectName(
            'vertical_layout_center_section')

        self.horizontal_layout_center_bottom = QHBoxLayout()
        self.horizontal_layout_center_bottom.setSpacing(4)
        self.horizontal_layout_center_bottom.setObjectName(
            'horizontal_layout_center_bottom')

    def _initialize_horizontal_spacer_center_bottom_right(self) -> None:
        """_initialize_horizontal_spacer_center_bottom_right
        """
        self.horizontal_spacer_center_bottom_right = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_center_bottom.addItem(
            self.horizontal_spacer_center_bottom_right)

        self.vertical_layout_center_section.addLayout(
            self.horizontal_layout_center_bottom)

        self.horizontal_layout_whole.addLayout(
            self.vertical_layout_center_section)

    def _initialize_horizontal_spacer_right(self) -> None:
        """_initialize_horizontal_spacer_right"""
        self.horizontal_spacer_right = QSpacerItem(
            40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_whole.addItem(self.horizontal_spacer_right)

    def _initialize_horizontal_spacer_left(self) -> None:
        """_initialize_horizontal_spacer_left"""
        self.horizontal_spacer_left = QSpacerItem(
            40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_whole.addItem(self.horizontal_spacer_left)

    def _initalize_horizontal_spacer_center_bottom_left(self) -> None:
        """_initalize_horizontal_spacer_center_bottom_left"""
        self.horizontal_spacer_center_bottom_left = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontal_layout_center_bottom.addItem(
            self.horizontal_spacer_center_bottom_left)

    def _initialize_slider_volume(self) -> None:
        """_initialize_slider_volume"""
        self.slider_volume = QSlider(self)
        self.slider_volume.setObjectName('slider_volume')
        size_policy_4 = QSizePolicy(QSizePolicy.Policy.Minimum,
                                    QSizePolicy.Policy.Fixed)
        size_policy_4.setHeightForWidth(
            self.slider_volume.sizePolicy().hasHeightForWidth())
        self.slider_volume.setSizePolicy(size_policy_4)
        self.slider_volume.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_volume.setRange(0, 100)
        self.slider_volume.setValue(100)
        self.slider_volume.setOrientation(Qt.Vertical)

        self.horizontal_layout_whole.addWidget(self.slider_volume)

    def _initialize_button_volume(self) -> None:
        """_initialize_button_volume"""
        self.btn_volume = QPushButton(self)
        self.btn_volume.setObjectName('btn_volume')
        self.btn_volume.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(IMAGE_VOLUME, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_volume.setIcon(icon14)

        self.horizontal_layout_whole.addWidget(self.btn_volume)

    def _initialize_button_play_order(self) -> None:
        """_initialize_button_play_order"""
        self.btn_play_order = QPushButton(self)
        self.btn_play_order.setObjectName('btn_play_order')
        size_policy_4 = QSizePolicy(QSizePolicy.Policy.Minimum,
                                    QSizePolicy.Policy.Fixed)
        size_policy_4.setHeightForWidth(
            self.btn_play_order.sizePolicy().hasHeightForWidth())
        self.btn_play_order.setSizePolicy(size_policy_4)
        self.btn_play_order.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        file_path = None
        PLAY_ORDERS = [
            (DEAFULT_PLAY_ORDER_LOOPS, IMAGE_LOOP),
            (DEFAULT_PLAY_ORDER_CYCLE, IMAGE_CYCLE),
            (DEFAULT_PLAY_ORDER_SHUFFLE, IMAGE_SHUFFLE)
        ]
        current_play_order = DEFAULT_PLAY_ORDER
        current_index = [order[0]
                         for order in PLAY_ORDERS].index(current_play_order)
        _, file_path = PLAY_ORDERS[current_index]
        icon13.addFile(file_path, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play_order.setIcon(icon13)

        self.horizontal_layout_whole.addWidget(self.btn_play_order)

    def _initialize_label_end_timestamp(self) -> None:
        """_initialize_label_end_timestamp"""
        self.label_end_timestamp = QLabel(self)
        self.label_end_timestamp.setObjectName('label_end_timestamp')

        self.horizontal_layout_whole.addWidget(self.label_end_timestamp)

    def _initialize_buttons(self) -> None:
        """_initialize_buttons"""
        # backward
        self.btn_backward = QPushButton(self)
        self.btn_backward.setObjectName('btn_backward')
        self.btn_backward.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(IMAGE_BACKWARD, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backward.setIcon(icon8)

        self.horizontal_layout_center_bottom.addWidget(self.btn_backward)

        # prev
        self.btn_prev = QPushButton(self)
        self.btn_prev.setObjectName('btn_prev')
        self.btn_prev.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(IMAGE_PREV, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_prev.setIcon(icon9)

        self.horizontal_layout_center_bottom.addWidget(self.btn_prev)

        # pause
        self.btn_play_pause = QPushButton(self)
        self.btn_play_pause.setObjectName('btn_play_pause')
        self.btn_play_pause.setCursor(QCursor(Qt.PointingHandCursor))
        icon_play_pause = QIcon()
        icon_play_pause.addFile(IMAGE_PLAY, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play_pause.setIcon(icon_play_pause)

        self.horizontal_layout_center_bottom.addWidget(self.btn_play_pause)

        # next
        self.btn_next = QPushButton(self)
        self.btn_next.setObjectName('btn_next')
        self.btn_next.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(IMAGE_NEXT, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next.setIcon(icon11)

        self.horizontal_layout_center_bottom.addWidget(self.btn_next)

        # forward
        self.btn_forward = QPushButton(self)
        self.btn_forward.setObjectName('btn_forward')
        self.btn_forward.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(IMAGE_FORWARD, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_forward.setIcon(icon12)
        self.btn_forward.setCheckable(False)

        self.horizontal_layout_center_bottom.addWidget(self.btn_forward)

    def _initialize_slider_progress(self) -> None:
        """_initialize_slider_progress"""
        self.slider_progress = QSlider(self)
        self.slider_progress.setObjectName('slider_progress')
        self.slider_progress.setMinimumSize(QSize(0, 20))
        self.slider_progress.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_progress.setOrientation(Qt.Horizontal)

        self.vertical_layout_center_section.addWidget(self.slider_progress)

    def _initialize_label_track_title(self) -> None:
        """_initialize_label_track_title"""
        self.label_play_title = QLabel(self)
        self.label_play_title.setObjectName('label_play_title')
        self.label_play_title.setMinimumSize(QSize(0, 25))
        self.label_play_title.setAlignment(Qt.AlignCenter)

        self.vertical_layout_center_section.addWidget(self.label_play_title)

    def _initialize_label_current_timestamp(self) -> None:
        """_initialize_label_current_timestamp"""
        self.label_current_timestamp = QLabel(self)
        self.label_current_timestamp.setObjectName('current_timestamp')

        self.horizontal_layout_whole.addWidget(self.label_current_timestamp)

    def _initialize_button_thumbnail(self) -> None:
        """_initialize_button_thumbnail"""
        self.btn_spinning_bocchi = QPushButton(self)

        self.btn_spinning_bocchi.setObjectName('thumbnail')
        size_policy_8 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                    QSizePolicy.Policy.Expanding)
        size_policy_8.setHeightForWidth(
            self.btn_spinning_bocchi.sizePolicy().hasHeightForWidth())
        self.btn_spinning_bocchi.setSizePolicy(size_policy_8)
        self.btn_spinning_bocchi.setMinimumSize(QSize(50, 50))
        self.btn_spinning_bocchi.setMaximumSize(QSize(100, 100))
        self.btn_spinning_bocchi.setSizeIncrement(QSize(5, 5))
        self.btn_spinning_bocchi.setIcon(QPixmap(IMAGE_LOGO))
        self.btn_spinning_bocchi.setIconSize(QSize(75, 75))
        self.btn_spinning_bocchi.setCheckable(True)

        self.horizontal_layout_whole.addWidget(self.btn_spinning_bocchi)

    def _apply_stylesheet(self) -> None:
        """_apply_stylesheet"""
        with open(STYLE_PLAY_BAR, 'r', encoding=DEFAULT_ENCODING) as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def _update_time(self) -> None:
        """_update_time"""
        self.current_time = self.current_time.addSecs(1)
        self.lcd_current_timestamp.display(self.current_time.toString('mm:ss'))

    def _configure_parameters(self) -> None:
        """_configure_parameters"""
        self.label_play_title.setText('Title')
        self.label_current_timestamp.setText('0:00')
        self.label_end_timestamp.setText('0:00')
