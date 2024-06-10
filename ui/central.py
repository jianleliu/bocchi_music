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
from config.style_manager import STYLE_CENTRAL, read_stylesheet

STYLE_DIR = os.path.join(os.path.dirname(__file__),
                              f'../resource/style')

TEMP_STYLE = """QWidget#central_widget {
  background-color: #ade8f4;
  background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 94, 86, 100), stop:1 rgba(255, 255, 255, 255));
}
"""

class CentralWidget(QFrame):
  def __init__(self, MainWindow):
    super().__init__(MainWindow)
    self.setObjectName('central_widget')
    
    
    # apply style sheet
    self.apply_stylesheet()
    # self.setStyleSheet(TEMP_STYLE)
    
  def apply_stylesheet(self):
    stylesheet_path = os.path.join(STYLE_DIR, STYLE_CENTRAL)
    with open(stylesheet_path, "r") as file:
        stylesheet = file.read()
        self.setStyleSheet(stylesheet)
