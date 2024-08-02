"""home page ui, currently blank."""
import logging

from PySide6.QtWidgets import QFrame, QLabel, QScrollArea, QVBoxLayout

from config.default_parameters import DEFAULT_PAGE_HOME_NAME

logger = logging.getLogger(__name__)


class HomePage(QFrame):
    """home page ui, currently blank.

    Args:
        QFrame (QFrame): PySide6.QtWidgets
    """

    def __init__(self):
        logger.info('initializing')
        super().__init__()
        self.setObjectName(DEFAULT_PAGE_HOME_NAME)
        self.vertical_layout_22 = QVBoxLayout(self)
        self.scroll_area = QScrollArea(self)
        self.text_label = QLabel(self.scroll_area)
        self.text_label.setText('this is home page')
        self.vertical_layout_22.addWidget(self.scroll_area)
