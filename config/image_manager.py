from os import path
DIR_ROOT = path.dirname(path.dirname(__file__))

DIR_IMAGE = path.join(path.join(DIR_ROOT, 'resource'),
                         'images')

# side bars
IMAGE_LOGO = path.join(DIR_IMAGE, 'logo.png')
IMAGE_HOME_BTN_1 = IMAGE_HOME_BTN_2 = path.join(DIR_IMAGE, 'home.png')
IMAGE_LIBRARY_BTN_1 = IMAGE_LIBRARY_BTN_2 = path.join(DIR_IMAGE, 'musical-library.png')
IMAGE_PLAYLIST_BTN_1 = IMAGE_PLAYLIST_BTN_2 = path.join(DIR_IMAGE, 'playlist.png')
IMAGE_DOWNLOAD_BTN_1 = IMAGE_DOWNLOAD_BTN_2 = path.join(DIR_IMAGE, 'download.png')
IMAGE_SETTINGS_BTN_1 = IMAGE_SETTINGS_BTN_2 = path.join(DIR_IMAGE, 'setting.png')

# top bar
IMAGE_MENU = path.join(DIR_IMAGE, 'menu.png')
IMAGE_SEARCH = path.join(DIR_IMAGE, 'search.png')

# play bar
IMAGE_BACKWARD = path.join(DIR_IMAGE, 'backward.png')
IMAGE_CYCLE = path.join(DIR_IMAGE, 'cycle.png')
IMAGE_FORWARD = path.join(DIR_IMAGE, 'forward.png')
IMAGE_NEXT = path.join(DIR_IMAGE, 'next.png')
IMAGE_PAUSE = path.join(DIR_IMAGE, 'pause.png')
IMAGE_PLAY = path.join(DIR_IMAGE, 'play.png')
IMAGE_PREV = path.join(DIR_IMAGE, 'prev.png')
IMAGE_REPEAT = path.join(DIR_IMAGE, 'repeat.png')
IMAGE_SHUFFLE = path.join(DIR_IMAGE, 'suffle.png')
IMAGE_VOLUME = path.join(DIR_IMAGE, 'volume.png')
