from PySide6.QtSerialPort import QSerialPortInfo
from PySide6.QtWidgets import QFrame, QComboBox, QVBoxLayout, QHBoxLayout, QLabel


class WidgetSerial(QFrame):
    class BoxItem(QFrame):
        def __init__(self, text):
            super().__init__()
            self.setLayout(QHBoxLayout())
            self.label = QLabel(self)
            self.comboBox = QComboBox(self)
            self.label.setText(text)
            self.layout().addWidget(self.label)
            self.layout().addWidget(self.comboBox)
    #     self.setLayout(QVBoxLayout(self))
    #     self.items = []
    #     for text in ["端口名：", "波特率：", "数据位：", "校验位：", "停止位："]:
    #         self.items.append(self.BoxItem(text))
    #         self.layout().addWidget(self.items[-1])
    #         self.items[-1].setObjectName("item"+str(len(self.items) - 1))
    #         print(self.items[-1].objectName())
    #     self.items[2].comboBox.addItems({"5": 5, "6": 6, "7": 7, "8": 8})
    #     self.items[3].comboBox.addItems({"None": None, "Even": None, "Mark": None, "Odd": None, "Space": None}) # Qt.EvenParity, "Mark": Qt.MarkParity, "Odd": Qt.OddParity, "Space": Qt.SpaceParity})
    #     self.items[4].comboBox.addItems({"1": 1, "1.5": 1.5, "2": 2})
    #     self.items[2].comboBox.setCurrentIndex(self.items[2].comboBox.count() - 1)
    #
    #     self.update_port()  # 先刷新串口列表，再connect信号槽
    #     self.items[0].comboBox.currentIndexChanged.connect(self.update_port)
    #
    #     # slot_list = {"item0": self.update_port}
    #     # for child in self.findChildren(QComboBox):
    #     #     if child.objectName() in slot_list:
    #     #         child.currentIndexChanged.connect(self.items[child.objectName()])
    #     # self.connect(self.items[])
    # def update_port(self):
    #     self.items[0].comboBox.clear()
    #     for port in QSerialPortInfo.availablePorts():
    #         self.items[0].comboBox.addItem(port.portName())
    #         # for baudRate in port.baudRates():
    #         for baudRates in port.standardBaudRates():
    #             self.items[1].comboBox.addItem(str(baudRates), baudRates)
    #         self.items[1].comboBox.setCurrentIndex(self.items[1].comboBox.findText("115200"))  # 默认选择115200波特率

    def __init__(self):
        super().__init__()
        self.layout_v = QVBoxLayout(self)
        self.comboBox_port = QComboBox(self)
        self.comboBox_baudRates = QComboBox(self)
        self.comboBox_dataBits = QComboBox(self)
        self.comboBox_checkBits = QComboBox(self)
        self.comboBox_stopBits = QComboBox(self)
        self.update_port()  # 先刷新串口列表，再connect信号槽
        self.comboBox_port.currentIndexChanged.connect(self.update_port)
        self.layout_v.addWidget(self.comboBox_port)
        self.layout_v.addWidget(self.comboBox_baudRates)
        self.layout_v.addWidget(self.comboBox_dataBits)
        self.layout_v.addWidget(self.comboBox_checkBits)
        self.layout_v.addWidget(self.comboBox_stopBits)
        self.comboBox_dataBits.addItems({"5": 5, "6": 6, "7": 7, "8": 8})
        self.comboBox_checkBits.addItems({"None": None, "Even": None, "Mark": None, "Odd": None, "Space": None})
        self.comboBox_stopBits.addItems({"1": 1, "1.5": 1.5, "2": 2})
        self.comboBox_dataBits.setCurrentIndex(self.comboBox_dataBits.count() - 1)

    def update_port(self):
        self.comboBox_port.clear()
        for port in QSerialPortInfo.availablePorts():
            # self.comboBox_port.addItem(port.portName(), port)
            self.comboBox_port.addItem(port.portName() + " " + port.description(), port)
            for baudRates in port.standardBaudRates():  # 添加波特率选项
                self.comboBox_baudRates.addItem(str(baudRates), baudRates)
        self.comboBox_baudRates.setCurrentIndex(self.comboBox_baudRates.findData(115200))  # 默认选择115200波特率
