from PySide6.QtCore import (QRect)
from PySide6.QtWidgets import (QMenuBar)


class MenuBar(QMenuBar):
    def __init__(self, centralWidget) -> None:
        super().__init__(centralWidget)
        self.setObjectName('menu_bar')
        self.setGeometry(QRect(0, 0, 749, 18))
