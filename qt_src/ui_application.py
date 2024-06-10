# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)
import resources_rc
import resources_rc
import resources_rc
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(749, 643)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background: #caf0f8;\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #ade8f4;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 94, 86, 100), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.side1 = QWidget(self.centralwidget)
        self.side1.setObjectName(u"side1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.side1.sizePolicy().hasHeightForWidth())
        self.side1.setSizePolicy(sizePolicy1)
        self.side1.setMouseTracking(False)
        self.side1.setStyleSheet(u"QWidget {\n"
"    background-color: #90e0ef;\n"
"	border: 5px solid transparent;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    text-align: left;\n"
"    border: 5px solid transparent; /* Add a transparent border */\n"
"    border-radius: 5px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid white; /* Set border color on hover */\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.side1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_5 = QLabel(self.side1)
        self.logo_5.setObjectName(u"logo_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.logo_5.sizePolicy().hasHeightForWidth())
        self.logo_5.setSizePolicy(sizePolicy2)
        self.logo_5.setMinimumSize(QSize(0, 0))
        self.logo_5.setMaximumSize(QSize(40, 40))
        self.logo_5.setAutoFillBackground(False)
        self.logo_5.setPixmap(QPixmap(u":/newPrefix/images/logo.png"))
        self.logo_5.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.home_btn_1 = QPushButton(self.side1)
        self.home_btn_1.setObjectName(u"home_btn_1")
        self.home_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/images/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_1.setIcon(icon1)
        self.home_btn_1.setIconSize(QSize(18, 18))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.home_btn_1)

        self.library_btn_1 = QPushButton(self.side1)
        self.library_btn_1.setObjectName(u"library_btn_1")
        self.library_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/images/musical-library.png", QSize(), QIcon.Normal, QIcon.Off)
        self.library_btn_1.setIcon(icon2)
        self.library_btn_1.setIconSize(QSize(18, 18))
        self.library_btn_1.setCheckable(True)
        self.library_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.library_btn_1)

        self.playlist_btn_1 = QPushButton(self.side1)
        self.playlist_btn_1.setObjectName(u"playlist_btn_1")
        self.playlist_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/images/playlist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playlist_btn_1.setIcon(icon3)
        self.playlist_btn_1.setIconSize(QSize(18, 18))
        self.playlist_btn_1.setCheckable(True)
        self.playlist_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.playlist_btn_1)

        self.download_btn_1 = QPushButton(self.side1)
        self.download_btn_1.setObjectName(u"download_btn_1")
        self.download_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/images/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.download_btn_1.setIcon(icon4)
        self.download_btn_1.setIconSize(QSize(18, 18))
        self.download_btn_1.setCheckable(True)
        self.download_btn_1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.download_btn_1)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 188, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.setting_btn_1 = QPushButton(self.side1)
        self.setting_btn_1.setObjectName(u"setting_btn_1")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/images/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_btn_1.setIcon(icon5)
        self.setting_btn_1.setIconSize(QSize(18, 18))
        self.setting_btn_1.setCheckable(True)
        self.setting_btn_1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.setting_btn_1)


        self.horizontalLayout_11.addWidget(self.side1)

        self.side2 = QWidget(self.centralwidget)
        self.side2.setObjectName(u"side2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.side2.sizePolicy().hasHeightForWidth())
        self.side2.setSizePolicy(sizePolicy3)
        self.side2.setStyleSheet(u"QWidget {\n"
"    background-color: #90e0ef;\n"
"	border: 5px solid transparent;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    text-align: left;\n"
"    border: 5px solid transparent; /* Add a transparent border */\n"
"    border-radius: 5px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid white; /* Set border color on hover */\n"
"}\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.side2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_3 = QLabel(self.side2)
        self.logo_3.setObjectName(u"logo_3")
        sizePolicy2.setHeightForWidth(self.logo_3.sizePolicy().hasHeightForWidth())
        self.logo_3.setSizePolicy(sizePolicy2)
        self.logo_3.setMinimumSize(QSize(0, 0))
        self.logo_3.setMaximumSize(QSize(40, 40))
        self.logo_3.setAutoFillBackground(False)
        self.logo_3.setPixmap(QPixmap(u":/newPrefix/images/logo.png"))
        self.logo_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_btn_2 = QPushButton(self.side2)
        self.home_btn_2.setObjectName(u"home_btn_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.home_btn_2.sizePolicy().hasHeightForWidth())
        self.home_btn_2.setSizePolicy(sizePolicy4)
        self.home_btn_2.setSizeIncrement(QSize(0, 0))
        self.home_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_2.setIcon(icon1)
        self.home_btn_2.setIconSize(QSize(18, 18))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_btn_2)

        self.library_btn_2 = QPushButton(self.side2)
        self.library_btn_2.setObjectName(u"library_btn_2")
        self.library_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.library_btn_2.setIcon(icon2)
        self.library_btn_2.setIconSize(QSize(18, 18))
        self.library_btn_2.setCheckable(True)
        self.library_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.library_btn_2)

        self.playlist_btn_2 = QPushButton(self.side2)
        self.playlist_btn_2.setObjectName(u"playlist_btn_2")
        self.playlist_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.playlist_btn_2.setIcon(icon3)
        self.playlist_btn_2.setIconSize(QSize(18, 18))
        self.playlist_btn_2.setCheckable(True)
        self.playlist_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.playlist_btn_2)

        self.download_btn_2 = QPushButton(self.side2)
        self.download_btn_2.setObjectName(u"download_btn_2")
        self.download_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.download_btn_2.setStyleSheet(u"")
        self.download_btn_2.setIcon(icon4)
        self.download_btn_2.setIconSize(QSize(18, 18))
        self.download_btn_2.setCheckable(True)
        self.download_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.download_btn_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.spacer_2 = QSpacerItem(17, 238, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.spacer_2)

        self.setting_btn_2 = QPushButton(self.side2)
        self.setting_btn_2.setObjectName(u"setting_btn_2")
        self.setting_btn_2.setIcon(icon5)
        self.setting_btn_2.setIconSize(QSize(18, 18))
        self.setting_btn_2.setCheckable(True)
        self.setting_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.setting_btn_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)


        self.horizontalLayout_11.addWidget(self.side2)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.menu_bar = QWidget(self.centralwidget)
        self.menu_bar.setObjectName(u"menu_bar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.menu_bar.sizePolicy().hasHeightForWidth())
        self.menu_bar.setSizePolicy(sizePolicy5)
        self.menu_bar.setStyleSheet(u"QWidget{\n"
"	background: #90e0ef;\n"
"	border: 5px solid transparent;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-bottom: 1px solid;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.menu_bar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menu_btn = QPushButton(self.menu_bar)
        self.menu_btn.setObjectName(u"menu_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy6)
        self.menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon6)
        self.menu_btn.setCheckable(True)
        self.menu_btn.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.menu_btn)

        self.horizontalSpacer_5 = QSpacerItem(138, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.search_bar = QLineEdit(self.menu_bar)
        self.search_bar.setObjectName(u"search_bar")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy7)
        self.search_bar.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.search_bar)

        self.search_btn = QPushButton(self.menu_bar)
        self.search_btn.setObjectName(u"search_btn")
        sizePolicy6.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy6)
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.search_btn)

        self.horizontalSpacer_6 = QSpacerItem(185, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_10.addWidget(self.menu_bar)

        self.page_widget = QStackedWidget(self.centralwidget)
        self.page_widget.setObjectName(u"page_widget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.page_widget.sizePolicy().hasHeightForWidth())
        self.page_widget.setSizePolicy(sizePolicy8)
        self.page_widget.setStyleSheet(u"background-color: white;\n"
"\n"
"QFrame{\n"
"	background: transparent;\n"
"}\n"
"")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_22 = QVBoxLayout(self.home_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.scrollArea = QScrollArea(self.home_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 304, 258))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_21.setSpacing(12)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.home_title_1 = QLabel(self.scrollAreaWidgetContents)
        self.home_title_1.setObjectName(u"home_title_1")
        sizePolicy.setHeightForWidth(self.home_title_1.sizePolicy().hasHeightForWidth())
        self.home_title_1.setSizePolicy(sizePolicy)
        self.home_title_1.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.home_title_1)

        self.recently_played_grid = QGridLayout()
        self.recently_played_grid.setObjectName(u"recently_played_grid")
        self.recently_played_grid.setHorizontalSpacing(30)
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(50, 50))
        self.widget.setSizeIncrement(QSize(5, 5))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/newPrefix/images/logo.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.label)


        self.recently_played_grid.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(50, 50))
        self.widget_3.setSizeIncrement(QSize(5, 5))
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/newPrefix/images/logo.png"))
        self.label_6.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_6)


        self.recently_played_grid.addWidget(self.widget_3, 0, 1, 1, 1)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(50, 50))
        self.widget_4.setSizeIncrement(QSize(5, 5))
        self.verticalLayout_12 = QVBoxLayout(self.widget_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/newPrefix/images/logo.png"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.label_7)


        self.recently_played_grid.addWidget(self.widget_4, 0, 2, 1, 1)

        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(50, 50))
        self.widget_5.setSizeIncrement(QSize(5, 5))
        self.verticalLayout_13 = QVBoxLayout(self.widget_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/newPrefix/images/logo.png"))
        self.label_8.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_8)


        self.recently_played_grid.addWidget(self.widget_5, 0, 3, 1, 1)


        self.verticalLayout_21.addLayout(self.recently_played_grid)

        self.home_title_2 = QLabel(self.scrollAreaWidgetContents)
        self.home_title_2.setObjectName(u"home_title_2")
        sizePolicy.setHeightForWidth(self.home_title_2.sizePolicy().hasHeightForWidth())
        self.home_title_2.setSizePolicy(sizePolicy)
        self.home_title_2.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.home_title_2)

        self.most_listened_grid = QGridLayout()
        self.most_listened_grid.setObjectName(u"most_listened_grid")
        self.most_listened_grid.setHorizontalSpacing(30)
        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(50, 50))
        self.widget_6.setSizeIncrement(QSize(5, 5))
        self.verticalLayout_14 = QVBoxLayout(self.widget_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u":/newPrefix/images/logo.png"))
        self.label_9.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.label_9)


        self.most_listened_grid.addWidget(self.widget_6, 0, 0, 1, 1)

        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(50, 50))
        self.widget_7.setSizeIncrement(QSize(5, 5))
        self.verticalLayout_15 = QVBoxLayout(self.widget_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/newPrefix/images/logo.png"))
        self.label_10.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.label_10)


        self.most_listened_grid.addWidget(self.widget_7, 0, 1, 1, 1)

        self.widget_8 = QWidget(self.scrollAreaWidgetContents)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(50, 50))
        self.widget_8.setSizeIncrement(QSize(5, 5))
        self.verticalLayout_16 = QVBoxLayout(self.widget_8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u":/newPrefix/images/logo.png"))
        self.label_11.setScaledContents(True)

        self.verticalLayout_16.addWidget(self.label_11)


        self.most_listened_grid.addWidget(self.widget_8, 0, 2, 1, 1)

        self.widget_9 = QWidget(self.scrollAreaWidgetContents)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(50, 50))
        self.widget_9.setSizeIncrement(QSize(5, 5))
        self.verticalLayout_17 = QVBoxLayout(self.widget_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_12 = QLabel(self.widget_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u":/newPrefix/images/logo.png"))
        self.label_12.setScaledContents(True)

        self.verticalLayout_17.addWidget(self.label_12)


        self.most_listened_grid.addWidget(self.widget_9, 0, 3, 1, 1)


        self.verticalLayout_21.addLayout(self.most_listened_grid)

        self.home_title_3 = QLabel(self.scrollAreaWidgetContents)
        self.home_title_3.setObjectName(u"home_title_3")
        sizePolicy.setHeightForWidth(self.home_title_3.sizePolicy().hasHeightForWidth())
        self.home_title_3.setSizePolicy(sizePolicy)
        self.home_title_3.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.home_title_3)

        self.playlist_grid = QGridLayout()
        self.playlist_grid.setObjectName(u"playlist_grid")
        self.playlist_grid.setHorizontalSpacing(30)
        self.widget_10 = QWidget(self.scrollAreaWidgetContents)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(50, 50))
        self.widget_10.setSizeIncrement(QSize(5, 5))
        self.verticalLayout_18 = QVBoxLayout(self.widget_10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_13 = QLabel(self.widget_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setPixmap(QPixmap(u":/newPrefix/images/musical-library.png"))
        self.label_13.setScaledContents(True)

        self.verticalLayout_18.addWidget(self.label_13)


        self.playlist_grid.addWidget(self.widget_10, 0, 0, 1, 1)

        self.widget_11 = QWidget(self.scrollAreaWidgetContents)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(50, 50))
        self.widget_11.setSizeIncrement(QSize(5, 5))
        self.verticalLayout_19 = QVBoxLayout(self.widget_11)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_14 = QLabel(self.widget_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u":/newPrefix/images/musical-library.png"))
        self.label_14.setScaledContents(True)

        self.verticalLayout_19.addWidget(self.label_14)


        self.playlist_grid.addWidget(self.widget_11, 0, 1, 1, 1)

        self.widget_12 = QWidget(self.scrollAreaWidgetContents)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(50, 50))
        self.widget_12.setSizeIncrement(QSize(5, 5))
        self.verticalLayout_20 = QVBoxLayout(self.widget_12)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_15 = QLabel(self.widget_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setPixmap(QPixmap(u":/newPrefix/images/musical-library.png"))
        self.label_15.setScaledContents(True)

        self.verticalLayout_20.addWidget(self.label_15)


        self.playlist_grid.addWidget(self.widget_12, 0, 2, 1, 1)


        self.verticalLayout_21.addLayout(self.playlist_grid)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_22.addWidget(self.scrollArea)

        self.page_widget.addWidget(self.home_page)
        self.library_page = QWidget()
        self.library_page.setObjectName(u"library_page")
        self.library_page.setStyleSheet(u"QLabel {\n"
"	font-size: 20px;\n"
"	background: transparent;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.library_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(494, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.play_random_btn = QPushButton(self.library_page)
        self.play_random_btn.setObjectName(u"play_random_btn")
        self.play_random_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.play_random_btn, 0, 1, 1, 1)

        self.song_table = QTableWidget(self.library_page)
        if (self.song_table.columnCount() < 6):
            self.song_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.song_table.setObjectName(u"song_table")
        self.song_table.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.song_table.setLineWidth(1)
        self.song_table.setDragDropOverwriteMode(False)
        self.song_table.setAlternatingRowColors(True)
        self.song_table.setSortingEnabled(True)
        self.song_table.setWordWrap(True)
        self.song_table.setRowCount(0)
        self.song_table.setColumnCount(6)

        self.gridLayout_3.addWidget(self.song_table, 1, 0, 1, 2)

        self.page_widget.addWidget(self.library_page)
        self.playlist_page = QWidget()
        self.playlist_page.setObjectName(u"playlist_page")
        self.verticalLayout_25 = QVBoxLayout(self.playlist_page)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.r1c1f = QFrame(self.playlist_page)
        self.r1c1f.setObjectName(u"r1c1f")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.r1c1f.sizePolicy().hasHeightForWidth())
        self.r1c1f.setSizePolicy(sizePolicy9)
        self.r1c1f.setFrameShape(QFrame.StyledPanel)
        self.r1c1f.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.r1c1f)

        self.r1c2f = QFrame(self.playlist_page)
        self.r1c2f.setObjectName(u"r1c2f")
        sizePolicy6.setHeightForWidth(self.r1c2f.sizePolicy().hasHeightForWidth())
        self.r1c2f.setSizePolicy(sizePolicy6)
        self.r1c2f.setFrameShape(QFrame.StyledPanel)
        self.r1c2f.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.r1c2f)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.import_btn = QPushButton(self.r1c2f)
        self.import_btn.setObjectName(u"import_btn")
        self.import_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.import_btn)

        self.create_new_playlist_btn = QPushButton(self.r1c2f)
        self.create_new_playlist_btn.setObjectName(u"create_new_playlist_btn")
        self.create_new_playlist_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.create_new_playlist_btn)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_9.addWidget(self.r1c2f)


        self.verticalLayout_25.addLayout(self.horizontalLayout_9)

        self.r2c1w = QWidget(self.playlist_page)
        self.r2c1w.setObjectName(u"r2c1w")
        sizePolicy3.setHeightForWidth(self.r2c1w.sizePolicy().hasHeightForWidth())
        self.r2c1w.setSizePolicy(sizePolicy3)

        self.verticalLayout_25.addWidget(self.r2c1w)

        self.page_widget.addWidget(self.playlist_page)
        self.download_page = QWidget()
        self.download_page.setObjectName(u"download_page")
        self.download_page.setStyleSheet(u"QPushButton{\n"
"	border: 0px transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	text-decoration: underline;\n"
"}")
        self.verticalLayout_24 = QVBoxLayout(self.download_page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.url_search_bar = QLineEdit(self.download_page)
        self.url_search_bar.setObjectName(u"url_search_bar")
        sizePolicy7.setHeightForWidth(self.url_search_bar.sizePolicy().hasHeightForWidth())
        self.url_search_bar.setSizePolicy(sizePolicy7)
        self.url_search_bar.setStyleSheet(u"border-bottom: 1px solid;")

        self.horizontalLayout_7.addWidget(self.url_search_bar)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.radio_song = QRadioButton(self.download_page)
        self.radio_song.setObjectName(u"radio_song")
        self.radio_song.setMinimumSize(QSize(0, 15))
        self.radio_song.setChecked(True)

        self.verticalLayout_23.addWidget(self.radio_song)

        self.radio_playlist = QRadioButton(self.download_page)
        self.radio_playlist.setObjectName(u"radio_playlist")
        self.radio_playlist.setMinimumSize(QSize(0, 15))

        self.verticalLayout_23.addWidget(self.radio_playlist)


        self.horizontalLayout_7.addLayout(self.verticalLayout_23)

        self.download_btn = QPushButton(self.download_page)
        self.download_btn.setObjectName(u"download_btn")
        sizePolicy6.setHeightForWidth(self.download_btn.sizePolicy().hasHeightForWidth())
        self.download_btn.setSizePolicy(sizePolicy6)
        self.download_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.download_btn.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.download_btn)


        self.verticalLayout_24.addLayout(self.horizontalLayout_7)

        self.advanced_btn = QPushButton(self.download_page)
        self.advanced_btn.setObjectName(u"advanced_btn")
        self.advanced_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_24.addWidget(self.advanced_btn)

        self.advanced_widget = QWidget(self.download_page)
        self.advanced_widget.setObjectName(u"advanced_widget")
        self.advanced_widget.setMinimumSize(QSize(0, 50))
        self.gridLayout = QGridLayout(self.advanced_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.audio_only_check = QCheckBox(self.advanced_widget)
        self.audio_only_check.setObjectName(u"audio_only_check")
        font = QFont()
        font.setPointSize(10)
        self.audio_only_check.setFont(font)
        self.audio_only_check.setChecked(True)

        self.gridLayout.addWidget(self.audio_only_check, 0, 0, 1, 1)

        self.use_default_path_check = QCheckBox(self.advanced_widget)
        self.use_default_path_check.setObjectName(u"use_default_path_check")
        self.use_default_path_check.setFont(font)
        self.use_default_path_check.setChecked(True)

        self.gridLayout.addWidget(self.use_default_path_check, 1, 0, 1, 1)

        self.thumbnail_check = QCheckBox(self.advanced_widget)
        self.thumbnail_check.setObjectName(u"thumbnail_check")
        self.thumbnail_check.setEnabled(False)
        self.thumbnail_check.setChecked(True)

        self.gridLayout.addWidget(self.thumbnail_check, 0, 1, 1, 1)


        self.verticalLayout_24.addWidget(self.advanced_widget)

        self.status_box = QTextBrowser(self.download_page)
        self.status_box.setObjectName(u"status_box")

        self.verticalLayout_24.addWidget(self.status_box)

        self.page_widget.addWidget(self.download_page)
        self.advanced_btn.raise_()
        self.status_box.raise_()
        self.advanced_widget.raise_()
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.verticalLayout_26 = QVBoxLayout(self.setting_page)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.tabWidget = QTabWidget(self.setting_page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Parameters = QWidget()
        self.Parameters.setObjectName(u"Parameters")
        self.label_2 = QLabel(self.Parameters)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 131, 21))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        self.widget_2 = QWidget(self.Parameters)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 50, 421, 121))
        self.layoutWidget = QWidget(self.widget_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 251, 40))
        self.verticalLayout_28 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
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

        self.layoutWidget1 = QWidget(self.widget_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 10, 251, 40))
        self.verticalLayout_27 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
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

        self.tabWidget.addTab(self.Parameters, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_26.addWidget(self.tabWidget)

        self.page_widget.addWidget(self.setting_page)

        self.verticalLayout_10.addWidget(self.page_widget)


        self.horizontalLayout_12.addLayout(self.verticalLayout_10)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.play_bar = QWidget(self.centralwidget)
        self.play_bar.setObjectName(u"play_bar")
        sizePolicy5.setHeightForWidth(self.play_bar.sizePolicy().hasHeightForWidth())
        self.play_bar.setSizePolicy(sizePolicy5)
        self.play_bar.setMinimumSize(QSize(0, 75))
        self.play_bar.setMaximumSize(QSize(16777215, 75))
        self.play_bar.setStyleSheet(u"QWidget{\n"
"	background: #48cae4;\n"
"	border: 5px solid transparent;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 1px solid transparent;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-bottom-color: black;\n"
"}\n"
"\n"
"QSlider{\n"
"	border-radius: 0px;\n"
"	padding-top: 0px;\n"
"	padding-bottom: 5px;\n"
"	border-bottom: 1px solid;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.play_bar)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.thumbnail = QPushButton(self.play_bar)
        self.thumbnail.setObjectName(u"thumbnail")
        sizePolicy8.setHeightForWidth(self.thumbnail.sizePolicy().hasHeightForWidth())
        self.thumbnail.setSizePolicy(sizePolicy8)
        self.thumbnail.setMinimumSize(QSize(50, 50))
        self.thumbnail.setMaximumSize(QSize(100, 100))
        self.thumbnail.setSizeIncrement(QSize(5, 5))
        self.thumbnail.setIcon(icon)
        self.thumbnail.setIconSize(QSize(100, 100))
        self.thumbnail.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.thumbnail)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.label_5 = QLabel(self.play_bar)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.play_title = QLabel(self.play_bar)
        self.play_title.setObjectName(u"play_title")
        self.play_title.setMinimumSize(QSize(0, 25))
        self.play_title.setStyleSheet(u"")
        self.play_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.play_title)

        self.song_progress_slide = QSlider(self.play_bar)
        self.song_progress_slide.setObjectName(u"song_progress_slide")
        self.song_progress_slide.setMinimumSize(QSize(0, 20))
        self.song_progress_slide.setCursor(QCursor(Qt.PointingHandCursor))
        self.song_progress_slide.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.song_progress_slide)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)

        self.backward_btn = QPushButton(self.play_bar)
        self.backward_btn.setObjectName(u"backward_btn")
        self.backward_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/images/backward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backward_btn.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.backward_btn)

        self.prev_btn = QPushButton(self.play_bar)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/images/prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev_btn.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.prev_btn)

        self.pause_start_btn = QPushButton(self.play_bar)
        self.pause_start_btn.setObjectName(u"pause_start_btn")
        self.pause_start_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/images/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_start_btn.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.pause_start_btn)

        self.next_btn = QPushButton(self.play_bar)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/images/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_btn.setIcon(icon11)

        self.horizontalLayout_5.addWidget(self.next_btn)

        self.forward_btn = QPushButton(self.play_bar)
        self.forward_btn.setObjectName(u"forward_btn")
        self.forward_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/newPrefix/images/forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.forward_btn.setIcon(icon12)
        self.forward_btn.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.forward_btn)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_16)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.label_16 = QLabel(self.play_bar)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_6.addWidget(self.label_16)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.play_order_btn = QPushButton(self.play_bar)
        self.play_order_btn.setObjectName(u"play_order_btn")
        sizePolicy4.setHeightForWidth(self.play_order_btn.sizePolicy().hasHeightForWidth())
        self.play_order_btn.setSizePolicy(sizePolicy4)
        self.play_order_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/newPrefix/images/cycle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_order_btn.setIcon(icon13)

        self.horizontalLayout_6.addWidget(self.play_order_btn)

        self.volume_btn = QPushButton(self.play_bar)
        self.volume_btn.setObjectName(u"volume_btn")
        self.volume_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/newPrefix/images/volume.png", QSize(), QIcon.Normal, QIcon.Off)
        self.volume_btn.setIcon(icon14)

        self.horizontalLayout_6.addWidget(self.volume_btn)

        self.volume_slide = QSlider(self.play_bar)
        self.volume_slide.setObjectName(u"volume_slide")
        sizePolicy4.setHeightForWidth(self.volume_slide.sizePolicy().hasHeightForWidth())
        self.volume_slide.setSizePolicy(sizePolicy4)
        self.volume_slide.setCursor(QCursor(Qt.PointingHandCursor))
        self.volume_slide.setValue(99)
        self.volume_slide.setOrientation(Qt.Vertical)

        self.horizontalLayout_6.addWidget(self.volume_slide)


        self.verticalLayout_9.addWidget(self.play_bar)


        self.gridLayout_2.addLayout(self.verticalLayout_9, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 749, 18))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.playlist_btn_1.toggled.connect(self.playlist_btn_2.setChecked)
        self.menu_btn.toggled.connect(self.side2.setVisible)
        self.menu_btn.toggled.connect(self.side1.setHidden)
        self.home_btn_1.toggled.connect(self.home_btn_2.setChecked)
        self.home_btn_2.toggled.connect(self.home_btn_1.setChecked)
        self.library_btn_1.toggled.connect(self.library_btn_2.setChecked)
        self.playlist_btn_2.toggled.connect(self.playlist_btn_1.setChecked)
        self.library_btn_2.toggled.connect(self.library_btn_1.setChecked)
        self.download_btn_2.toggled.connect(self.download_btn_1.setChecked)
        self.download_btn_1.toggled.connect(self.download_btn_2.setChecked)

        self.page_widget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bocchi Music", None))
        self.logo_5.setText("")
        self.home_btn_1.setText("")
        self.library_btn_1.setText("")
        self.playlist_btn_1.setText("")
        self.download_btn_1.setText("")
        self.setting_btn_1.setText("")
        self.logo_3.setText("")
        self.home_btn_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.library_btn_2.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.playlist_btn_2.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.download_btn_2.setText(QCoreApplication.translate("MainWindow", u" Download", None))
        self.setting_btn_2.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.menu_btn.setText("")
        self.search_bar.setText("")
        self.search_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_btn.setText("")
        self.home_title_1.setText(QCoreApplication.translate("MainWindow", u"Recently Played:", None))
        self.label.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.home_title_2.setText(QCoreApplication.translate("MainWindow", u"Most Listened:", None))
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.home_title_3.setText(QCoreApplication.translate("MainWindow", u"Playlists:", None))
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.play_random_btn.setText(QCoreApplication.translate("MainWindow", u"Shuffle", None))
        ___qtablewidgetitem = self.song_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem1 = self.song_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem2 = self.song_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Artist", None));
        ___qtablewidgetitem3 = self.song_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Last Played", None));
        ___qtablewidgetitem4 = self.song_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Date Added", None));
        ___qtablewidgetitem5 = self.song_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Times Played", None));
        self.import_btn.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.create_new_playlist_btn.setText(QCoreApplication.translate("MainWindow", u"Create New Playlist", None))
        self.url_search_bar.setText("")
        self.url_search_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.radio_song.setText(QCoreApplication.translate("MainWindow", u"Song", None))
        self.radio_playlist.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.download_btn.setText("")
        self.advanced_btn.setText(QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.audio_only_check.setText(QCoreApplication.translate("MainWindow", u"Audio only", None))
        self.use_default_path_check.setText(QCoreApplication.translate("MainWindow", u"Use default path", None))
        self.thumbnail_check.setText(QCoreApplication.translate("MainWindow", u"Include Thumbnail", None))
        self.status_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"....", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Default playlist download path", None))
        self.playlist_dir_le.setText(QCoreApplication.translate("MainWindow", u"./songs/playlist", None))
        self.playlist_dir_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./", None))
        self.playlist_path_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Default track download path", None))
        self.song_dir_le.setText(QCoreApplication.translate("MainWindow", u"./songs", None))
        self.song_dir_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./", None))
        self.song_path_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Parameters), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.thumbnail.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.play_title.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.backward_btn.setText("")
        self.prev_btn.setText("")
        self.pause_start_btn.setText("")
        self.next_btn.setText("")
        self.forward_btn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.play_order_btn.setText("")
        self.volume_btn.setText("")
    # retranslateUi

