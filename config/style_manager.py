# all stylesheets are in style folder
STYLE_MAIN_WINDOW = 'main_window.qss'
STYLE_CENTRAL = 'central.qss'
STYLE_SIDE_SHRINKED = 'side_shrinked.qss'
STYLE_SIDE_EXPANDED = 'side_expanded.qss'
STYLE_TOP_BAR = 'top_bar.qss'
STYLE_PLAY_BAR = 'play_bar.qss'

# center stacked pages widget
STYLE_CENTER = 'center.qss'
STYLE_LIBRARY_PAGE = 'library_page.qss'
STYLE_DOWNLOAD_PAGE = 'download_page.qss'

import os

STYLE_DIR = os.path.join(os.path.dirname(__file__), '../resource/style')

def read_stylesheet(stylesheet_name):
  stylesheet_path = os.path.join(STYLE_DIR, stylesheet_name)
  
  with open(stylesheet_path, "r") as file:
      return file.read()