# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_chart.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

from part_switch_button import SwitchButton

class Ui_data_view(object):
    def setupUi(self, data_view):
        if not data_view.objectName():
            data_view.setObjectName(u"data_view")
        data_view.resize(1432, 928)
        self.gridLayout_2 = QGridLayout(data_view)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_10 = QFrame(data_view)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_val_at = QLabel(self.frame_10)
        self.label_val_at.setObjectName(u"label_val_at")
        font = QFont()
        font.setPointSize(20)
        self.label_val_at.setFont(font)

        self.gridLayout_4.addWidget(self.label_val_at, 0, 1, 1, 1)

        self.label_title_at = QLabel(self.frame_10)
        self.label_title_at.setObjectName(u"label_title_at")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_title_at.setFont(font1)

        self.gridLayout_4.addWidget(self.label_title_at, 1, 1, 1, 1)

        self.label_img_at = QLabel(self.frame_10)
        self.label_img_at.setObjectName(u"label_img_at")

        self.gridLayout_4.addWidget(self.label_img_at, 0, 0, 2, 1)


        self.horizontalLayout.addWidget(self.frame_10)

        self.frame_11 = QFrame(data_view)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_img_ah = QLabel(self.frame_11)
        self.label_img_ah.setObjectName(u"label_img_ah")

        self.gridLayout.addWidget(self.label_img_ah, 0, 0, 2, 1)

        self.label_val_ah = QLabel(self.frame_11)
        self.label_val_ah.setObjectName(u"label_val_ah")
        self.label_val_ah.setFont(font)

        self.gridLayout.addWidget(self.label_val_ah, 0, 1, 1, 1)

        self.label_title_ah = QLabel(self.frame_11)
        self.label_title_ah.setObjectName(u"label_title_ah")
        self.label_title_ah.setFont(font1)

        self.gridLayout.addWidget(self.label_title_ah, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.frame_11)

        self.frame_12 = QFrame(data_view)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_title_st = QLabel(self.frame_12)
        self.label_title_st.setObjectName(u"label_title_st")
        self.label_title_st.setFont(font1)

        self.gridLayout_5.addWidget(self.label_title_st, 1, 1, 1, 1)

        self.label_val_st = QLabel(self.frame_12)
        self.label_val_st.setObjectName(u"label_val_st")
        self.label_val_st.setFont(font)

        self.gridLayout_5.addWidget(self.label_val_st, 0, 1, 1, 1)

        self.label_img_st = QLabel(self.frame_12)
        self.label_img_st.setObjectName(u"label_img_st")

        self.gridLayout_5.addWidget(self.label_img_st, 0, 0, 2, 1)


        self.horizontalLayout.addWidget(self.frame_12)

        self.frame_13 = QFrame(data_view)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_13)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_img_sh = QLabel(self.frame_13)
        self.label_img_sh.setObjectName(u"label_img_sh")

        self.gridLayout_3.addWidget(self.label_img_sh, 0, 0, 2, 1)

        self.label_val_sh = QLabel(self.frame_13)
        self.label_val_sh.setObjectName(u"label_val_sh")
        self.label_val_sh.setFont(font)

        self.gridLayout_3.addWidget(self.label_val_sh, 0, 1, 1, 1)

        self.label_title_sh = QLabel(self.frame_13)
        self.label_title_sh.setObjectName(u"label_title_sh")
        self.label_title_sh.setFont(font1)

        self.gridLayout_3.addWidget(self.label_title_sh, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.frame_13)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 2, 1)

        self.graphicsView_t = QChartView(data_view)
        self.graphicsView_t.setObjectName(u"graphicsView_t")

        self.gridLayout_2.addWidget(self.graphicsView_t, 2, 0, 1, 1)

        self.graphicsView_h = QChartView(data_view)
        self.graphicsView_h.setObjectName(u"graphicsView_h")

        self.gridLayout_2.addWidget(self.graphicsView_h, 3, 0, 1, 1)

        self.scrollArea = QScrollArea(data_view)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setBaseSize(QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 197, 820))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_14 = QFrame(self.scrollAreaWidgetContents)
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


        self.verticalLayout_5.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents)
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


        self.verticalLayout_5.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_16)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_type_dev3 = QLabel(self.frame_16)
        self.label_type_dev3.setObjectName(u"label_type_dev3")

        self.gridLayout_8.addWidget(self.label_type_dev3, 0, 1, 1, 1)

        self.label_state_dev3 = QLabel(self.frame_16)
        self.label_state_dev3.setObjectName(u"label_state_dev3")

        self.gridLayout_8.addWidget(self.label_state_dev3, 1, 1, 1, 1)

        self.label_img_dev3 = QLabel(self.frame_16)
        self.label_img_dev3.setObjectName(u"label_img_dev3")

        self.gridLayout_8.addWidget(self.label_img_dev3, 0, 0, 2, 1)

        self.button_dev3 = SwitchButton(self.frame_16)
        self.button_dev3.setObjectName(u"button_dev3")

        self.gridLayout_8.addWidget(self.button_dev3, 0, 3, 2, 1)


        self.verticalLayout_5.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents)
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


        self.verticalLayout_5.addWidget(self.frame_17)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 2, 1, 2, 1)

        self.frame = QFrame(data_view)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_time = QLabel(self.frame)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_time)


        self.gridLayout_2.addWidget(self.frame, 0, 1, 2, 1)


        self.retranslateUi(data_view)

        QMetaObject.connectSlotsByName(data_view)
    # setupUi

    def retranslateUi(self, data_view):
        data_view.setWindowTitle(QCoreApplication.translate("data_view", u"Frame", None))
        self.label_val_at.setText(QCoreApplication.translate("data_view", u"N/A", None))
        self.label_title_at.setText(QCoreApplication.translate("data_view", u"\u7a7a\u6c14\u6e29\u5ea6", None))
        self.label_img_at.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.label_img_ah.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.label_val_ah.setText(QCoreApplication.translate("data_view", u"N/A", None))
        self.label_title_ah.setText(QCoreApplication.translate("data_view", u"\u7a7a\u6c14\u6e7f\u5ea6", None))
        self.label_title_st.setText(QCoreApplication.translate("data_view", u"\u571f\u58e4\u6e29\u5ea6", None))
        self.label_val_st.setText(QCoreApplication.translate("data_view", u"N/A", None))
        self.label_img_st.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.label_img_sh.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.label_val_sh.setText(QCoreApplication.translate("data_view", u"N/A", None))
        self.label_title_sh.setText(QCoreApplication.translate("data_view", u"\u571f\u58e4\u6e7f\u5ea6", None))
        self.label_tyoe_dev1.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u7c7b\u578b", None))
        self.label_state_dev1.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_dev1.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_dev1.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
        self.label_type_dev2.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u7c7b\u578b", None))
        self.label_state_dev2.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_dev2.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_dev.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
        self.label_type_dev3.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u7c7b\u578b", None))
        self.label_state_dev3.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_dev3.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_dev3.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
        self.label_type_dev4.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u7c7b\u578b", None))
        self.label_state_dev4.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_dev4.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_dev4.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
        self.label_time.setText(QCoreApplication.translate("data_view", u"TextLabel", None))
    # retranslateUi

