# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_window(object):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(574, 489)
        self.left_menu_frame = QFrame(window)
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        self.left_menu_frame.setGeometry(QRect(140, 80, 56, 98))
        self.left_menu_frame.setMinimumSize(QSize(56, 0))
        self.left_menu_frame.setMaximumSize(QSize(56, 17280))
        self.left_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_frame.setFrameShadow(QFrame.Raised)
        self.left_menu_layout = QHBoxLayout(self.left_menu_frame)
        self.left_menu_layout.setObjectName(u"left_menu_layout")
        self.left_menu_layout.setContentsMargins(3, 3, 3, 3)
        self.left_menu = QWidget(self.left_menu_frame)
        self.left_menu.setObjectName(u"left_menu")
        self.verticalLayout_3 = QVBoxLayout(self.left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bg = QFrame(self.left_menu)
        self.bg.setObjectName(u"bg")
        self.bg.setCursor(QCursor(Qt.PointingHandCursor))
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.bg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.bg)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.top_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.top_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.top_frame)


        self.verticalLayout_3.addWidget(self.bg)


        self.left_menu_layout.addWidget(self.left_menu)


        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"Frame", None))
        self.pushButton.setText(QCoreApplication.translate("window", u"PushButton", None))
    # retranslateUi

