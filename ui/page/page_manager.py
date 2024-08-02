"""page manager ui."""
import logging

from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import QFrame, QSizePolicy, QStackedWidget

from config.default_parameters import (DEFAULT_ENCODING,
                                       DEFAULT_PAGE_DOWNLOAD_NAME,
                                       DEFAULT_PAGE_HOME_NAME,
                                       DEFAULT_PAGE_LIBRARY_NAME,
                                       DEFAULT_PAGE_PLAYLIST_NAME,
                                       DEFAULT_PAGE_SETTINGS_NAME)
from config.style_manager import STYLE_CENTER

from .download_page import DownloadPage
from .home_page import HomePage
from .library_page import LibraryPage
from .playlist_page import PlaylistPage
from .setting_page import SettingPage

logger = logging.getLogger(__name__)


class PageManager(QStackedWidget):
    """page manager ui, inherits QStackedWidget.

    Args:
        QStackedWidget (QStackedWidget): PySide6.QtWidgets 
    """

    def __init__(self, centralWidget):
        """child of centralWidget

        Args:
            centralWidget (QFrame): PySide6.QtWidgets 
        """
        logger.info('initializing')
        super().__init__(centralWidget)
        self.setObjectName('center_pages')
        self.pages = {}
        size_policy_8 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                    QSizePolicy.Policy.Expanding)
        size_policy_8.setHorizontalStretch(0)
        size_policy_8.setVerticalStretch(0)
        size_policy_8.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy_8)

        # add pages to this stacked widget
        logger.info('initializing pages')
        self.add_page(DEFAULT_PAGE_HOME_NAME, HomePage())
        self.add_page(DEFAULT_PAGE_LIBRARY_NAME, LibraryPage())
        self.add_page(DEFAULT_PAGE_PLAYLIST_NAME, PlaylistPage())
        self.add_page(DEFAULT_PAGE_DOWNLOAD_NAME, DownloadPage())
        self.add_page(DEFAULT_PAGE_SETTINGS_NAME, SettingPage())

        # apply stylesheet
        logger.info('initializing stylesheet')
        self._apply_stylesheet()
        self.setCurrentIndex(3)

    def add_page(self, name: str, page: QFrame, style_sheet: str = None) -> None:
        """add page to this instance.

        Args:
            name (str):  object name of the new page, can be found in default parameters.
            page (QFrame): QFrame object as new page.
            style_sheet (str, optional): stylesheet path. Defaults to None.
        """
        logger.info('initializing %s', name)
        if style_sheet:
            page.setStyleSheet(style_sheet)
        self.addWidget(page)
        self.pages[name] = page

    def get_page(self, name: str) -> QFrame:
        """getter for page instance.

        Args:
            name (str): page instance object name.

        Returns:
            QFrame: page instance.
        """
        return self.pages.get(name)

    def set_current_page(self, name: str) -> None:
        """setter for current display page.

        Args:
            name (str): page instance object name.
        """
        page = self.get_page(name)
        if page:
            self.setCurrentWidget(page)

    def _apply_stylesheet(self):
        """_apply_stylesheet
        """
        with open(STYLE_CENTER, 'r', encoding=DEFAULT_ENCODING) as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    # pylint: disable=unnecessary-pass
    def paintEvent(self, arg__1: QPaintEvent) -> None:
        """not used. override default paintEvent().

        Args:
            arg__1 (QPaintEvent): _description_
        """
        pass
    # pylint: enable=unnecessary-pass
