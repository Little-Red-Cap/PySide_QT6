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
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from part_switch_button import SwitchButton

class Ui_data_view(object):
    def setupUi(self, data_view):
        if not data_view.objectName():
            data_view.setObjectName(u"data_view")
        data_view.resize(1432, 928)
        self.gridLayout_13 = QGridLayout(data_view)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.graphicsView_t = QChartView(data_view)
        self.graphicsView_t.setObjectName(u"graphicsView_t")

        self.gridLayout_13.addWidget(self.graphicsView_t, 1, 0, 1, 1)

        self.widget_3 = QWidget(data_view)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 0, 9)
        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_time_img = QLabel(self.frame)
        self.label_time_img.setObjectName(u"label_time_img")
        font = QFont()
        font.setPointSize(9)
        self.label_time_img.setFont(font)

        self.gridLayout_2.addWidget(self.label_time_img, 0, 0, 4, 1)

        self.label_time_time = QLabel(self.frame)
        self.label_time_time.setObjectName(u"label_time_time")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_time_time.setFont(font1)

        self.gridLayout_2.addWidget(self.label_time_time, 0, 1, 1, 3)

        self.label_time_week = QLabel(self.frame)
        self.label_time_week.setObjectName(u"label_time_week")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_time_week.setFont(font2)

        self.gridLayout_2.addWidget(self.label_time_week, 1, 3, 2, 1)

        self.label_time_date = QLabel(self.frame)
        self.label_time_date.setObjectName(u"label_time_date")
        self.label_time_date.setFont(font2)

        self.gridLayout_2.addWidget(self.label_time_date, 1, 1, 2, 2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_li = QFrame(self.widget_3)
        self.frame_li.setObjectName(u"frame_li")
        self.frame_li.setFrameShape(QFrame.StyledPanel)
        self.frame_li.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_li)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_img_li = QLabel(self.frame_li)
        self.label_img_li.setObjectName(u"label_img_li")

        self.gridLayout_12.addWidget(self.label_img_li, 0, 0, 2, 1)

        self.label_val_li = QLabel(self.frame_li)
        self.label_val_li.setObjectName(u"label_val_li")
        self.label_val_li.setFont(font1)

        self.gridLayout_12.addWidget(self.label_val_li, 0, 1, 1, 1)

        self.label_title_li = QLabel(self.frame_li)
        self.label_title_li.setObjectName(u"label_title_li")
        self.label_title_li.setFont(font2)

        self.gridLayout_12.addWidget(self.label_title_li, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_li)

        self.graphicsView_li = QChartView(self.widget_3)
        self.graphicsView_li.setObjectName(u"graphicsView_li")

        self.verticalLayout.addWidget(self.graphicsView_li)

        self.frame_ap = QFrame(self.widget_3)
        self.frame_ap.setObjectName(u"frame_ap")
        self.frame_ap.setFrameShape(QFrame.StyledPanel)
        self.frame_ap.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_ap)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_img_ap = QLabel(self.frame_ap)
        self.label_img_ap.setObjectName(u"label_img_ap")

        self.gridLayout_11.addWidget(self.label_img_ap, 0, 0, 2, 1)

        self.label_val_ap = QLabel(self.frame_ap)
        self.label_val_ap.setObjectName(u"label_val_ap")
        self.label_val_ap.setFont(font1)

        self.gridLayout_11.addWidget(self.label_val_ap, 0, 1, 1, 1)

        self.label_title_ap = QLabel(self.frame_ap)
        self.label_title_ap.setObjectName(u"label_title_ap")
        self.label_title_ap.setFont(font2)

        self.gridLayout_11.addWidget(self.label_title_ap, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_ap)

        self.graphicsView_ap = QChartView(self.widget_3)
        self.graphicsView_ap.setObjectName(u"graphicsView_ap")

        self.verticalLayout.addWidget(self.graphicsView_ap)


        self.gridLayout_13.addWidget(self.widget_3, 0, 2, 3, 1)

        self.widget_2 = QWidget(data_view)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_at = QFrame(self.widget_2)
        self.frame_at.setObjectName(u"frame_at")
        self.frame_at.setFrameShape(QFrame.StyledPanel)
        self.frame_at.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_at)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_val_at = QLabel(self.frame_at)
        self.label_val_at.setObjectName(u"label_val_at")
        self.label_val_at.setFont(font1)

        self.gridLayout_4.addWidget(self.label_val_at, 0, 1, 1, 1)

        self.label_title_at = QLabel(self.frame_at)
        self.label_title_at.setObjectName(u"label_title_at")
        self.label_title_at.setFont(font2)

        self.gridLayout_4.addWidget(self.label_title_at, 1, 1, 1, 1)

        self.label_img_at = QLabel(self.frame_at)
        self.label_img_at.setObjectName(u"label_img_at")

        self.gridLayout_4.addWidget(self.label_img_at, 0, 0, 2, 1)


        self.horizontalLayout_3.addWidget(self.frame_at)

        self.frame_ah = QFrame(self.widget_2)
        self.frame_ah.setObjectName(u"frame_ah")
        self.frame_ah.setFrameShape(QFrame.StyledPanel)
        self.frame_ah.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_ah)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_img_ah = QLabel(self.frame_ah)
        self.label_img_ah.setObjectName(u"label_img_ah")

        self.gridLayout.addWidget(self.label_img_ah, 0, 0, 2, 1)

        self.label_val_ah = QLabel(self.frame_ah)
        self.label_val_ah.setObjectName(u"label_val_ah")
        self.label_val_ah.setFont(font1)

        self.gridLayout.addWidget(self.label_val_ah, 0, 1, 1, 1)

        self.label_title_ah = QLabel(self.frame_ah)
        self.label_title_ah.setObjectName(u"label_title_ah")
        self.label_title_ah.setFont(font2)

        self.gridLayout.addWidget(self.label_title_ah, 1, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_ah)

        self.frame_st = QFrame(self.widget_2)
        self.frame_st.setObjectName(u"frame_st")
        self.frame_st.setFrameShape(QFrame.StyledPanel)
        self.frame_st.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_st)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_title_st = QLabel(self.frame_st)
        self.label_title_st.setObjectName(u"label_title_st")
        self.label_title_st.setFont(font2)

        self.gridLayout_5.addWidget(self.label_title_st, 1, 1, 1, 1)

        self.label_val_st = QLabel(self.frame_st)
        self.label_val_st.setObjectName(u"label_val_st")
        self.label_val_st.setFont(font1)

        self.gridLayout_5.addWidget(self.label_val_st, 0, 1, 1, 1)

        self.label_img_st = QLabel(self.frame_st)
        self.label_img_st.setObjectName(u"label_img_st")

        self.gridLayout_5.addWidget(self.label_img_st, 0, 0, 2, 1)


        self.horizontalLayout_3.addWidget(self.frame_st)

        self.frame_sh = QFrame(self.widget_2)
        self.frame_sh.setObjectName(u"frame_sh")
        self.frame_sh.setFrameShape(QFrame.StyledPanel)
        self.frame_sh.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_sh)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_img_sh = QLabel(self.frame_sh)
        self.label_img_sh.setObjectName(u"label_img_sh")

        self.gridLayout_3.addWidget(self.label_img_sh, 0, 0, 2, 1)

        self.label_val_sh = QLabel(self.frame_sh)
        self.label_val_sh.setObjectName(u"label_val_sh")
        self.label_val_sh.setFont(font1)

        self.gridLayout_3.addWidget(self.label_val_sh, 0, 1, 1, 1)

        self.label_title_sh = QLabel(self.frame_sh)
        self.label_title_sh.setObjectName(u"label_title_sh")
        self.label_title_sh.setFont(font2)

        self.gridLayout_3.addWidget(self.label_title_sh, 1, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_sh)


        self.gridLayout_13.addWidget(self.widget_2, 0, 0, 1, 1)

        self.graphicsView_h = QChartView(data_view)
        self.graphicsView_h.setObjectName(u"graphicsView_h")

        self.gridLayout_13.addWidget(self.graphicsView_h, 2, 0, 1, 1)

        self.widget = QWidget(data_view)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_ctrl = QPushButton(self.widget)
        self.pushButton_ctrl.setObjectName(u"pushButton_ctrl")

        self.verticalLayout_2.addWidget(self.pushButton_ctrl)

        self.frame_waterPump = QFrame(self.widget)
        self.frame_waterPump.setObjectName(u"frame_waterPump")
        self.frame_waterPump.setFrameShape(QFrame.StyledPanel)
        self.frame_waterPump.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_waterPump)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_type_waterPump = QLabel(self.frame_waterPump)
        self.label_type_waterPump.setObjectName(u"label_type_waterPump")

        self.gridLayout_8.addWidget(self.label_type_waterPump, 0, 1, 1, 1)

        self.label_state_waterPump = QLabel(self.frame_waterPump)
        self.label_state_waterPump.setObjectName(u"label_state_waterPump")

        self.gridLayout_8.addWidget(self.label_state_waterPump, 1, 1, 1, 1)

        self.label_img_waterPump = QLabel(self.frame_waterPump)
        self.label_img_waterPump.setObjectName(u"label_img_waterPump")

        self.gridLayout_8.addWidget(self.label_img_waterPump, 0, 0, 2, 1)

        self.button_waterPump = SwitchButton(self.frame_waterPump)
        self.button_waterPump.setObjectName(u"button_waterPump")

        self.gridLayout_8.addWidget(self.button_waterPump, 0, 3, 2, 1)


        self.verticalLayout_2.addWidget(self.frame_waterPump)

        self.frame_fan = QFrame(self.widget)
        self.frame_fan.setObjectName(u"frame_fan")
        self.frame_fan.setFrameShape(QFrame.StyledPanel)
        self.frame_fan.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_fan)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_type_fan = QLabel(self.frame_fan)
        self.label_type_fan.setObjectName(u"label_type_fan")

        self.gridLayout_7.addWidget(self.label_type_fan, 0, 1, 1, 1)

        self.label_state_fan = QLabel(self.frame_fan)
        self.label_state_fan.setObjectName(u"label_state_fan")

        self.gridLayout_7.addWidget(self.label_state_fan, 1, 1, 1, 1)

        self.label_img_fan = QLabel(self.frame_fan)
        self.label_img_fan.setObjectName(u"label_img_fan")

        self.gridLayout_7.addWidget(self.label_img_fan, 0, 0, 2, 1)

        self.button_fan = SwitchButton(self.frame_fan)
        self.button_fan.setObjectName(u"button_fan")

        self.gridLayout_7.addWidget(self.button_fan, 0, 3, 2, 1)


        self.verticalLayout_2.addWidget(self.frame_fan)

        self.frame_light = QFrame(self.widget)
        self.frame_light.setObjectName(u"frame_light")
        self.frame_light.setFrameShape(QFrame.StyledPanel)
        self.frame_light.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_light)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_tyoe_light = QLabel(self.frame_light)
        self.label_tyoe_light.setObjectName(u"label_tyoe_light")

        self.gridLayout_6.addWidget(self.label_tyoe_light, 0, 1, 1, 1)

        self.label_state_light = QLabel(self.frame_light)
        self.label_state_light.setObjectName(u"label_state_light")

        self.gridLayout_6.addWidget(self.label_state_light, 1, 1, 1, 1)

        self.label_img_light = QLabel(self.frame_light)
        self.label_img_light.setObjectName(u"label_img_light")

        self.gridLayout_6.addWidget(self.label_img_light, 0, 0, 2, 1)

        self.button_light = SwitchButton(self.frame_light)
        self.button_light.setObjectName(u"button_light")

        self.gridLayout_6.addWidget(self.button_light, 0, 3, 2, 1)


        self.verticalLayout_2.addWidget(self.frame_light)

        self.frame_InsectKillingLamp = QFrame(self.widget)
        self.frame_InsectKillingLamp.setObjectName(u"frame_InsectKillingLamp")
        self.frame_InsectKillingLamp.setFrameShape(QFrame.StyledPanel)
        self.frame_InsectKillingLamp.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_InsectKillingLamp)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_type_InsectKillingLamp = QLabel(self.frame_InsectKillingLamp)
        self.label_type_InsectKillingLamp.setObjectName(u"label_type_InsectKillingLamp")

        self.gridLayout_9.addWidget(self.label_type_InsectKillingLamp, 0, 1, 1, 1)

        self.label_state_InsectKillingLamp = QLabel(self.frame_InsectKillingLamp)
        self.label_state_InsectKillingLamp.setObjectName(u"label_state_InsectKillingLamp")

        self.gridLayout_9.addWidget(self.label_state_InsectKillingLamp, 1, 1, 1, 1)

        self.label_img_InsectKillingLamp = QLabel(self.frame_InsectKillingLamp)
        self.label_img_InsectKillingLamp.setObjectName(u"label_img_InsectKillingLamp")

        self.gridLayout_9.addWidget(self.label_img_InsectKillingLamp, 0, 0, 2, 1)

        self.button_InsectKillingLamp = SwitchButton(self.frame_InsectKillingLamp)
        self.button_InsectKillingLamp.setObjectName(u"button_InsectKillingLamp")

        self.gridLayout_9.addWidget(self.button_InsectKillingLamp, 0, 3, 2, 1)


        self.verticalLayout_2.addWidget(self.frame_InsectKillingLamp)

        self.frame_beep = QFrame(self.widget)
        self.frame_beep.setObjectName(u"frame_beep")
        self.frame_beep.setFrameShape(QFrame.StyledPanel)
        self.frame_beep.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_beep)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_type_beep = QLabel(self.frame_beep)
        self.label_type_beep.setObjectName(u"label_type_beep")

        self.gridLayout_10.addWidget(self.label_type_beep, 0, 1, 1, 1)

        self.label_state_beep = QLabel(self.frame_beep)
        self.label_state_beep.setObjectName(u"label_state_beep")

        self.gridLayout_10.addWidget(self.label_state_beep, 1, 1, 1, 1)

        self.label_img_beep = QLabel(self.frame_beep)
        self.label_img_beep.setObjectName(u"label_img_beep")

        self.gridLayout_10.addWidget(self.label_img_beep, 0, 0, 2, 1)

        self.button_beep = SwitchButton(self.frame_beep)
        self.button_beep.setObjectName(u"button_beep")

        self.gridLayout_10.addWidget(self.button_beep, 0, 3, 2, 1)


        self.verticalLayout_2.addWidget(self.frame_beep)


        self.gridLayout_13.addWidget(self.widget, 0, 3, 3, 1)


        self.retranslateUi(data_view)

        QMetaObject.connectSlotsByName(data_view)
    # setupUi

    def retranslateUi(self, data_view):
        data_view.setWindowTitle(QCoreApplication.translate("data_view", u"Frame", None))
        self.label_time_img.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.label_time_time.setText(QCoreApplication.translate("data_view", u"\u65f6\u5206\u79d2", None))
        self.label_time_week.setText(QCoreApplication.translate("data_view", u"\u661f\u671f", None))
        self.label_time_date.setText(QCoreApplication.translate("data_view", u"\u5e74\u6708\u65e5", None))
        self.label_img_li.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.label_val_li.setText(QCoreApplication.translate("data_view", u"N/A", None))
        self.label_title_li.setText(QCoreApplication.translate("data_view", u"\u5149\u7167\u5f3a\u5ea6", None))
        self.label_img_ap.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.label_val_ap.setText(QCoreApplication.translate("data_view", u"N/A", None))
        self.label_title_ap.setText(QCoreApplication.translate("data_view", u"\u5927\u6c14\u538b\u5f3a", None))
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
        self.pushButton_ctrl.setText(QCoreApplication.translate("data_view", u"\u81ea\u52a8", None))
        self.label_type_waterPump.setText(QCoreApplication.translate("data_view", u"\u704c\u6e89\u6c34\u6cf5", None))
        self.label_state_waterPump.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_waterPump.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_waterPump.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
        self.label_type_fan.setText(QCoreApplication.translate("data_view", u"\u6362\u6c14\u98ce\u6247", None))
        self.label_state_fan.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_fan.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_fan.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
        self.label_tyoe_light.setText(QCoreApplication.translate("data_view", u"\u7167\u660e\u706f", None))
        self.label_state_light.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_light.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_light.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
        self.label_type_InsectKillingLamp.setText(QCoreApplication.translate("data_view", u"\u706d\u866b\u706f", None))
        self.label_state_InsectKillingLamp.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_InsectKillingLamp.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_InsectKillingLamp.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
        self.label_type_beep.setText(QCoreApplication.translate("data_view", u"\u62a5\u8b66\u5668", None))
        self.label_state_beep.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_beep.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_beep.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
    # retranslateUi

