from PySide6.QtCore import (QSize, Qt)
from PySide6.QtGui import (QCursor, QIcon)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSlider, QSpacerItem,
                               QVBoxLayout)
import os
from config.style_manager import STYLE_PLAY_BAR
from config.image_manager import (IMAGE_LOGO, IMAGE_BACKWARD, IMAGE_CYCLE,
                                  IMAGE_FORWARD, IMAGE_NEXT, IMAGE_PAUSE,
                                  IMAGE_PREV, IMAGE_VOLUME)
IMAGE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/images')
STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class PlayBar(QFrame):
    def __init__(self, centralWidget):
        super().__init__(centralWidget)
        self.setObjectName(u"play_bar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy5.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy5)
        self.setMinimumSize(QSize(0, 75))
        self.setMaximumSize(QSize(16777215, 75))

        self.horizontalLayout_6 = QHBoxLayout(self)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        # thumbnail
        self.initialize_button_thumbnail()

        # spacer
        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        # current track timestamp
        self.initialize_label_current_timestamp()

        # center box
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        # song title
        self.initialize_label_track_title()

        # progress slider
        self.initialize_slider_progress()

        # left horizontal spacer
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_15 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)

        # buttons
        self.initialize_buttons()

        # right horizontal spacer
        self.horizontalSpacer_16 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_16)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        # track end timestamp
        self.initialize_label_end_timestamp()

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        # play order button
        self.initialize_button_play_order()

        # volume button
        self.initialize_button_volume()

        # volume slider
        self.initialize_slider_volume()

        # apply stylesheet
        self.apply_stylesheet()
        # self.setStyleSheet(TEMP_STYLE)

    def initialize_slider_volume(self):
        self.volume_slide = QSlider(self)
        self.volume_slide.setObjectName(u"volume_slide")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy4.setHeightForWidth(
            self.volume_slide.sizePolicy().hasHeightForWidth())
        self.volume_slide.setSizePolicy(sizePolicy4)
        self.volume_slide.setCursor(QCursor(Qt.PointingHandCursor))
        self.volume_slide.setValue(99)
        self.volume_slide.setOrientation(Qt.Vertical)

        self.horizontalLayout_6.addWidget(self.volume_slide)

    def initialize_button_volume(self):
        self.volume_btn = QPushButton(self)
        self.volume_btn.setObjectName(u"volume_btn")
        self.volume_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_VOLUME)
        icon14.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.volume_btn.setIcon(icon14)

        self.horizontalLayout_6.addWidget(self.volume_btn)

    def initialize_button_play_order(self):
        self.play_order_btn = QPushButton(self)
        self.play_order_btn.setObjectName(u"play_order_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy4.setHeightForWidth(
            self.play_order_btn.sizePolicy().hasHeightForWidth())
        self.play_order_btn.setSizePolicy(sizePolicy4)
        self.play_order_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_CYCLE)
        icon13.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.play_order_btn.setIcon(icon13)

        self.horizontalLayout_6.addWidget(self.play_order_btn)

    def initialize_label_end_timestamp(self):
        self.label_16 = QLabel(self)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_6.addWidget(self.label_16)

    def initialize_buttons(self):
        # backward
        self.backward_btn = QPushButton(self)
        self.backward_btn.setObjectName(u"backward_btn")
        self.backward_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_BACKWARD)
        icon8.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.backward_btn.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.backward_btn)

        # prev
        self.prev_btn = QPushButton(self)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_PREV)
        icon9.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.prev_btn.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.prev_btn)

        # pause
        self.pause_start_btn = QPushButton(self)
        self.pause_start_btn.setObjectName(u"pause_start_btn")
        self.pause_start_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_PAUSE)
        icon10.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.pause_start_btn.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.pause_start_btn)

        # next
        self.next_btn = QPushButton(self)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_NEXT)
        icon11.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.next_btn.setIcon(icon11)

        self.horizontalLayout_5.addWidget(self.next_btn)

        # forward
        self.forward_btn = QPushButton(self)
        self.forward_btn.setObjectName(u"forward_btn")
        self.forward_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_FORWARD)
        icon12.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.forward_btn.setIcon(icon12)
        self.forward_btn.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.forward_btn)

    def initialize_slider_progress(self):
        self.song_progress_slide = QSlider(self)
        self.song_progress_slide.setObjectName(u"song_progress_slide")
        self.song_progress_slide.setMinimumSize(QSize(0, 20))
        self.song_progress_slide.setCursor(QCursor(Qt.PointingHandCursor))
        self.song_progress_slide.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.song_progress_slide)

    def initialize_label_track_title(self):
        self.play_title = QLabel(self)
        self.play_title.setObjectName(u"play_title")
        self.play_title.setMinimumSize(QSize(0, 25))
        self.play_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.play_title)

    def initialize_label_current_timestamp(self):
        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"current_timestamp")

        self.horizontalLayout_6.addWidget(self.label_5)

    def initialize_button_thumbnail(self):
        self.thumbnail = QPushButton(self)
        self.thumbnail.setObjectName(u"thumbnail")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Expanding)
        sizePolicy8.setHeightForWidth(
            self.thumbnail.sizePolicy().hasHeightForWidth())
        self.thumbnail.setSizePolicy(sizePolicy8)
        self.thumbnail.setMinimumSize(QSize(50, 50))
        self.thumbnail.setMaximumSize(QSize(100, 100))
        self.thumbnail.setSizeIncrement(QSize(5, 5))
        icon = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_LOGO)
        icon.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.thumbnail.setIcon(icon)
        self.thumbnail.setIconSize(QSize(100, 100))
        self.thumbnail.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.thumbnail)

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_PLAY_BAR)

        with open(stylesheet_path, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
