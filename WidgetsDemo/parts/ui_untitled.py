# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 720)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(160, 180, 721, 361))
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(19, 109, 211, 161))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(20, 20, 161, 121))
        self.frame_5.setStyleSheet(u"QFrame#frame_5{\n"
"/*    border: 1px solid #888;*/\n"
"    border: none;\n"
"    border-radius:15px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                        stop:0.102273 rgba(212, 137, 255, 255),\n"
"                                        stop:0.5 rgba(121, 133, 255, 255),\n"
"                                        stop:0.926136 rgba(106, 216, 253, 255)\n"
"                                        );\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(240, 100, 211, 161))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(20, 20, 161, 121))
        self.frame_9.setStyleSheet(u"QFrame#frame_9{\n"
"/*    border: 1px solid #888;*/\n"
"    border: none;\n"
"    border-radius:15px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                        stop:0.102273 rgba(212, 137, 255, 255),\n"
"                                        stop:0.5 rgba(121, 133, 255, 255),\n"
"                                        stop:0.926136 rgba(106, 216, 253, 255)\n"
"                                        );\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_15 = QLabel(self.frame_9)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 3, 0, 1, 1)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(470, 100, 211, 161))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(20, 20, 161, 121))
        self.frame_10.setStyleSheet(u"QFrame#frame_10{\n"
"/*    border: 1px solid #888;*/\n"
"    border: none;\n"
"    border-radius:15px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                        stop:0.102273 rgba(212, 137, 255, 255),\n"
"                                        stop:0.5 rgba(121, 133, 255, 255),\n"
"                                        stop:0.926136 rgba(106, 216, 253, 255)\n"
"                                        );\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_17 = QLabel(self.frame_10)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 0, 1, 1, 1)

        self.label_18 = QLabel(self.frame_10)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 2, 0, 1, 1)

        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.gridLayout_4.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_20 = QLabel(self.frame_10)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Card Title1", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Icon", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Describe here", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Card Title1", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Icon", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Describe here", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Card Title1", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Icon", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Describe here", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

