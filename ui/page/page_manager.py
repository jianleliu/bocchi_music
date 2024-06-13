from PySide6.QtGui import (QPaintEvent)
from PySide6.QtWidgets import (QSizePolicy, QFrame, QStackedWidget)
import os
from config.style_manager import STYLE_CENTER
from .home_page import HomePage
from .library_page import LibraryPage
from .playlist_page import PlaylistPage
from .download_page import DownloadPage
from .setting_page import SettingPage

STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class PageManager(QStackedWidget):
    def __init__(self, centralWidget):
        super().__init__(centralWidget)
        self.setObjectName(u"center_pages")
        self.pages = {}
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy8)
        
        
        # add pages to this stacked widget
        self.add_page('page_home', HomePage())
        self.add_page('page_library', LibraryPage())
        self.add_page('page_playlist', PlaylistPage())
        self.add_page('page_download', DownloadPage())
        self.add_page('page_settings', SettingPage())
        

        # apply stylesheet
        self.apply_stylesheet()
        self.setCurrentIndex(2)

    def add_page(self, name: str, page: QFrame, style_sheet=None):
        if style_sheet:
            page.setStyleSheet(style_sheet)
        self.addWidget(page)
        self.pages[name] = page

    def get_page(self, name: str) -> QFrame:
        return self.pages.get(name)

    def set_current_page(self, name: str):
        page = self.get_page(name)
        if page:
            self.setCurrentWidget(page)

    def apply_stylesheet(self):
        with open(STYLE_CENTER, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def paintEvent(self, arg__1: QPaintEvent) -> None:
        pass
