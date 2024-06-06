from PySide6.QtCore import (QRect, Qt)
from PySide6.QtGui import (QCursor, QFont)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QTabWidget, QVBoxLayout, QWidget)


class SettingPage(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"setting_page")
        self.verticalLayout_26 = QVBoxLayout(self)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")

        #
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setObjectName(u"tabWidget")

        # initialize tabs
        self.parameter_tab()
        self.second_tab()

    def parameter_tab(self):
        self.parameters_tab = QWidget()
        self.parameters_tab.setObjectName(u"parameters_tab")
        self.label_2 = QLabel(self.parameters_tab)
        self.label_2.setObjectName(u"title_download")
        self.label_2.setGeometry(QRect(20, 20, 131, 21))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_2.setFont(font1)

        # widget stores components below
        self.widget_2 = QWidget(self.parameters_tab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 50, 421, 121))
        self.layoutWidget = QWidget(self.widget_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 251, 40))

        # default playlist download path
        self.verticalLayout_28 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_default_playlist_download_path")
        font = QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)

        self.verticalLayout_28.addWidget(self.label_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.playlist_dir_le = QLineEdit(self.layoutWidget)
        self.playlist_dir_le.setObjectName(u"playlist_dir_le")

        self.horizontalLayout_13.addWidget(self.playlist_dir_le)

        self.playlist_path_browse = QPushButton(self.layoutWidget)
        self.playlist_path_browse.setObjectName(u"playlist_path_browse")
        self.playlist_path_browse.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_13.addWidget(self.playlist_path_browse)

        self.verticalLayout_28.addLayout(self.horizontalLayout_13)

        # default track download path
        self.layoutWidget1 = QWidget(self.widget_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 10, 251, 40))
        self.verticalLayout_27 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_default_track_download_path")
        self.label_3.setFont(font)

        self.verticalLayout_27.addWidget(self.label_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.song_dir_le = QLineEdit(self.layoutWidget1)
        self.song_dir_le.setObjectName(u"song_dir_le")

        self.horizontalLayout_10.addWidget(self.song_dir_le)

        self.song_path_browse = QPushButton(self.layoutWidget1)
        self.song_path_browse.setObjectName(u"song_path_browse")
        self.song_path_browse.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.song_path_browse)

        self.verticalLayout_27.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.parameters_tab, "Parameters")

    def second_tab(self):
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "Other")

        self.verticalLayout_26.addWidget(self.tabWidget)
