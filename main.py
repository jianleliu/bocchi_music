import sys

# this has to be instantiated before any widgets instance.
from app import app
from ui.MainWindow import MainWindow



if __name__ == '__main__':
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
