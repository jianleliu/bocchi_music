"""Not used"""
from PySide6.QtWidgets import QStatusBar


class StatusBar(QStatusBar):
    """GUI status bar.

    Args:
        QStatusBar (QStatusBar): PySide6.QtWidgets
    """

    def __init__(self, centralWidget):
        super().__init__(centralWidget)
        self.setObjectName('status_bar')
