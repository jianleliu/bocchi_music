from .download_page import DownloadPage
from .library_page import LibraryPage
from .setting_page import SettingPage
from .home_page import HomePage
from .playlist_page import PlaylistPage

Pages = [
    HomePage(),
    LibraryPage(),
    PlaylistPage(),
    DownloadPage(),  
    SettingPage(),
]
