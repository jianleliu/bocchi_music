from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTableView, QHeaderView
from PySide6.QtCore import Qt, QSortFilterProxyModel
import sys

class MyTableWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setRowCount(5)  # Example: set initial row count to 5
        
        # Populate table (just for demonstration)
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = QTableWidgetItem(f"Row {row}, Col {col}")
                self.table.setItem(row, col, item)
        
        # Setup table view and proxy model
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.table.model())
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        
        self.table_view = QTableView()
        self.table_view.setModel(self.proxy_model)
        self.table_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_view.verticalHeader().hide()
        self.table_view.setSortingEnabled(True)
        self.table_view.setSelectionMode(QTableView.SingleSelection)
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        
        # Add a QLineEdit for entering search text
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Enter text to search")
        self.search_box.textChanged.connect(self.filter_table)
        
        # Setup layout
        layout = QVBoxLayout()
        layout.addWidget(self.search_box)
        layout.addWidget(self.table_view)
        
        self.setLayout(layout)
    
    def filter_table(self):
        text_to_search = self.search_box.text().strip()
        self.proxy_model.setFilterFixedString(text_to_search)
        self.proxy_model.setFilterKeyColumn(-1)  # Filter all columns

if __name__ == '__main__':
    app = QApplication(sys.argv)
    table_widget = MyTableWidget()
    table_widget.setWindowTitle('Filtered Table Example')
    table_widget.resize(600, 400)
    table_widget.show()
    sys.exit(app.exec_())
