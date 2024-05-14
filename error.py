from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox

class ErrorPopup(QMessageBox):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setIcon(QMessageBox.Critical)
        self.setText("Error")
        self.setInformativeText(message)
        self.setWindowTitle("Error")