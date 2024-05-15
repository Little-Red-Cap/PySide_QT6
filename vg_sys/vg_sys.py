# This Python file uses the following encoding: utf-8
import os
import sys
import random
from ctypes.wintypes import MSG

import numpy as np
import math
from functools import partial
from pathlib import Path

from qframelesswindow import AcrylicWindow
from qframelesswindow.windows import WindowsWindowEffect
# import cv2
# from ultralytics import YOLO

# from QtFusion.path import abs_path
# from YOLOv8Model import YOLOv8Detector
# from QtFusion.config import QF_Config

# from qt_material import *
from qt_material import apply_stylesheet

import win32api
import win32con
import win32gui
# from qfluentwidgets import *
# from qfluentwidgets import FluentIcon as FIF
# from qfluentwidgets.components.widgets.frameless_window import FramelessWindow

# import pyecharts
# from pyecharts import charts

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import *
from PySide6.QtSerialPort import *
from PySide6.QtWebChannel import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtUiTools import *
import PySide6.QtSql


from ui_main import *
from ui_page_setting import *
from page_left import *
from part_animation import *
from part_about import *
from part_serial_port import *
from part_base_frame import *
from part_device import *
from part_switch_button import *
from page_communi import *
from page_data_analysis import *
from page_data_view import *
from page_manage import *

from base_part.win32_utils import *
from base_part import startSystemMove
from base_part.title_bar_buttons import *
# from vg_sys.base_part.win32_utils import Taskbar


# from base_part.title_bar import TitleBar


# from part_chart import *
# from part_web import *


# class MainWidget(QSplitter, PartAnimation):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle(QObject.tr("Village Green System", "Village Green System"))
#         self.setWindowIcon(QIcon("img/hei.ico"))
#
#         # self.page_left = InfoWidget()
#         self.page_left = PageLeft()
#         self.page_left.setMaximumWidth(100)
#         self.page_communication = PageCommunication()
#         self.page_data_analysis = PageDataAnalysis()
#         self.page_data_view = PageDataView()
#         self.page_manage = PageManage()
#         self.stacked_pages = QStackedWidget(self)
#         self.stacked_pages.addWidget(self.page_communication)
#         self.stacked_pages.addWidget(self.page_data_view)
#         self.stacked_pages.addWidget(self.page_data_analysis)
#         self.stacked_pages.addWidget(self.page_manage)
#         self.page_left.page_index_changed.connect(self.stacked_pages.setCurrentIndex)  # 将左、右侧页面的切换信号作关联
#         self.addWidget(self.page_left)
#         self.addWidget(self.stacked_pages)
#         self.resize(1280, 800)
#
#     def keyPressEvent(self, event: QKeyEvent):
#         if event.key() == Qt.Key_F2:
#             if self.page_left.isHidden():
#                 self.page_left.show()
#             else:
#                 self.page_left.setHidden(True)
#
#     # def showEvent(self, event) -> None:
#     #     self.show_animation()
#     #
#     # def closeEvent(self, event):
#     #     self.close_animation(event)

class TitleBarBase(QWidget):
    """ Title bar base class """

    def __init__(self, parent):
        super().__init__(parent)
        self.minBtn = MinimizeButton(parent=self)
        self.closeBtn = CloseButton(parent=self)
        self.maxBtn = MaximizeButton(parent=self)

        self._isDoubleClickEnabled = True

        self.resize(200, 32)
        self.setFixedHeight(32)

        # connect signal to slot
        self.minBtn.clicked.connect(self.window().showMinimized)
        self.maxBtn.clicked.connect(self.__toggleMaxState)
        self.closeBtn.clicked.connect(self.window().close)

        self.window().installEventFilter(self)

    def eventFilter(self, obj, e):
        if obj is self.window():
            if e.type() == QEvent.WindowStateChange:
                self.maxBtn.setMaxState(self.window().isMaximized())
                return False

        return super().eventFilter(obj, e)

    def mouseDoubleClickEvent(self, event):
        """ Toggles the maximization state of the window """
        if event.button() != Qt.LeftButton or not self._isDoubleClickEnabled:
            return

        self.__toggleMaxState()

    def mouseMoveEvent(self, e):
        if sys.platform != "win32" or not self.canDrag(e.pos()):
            return

        startSystemMove(self.window(), e.globalPos())

    def mousePressEvent(self, e):
        if sys.platform == "win32" or not self.canDrag(e.pos()):
            return

        startSystemMove(self.window(), e.globalPos())

    def __toggleMaxState(self):
        """ Toggles the maximization state of the window and change icon """
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()

        if sys.platform == "win32":
            from base_part.win32_utils import releaseMouseLeftButton
            releaseMouseLeftButton(self.window().winId())

    def _isDragRegion(self, pos):
        """ Check whether the position belongs to the area where dragging is allowed """
        width = 0
        for button in self.findChildren(TitleBarButton):
            if button.isVisible():
                width += button.width()

        return 0 < pos.x() < self.width() - width

    def _hasButtonPressed(self):
        """ whether any button is pressed """
        return any(btn.isPressed() for btn in self.findChildren(TitleBarButton))

    def canDrag(self, pos):
        """ whether the position is draggable """
        return self._isDragRegion(pos) and not self._hasButtonPressed()

    def setDoubleClickEnabled(self, isEnabled):
        """ whether to switch window maximization status when double clicked

        Parameters
        ----------
        isEnabled: bool
            whether to enable double click
        """
        self._isDoubleClickEnabled = isEnabled


class TitleBar(TitleBarBase):
    """ Title bar with minimize, maximum and close button """

    def __init__(self, parent):
        super().__init__(parent)
        self.hBoxLayout = QHBoxLayout(self)

        # add buttons to layout
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.minBtn, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.maxBtn, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.closeBtn, 0, Qt.AlignRight)


class StandardTitleBar(TitleBar):
    """ Title bar with icon and title """

    def __init__(self, parent):
        super().__init__(parent)
        # add window icon
        self.iconLabel = QLabel(self)
        self.iconLabel.setFixedSize(20, 20)
        self.hBoxLayout.insertSpacing(0, 10)
        self.hBoxLayout.insertWidget(1, self.iconLabel, 0, Qt.AlignLeft)
        self.window().windowIconChanged.connect(self.setIcon)

        # add title label
        self.titleLabel = QLabel(self)
        self.hBoxLayout.insertWidget(2, self.titleLabel, 0, Qt.AlignLeft)
        self.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Segoe UI';
                padding: 0 4px
            }
        """)
        self.window().windowTitleChanged.connect(self.setTitle)

    def setTitle(self, title):
        """ set the title of title bar

        Parameters
        ----------
        title: str
            the title of title bar
        """
        self.titleLabel.setText(title)
        self.titleLabel.adjustSize()

    def setIcon(self, icon):
        """ set the icon of title bar

        Parameters
        ----------
        icon: QIcon | QPixmap | str
            the icon of title bar
        """
        self.iconLabel.setPixmap(QIcon(icon).pixmap(20, 20))



class PageCommunication(QFrame):
    def __init__(self):
        super().__init__()
        self.button_state = False
        self.settings = Ui_Frame()
        self.settings.setupUi(self)

        self.serial = QSerialPort()
        self.serial.setBaudRate(115200)



class MainWidget(QSplitter, PartAnimation):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(QObject.tr("Village Green System", "Village Green System"))
        self.setWindowIcon(QIcon("img/hei.ico"))

        # self.titleBar = StandardTitleBar(self)
        # self.titleBar = TitleBar(self)
        self.windowEffect = WindowsWindowEffect(self)
        self.updateFrameless()# solve issue #5
        self.windowHandle().screenChanged.connect(self.__onScreenChanged)
        self.resize(500, 500)
        # self.titleBar.raise_()

        self.page_communication = PageCommunication()
        self.stacked_pages = QStackedWidget(self)
        self.stacked_pages.addWidget(self.page_communication)
        self.addWidget(self.stacked_pages)
        # self.resize(1280, 800)

    def updateFrameless(self):
        """ update frameless window """
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        # add DWM shadow and window animation
        self.windowEffect.addWindowAnimation(self.winId())
        if not isinstance(self, AcrylicWindow):
            self.windowEffect.addShadowEffect(self.winId())

    def __onScreenChanged(self):
        hWnd = int(self.windowHandle().winId())
        win32gui.SetWindowPos(hWnd, None, 0, 0, 0, 0, win32con.SWP_NOMOVE |
                              win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWidget()
    # apply_stylesheet(app, theme='dark_blue.xml')
    # apply_stylesheet(app, theme='dark_teal.xml')
    # apply_stylesheet(app, theme='dark_purple.xml')
    # apply_stylesheet(app, theme='light_yellow.xml')
    widget.show()
    sys.exit(app.exec())

# <a href="https://www.flaticon.com/free-icons/chart" title="chart icons">Chart icons created by DinosoftLabs - Flaticon</a>
