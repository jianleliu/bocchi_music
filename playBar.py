from PySide6.QtCore import Qt
from ui_application import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class PlayBar():
  def __init__(self, playlist: dict, current_song: str) -> None:
    self.playlist = playlist
    self.current_song = current_song
    
  def play_song(self, path):
    pass
  
  def forward(self):
    pass
  
  def backward(self):
    pass
  
  def next_song(self):
    pass
  
  def prev_song(self):
    pass
  
  def resume_song(self):
    pass
  
  def pause_song(self):
    pass