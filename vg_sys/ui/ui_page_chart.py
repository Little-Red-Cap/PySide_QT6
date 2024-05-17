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
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

from part_switch_button import SwitchButton

class Ui_data_view(object):
    def setupUi(self, data_view):
        if not data_view.objectName():
            data_view.setObjectName(u"data_view")
        data_view.resize(1432, 928)
        self.graphicsView_t = QChartView(data_view)
        self.graphicsView_t.setObjectName(u"graphicsView_t")
        self.graphicsView_t.setGeometry(QRect(59, 167, 631, 231))
        self.graphicsView_h = QChartView(data_view)
        self.graphicsView_h.setObjectName(u"graphicsView_h")
        self.graphicsView_h.setGeometry(QRect(60, 430, 631, 251))
        self.widget = QWidget(data_view)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(970, 170, 261, 531))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_16 = QFrame(self.widget)
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

        self.widget_2 = QWidget(data_view)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(50, 30, 641, 98))
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
        font = QFont()
        font.setPointSize(20)
        self.label_val_at.setFont(font)

        self.gridLayout_4.addWidget(self.label_val_at, 0, 1, 1, 1)

        self.label_title_at = QLabel(self.frame_at)
        self.label_title_at.setObjectName(u"label_title_at")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_title_at.setFont(font1)

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
        self.label_val_ah.setFont(font)

        self.gridLayout.addWidget(self.label_val_ah, 0, 1, 1, 1)

        self.label_title_ah = QLabel(self.frame_ah)
        self.label_title_ah.setObjectName(u"label_title_ah")
        self.label_title_ah.setFont(font1)

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
        self.label_title_st.setFont(font1)

        self.gridLayout_5.addWidget(self.label_title_st, 1, 1, 1, 1)

        self.label_val_st = QLabel(self.frame_st)
        self.label_val_st.setObjectName(u"label_val_st")
        self.label_val_st.setFont(font)

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
        self.label_val_sh.setFont(font)

        self.gridLayout_3.addWidget(self.label_val_sh, 0, 1, 1, 1)

        self.label_title_sh = QLabel(self.frame_sh)
        self.label_title_sh.setObjectName(u"label_title_sh")
        self.label_title_sh.setFont(font1)

        self.gridLayout_3.addWidget(self.label_title_sh, 1, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_sh)

        self.widget_3 = QWidget(data_view)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(720, 40, 221, 641))
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_time_img = QLabel(self.frame)
        self.label_time_img.setObjectName(u"label_time_img")
        font2 = QFont()
        font2.setPointSize(9)
        self.label_time_img.setFont(font2)

        self.gridLayout_2.addWidget(self.label_time_img, 0, 0, 4, 1)

        self.label_time_time = QLabel(self.frame)
        self.label_time_time.setObjectName(u"label_time_time")
        self.label_time_time.setFont(font)

        self.gridLayout_2.addWidget(self.label_time_time, 0, 1, 1, 3)

        self.label_time_week = QLabel(self.frame)
        self.label_time_week.setObjectName(u"label_time_week")
        self.label_time_week.setFont(font1)

        self.gridLayout_2.addWidget(self.label_time_week, 1, 3, 2, 1)

        self.label_time_date = QLabel(self.frame)
        self.label_time_date.setObjectName(u"label_time_date")
        self.label_time_date.setFont(font1)

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
        self.label_val_li.setFont(font)

        self.gridLayout_12.addWidget(self.label_val_li, 0, 1, 1, 1)

        self.label_title_li = QLabel(self.frame_li)
        self.label_title_li.setObjectName(u"label_title_li")
        self.label_title_li.setFont(font1)

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
        self.label_val_ap.setFont(font)

        self.gridLayout_11.addWidget(self.label_val_ap, 0, 1, 1, 1)

        self.label_title_ap = QLabel(self.frame_ap)
        self.label_title_ap.setObjectName(u"label_title_ap")
        self.label_title_ap.setFont(font1)

        self.gridLayout_11.addWidget(self.label_title_ap, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_ap)

        self.graphicsView_ap = QChartView(self.widget_3)
        self.graphicsView_ap.setObjectName(u"graphicsView_ap")

        self.verticalLayout.addWidget(self.graphicsView_ap)


        self.retranslateUi(data_view)

        QMetaObject.connectSlotsByName(data_view)
    # setupUi

    def retranslateUi(self, data_view):
        data_view.setWindowTitle(QCoreApplication.translate("data_view", u"Frame", None))
        self.label_type_dev3.setText(QCoreApplication.translate("data_view", u"\u704c\u6e89\u6c34\u6cf5", None))
        self.label_state_dev3.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_dev3.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_dev3.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
        self.label_type_dev2.setText(QCoreApplication.translate("data_view", u"\u6362\u6c14\u98ce\u6247", None))
        self.label_state_dev2.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_dev2.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_dev.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
        self.label_tyoe_dev1.setText(QCoreApplication.translate("data_view", u"\u7167\u660e\u706f", None))
        self.label_state_dev1.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_dev1.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_dev1.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
        self.label_type_dev4.setText(QCoreApplication.translate("data_view", u"\u706d\u866b\u706f", None))
        self.label_state_dev4.setText(QCoreApplication.translate("data_view", u"\u8bbe\u5907\u72b6\u6001", None))
        self.label_img_dev4.setText(QCoreApplication.translate("data_view", u"\u56fe\u6807", None))
        self.button_dev4.setText(QCoreApplication.translate("data_view", u"\u6253\u5f00", None))
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
    # retranslateUi

