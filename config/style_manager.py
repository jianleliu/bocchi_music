"""CONSTANT file storing stylesheet path."""
from os import path
DIR_ROOT = path.dirname(path.dirname(__file__))

DIR_STYLE = path.join(path.join(DIR_ROOT, 'resource'), 'style')

# all stylesheets are in style folder
STYLE_MAIN_WINDOW = path.join(DIR_STYLE, 'main_window.qss')
STYLE_CENTRAL = path.join(DIR_STYLE, 'central.qss')
STYLE_SIDE_SHRINKED = path.join(DIR_STYLE, 'side_shrinked.qss')
STYLE_SIDE_EXPANDED = path.join(DIR_STYLE, 'side_expanded.qss')
STYLE_TOP_BAR = path.join(DIR_STYLE, 'top_bar.qss')
STYLE_PLAY_BAR = path.join(DIR_STYLE, 'play_bar.qss')

# center stacked pages widget
STYLE_CENTER = path.join(DIR_STYLE, 'center.qss')
STYLE_LIBRARY_PAGE = path.join(DIR_STYLE, 'library_page.qss')
STYLE_DOWNLOAD_PAGE = path.join(DIR_STYLE, 'download_page.qss')
