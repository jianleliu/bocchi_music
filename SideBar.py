from PySide6.QtCore import Qt
from ui_application import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class SideBar(QMainWindow, Ui_MainWindow):
  def __init__(self) -> None:
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle('Bocchi Music')
    
    self.side1.setHidden(True)
    
    self.home_btn_1.clicked.connect(self.switch_to_home_page)
    self.home_btn_2.clicked.connect(self.switch_to_home_page)
    
    self.library_btn_1.clicked.connect(self.switch_to_library_page)
    self.library_btn_2.clicked.connect(self.switch_to_library_page)
    
    self.playlist_btn_1.clicked.connect(self.switch_to_playlist_page)
    self.playlist_btn_2.clicked.connect(self.switch_to_playlist_page)
    
    self.download_btn_1.clicked.connect(self.switch_to_download_page)
    self.download_btn_2.clicked.connect(self.switch_to_download_page)
    
    self.setting_btn_1.clicked.connect(self.switch_to_setting_page)
    self.setting_btn_2.clicked.connect(self.switch_to_setting_page)
    
  def switch_to_home_page(self):
    self.page_widget.setCurrentIndex(0)
  
  def switch_to_library_page(self):
    self.page_widget.setCurrentIndex(1)
    
  def switch_to_playlist_page(self):
    self.page_widget.setCurrentIndex(2)

  def switch_to_download_page(self):
    self.page_widget.setCurrentIndex(3)

  def switch_to_setting_page(self):
    self.page_widget.setCurrentIndex(4)