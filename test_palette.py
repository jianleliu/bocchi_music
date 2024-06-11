# from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
# from PySide6.QtGui import QColor

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.tableWidget = QTableWidget()
#         self.tableWidget.setRowCount(3)
#         self.tableWidget.setColumnCount(3)

#         self.fill_table()

#         self.setCentralWidget(self.tableWidget)

#     def fill_table(self):
#         for i in range(self.tableWidget.rowCount()):
#             for j in range(self.tableWidget.columnCount()):
#                 item = QTableWidgetItem(f"Row {i} Col {j}")
#                 self.tableWidget.setItem(i, j, item)

#         # Set the background color for the second row
#         self.set_row_background_color(1, QColor(255, 200, 200))  # Adjust RGB values as needed

#     def set_row_background_color(self, row, color):
#         for column in range(self.tableWidget.columnCount()):
#             item = self.tableWidget.item(row, column)
#             item.setBackground(color)

# if __name__ == "__main__":
#     app = QApplication([])

#     mainWindow = MainWindow()
#     mainWindow.show()

#     app.exec()
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QPushButton, QColorDialog
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
class ColorPicker(QWidget):
    def __init__(self, table_widget):
        super().__init__()
        self.table_widget = table_widget
        self.color = QColorDialog().getColor()
        layout = QVBoxLayout()
        self.color_btn = QPushButton('Pick a Color')
        self.color_btn.clicked.connect(self.pick_color)
        layout.addWidget(self.color_btn)
        self.setLayout(layout)
        self.color.currentColorChanged.connect(self.pick_color)

    def pick_color(self):
      selected_items = self.table_widget.selectedItems()
      for item in selected_items:
          item.setBackground(color)


class TableWidgetDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Table Widget Demo")

        # Initialize table widget
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)

        # Set headers
        self.tableWidget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Insert data into table
        for row in range(5):
            for col in range(3):
                self.tableWidget.setItem(row, col, QTableWidgetItem(f"Item {row}-{col}"))

        # Initialize color picker widget
        self.color_picker = ColorPicker(self.tableWidget)
        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.color_picker)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableWidgetDemo()
    window.setGeometry(100, 100, 600, 400)
    window.show()
    sys.exit(app.exec())