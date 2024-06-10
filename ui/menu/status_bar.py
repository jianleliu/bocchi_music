from PySide6.QtWidgets import (QStatusBar)


class StatusBar(QStatusBar):
    def __init__(self, centralWidget):
        super().__init__(centralWidget)
        self.setObjectName('status_bar')
