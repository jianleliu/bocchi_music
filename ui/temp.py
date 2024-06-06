
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget)
import os
from config.style_manager import STYLE_CENTRAL, read_stylesheet
import sys

STYLE_DIR = os.path.join(os.path.dirname(__file__), '../resource/style')

class CentralWidget(QWidget):
    def __init__(self, MainWindow):
        super().__init__(MainWindow)
        self.setObjectName("central_widget")
        
        # Example layout with a button to show the widget
        layout = QVBoxLayout(self)
        button = QPushButton("Test Button", self)
        layout.addWidget(button)
        
        self.setStyleSheet(read_stylesheet(STYLE_CENTRAL))
        # Apply style sheet
        # self.apply_stylesheet()
        # self.setStyleSheet("background-color: #ade8f4;background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 rgba(3, 94, 86, 255), stop: 1 rgba(255, 255, 255, 255));")
        self.setStyleSheet()

    def apply_stylesheet(self):
        stylesheet_path = os.path.join(STYLE_DIR, STYLE_CENTRAL)
        with open(stylesheet_path, "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
            print(stylesheet)

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stylesheet Test")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec())
