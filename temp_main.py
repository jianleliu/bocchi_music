import sys
import os
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

# Define a placeholder for IMAGE_CYCLE, replace it with the actual image name
from config.image_manager import IMAGE_CYCLE

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Icon Test")
        self.setGeometry(100, 100, 300, 200)
        
        self.play_order_btn = QPushButton("Test Button", self)
        self.play_order_btn.setGeometry(50, 50, 200, 50)
        
        icon13 = QIcon()
        image_path = os.path.join(os.path.dirname(__file__), f'resource/images/{IMAGE_CYCLE}')
        icon13.addFile(image_path, QSize(), QIcon.Normal, QIcon.Off)
        self.play_order_btn.setIcon(icon13)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec())
