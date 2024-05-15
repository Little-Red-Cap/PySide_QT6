# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_setting_test.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(769, 743)
        self.horizontalLayout_16 = QHBoxLayout(Frame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.scrollArea_2 = QScrollArea(Frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(240, 0))
        self.scrollArea_2.setMaximumSize(QSize(400, 16777215))
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 240, 725))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_19 = QFrame(self.groupBox_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_16 = QLabel(self.frame_19)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_19.addWidget(self.label_16)

        self.comboBox_12 = QComboBox(self.frame_19)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")

        self.horizontalLayout_19.addWidget(self.comboBox_12)


        self.verticalLayout_4.addWidget(self.frame_19, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_23 = QFrame(self.groupBox_5)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_port = QLabel(self.frame_23)
        self.label_port.setObjectName(u"label_port")

        self.horizontalLayout_23.addWidget(self.label_port)

        self.comboBox_port = QComboBox(self.frame_23)
        self.comboBox_port.setObjectName(u"comboBox_port")

        self.horizontalLayout_23.addWidget(self.comboBox_port)


        self.verticalLayout_2.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.groupBox_5)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_baudRates = QLabel(self.frame_24)
        self.label_baudRates.setObjectName(u"label_baudRates")

        self.horizontalLayout_24.addWidget(self.label_baudRates)

        self.comboBox_baudRates = QComboBox(self.frame_24)
        self.comboBox_baudRates.setObjectName(u"comboBox_baudRates")

        self.horizontalLayout_24.addWidget(self.comboBox_baudRates)


        self.verticalLayout_2.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.groupBox_5)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_dataBits = QLabel(self.frame_25)
        self.label_dataBits.setObjectName(u"label_dataBits")

        self.horizontalLayout_25.addWidget(self.label_dataBits)

        self.comboBox_dataBits = QComboBox(self.frame_25)
        self.comboBox_dataBits.addItem("")
        self.comboBox_dataBits.addItem("")
        self.comboBox_dataBits.addItem("")
        self.comboBox_dataBits.addItem("")
        self.comboBox_dataBits.setObjectName(u"comboBox_dataBits")

        self.horizontalLayout_25.addWidget(self.comboBox_dataBits)


        self.verticalLayout_2.addWidget(self.frame_25)

        self.frame_27 = QFrame(self.groupBox_5)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_checkBits = QLabel(self.frame_27)
        self.label_checkBits.setObjectName(u"label_checkBits")

        self.horizontalLayout_27.addWidget(self.label_checkBits)

        self.comboBox_checkBits = QComboBox(self.frame_27)
        self.comboBox_checkBits.addItem("")
        self.comboBox_checkBits.addItem("")
        self.comboBox_checkBits.addItem("")
        self.comboBox_checkBits.addItem("")
        self.comboBox_checkBits.setObjectName(u"comboBox_checkBits")

        self.horizontalLayout_27.addWidget(self.comboBox_checkBits)


        self.verticalLayout_2.addWidget(self.frame_27)

        self.frame_29 = QFrame(self.groupBox_5)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_stopBits = QLabel(self.frame_29)
        self.label_stopBits.setObjectName(u"label_stopBits")

        self.horizontalLayout_29.addWidget(self.label_stopBits)

        self.comboBox_stopBits = QComboBox(self.frame_29)
        self.comboBox_stopBits.addItem("")
        self.comboBox_stopBits.addItem("")
        self.comboBox_stopBits.addItem("")
        self.comboBox_stopBits.setObjectName(u"comboBox_stopBits")
        self.comboBox_stopBits.setEditable(False)

        self.horizontalLayout_29.addWidget(self.comboBox_stopBits)


        self.verticalLayout_2.addWidget(self.frame_29)

        self.pushButton_port = QPushButton(self.groupBox_5)
        self.pushButton_port.setObjectName(u"pushButton_port")

        self.verticalLayout_2.addWidget(self.pushButton_port)


        self.verticalLayout_3.addWidget(self.groupBox_5, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_16.addWidget(self.scrollArea_2)

        self.scrollArea = QScrollArea(Frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(400, 0))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 458, 725))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_3 = QFormLayout(self.groupBox_4)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.frame_20 = QFrame(self.groupBox_4)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.frame_20)

        self.frame_21 = QFrame(self.groupBox_4)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_19 = QLabel(self.frame_21)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_21.addWidget(self.label_19)

        self.comboBox_14 = QComboBox(self.frame_21)
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")

        self.horizontalLayout_21.addWidget(self.comboBox_14)


        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.frame_21)

        self.frame_22 = QFrame(self.groupBox_4)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_20 = QLabel(self.frame_22)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_22.addWidget(self.label_20)

        self.comboBox_17 = QComboBox(self.frame_22)
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.setObjectName(u"comboBox_17")

        self.horizontalLayout_22.addWidget(self.comboBox_17)


        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.frame_22)

        self.frame_28 = QFrame(self.groupBox_4)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_26 = QLabel(self.frame_28)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_28.addWidget(self.label_26)

        self.comboBox_21 = QComboBox(self.frame_28)
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")

        self.horizontalLayout_28.addWidget(self.comboBox_21)


        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.frame_28)

        self.frame_26 = QFrame(self.groupBox_4)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_24 = QLabel(self.frame_26)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_26.addWidget(self.label_24)

        self.comboBox_19 = QComboBox(self.frame_26)
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")

        self.horizontalLayout_26.addWidget(self.comboBox_19)


        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.frame_26)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.frame_7 = QFrame(self.groupBox)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_7.addWidget(self.lineEdit)


        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.frame_7)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.frame)

        self.frame_5 = QFrame(self.groupBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.comboBox_5 = QComboBox(self.frame_5)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_5.addWidget(self.comboBox_5)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.frame_5)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.frame_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_2.addWidget(self.comboBox_2)


        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.frame_2)

        self.frame_6 = QFrame(self.groupBox)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.comboBox_6 = QComboBox(self.frame_6)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_6.addWidget(self.comboBox_6)


        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.frame_6)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox_3 = QComboBox(self.frame_3)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_3.addWidget(self.comboBox_3)


        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.frame_3)

        self.frame_9 = QFrame(self.groupBox)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.comboBox_8 = QComboBox(self.frame_9)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.horizontalLayout_9.addWidget(self.comboBox_8)


        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.frame_9)

        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.comboBox_4 = QComboBox(self.frame_4)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_4.addWidget(self.comboBox_4)


        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.frame_4)

        self.frame_8 = QFrame(self.groupBox)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.comboBox_7 = QComboBox(self.frame_8)
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_8.addWidget(self.comboBox_7)


        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.frame_8)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_2 = QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.frame_10 = QFrame(self.groupBox_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.comboBox_9 = QComboBox(self.frame_10)
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.horizontalLayout_10.addWidget(self.comboBox_9)


        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.frame_10)

        self.frame_11 = QFrame(self.groupBox_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.frame_11)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.comboBox_10 = QComboBox(self.frame_11)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.horizontalLayout_11.addWidget(self.comboBox_10)


        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.frame_11)

        self.frame_12 = QFrame(self.groupBox_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.comboBox_11 = QComboBox(self.frame_12)
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.horizontalLayout_12.addWidget(self.comboBox_11)


        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.frame_12)

        self.frame_15 = QFrame(self.groupBox_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.lineEdit_2 = QLineEdit(self.frame_15)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_15.addWidget(self.lineEdit_2)


        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.frame_15)

        self.frame_13 = QFrame(self.groupBox_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.frame_13)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.lineEdit_3 = QLineEdit(self.frame_13)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_13.addWidget(self.lineEdit_3)


        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.frame_13)

        self.frame_18 = QFrame(self.groupBox_3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_18 = QLabel(self.frame_18)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_18.addWidget(self.label_18)

        self.comboBox_16 = QComboBox(self.frame_18)
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")

        self.horizontalLayout_18.addWidget(self.comboBox_16)


        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.frame_18)

        self.frame_14 = QFrame(self.groupBox_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton = QPushButton(self.frame_14)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_14.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_2 = QPushButton(self.frame_14)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_14.addWidget(self.pushButton_2)


        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.frame_14)

        self.frame_17 = QFrame(self.groupBox_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_17 = QLabel(self.frame_17)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_17.addWidget(self.label_17)

        self.comboBox_15 = QComboBox(self.frame_17)
        self.comboBox_15.addItem("")
        self.comboBox_15.setObjectName(u"comboBox_15")

        self.horizontalLayout_17.addWidget(self.comboBox_15)


        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.frame_17)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_16.addWidget(self.scrollArea)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Frame", u"\u6570\u636e\u6d41\u8bbe\u7f6e", None))
        self.label_16.setText(QCoreApplication.translate("Frame", u"\u91c7\u96c6\u95f4\u9694", None))
        self.comboBox_12.setItemText(0, QCoreApplication.translate("Frame", u"1.0\u79d2", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("Frame", u"10\u79d2", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("Frame", u"1\u5206\u949f", None))
        self.comboBox_12.setItemText(3, QCoreApplication.translate("Frame", u"30\u5206\u949f", None))

        self.groupBox_5.setTitle(QCoreApplication.translate("Frame", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.label_port.setText(QCoreApplication.translate("Frame", u"\u7aef\u53e3\u540d\uff1a", None))
        self.label_baudRates.setText(QCoreApplication.translate("Frame", u"\u6ce2\u7279\u7387\uff1a", None))
        self.label_dataBits.setText(QCoreApplication.translate("Frame", u"\u6570\u636e\u4f4d\uff1a", None))
        self.comboBox_dataBits.setItemText(0, QCoreApplication.translate("Frame", u"8", None))
        self.comboBox_dataBits.setItemText(1, QCoreApplication.translate("Frame", u"7", None))
        self.comboBox_dataBits.setItemText(2, QCoreApplication.translate("Frame", u"6", None))
        self.comboBox_dataBits.setItemText(3, QCoreApplication.translate("Frame", u"5", None))

        self.label_checkBits.setText(QCoreApplication.translate("Frame", u"\u6821\u9a8c\u4f4d\uff1a", None))
        self.comboBox_checkBits.setItemText(0, QCoreApplication.translate("Frame", u"None", None))
        self.comboBox_checkBits.setItemText(1, QCoreApplication.translate("Frame", u"Even", None))
        self.comboBox_checkBits.setItemText(2, QCoreApplication.translate("Frame", u"Mark", None))
        self.comboBox_checkBits.setItemText(3, QCoreApplication.translate("Frame", u"Odd", None))

        self.label_stopBits.setText(QCoreApplication.translate("Frame", u"\u505c\u6b62\u4f4d\uff1a", None))
        self.comboBox_stopBits.setItemText(0, QCoreApplication.translate("Frame", u"1", None))
        self.comboBox_stopBits.setItemText(1, QCoreApplication.translate("Frame", u"1.5", None))
        self.comboBox_stopBits.setItemText(2, QCoreApplication.translate("Frame", u"2", None))

        self.pushButton_port.setText(QCoreApplication.translate("Frame", u"\u6253\u5f00", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Frame", u"\u5e38\u89c4\u5e93\u8bbe\u7f6e", None))
        self.label_19.setText(QCoreApplication.translate("Frame", u"\u5f00\u673a\u542f\u52a8", None))
        self.comboBox_14.setItemText(0, QCoreApplication.translate("Frame", u"\u76f4\u8fde\u6570\u636e\u5e93", None))

        self.label_20.setText(QCoreApplication.translate("Frame", u"\u914d\u8272\u65b9\u6848", None))
        self.comboBox_17.setItemText(0, QCoreApplication.translate("Frame", u"\u8ddf\u968f\u7cfb\u7edf", None))
        self.comboBox_17.setItemText(1, QCoreApplication.translate("Frame", u"\u4eae\u8272\u6a21\u5f0f", None))
        self.comboBox_17.setItemText(2, QCoreApplication.translate("Frame", u"\u7070\u6697\u6a21\u5f0f", None))

        self.label_26.setText(QCoreApplication.translate("Frame", u"\u5168\u5c4f\u6a21\u5f0f", None))
        self.comboBox_21.setItemText(0, QCoreApplication.translate("Frame", u"big screen", None))

        self.label_24.setText(QCoreApplication.translate("Frame", u"\u9690\u85cf\u9f20\u6807", None))
        self.comboBox_19.setItemText(0, QCoreApplication.translate("Frame", u"5\u79d2", None))
        self.comboBox_19.setItemText(1, QCoreApplication.translate("Frame", u"\u4e0d\u9690\u85cf", None))

        self.groupBox.setTitle(QCoreApplication.translate("Frame", u"\u89c6\u9891\u8bbe\u7f6e", None))
        self.label_7.setText(QCoreApplication.translate("Frame", u"\u89c6\u9891\u6d41\u5730\u5740", None))
        self.label.setText(QCoreApplication.translate("Frame", u"\u64ad\u653e\u7b56\u7565", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Frame", u"\u5b9e\u65f6\u64ad\u653e", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Frame", u"\u5faa\u73af\u64ad\u653e", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Frame", u"\u5355\u6b21\u64ad\u653e", None))

        self.label_5.setText(QCoreApplication.translate("Frame", u"\u786c\u4ef6\u52a0\u901f", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Frame", u"None", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Frame", u"GPU", None))

        self.label_2.setText(QCoreApplication.translate("Frame", u"\u663e\u793a\u6a21\u5f0f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Frame", u"\u53e5\u67c4", None))

        self.label_6.setText(QCoreApplication.translate("Frame", u"\u4f20\u8f93\u534f\u8bae", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("Frame", u"TCP", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("Frame", u"UDP", None))

        self.label_3.setText(QCoreApplication.translate("Frame", u"\u753b\u9762\u663e\u793a", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Frame", u"\u4e0d\u62c9\u4f38\u586b\u5145", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Frame", u"\u62c9\u4f38\u586b\u5145", None))

        self.label_9.setText(QCoreApplication.translate("Frame", u"\u89e3\u7801\u7b56\u7565", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("Frame", u"\u901f\u5ea6\u4f18\u5148", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("Frame", u"\u8d28\u91cf\u4f18\u5148", None))

        self.label_4.setText(QCoreApplication.translate("Frame", u"\u8bfb\u53d6\u8d85\u65f6", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Frame", u"\u4e0d\u5904\u7406", None))

        self.label_8.setText(QCoreApplication.translate("Frame", u"\u8fde\u63a5\u8d85\u65f6", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("Frame", u"\u4e0d\u5904\u7406", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("Frame", u"\u6570\u636e\u5e93\u8bbe\u7f6e", None))
        self.label_10.setText(QCoreApplication.translate("Frame", u"\u8fde\u63a5\u65b9\u5f0f", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("Frame", u"\u76f4\u8fde\u6570\u636e\u5e93", None))

        self.label_11.setText(QCoreApplication.translate("Frame", u"\u4e3b\u673a\u7c7b\u578b", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("Frame", u"SQLite", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("Frame", u"MySQL", None))

        self.label_12.setText(QCoreApplication.translate("Frame", u"\u6570\u636e\u5e93\u540d", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("Frame", u"big screen", None))

        self.label_15.setText(QCoreApplication.translate("Frame", u"\u4e3b\u673a\u4fe1\u606f", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Frame", u"127.0.0.1::3306", None))
        self.label_13.setText(QCoreApplication.translate("Frame", u"\u7528\u6237\u540d\u79f0", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Frame", u"root", None))
        self.label_18.setText(QCoreApplication.translate("Frame", u"\u7528\u6237\u5bc6\u7801", None))
        self.comboBox_16.setItemText(0, QCoreApplication.translate("Frame", u"\u901f\u5ea6\u4f18\u5148", None))
        self.comboBox_16.setItemText(1, QCoreApplication.translate("Frame", u"\u8d28\u91cf\u4f18\u5148", None))

        self.pushButton.setText(QCoreApplication.translate("Frame", u"\u8fde\u63a5\u6d4b\u8bd5", None))
        self.pushButton_2.setText(QCoreApplication.translate("Frame", u"\u521d\u59cb\u5316\u6570\u636e", None))
        self.label_17.setText(QCoreApplication.translate("Frame", u"\u8fde\u63a5\u8d85\u65f6", None))
        self.comboBox_15.setItemText(0, QCoreApplication.translate("Frame", u"\u4e0d\u5904\u7406", None))

    # retranslateUi

