import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QPainter, QPen, QFont, QIcon, QTransform
from PySide6.QtCore import Qt, QTimer, QSize, QRect
from config.image_manager import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rotating Button")
        self.setGeometry(100, 100, 300, 200)

        self.horizontalLayout_whole = QHBoxLayout(self)
        self.setLayout(self.horizontalLayout_whole)

        self.initialize_button_thumbnail()

        # Create timer to continuously rotate button
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.rotateButton)
        self.timer.start(50)  # Adjust the speed of rotation by changing the timeout value

    def initialize_button_thumbnail(self):
        self.btn_spinning_bocchi = QPushButton(self)
        self.btn_spinning_bocchi.setObjectName('thumbnail')
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Expanding)
        sizePolicy8.setHeightForWidth(
            self.btn_spinning_bocchi.sizePolicy().hasHeightForWidth())
        self.btn_spinning_bocchi.setSizePolicy(sizePolicy8)
        self.btn_spinning_bocchi.setMinimumSize(QSize(50, 50))
        self.btn_spinning_bocchi.setMaximumSize(QSize(100, 100))
        self.btn_spinning_bocchi.setSizeIncrement(QSize(5, 5))
        # Replace 'IMAGE_LOGO' with the path to the image you want to set as the icon for the button
        icon = QIcon(IMAGE_LOGO)
        self.btn_spinning_bocchi.setIcon(icon)
        self.btn_spinning_bocchi.setIconSize(QSize(100, 100))
        self.btn_spinning_bocchi.setCheckable(True)

        self.horizontalLayout_whole.addWidget(self.btn_spinning_bocchi)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.blue, 1, Qt.DashLine))

        # Get button's geometry
        rect = self.btn_spinning_bocchi.geometry()

        # Draw rectangle around the button
        painter.drawRect(rect)

        transform = painter.transform()
        transform.translate(rect.center().x(), rect.center().y())
        transform.rotate(self.angle)
        painter.setTransform(transform)

        painter.setFont(QFont("Helvetica", 12))
        painter.setPen(QPen(Qt.black, 1))
        text_rect = QRect(-rect.width()/2, -rect.height()/2, rect.width(), rect.height())
        painter.drawText(text_rect, Qt.AlignCenter, self.btn_spinning_bocchi.text())

    def rotateButton(self):
        # Rotate button by 10 degrees on each timeout
        self.angle += 10
        transform = QTransform().rotate(self.angle)
        self.button.setTransform(transform)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())