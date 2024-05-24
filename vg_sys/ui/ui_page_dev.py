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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QSizePolicy,
    QSlider, QSpinBox, QVBoxLayout, QWidget)

from part_switch_button import SwitchButton

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1073, 608)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_waterPump = QFrame(Form)
        self.frame_waterPump.setObjectName(u"frame_waterPump")
        self.frame_waterPump.setFrameShape(QFrame.StyledPanel)
        self.frame_waterPump.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_waterPump)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.button_waterPump = SwitchButton(self.frame_waterPump)
        self.button_waterPump.setObjectName(u"button_waterPump")

        self.gridLayout_8.addWidget(self.button_waterPump, 0, 3, 2, 1)

        self.label_state_waterPump = QLabel(self.frame_waterPump)
        self.label_state_waterPump.setObjectName(u"label_state_waterPump")
        self.label_state_waterPump.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_state_waterPump, 1, 1, 1, 1)

        self.label_type_waterPump = QLabel(self.frame_waterPump)
        self.label_type_waterPump.setObjectName(u"label_type_waterPump")
        self.label_type_waterPump.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_type_waterPump, 0, 1, 1, 1)

        self.label_img_waterPump = QLabel(self.frame_waterPump)
        self.label_img_waterPump.setObjectName(u"label_img_waterPump")

        self.gridLayout_8.addWidget(self.label_img_waterPump, 0, 0, 2, 1)


        self.horizontalLayout.addWidget(self.frame_waterPump)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox_min_waterPump = QSpinBox(self.frame)
        self.spinBox_min_waterPump.setObjectName(u"spinBox_min_waterPump")

        self.gridLayout.addWidget(self.spinBox_min_waterPump, 1, 1, 1, 1)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 2, 3, 1, 2)

        self.comboBox_waterPump = QComboBox(self.frame)
        self.comboBox_waterPump.addItem("")
        self.comboBox_waterPump.addItem("")
        self.comboBox_waterPump.addItem("")
        self.comboBox_waterPump.addItem("")
        self.comboBox_waterPump.addItem("")
        self.comboBox_waterPump.addItem("")
        self.comboBox_waterPump.addItem("")
        self.comboBox_waterPump.setObjectName(u"comboBox_waterPump")

        self.gridLayout.addWidget(self.comboBox_waterPump, 2, 2, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 2)

        self.horizontalSlider_waterPump = QSlider(self.frame)
        self.horizontalSlider_waterPump.setObjectName(u"horizontalSlider_waterPump")
        self.horizontalSlider_waterPump.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_waterPump, 1, 2, 1, 1)

        self.spinBox_max_waterPump = QSpinBox(self.frame)
        self.spinBox_max_waterPump.setObjectName(u"spinBox_max_waterPump")

        self.gridLayout.addWidget(self.spinBox_max_waterPump, 1, 4, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_fan = QFrame(Form)
        self.frame_fan.setObjectName(u"frame_fan")
        self.frame_fan.setFrameShape(QFrame.StyledPanel)
        self.frame_fan.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_fan)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_type_fan = QLabel(self.frame_fan)
        self.label_type_fan.setObjectName(u"label_type_fan")
        self.label_type_fan.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_type_fan, 0, 1, 1, 1)

        self.label_state_fan = QLabel(self.frame_fan)
        self.label_state_fan.setObjectName(u"label_state_fan")
        self.label_state_fan.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_state_fan, 1, 1, 1, 1)

        self.label_img_fan = QLabel(self.frame_fan)
        self.label_img_fan.setObjectName(u"label_img_fan")

        self.gridLayout_7.addWidget(self.label_img_fan, 0, 0, 2, 1)

        self.button_fan = SwitchButton(self.frame_fan)
        self.button_fan.setObjectName(u"button_fan")

        self.gridLayout_7.addWidget(self.button_fan, 0, 3, 2, 1)


        self.horizontalLayout_2.addWidget(self.frame_fan)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spinBox_min_fan = QSpinBox(self.frame_2)
        self.spinBox_min_fan.setObjectName(u"spinBox_min_fan")

        self.gridLayout_2.addWidget(self.spinBox_min_fan, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.frame_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_2.addWidget(self.checkBox_2, 2, 3, 1, 2)

        self.comboBox_fan = QComboBox(self.frame_2)
        self.comboBox_fan.addItem("")
        self.comboBox_fan.addItem("")
        self.comboBox_fan.addItem("")
        self.comboBox_fan.addItem("")
        self.comboBox_fan.addItem("")
        self.comboBox_fan.addItem("")
        self.comboBox_fan.addItem("")
        self.comboBox_fan.setObjectName(u"comboBox_fan")

        self.gridLayout_2.addWidget(self.comboBox_fan, 2, 2, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 2)

        self.horizontalSlider_fan = QSlider(self.frame_2)
        self.horizontalSlider_fan.setObjectName(u"horizontalSlider_fan")
        self.horizontalSlider_fan.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_fan, 1, 2, 1, 1)

        self.spinBox_max_fan = QSpinBox(self.frame_2)
        self.spinBox_max_fan.setObjectName(u"spinBox_max_fan")

        self.gridLayout_2.addWidget(self.spinBox_max_fan, 1, 4, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 1, 3, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_light = QFrame(Form)
        self.frame_light.setObjectName(u"frame_light")
        self.frame_light.setFrameShape(QFrame.StyledPanel)
        self.frame_light.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_light)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_tyoe_light = QLabel(self.frame_light)
        self.label_tyoe_light.setObjectName(u"label_tyoe_light")
        self.label_tyoe_light.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_tyoe_light, 0, 1, 1, 1)

        self.label_state_light = QLabel(self.frame_light)
        self.label_state_light.setObjectName(u"label_state_light")
        self.label_state_light.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_state_light, 1, 1, 1, 1)

        self.label_img_light = QLabel(self.frame_light)
        self.label_img_light.setObjectName(u"label_img_light")

        self.gridLayout_6.addWidget(self.label_img_light, 0, 0, 2, 1)

        self.button_light = SwitchButton(self.frame_light)
        self.button_light.setObjectName(u"button_light")

        self.gridLayout_6.addWidget(self.button_light, 0, 3, 2, 1)


        self.horizontalLayout_3.addWidget(self.frame_light)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.spinBox_min_light = QSpinBox(self.frame_3)
        self.spinBox_min_light.setObjectName(u"spinBox_min_light")

        self.gridLayout_3.addWidget(self.spinBox_min_light, 1, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.frame_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_3.addWidget(self.checkBox_3, 2, 3, 1, 2)

        self.comboBox_light = QComboBox(self.frame_3)
        self.comboBox_light.addItem("")
        self.comboBox_light.addItem("")
        self.comboBox_light.addItem("")
        self.comboBox_light.addItem("")
        self.comboBox_light.addItem("")
        self.comboBox_light.addItem("")
        self.comboBox_light.addItem("")
        self.comboBox_light.setObjectName(u"comboBox_light")

        self.gridLayout_3.addWidget(self.comboBox_light, 2, 2, 1, 1)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 2)

        self.horizontalSlider_light = QSlider(self.frame_3)
        self.horizontalSlider_light.setObjectName(u"horizontalSlider_light")
        self.horizontalSlider_light.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider_light, 1, 2, 1, 1)

        self.spinBox_max_light = QSpinBox(self.frame_3)
        self.spinBox_max_light.setObjectName(u"spinBox_max_light")

        self.gridLayout_3.addWidget(self.spinBox_max_light, 1, 4, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 1, 3, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_InsectKillingLamp = QFrame(Form)
        self.frame_InsectKillingLamp.setObjectName(u"frame_InsectKillingLamp")
        self.frame_InsectKillingLamp.setFrameShape(QFrame.StyledPanel)
        self.frame_InsectKillingLamp.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_InsectKillingLamp)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_type_InsectKillingLamp = QLabel(self.frame_InsectKillingLamp)
        self.label_type_InsectKillingLamp.setObjectName(u"label_type_InsectKillingLamp")
        self.label_type_InsectKillingLamp.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_type_InsectKillingLamp, 0, 1, 1, 1)

        self.label_state_InsectKillingLamp = QLabel(self.frame_InsectKillingLamp)
        self.label_state_InsectKillingLamp.setObjectName(u"label_state_InsectKillingLamp")
        self.label_state_InsectKillingLamp.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_state_InsectKillingLamp, 1, 1, 1, 1)

        self.label_img_InsectKillingLamp = QLabel(self.frame_InsectKillingLamp)
        self.label_img_InsectKillingLamp.setObjectName(u"label_img_InsectKillingLamp")

        self.gridLayout_9.addWidget(self.label_img_InsectKillingLamp, 0, 0, 2, 1)

        self.button_InsectKillingLamp = SwitchButton(self.frame_InsectKillingLamp)
        self.button_InsectKillingLamp.setObjectName(u"button_InsectKillingLamp")

        self.gridLayout_9.addWidget(self.button_InsectKillingLamp, 0, 3, 2, 1)


        self.horizontalLayout_4.addWidget(self.frame_InsectKillingLamp)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.spinBox_min_InsectKillingLamp = QSpinBox(self.frame_4)
        self.spinBox_min_InsectKillingLamp.setObjectName(u"spinBox_min_InsectKillingLamp")

        self.gridLayout_4.addWidget(self.spinBox_min_InsectKillingLamp, 1, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self.frame_4)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_4.addWidget(self.checkBox_4, 2, 3, 1, 2)

        self.comboBox_InsectKillingLamp = QComboBox(self.frame_4)
        self.comboBox_InsectKillingLamp.addItem("")
        self.comboBox_InsectKillingLamp.addItem("")
        self.comboBox_InsectKillingLamp.addItem("")
        self.comboBox_InsectKillingLamp.addItem("")
        self.comboBox_InsectKillingLamp.addItem("")
        self.comboBox_InsectKillingLamp.addItem("")
        self.comboBox_InsectKillingLamp.addItem("")
        self.comboBox_InsectKillingLamp.setObjectName(u"comboBox_InsectKillingLamp")

        self.gridLayout_4.addWidget(self.comboBox_InsectKillingLamp, 2, 2, 1, 1)

        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 2, 0, 1, 2)

        self.horizontalSlider_InsectKillingLamp = QSlider(self.frame_4)
        self.horizontalSlider_InsectKillingLamp.setObjectName(u"horizontalSlider_InsectKillingLamp")
        self.horizontalSlider_InsectKillingLamp.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider_InsectKillingLamp, 1, 2, 1, 1)

        self.spinBox_max_InsectKillingLamp = QSpinBox(self.frame_4)
        self.spinBox_max_InsectKillingLamp.setObjectName(u"spinBox_max_InsectKillingLamp")

        self.gridLayout_4.addWidget(self.spinBox_max_InsectKillingLamp, 1, 4, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 1)

        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 1, 3, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_beep = QFrame(Form)
        self.frame_beep.setObjectName(u"frame_beep")
        self.frame_beep.setFrameShape(QFrame.StyledPanel)
        self.frame_beep.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_beep)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_type_beep = QLabel(self.frame_beep)
        self.label_type_beep.setObjectName(u"label_type_beep")
        self.label_type_beep.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_type_beep, 0, 1, 1, 1)

        self.label_state_beep = QLabel(self.frame_beep)
        self.label_state_beep.setObjectName(u"label_state_beep")
        self.label_state_beep.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_state_beep, 1, 1, 1, 1)

        self.label_img_beep = QLabel(self.frame_beep)
        self.label_img_beep.setObjectName(u"label_img_beep")

        self.gridLayout_10.addWidget(self.label_img_beep, 0, 0, 2, 1)

        self.button_beep = SwitchButton(self.frame_beep)
        self.button_beep.setObjectName(u"button_beep")

        self.gridLayout_10.addWidget(self.button_beep, 0, 3, 2, 1)


        self.horizontalLayout_5.addWidget(self.frame_beep)

        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.spinBox_min_beep = QSpinBox(self.frame_5)
        self.spinBox_min_beep.setObjectName(u"spinBox_min_beep")

        self.gridLayout_5.addWidget(self.spinBox_min_beep, 1, 1, 1, 1)

        self.checkBox_5 = QCheckBox(self.frame_5)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_5.addWidget(self.checkBox_5, 2, 3, 1, 2)

        self.comboBox_beep = QComboBox(self.frame_5)
        self.comboBox_beep.addItem("")
        self.comboBox_beep.addItem("")
        self.comboBox_beep.addItem("")
        self.comboBox_beep.addItem("")
        self.comboBox_beep.addItem("")
        self.comboBox_beep.addItem("")
        self.comboBox_beep.addItem("")
        self.comboBox_beep.setObjectName(u"comboBox_beep")

        self.gridLayout_5.addWidget(self.comboBox_beep, 2, 2, 1, 1)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 2, 0, 1, 2)

        self.horizontalSlider_beep = QSlider(self.frame_5)
        self.horizontalSlider_beep.setObjectName(u"horizontalSlider_beep")
        self.horizontalSlider_beep.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.horizontalSlider_beep, 1, 2, 1, 1)

        self.spinBox_max_beep = QSpinBox(self.frame_5)
        self.spinBox_max_beep.setObjectName(u"spinBox_max_beep")

        self.gridLayout_5.addWidget(self.spinBox_max_beep, 1, 4, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_5.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_5.addWidget(self.label_20, 1, 3, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_waterPump.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.label_state_waterPump.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_type_waterPump.setText(QCoreApplication.translate("Form", u"\u704c\u6e89\u6c34\u6cf5", None))
        self.label_img_waterPump.setText(QCoreApplication.translate("Form", u"\u56fe\u6807", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u4e3a\u53ef\u7528", None))
        self.comboBox_waterPump.setItemText(0, QCoreApplication.translate("Form", u"\u7531\u7ba1\u7406\u5458\u51b3\u5b9a", None))
        self.comboBox_waterPump.setItemText(1, QCoreApplication.translate("Form", u"\u7531\u7a7a\u6c14\u6e29\u5ea6\u51b3\u5b9a", None))
        self.comboBox_waterPump.setItemText(2, QCoreApplication.translate("Form", u"\u7531\u7a7a\u6c14\u6e7f\u5ea6\u51b3\u5b9a", None))
        self.comboBox_waterPump.setItemText(3, QCoreApplication.translate("Form", u"\u7531\u571f\u58e4\u6e29\u5ea6\u51b3\u5b9a", None))
        self.comboBox_waterPump.setItemText(4, QCoreApplication.translate("Form", u"\u7531\u571f\u58e4\u6e7f\u5ea6\u51b3\u5b9a", None))
        self.comboBox_waterPump.setItemText(5, QCoreApplication.translate("Form", u"\u7531\u5149\u7167\u5f3a\u5ea6\u51b3\u5b9a", None))
        self.comboBox_waterPump.setItemText(6, QCoreApplication.translate("Form", u"\u7531\u56fe\u50cf\u8bc6\u522b\u51b3\u5b9a", None))

        self.label_6.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u51b3\u7b56\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u9608\u503c", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u6700\u5c0f\u503c", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u6700\u5927\u503c", None))
        self.label_type_fan.setText(QCoreApplication.translate("Form", u"\u6362\u6c14\u98ce\u6247", None))
        self.label_state_fan.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_fan.setText(QCoreApplication.translate("Form", u"\u56fe\u6807", None))
        self.button_fan.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u4e3a\u53ef\u7528", None))
        self.comboBox_fan.setItemText(0, QCoreApplication.translate("Form", u"\u7531\u7ba1\u7406\u5458\u51b3\u5b9a", None))
        self.comboBox_fan.setItemText(1, QCoreApplication.translate("Form", u"\u7531\u7a7a\u6c14\u6e29\u5ea6\u51b3\u5b9a", None))
        self.comboBox_fan.setItemText(2, QCoreApplication.translate("Form", u"\u7531\u7a7a\u6c14\u6e7f\u5ea6\u51b3\u5b9a", None))
        self.comboBox_fan.setItemText(3, QCoreApplication.translate("Form", u"\u7531\u571f\u58e4\u6e29\u5ea6\u51b3\u5b9a", None))
        self.comboBox_fan.setItemText(4, QCoreApplication.translate("Form", u"\u7531\u571f\u58e4\u6e7f\u5ea6\u51b3\u5b9a", None))
        self.comboBox_fan.setItemText(5, QCoreApplication.translate("Form", u"\u7531\u5149\u7167\u5f3a\u5ea6\u51b3\u5b9a", None))
        self.comboBox_fan.setItemText(6, QCoreApplication.translate("Form", u"\u7531\u56fe\u50cf\u8bc6\u522b\u51b3\u5b9a", None))

        self.label_9.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u51b3\u7b56\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u9608\u503c", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u6700\u5c0f\u503c", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u6700\u5927\u503c", None))
        self.label_tyoe_light.setText(QCoreApplication.translate("Form", u"\u7167\u660e\u706f", None))
        self.label_state_light.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_light.setText(QCoreApplication.translate("Form", u"\u56fe\u6807", None))
        self.button_light.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u4e3a\u53ef\u7528", None))
        self.comboBox_light.setItemText(0, QCoreApplication.translate("Form", u"\u7531\u7ba1\u7406\u5458\u51b3\u5b9a", None))
        self.comboBox_light.setItemText(1, QCoreApplication.translate("Form", u"\u7531\u7a7a\u6c14\u6e29\u5ea6\u51b3\u5b9a", None))
        self.comboBox_light.setItemText(2, QCoreApplication.translate("Form", u"\u7531\u7a7a\u6c14\u6e7f\u5ea6\u51b3\u5b9a", None))
        self.comboBox_light.setItemText(3, QCoreApplication.translate("Form", u"\u7531\u571f\u58e4\u6e29\u5ea6\u51b3\u5b9a", None))
        self.comboBox_light.setItemText(4, QCoreApplication.translate("Form", u"\u7531\u571f\u58e4\u6e7f\u5ea6\u51b3\u5b9a", None))
        self.comboBox_light.setItemText(5, QCoreApplication.translate("Form", u"\u7531\u5149\u7167\u5f3a\u5ea6\u51b3\u5b9a", None))
        self.comboBox_light.setItemText(6, QCoreApplication.translate("Form", u"\u7531\u56fe\u50cf\u8bc6\u522b\u51b3\u5b9a", None))

        self.label_12.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u51b3\u7b56\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u9608\u503c", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u6700\u5c0f\u503c", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u6700\u5927\u503c", None))
        self.label_type_InsectKillingLamp.setText(QCoreApplication.translate("Form", u"\u706d\u866b\u706f", None))
        self.label_state_InsectKillingLamp.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_InsectKillingLamp.setText(QCoreApplication.translate("Form", u"\u56fe\u6807", None))
        self.button_InsectKillingLamp.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u4e3a\u53ef\u7528", None))
        self.comboBox_InsectKillingLamp.setItemText(0, QCoreApplication.translate("Form", u"\u7531\u7ba1\u7406\u5458\u51b3\u5b9a", None))
        self.comboBox_InsectKillingLamp.setItemText(1, QCoreApplication.translate("Form", u"\u7531\u7a7a\u6c14\u6e29\u5ea6\u51b3\u5b9a", None))
        self.comboBox_InsectKillingLamp.setItemText(2, QCoreApplication.translate("Form", u"\u7531\u7a7a\u6c14\u6e7f\u5ea6\u51b3\u5b9a", None))
        self.comboBox_InsectKillingLamp.setItemText(3, QCoreApplication.translate("Form", u"\u7531\u571f\u58e4\u6e29\u5ea6\u51b3\u5b9a", None))
        self.comboBox_InsectKillingLamp.setItemText(4, QCoreApplication.translate("Form", u"\u7531\u571f\u58e4\u6e7f\u5ea6\u51b3\u5b9a", None))
        self.comboBox_InsectKillingLamp.setItemText(5, QCoreApplication.translate("Form", u"\u7531\u5149\u7167\u5f3a\u5ea6\u51b3\u5b9a", None))
        self.comboBox_InsectKillingLamp.setItemText(6, QCoreApplication.translate("Form", u"\u7531\u56fe\u50cf\u8bc6\u522b\u51b3\u5b9a", None))

        self.label_15.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u51b3\u7b56\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u9608\u503c", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u6700\u5c0f\u503c", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u6700\u5927\u503c", None))
        self.label_type_beep.setText(QCoreApplication.translate("Form", u"\u62a5\u8b66\u5668", None))
        self.label_state_beep.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_beep.setText(QCoreApplication.translate("Form", u"\u56fe\u6807", None))
        self.button_beep.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u4e3a\u53ef\u7528", None))
        self.comboBox_beep.setItemText(0, QCoreApplication.translate("Form", u"\u7531\u7ba1\u7406\u5458\u51b3\u5b9a", None))
        self.comboBox_beep.setItemText(1, QCoreApplication.translate("Form", u"\u7531\u7a7a\u6c14\u6e29\u5ea6\u51b3\u5b9a", None))
        self.comboBox_beep.setItemText(2, QCoreApplication.translate("Form", u"\u7531\u7a7a\u6c14\u6e7f\u5ea6\u51b3\u5b9a", None))
        self.comboBox_beep.setItemText(3, QCoreApplication.translate("Form", u"\u7531\u571f\u58e4\u6e29\u5ea6\u51b3\u5b9a", None))
        self.comboBox_beep.setItemText(4, QCoreApplication.translate("Form", u"\u7531\u571f\u58e4\u6e7f\u5ea6\u51b3\u5b9a", None))
        self.comboBox_beep.setItemText(5, QCoreApplication.translate("Form", u"\u7531\u5149\u7167\u5f3a\u5ea6\u51b3\u5b9a", None))
        self.comboBox_beep.setItemText(6, QCoreApplication.translate("Form", u"\u7531\u56fe\u50cf\u8bc6\u522b\u51b3\u5b9a", None))

        self.label_18.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u51b3\u7b56\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u9608\u503c", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u6700\u5c0f\u503c", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u6700\u5927\u503c", None))
    # retranslateUi

