from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QFile, QTextStream,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)

import os
from config.style_manager import STYLE_CENTRAL


class CentralWidget(QFrame):
  def __init__(self, MainWindow):
    super().__init__(MainWindow)
    self.setObjectName('central_widget')
    
    
    # apply style sheet
    self.apply_stylesheet()
    # self.setStyleSheet(TEMP_STYLE)
    
  def apply_stylesheet(self):
    with open(STYLE_CENTRAL, "r") as file:
        stylesheet = file.read()
        self.setStyleSheet(stylesheet)
