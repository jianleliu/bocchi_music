from PySide6.QtWidgets import QApplication
import sys
# this has to be instantiated before any widgets instance.
app = QApplication(sys.argv)
from ui.MainWindow import MainWindow



if __name__ == '__main__':
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
