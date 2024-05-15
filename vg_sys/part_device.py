from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout
from part_switch_button import *


class Device(QFrame):
    def __init__(self, dev_type=None):
        super().__init__()
        self.is_online = bool
        self.horizontalLayout = QHBoxLayout(self)
        self.label_icon = QLabel(self)
        self.frame_untitled = QFrame(self)
        self.verticalLayout = QVBoxLayout(self.frame_untitled)
        self.label_dev_name = QLabel(self.frame_untitled)
        self.label_dev_state = QLabel(self.frame_untitled)
        self.frame = SwitchButton()

        self.horizontalLayout.addWidget(self.label_icon)
        self.verticalLayout.addWidget(self.label_dev_name)
        self.verticalLayout.addWidget(self.label_dev_state)
        self.horizontalLayout.addWidget(self.frame_untitled)
        self.horizontalLayout.addWidget(self.frame)

        self.frame_untitled.setFrameShape(QFrame.StyledPanel)
        self.frame_untitled.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName(u"frame")
        self.frame_untitled.setObjectName(u"frame_untitled")
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_icon.setObjectName(u"label")
        self.label_dev_state.setObjectName(u"label_dev_state")
        self.label_dev_name.setObjectName(u"label_dev_name")

        dev_info = {"fan": ["FAN","img/dev_type/fan.png"],
                         "motor": ["Motor", "img/dev_type/motor.png"],
                         "led": ["LED", "img/dev_type/led.png"],
                         }  # dev_type : [dev_name, icon_path]
        if dev_type is not None:
            self.label_dev_name.setText(dev_info[dev_type][0])
            self.label_icon.setPixmap(QPixmap(dev_info[dev_type][1]))

    def update_state(self, is_online):
        self.is_online = is_online
        self.label_dev_state.setText("在线" if self.is_online else "离线")


class DeviceList(QFrame):
    def __init__(self):
        super().__init__()
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dev = []
        for item in ["fan", "motor"]:
            self.dev.append(Device(item))
            self.verticalLayout.addWidget(self.dev[-1])
            # self.dev[-1].update_state(False)
        self.setLayout(self.verticalLayout)
        # self.label_info.setText(f"{self.name}({self.id})")
