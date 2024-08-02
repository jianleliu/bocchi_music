"""ui file for central widget."""
import logging

from PySide6.QtWidgets import QFrame

from config.style_manager import STYLE_CENTRAL
from config.default_parameters import DEFAULT_ENCODING

logger = logging.getLogger(__name__)


class CentralWidget(QFrame):
    """central widget, base widget for all other widget. inehrit QFrame.

    Args:
        QFrame (QFrame): PySide6.QtWidgets
    """

    def __init__(self, MainWindow):
        """child of MainWindow.

        Args:
            MainWindow (QMainWindow): Window GUI.
        """
        logger.info('initializing')
        super().__init__(MainWindow)

        self.setObjectName('central_widget')

        # apply style sheet
        logger.info('initializing stylesheet')
        self._apply_stylesheet()
        # self.setStyleSheet(TEMP_STYLE)

    def _apply_stylesheet(self) -> None:
        """_apply_stylesheet
        """
        with open(STYLE_CENTRAL, "r", encoding=DEFAULT_ENCODING) as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
