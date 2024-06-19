from PySide6.QtWidgets import (QFrame, QLabel, QScrollArea, QVBoxLayout)
import logging

logger = logging.getLogger(__name__)

class HomePage(QFrame):
    def __init__(self):
        logger.info('initializing')
        super().__init__()
        self.setObjectName('home_page')
        self.verticalLayout_22 = QVBoxLayout(self)
        self.scrollArea = QScrollArea(self)
        self.textLabel = QLabel(self.scrollArea)
        self.textLabel.setText('this is home page')
        self.verticalLayout_22.addWidget(self.scrollArea)
