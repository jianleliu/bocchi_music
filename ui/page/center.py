from .page_manager import Pages
from PySide6.QtGui import (QPaintEvent)
from PySide6.QtWidgets import (QSizePolicy, QStackedWidget)
import os
from config.style_manager import STYLE_CENTER

STYLE_DIR = os.path.join(os.path.dirname(__file__),
                         f'../../resource/style')


class CenterPages(QStackedWidget):
    def __init__(self, centralWidget):
        super().__init__(centralWidget)
        self.setObjectName(u"center_pages")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy8)
        # add pages to this stacked widget
        self.add_pages()
        self.setCurrentIndex(0)

        # apply stylesheet
        self.apply_stylesheet()
        # self.setParent()

    def add_pages(self):
        for page in Pages:
            self.addWidget(page)

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_CENTER)

        with open(stylesheet_path, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def paintEvent(self, arg__1: QPaintEvent) -> None:
        pass
