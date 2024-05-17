# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_dev.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

from part_switch_button import SwitchButton

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(928, 596)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 30, 261, 531))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_16 = QFrame(self.widget)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_16)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.button_dev3 = SwitchButton(self.frame_16)
        self.button_dev3.setObjectName(u"button_dev3")

        self.gridLayout_8.addWidget(self.button_dev3, 0, 3, 2, 1)

        self.label_state_dev3 = QLabel(self.frame_16)
        self.label_state_dev3.setObjectName(u"label_state_dev3")

        self.gridLayout_8.addWidget(self.label_state_dev3, 1, 1, 1, 1)

        self.label_type_dev3 = QLabel(self.frame_16)
        self.label_type_dev3.setObjectName(u"label_type_dev3")

        self.gridLayout_8.addWidget(self.label_type_dev3, 0, 1, 1, 1)

        self.label_img_dev3 = QLabel(self.frame_16)
        self.label_img_dev3.setObjectName(u"label_img_dev3")

        self.gridLayout_8.addWidget(self.label_img_dev3, 0, 0, 2, 1)


        self.verticalLayout_2.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.widget)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_15)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_type_dev2 = QLabel(self.frame_15)
        self.label_type_dev2.setObjectName(u"label_type_dev2")

        self.gridLayout_7.addWidget(self.label_type_dev2, 0, 1, 1, 1)

        self.label_state_dev2 = QLabel(self.frame_15)
        self.label_state_dev2.setObjectName(u"label_state_dev2")

        self.gridLayout_7.addWidget(self.label_state_dev2, 1, 1, 1, 1)

        self.label_img_dev2 = QLabel(self.frame_15)
        self.label_img_dev2.setObjectName(u"label_img_dev2")

        self.gridLayout_7.addWidget(self.label_img_dev2, 0, 0, 2, 1)

        self.button_dev = SwitchButton(self.frame_15)
        self.button_dev.setObjectName(u"button_dev")

        self.gridLayout_7.addWidget(self.button_dev, 0, 3, 2, 1)


        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame_14 = QFrame(self.widget)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_14)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_tyoe_dev1 = QLabel(self.frame_14)
        self.label_tyoe_dev1.setObjectName(u"label_tyoe_dev1")

        self.gridLayout_6.addWidget(self.label_tyoe_dev1, 0, 1, 1, 1)

        self.label_state_dev1 = QLabel(self.frame_14)
        self.label_state_dev1.setObjectName(u"label_state_dev1")

        self.gridLayout_6.addWidget(self.label_state_dev1, 1, 1, 1, 1)

        self.label_img_dev1 = QLabel(self.frame_14)
        self.label_img_dev1.setObjectName(u"label_img_dev1")

        self.gridLayout_6.addWidget(self.label_img_dev1, 0, 0, 2, 1)

        self.button_dev1 = SwitchButton(self.frame_14)
        self.button_dev1.setObjectName(u"button_dev1")

        self.gridLayout_6.addWidget(self.button_dev1, 0, 3, 2, 1)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_17 = QFrame(self.widget)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_17)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_type_dev4 = QLabel(self.frame_17)
        self.label_type_dev4.setObjectName(u"label_type_dev4")

        self.gridLayout_9.addWidget(self.label_type_dev4, 0, 1, 1, 1)

        self.label_state_dev4 = QLabel(self.frame_17)
        self.label_state_dev4.setObjectName(u"label_state_dev4")

        self.gridLayout_9.addWidget(self.label_state_dev4, 1, 1, 1, 1)

        self.label_img_dev4 = QLabel(self.frame_17)
        self.label_img_dev4.setObjectName(u"label_img_dev4")

        self.gridLayout_9.addWidget(self.label_img_dev4, 0, 0, 2, 1)

        self.button_dev4 = SwitchButton(self.frame_17)
        self.button_dev4.setObjectName(u"button_dev4")

        self.gridLayout_9.addWidget(self.button_dev4, 0, 3, 2, 1)


        self.verticalLayout_2.addWidget(self.frame_17)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(350, 90, 160, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider_2 = QSlider(Form)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(340, 220, 160, 22))
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_3 = QSlider(Form)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setGeometry(QRect(340, 350, 160, 22))
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(540, 90, 80, 19))
        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(550, 220, 80, 19))
        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(550, 350, 80, 19))
        self.horizontalSlider_4 = QSlider(Form)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setGeometry(QRect(340, 470, 160, 22))
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)
        self.checkBox_4 = QCheckBox(Form)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(550, 470, 80, 19))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_dev3.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.label_state_dev3.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_type_dev3.setText(QCoreApplication.translate("Form", u"\u704c\u6e89\u6c34\u6cf5", None))
        self.label_img_dev3.setText(QCoreApplication.translate("Form", u"\u56fe\u6807", None))
        self.label_type_dev2.setText(QCoreApplication.translate("Form", u"\u6362\u6c14\u98ce\u6247", None))
        self.label_state_dev2.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_dev2.setText(QCoreApplication.translate("Form", u"\u56fe\u6807", None))
        self.button_dev.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.label_tyoe_dev1.setText(QCoreApplication.translate("Form", u"\u7167\u660e\u706f", None))
        self.label_state_dev1.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_dev1.setText(QCoreApplication.translate("Form", u"\u56fe\u6807", None))
        self.button_dev1.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.label_type_dev4.setText(QCoreApplication.translate("Form", u"\u706d\u866b\u706f", None))
        self.label_state_dev4.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_dev4.setText(QCoreApplication.translate("Form", u"\u56fe\u6807", None))
        self.button_dev4.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"CheckBox", None))
    # retranslateUi

