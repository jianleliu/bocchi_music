from handler.handler_topBar import handle_toggle_menu
from handler.handler_side1 import handle_page_switch
from initialization.initialization_external import initialize_external
from ui.menu.status_bar import StatusBar
from ui.menu.menu_bar import MenuBar
from config.style_manager import STYLE_MAIN_WINDOW
from config.image_manager import IMAGE_LOGO
from .central import CentralWidget
from ui.top.top_bar import TopBar
from ui.side.Side_2 import SideExpanded
from ui.side.side_1 import SideShrinked
from ui.page.center import CenterPages
from ui.bottom.play_bar import PlayBar
from PySide6.QtCore import (
    QSize)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QSizePolicy,
                               QGridLayout, QHBoxLayout, QMainWindow, QVBoxLayout)
import os

IMAGE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../resource/images')
STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../resource/style')


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # self.setupUi(self)
        initialize_external()
        self.setObjectName('main_window')
        self.setWindowTitle('Bocchi Music')
        # self.apply_stylesheet()

        self.widget_centralWidget = CentralWidget(self)

        # initialize widgets
        self.widget_playBar = PlayBar(self.widget_centralWidget)
        self.widget_centerPages = CenterPages(self.widget_centralWidget)
        self.widget_sideShrinked = SideShrinked(self.widget_centralWidget)
        self.widget_sideExpanded = SideExpanded(self.widget_centralWidget)
        self.widget_topBar = TopBar(self.widget_centralWidget)

        # menu bar
        self.setCentralWidget(self.widget_centralWidget)
        self.menuBar_menu_bar = MenuBar(self)
        self.statusBar_status_bar = StatusBar(self)
        self.setMenuBar(self.menuBar_menu_bar)
        self.setStatusBar(self.statusBar_status_bar)

        # configure widget layouts
        self.configure_layout()
        self.configure_default_value()

        # apply stylesheet
        self.apply_stylesheet()

        # handle widget signal
        self.handle_signal()

    def handle_signal(self):
        self.handle_playBar_signal()
        self.handle_centerPages_signal()
        self.handle_sideExpanded_signal()
        self.handle_sideShrinked_signal()
        self.handle_topBar_signal()

    def handle_playBar_signal(self):
        pass

    def handle_centerPages_signal(self):
        pass

    def handle_sideShrinked_signal(self):
        self.widget_sideShrinked.signal_page_switch.connect(
            lambda page_num: handle_page_switch(self, page_num))

    def handle_sideExpanded_signal(self):
        self.widget_sideExpanded.signal_page_switch.connect(
            lambda page_num: handle_page_switch(self, page_num))

    def handle_topBar_signal(self):
        self.widget_topBar.signal_menu_toggle.connect(
            lambda checked: handle_toggle_menu(self, checked))

    def configure_layout(self):
        self.gridLayout_2 = QGridLayout(self.widget_centralWidget)
        self.gridLayout_2.setObjectName('Outer_most_layout')
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_12 = QHBoxLayout()
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"top_and_center")
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"side_bars")

        self.horizontalLayout_11.addWidget(self.widget_sideShrinked)
        self.horizontalLayout_11.addWidget(self.widget_sideExpanded)

        self.verticalLayout_10.addWidget(self.widget_topBar)
        self.verticalLayout_10.addWidget(self.widget_centerPages)

        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.verticalLayout_9.addWidget(self.widget_playBar)

        self.gridLayout_2.addLayout(self.verticalLayout_9, 1, 0, 1, 1)

    def configure_default_value(self):
        self.setEnabled(True)
        self.resize(749, 643)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMouseTracking(False)
        icon = QIcon()
        image_path = os.path.join(IMAGE_DIR, IMAGE_LOGO)
        icon.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_MAIN_WINDOW)

        with open(stylesheet_path, "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
