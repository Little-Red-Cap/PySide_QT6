from import_modules import *
from ui.ui_page_setting import *


class PageCommunication(QFrame):
    def __init__(self, parent_obj=None):
        super().__init__()
        self.parent_obj = parent_obj
        # self.chart = EnvironmentalDataVisualizer()
        # self.layout().addWidget(self.chart)
        # self.setLayout(QGridLayout(self))
        self.button_state = False
        self.settings = Ui_Frame()
        self.settings.setupUi(self)
        self.settings.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        # self.settings.dockWidget.setWindowTitle(self.parent_obj.windowTitle())
        self.settings.dockWidget.setWindowTitle("log")

        self.serial = QSerialPort()
        for baudRates in QSerialPortInfo.standardBaudRates():  # 添加波特率选项
            self.settings.comboBox_baudRates.addItem(str(baudRates), baudRates)
        self.serial.setBaudRate(115200)
        self.serial.readyRead.connect(self.data_received)
        self.buffer = b''
        self.serialPortList = []
        # self.serial.setPortName('COM3')
        # self.serial.setDataBits(Qt.Data8)
        # self.serial.setParity(Qt.NoParity)
        # self.serial.setStopBits(Qt.OneStop)
        # self.serial.setFlowControl(Qt.NoFlowControl)
        self.settings.checkBox.setChecked(True)
        self.text_changed()  # 初始化视频流地址
        self.update_port()  # 先刷新串口列表，再connect信号槽
        # self.settings.comboBox_port.currentIndexChanged.connect(self.update_port)
        self.settings.pushButton_refresh.clicked.connect(self.update_port)
        self.settings.pushButton_port.clicked.connect(self.update_port_state)
        self.settings.lineEdit.textChanged.connect(self.text_changed)
        self.settings.pushButton_clear.clicked.connect(self.settings.textBrowser.clear)

    def text_changed(self):
        self.parent_obj.web_url = "http://" + self.settings.lineEdit.text() + "/"
        self.parent_obj.stream_url = "http://" + self.settings.lineEdit.text() + ":81/stream"

    def data_received(self):
        data = self.serial.readAll()
        self.buffer += data.data()  # 将新数据追加到缓冲区
        while True:
            try:    # 尝试从缓冲区中解析一个完整的JSON对象, 假设换行符结尾
                index = self.buffer.find(b'\n')
                if index == -1:     # 没有找到换行符，说明可能是一个不完整的JSON对象，退出循环
                    break
                json_data = self.buffer[:index].decode()  # 解码字节串为字符串
                self.buffer = self.buffer[index+1:]  # 移除已解析的部分和换行符
                # 发送解析后的JSON数据
                # self.dataReceived.emit(json_data)
                json_string = json.dumps(json_data, indent=4)
                print(json_string)
                print("=" * 50)
            except json.JSONDecodeError:
                # 如果解析失败，可能是因为数据不完整，回到循环的开头等待更多数据
                break
        if self.settings.checkBox.isChecked():
            self.settings.textBrowser.append(data.toStdString())

    def update_port(self):
        self.settings.comboBox_port.clear()
        self.serialPortList = QSerialPortInfo.availablePorts()
        if self.serialPortList.__len__() == 0:
            self.settings.comboBox_port.addItem("未发现串口")
        else:
            for info in self.serialPortList:
                self.settings.comboBox_port.addItem(info.portName() + " " + info.description(), info)
            self.settings.comboBox_baudRates.setCurrentIndex(
                self.settings.comboBox_baudRates.findData(self.serial.baudRate()))

    def update_port_state(self):
        if self.serial.isOpen():
            self.serial.close()
            self.settings.pushButton_port.setText("打开串口")
        else:
            self.serial.setPort(self.settings.comboBox_port.currentData())
            if self.serial.open(QIODevice.ReadWrite):
                self.settings.pushButton_port.setText("关闭串口")
            else:
                QMessageBox.critical(self, "错误", "打开串口失败！")
            # data = QByteArray(b"555")
            # self.serial.write(data)
