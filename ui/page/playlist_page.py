from PySide6.QtCore import (Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout, QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class PlaylistPage(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"playlist_page")
        self.verticalLayout_25 = QVBoxLayout(self)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        # right1_Column1_Frame
        self.r1c1f = QFrame(self)
        self.r1c1f.setObjectName(u"r1c1f")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(
            self.r1c1f.sizePolicy().hasHeightForWidth())
        self.r1c1f.setSizePolicy(sizePolicy9)
        self.r1c1f.setFrameShape(QFrame.StyledPanel)
        self.r1c1f.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.r1c1f)

        self.r1c2f = QFrame(self)
        self.r1c2f.setObjectName(u"r1c2f")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed,
                                  QSizePolicy.Policy.Fixed)
        sizePolicy6.setHeightForWidth(
            self.r1c2f.sizePolicy().hasHeightForWidth())
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred,
                                  QSizePolicy.Policy.Expanding)
        sizePolicy3.setHeightForWidth(
            self.r2c1w.sizePolicy().hasHeightForWidth())
        self.r2c1w.setSizePolicy(sizePolicy3)

        self.verticalLayout_25.addWidget(self.r2c1w)
