from PySide6.QtCore import (QSize, Qt, QTimer, QTime, Signal)
from PySide6.QtGui import (QCursor, QIcon)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSlider, QSpacerItem,
                               QVBoxLayout, QLCDNumber)
import os
from config.style_manager import STYLE_PLAY_BAR
from config.image_manager import *
from config.default_parameters import *
IMAGE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/images')
STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class PlayBar(QFrame):
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
        super().__init__(centralWidget)
        self.setObjectName('play_bar')
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy5.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy5)
        self.setMinimumSize(QSize(0, 85))
        self.setMaximumSize(QSize(16777215, 85))

        # layouts
        self.initialize_layout()

        # components
        self.initalize_components()

        # apply stylesheet
        self.apply_stylesheet()
        # self.setStyleSheet(TEMP_STYLE)

        # configure display text
        self.configure_parameters()

        # emit signals
        self.emit_signal()

    def emit_signal(self):
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

    def initalize_components(self):
        self.initialize_button_thumbnail()
        self.initialize_horizontalSpacer_left()
        self.initialize_label_current_timestamp()
        self.initialize_label_track_title()
        self.initialize_slider_progress()
        # self.initialize_lcd_current_timestamp()
        self.initalize_horizontalSpacer_center_bottom_left()
        self.initialize_buttons()
        self.initialize_horizontalSpacer_center_bottom_right()
        self.initialize_label_end_timestamp()
        self.initialize_horizontalSpacer_right()
        self.initialize_button_play_order()
        self.initialize_button_volume()
        self.initialize_slider_volume()

    def initialize_layout(self):
        self.horizontalLayout_whole = QHBoxLayout(self)
        self.horizontalLayout_whole.setObjectName(
            'horizontalLayout_whole')

        self.verticalLayout_center_section = QVBoxLayout()
        self.verticalLayout_center_section.setSpacing(4)
        self.verticalLayout_center_section.setObjectName(
            'verticalLayout_center_section')

        self.horizontalLayout_center_bottom = QHBoxLayout()
        self.horizontalLayout_center_bottom.setSpacing(4)
        self.horizontalLayout_center_bottom.setObjectName(
            'horizontalLayout_center_bottom')

    def initialize_horizontalSpacer_center_bottom_right(self):
        self.horizontalSpacer_center_bottom_right = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_center_bottom.addItem(
            self.horizontalSpacer_center_bottom_right)

        self.verticalLayout_center_section.addLayout(
            self.horizontalLayout_center_bottom)

        self.horizontalLayout_whole.addLayout(
            self.verticalLayout_center_section)

    def initialize_horizontalSpacer_right(self):
        self.horizontalSpacer_right = QSpacerItem(
            40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_whole.addItem(self.horizontalSpacer_right)

    def initialize_horizontalSpacer_left(self):
        self.horizontalSpacer_left = QSpacerItem(
            40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_whole.addItem(self.horizontalSpacer_left)

    def initalize_horizontalSpacer_center_bottom_left(self):
        self.horizontalSpacer_center_bottom_left = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_center_bottom.addItem(
            self.horizontalSpacer_center_bottom_left)

    def initialize_slider_volume(self):
        self.slider_volume = QSlider(self)
        self.slider_volume.setObjectName('slider_volume')
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy4.setHeightForWidth(
            self.slider_volume.sizePolicy().hasHeightForWidth())
        self.slider_volume.setSizePolicy(sizePolicy4)
        self.slider_volume.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_volume.setRange(0, 100)
        self.slider_volume.setValue(100)
        self.slider_volume.setOrientation(Qt.Vertical)

        self.horizontalLayout_whole.addWidget(self.slider_volume)

    def initialize_button_volume(self):
        self.btn_volume = QPushButton(self)
        self.btn_volume.setObjectName('btn_volume')
        self.btn_volume.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(IMAGE_VOLUME, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_volume.setIcon(icon14)

        self.horizontalLayout_whole.addWidget(self.btn_volume)

    def initialize_button_play_order(self):
        self.btn_play_order = QPushButton(self)
        self.btn_play_order.setObjectName('btn_play_order')
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy4.setHeightForWidth(
            self.btn_play_order.sizePolicy().hasHeightForWidth())
        self.btn_play_order.setSizePolicy(sizePolicy4)
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
        _ , file_path = PLAY_ORDERS[current_index]
        icon13.addFile(file_path, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play_order.setIcon(icon13)

        self.horizontalLayout_whole.addWidget(self.btn_play_order)

    def initialize_label_end_timestamp(self):
        self.label_end_timestamp = QLabel(self)
        self.label_end_timestamp.setObjectName('label_end_timestamp')

        self.horizontalLayout_whole.addWidget(self.label_end_timestamp)

    def initialize_buttons(self):
        # backward
        self.btn_backward = QPushButton(self)
        self.btn_backward.setObjectName('btn_backward')
        self.btn_backward.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(IMAGE_BACKWARD, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backward.setIcon(icon8)

        self.horizontalLayout_center_bottom.addWidget(self.btn_backward)

        # prev
        self.btn_prev = QPushButton(self)
        self.btn_prev.setObjectName('btn_prev')
        self.btn_prev.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(IMAGE_PREV, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_prev.setIcon(icon9)

        self.horizontalLayout_center_bottom.addWidget(self.btn_prev)

        # pause
        self.btn_play_pause = QPushButton(self)
        self.btn_play_pause.setObjectName('btn_play_pause')
        self.btn_play_pause.setCursor(QCursor(Qt.PointingHandCursor))
        icon_play_pause = QIcon()
        icon_play_pause.addFile(IMAGE_PLAY, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play_pause.setIcon(icon_play_pause)

        self.horizontalLayout_center_bottom.addWidget(self.btn_play_pause)

        # next
        self.btn_next = QPushButton(self)
        self.btn_next.setObjectName('btn_next')
        self.btn_next.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(IMAGE_NEXT, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next.setIcon(icon11)

        self.horizontalLayout_center_bottom.addWidget(self.btn_next)

        # forward
        self.btn_forward = QPushButton(self)
        self.btn_forward.setObjectName('btn_forward')
        self.btn_forward.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(IMAGE_FORWARD, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_forward.setIcon(icon12)
        self.btn_forward.setCheckable(False)

        self.horizontalLayout_center_bottom.addWidget(self.btn_forward)

    def initialize_slider_progress(self):
        self.slider_progress = QSlider(self)
        self.slider_progress.setObjectName('slider_progress')
        self.slider_progress.setMinimumSize(QSize(0, 20))
        self.slider_progress.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_progress.setOrientation(Qt.Horizontal)

        self.verticalLayout_center_section.addWidget(self.slider_progress)

    def initialize_label_track_title(self):
        self.label_play_title = QLabel(self)
        self.label_play_title.setObjectName('label_play_title')
        self.label_play_title.setMinimumSize(QSize(0, 25))
        self.label_play_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_center_section.addWidget(self.label_play_title)

    def initialize_label_current_timestamp(self):
        self.label_current_timestamp = QLabel(self)
        self.label_current_timestamp.setObjectName('current_timestamp')

        self.horizontalLayout_whole.addWidget(self.label_current_timestamp)

    def initialize_lcd_current_timestamp(self):
        self.lcd_current_timestamp = QLCDNumber(self)
        self.lcd_current_timestamp.setDigitCount(5)

        self.horizontalLayout_whole.addWidget(self.lcd_current_timestamp)

        # Set up a timer to update the timestamp every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        # Simulate starting the song at 00:00
        self.current_time = QTime(0, 0, 0)
        self.current_time.setHMS(0, 0, 1000)

    def initialize_button_thumbnail(self):
        self.btn_spinning_bocchi = QPushButton(self)
        self.btn_spinning_bocchi.setObjectName('thumbnail')
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Expanding)
        sizePolicy8.setHeightForWidth(
            self.btn_spinning_bocchi.sizePolicy().hasHeightForWidth())
        self.btn_spinning_bocchi.setSizePolicy(sizePolicy8)
        self.btn_spinning_bocchi.setMinimumSize(QSize(50, 50))
        self.btn_spinning_bocchi.setMaximumSize(QSize(100, 100))
        self.btn_spinning_bocchi.setSizeIncrement(QSize(5, 5))
        icon = QIcon()
        icon.addFile(IMAGE_LOGO, QSize(), QIcon.Normal, QIcon.Off)
        self.btn_spinning_bocchi.setIcon(icon)
        self.btn_spinning_bocchi.setIconSize(QSize(100, 100))
        self.btn_spinning_bocchi.setCheckable(True)

        self.horizontalLayout_whole.addWidget(self.btn_spinning_bocchi)

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_PLAY_BAR)

        with open(stylesheet_path, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def update_time(self):
        self.current_time = self.current_time.addSecs(1)
        self.lcd_current_timestamp.display(self.current_time.toString('mm:ss'))

    def configure_parameters(self):
        self.label_play_title.setText('Title')
        self.label_current_timestamp.setText('0:00')
        self.label_end_timestamp.setText('0:00')
