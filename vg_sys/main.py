# This Python file uses the following encoding: utf-8
from import_modules import *

from page_left import *
from part_animation import *
from part_about import *
from part_serial_port import *
from part_base_frame import *
from part_device import *
from page_communi import *
from page_data_analysis import *
from page_data_view import *
from page_manage import *

# import bottle
# from bottle import Bottle, run
# import pyqtgraph as pg
from part_switch_button import *
from py_gf.render_svg_to_pixmap import gf_to_icon
from ui.ui_page_chart import *
from ui.ui_page_setting import *
from ui.ui_page_dev import *


class EnvironmentalData:
    air_temperature = float
    air_humidity = float
    soil_temperature = float
    soil_humidity = float
    light_intensity = float
    atmospheric_pressure = float

    def __init__(self):
        self.timestamp = None
        self.air_temperature = None
        self.air_humidity = None
        self.soil_temperature = None
        self.soil_humidity = None
        self.light_intensity = None
        self.atmospheric_pressure = None

    def update_data(self, air_temp, air_hum, soil_temp, soil_hum, light_int, atmospheric_press):
        self.air_temperature = air_temp
        self.air_humidity = air_hum
        self.soil_temperature = soil_temp
        self.soil_humidity = soil_hum
        self.light_intensity = light_int
        self.atmospheric_pressure = atmospheric_press


class EnvironmentalDataVisualizer(QWidget, EnvironmentalData):
    def __init__(self):
        super().__init__()
        self.timer = None
        self.data_model = EnvironmentalData()
        self.init_ui()
        self.start_timer()

    def init_ui(self):
        layout = QVBoxLayout()

        # 创建标签来显示数据
        self.air_temp_label = QLabel("Air Temperature: N/A")
        self.air_hum_label = QLabel("Air Humidity: N/A")
        self.soil_temp_label = QLabel("Soil Temperature: N/A")
        self.soil_hum_label = QLabel("Soil Humidity: N/A")
        self.light_int_label = QLabel("Light Intensity: N/A")
        self.atm_press_label = QLabel("Atmospheric Pressure: N/A")

        # 将标签添加到布局中
        layout.addWidget(self.air_temp_label)
        layout.addWidget(self.air_hum_label)
        layout.addWidget(self.soil_temp_label)
        layout.addWidget(self.soil_hum_label)
        layout.addWidget(self.light_int_label)
        layout.addWidget(self.atm_press_label)

        self.setLayout(layout)

    def update_display(self):
        # 更新标签的文本以显示最新的数据
        self.air_temp_label.setText(f"Air Temperature: {self.data_model.air_temperature}")
        self.air_hum_label.setText(f"Air Humidity: {self.data_model.air_humidity}")
        self.soil_temp_label.setText(f"Soil Temperature: {self.data_model.soil_temperature}")
        self.soil_hum_label.setText(f"Soil Humidity: {self.data_model.soil_humidity}")
        self.light_int_label.setText(f"Light Intensity: {self.data_model.light_intensity}")
        self.atm_press_label.setText(f"Atmospheric Pressure: {self.data_model.atmospheric_pressure}")

    def update_data1(self):
        # 生成随机数据
        air_temp = random.uniform(0, 50)  # 假设空气温度在0到50度之间
        air_hum = random.uniform(0, 100)  # 假设空气湿度在0到100%之间
        soil_temp = random.uniform(0, 50)  # 假设空气湿度在0到100%之间
        soil_hum = random.uniform(0, 100)  # 假设空气湿度在0到100%之间
        light_int = random.uniform(0, 100)  # 假设空气湿度在0到100%之间
        atmospheric_press = random.uniform(0, 100)  # 假设空气湿度在0到100%之间
        # ...（为其他变量生成随机值）

        # 更新数据模型
        self.data_model.update_data(air_temp, air_hum, soil_temp, soil_hum, light_int, atmospheric_press)

        # 更新UI显示
        self.update_display()

    def start_timer(self):
        # 创建一个定时器，每1000毫秒（1秒）触发一次timeout信号
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data1)
        self.timer.start(1000)  # 启动定时器，每1秒触发一次


class ChartTest(QFrame):
    def __init__(self):
        super().__init__()
        self.verticalLayout = QVBoxLayout(self)
        self.chart = QChart()
        self.chart.setTitle("Temperature and Humidity Chart")
        # self.chart.setTheme(QChart.ChartThemeDark)
        # self.chart.setTitle("Temperature Chart")
        # self.chart.setAnimationOptions(QChart.SeriesAnimations)
        # self.chart.setAnimationDuration(1000)
        # self.series = QLineSeries()
        # self.series.setName("Temperature")
        # self.chart.addSeries(self.series)
        # self.series.append(0, 25)
        # self.chart.addSeries(self.series)
        # self.chart.legend().setVisible(True)
        # self.chart.legend().setAlignment(Qt.AlignBottom)

        # self.chart_view.setChart(self.chart)

        # self.line1 = QLineEdit()
        self.line1 = QLineSeries()
        # self.line2 = QLineSeries()
        # self.line1.setName("Temperature")
        # self.line2.setName("Humidity")
        #
        # self.chart.addSeries(self.line1)
        # self.chart.addSeries(self.line2)
        #
        # self.chart.createDefaultAxes()
        #
        # self.chart.setAxisX(QValueAxis(), self.line1)
        # self.chart.setAxisY(QValueAxis(), self.line1)
        #
        # self.chart.setAnimationDuration(1000)
        # self.chart.setAnimationOptions(QChart.SeriesAnimations)
        # self.chart.legend().setVisible(True)
        # self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chart.addSeries(self.line1)
        self.chart.createDefaultAxes()
        # self.chart.setAnimationDuration(1000)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)

        self.chart_view = QChartView(self.chart, self)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.verticalLayout.addWidget(self.chart_view)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(500)  # 每100毫秒触发一次，即10次/秒

    def update_data(self):
        print("update_data")
        # 生成一个新的正弦数据点
        x = self.line1.count()  # 使用系列中的点数作为x值
        y = math.sin(x / 10.0) * 50 + 50  # 调整正弦波幅值和偏移量以适配视图
        point = QPointF(x, y)

        # line1 QLineSeries
        self.line1.append(point)

        # 限制数据点数量，避免图表过于拥挤
        if self.line1.count() > 100:
            self.line1.removePoints(0, 1)  # 移除最旧的数据点

        # 刷新图表视图以显示更新后的数据
        self.chart_view.repaint()

    def update_chart(self):
        self.line1.append(QDateTime.currentDateTime().toMSecsSinceEpoch(), random.uniform(0, 50))
        self.chart.axisX().setRange(QDateTime.currentDateTime().addSecs(-10), QDateTime.currentDateTime())


class InfoWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.resize(1000, 600)
        self.layout_v = QVBoxLayout(self)
        self.layout_h = QHBoxLayout(self)
        self.splitter = QSplitter(self, Qt.Horizontal)
        # self.splitter1 = DeviceList()
        # self.splitter1.update_name_id("device1", 1)
        # self.splitter1 = SwitchButton()
        # self.splitter1 = dev("motor")
        self.splitter1 = DeviceList()
        # QAbstractButton(self)
        self.air_frame = BaseFrame("Air Temperature", "°C")
        self.soil_frame = BaseFrame("Soil Temperature", "°C")
        self.splitter.addWidget(self.air_frame)
        self.splitter.addWidget(self.soil_frame)

        self.port = WidgetSerial()
        self.chart = ChartTest()

        self.toolbox = QToolBox(self)
        self.toolbox.addItem(self.port, "数据收发")  # Serial Port
        self.toolbox.addItem(self.chart, "数据可视化")
        self.toolbox.addItem(self.splitter, "信息化管理")
        self.toolbox.addItem(self.splitter1, "数据分析与决策")
        # self.toolbox.addItem(self.air_frame, "Air Temperature")
        # self.toolbox.addItem(self.soil_frame, "Soil Temperature")
        # self.splitter.addWidget(self.toolbox)

        # self.layout_h.addWidget(self.toolbox)
        # self.layout_h.addWidget(self.splitter)
        self.layout_v.addWidget(self.toolbox)
        # self.layout_h.addWidget(self.toolbox, self.splitter)

        with open('theme/InfoWidget.qss', 'r') as file:
            self.setStyleSheet(file.read())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        chart = QChart()
        chart.setTitle("Two Lines Chart")

        # 准备数据
        axisX_date = [QDateTime.currentDateTime().addDays(i) for i in range(5)]
        axisY_value1 = [10 - 2 * i for i in range(5)]
        axisY_value2 = [5 + i * (-1) ** i for i in range(5)]

        series1 = QLineSeries()
        for i in range(5):
            series1.append(np.int64(axisX_date[i].toMSecsSinceEpoch()), axisY_value1[i])

        series2 = QLineSeries()
        for i in range(5):
            series2.append(np.int64(axisX_date[i].toMSecsSinceEpoch()), axisY_value2[i])

        # 将series添加到chart中
        chart.addSeries(series1)
        chart.addSeries(series2)

        # 创建x轴
        axisX = QDateTimeAxis()
        axisX.setFormat("yyyy/MM/dd")
        axisX.setTitleText("Date")
        axisX.setTickCount(5)
        axisX.setRange(QDateTime.currentDateTime(), QDateTime.currentDateTime().addDays(4))
        # 将x轴与chart和series绑定
        chart.addAxis(axisX, Qt.AlignBottom)
        series1.attachAxis(axisX)
        series2.attachAxis(axisX)

        # 创建y轴
        axisY = QValueAxis()
        axisY.setTitleText("Value")
        axisY.setRange(0, 10)
        # 将y轴与chart和series绑定
        chart.addAxis(axisY, Qt.AlignLeft)
        series1.attachAxis(axisY)
        series2.attachAxis(axisY)

        # 显示图表
        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        # window.setCentralWidget(chartView)
        self.setCentralWidget(chartView)


class SinWaveChart(QChart):
    def __init__(self):
        super().__init__()

        # 显示的时间范围
        self.t_range = 1
        self.Ts = 0.01

        # 创建一个序列
        self.series = QLineSeries()
        self.addSeries(self.series)

        # 创建坐标轴
        self.axisX_ = QValueAxis()
        self.axisY_ = QValueAxis()
        self.addAxis(self.axisX_, Qt.AlignBottom)
        self.addAxis(self.axisY_, Qt.AlignLeft)
        self.series.attachAxis(self.axisX_)
        self.series.attachAxis(self.axisY_)
        self.axisX_.setTickCount(11)

        # 初始化x的值
        self.x = 0

        # 设置y轴的范围
        self.axisX_.setMin(self.x)
        self.axisX_.setMax(self.t_range)
        self.axisY_.setMin(-1)
        self.axisY_.setMax(1)

        self.points = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimeout)
        self.timer.start(self.Ts * 1000)  # 更新频率60帧/秒

        self.resize(500, 500)

    def handleTimeout(self):
        y = math.sin(2 * np.pi * self.x)
        self.points.append(QPointF(self.x, y))  # 创建QPointF对象

        self.x += self.Ts

        if self.x > self.t_range:
            self.axisX_.setRange(self.x - self.t_range, self.x - self.Ts)
            self.points = self.points[-int(self.t_range / self.Ts):]

        self.series.replace(self.points)  # 使用replace()替换整个数据集


class BaseChart(QChart):
    def __init__(self, title=None, unit=None, x_max=100, time_step=1):
        super().__init__(None)
        # self.title = title
        self.setTitle(title)
        self.x_max = x_max
        self.Ts = time_step
        # 创建一个序列
        self.series = QLineSeries()
        self.addSeries(self.series)
        # 创建坐标轴
        self.axisX_ = QValueAxis()
        self.axisY_ = QValueAxis()
        self.addAxis(self.axisX_, Qt.AlignBottom)
        self.addAxis(self.axisY_, Qt.AlignLeft)
        self.series.attachAxis(self.axisX_)
        self.series.attachAxis(self.axisY_)
        self.axisX_.setTickCount(11)
        # 初始化x的值
        self.x = 0
        # 设置y轴的范围
        self.axisX_.setMin(self.x)
        self.axisX_.setMax(self.x_max)
        # self.axisY_.setMin(-1)
        # self.axisY_.setMax(1)
        self.points = []

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(100)

    def update_data(self):
        y = random.uniform(-1, 1.5)  # 随机生成一个数
        self.points.append(QPointF(self.x, y))  # 创建QPointF对象

        self.x += 1
        if self.x > self.x_max:
            self.axisX_.setRange(self.x - self.x_max, self.x - self.Ts)
            self.points = self.points[-int(self.x_max / self.Ts):]
        # self.axisY_.setRange(min(self.points, key=lambda p: p.y()).y() - 1, max(self.points, key=lambda p: p.y()).y() + 1)
        if self.axisY_.min() > y:
            self.axisY_.setMin(y)
        elif self.axisY_.max() < y:
            self.axisY_.setMax(y)
        self.series.replace(self.points)  # 使用replace()替换整个数据集


class PartChart(QFrame):
    def __init__(self):
        super().__init__()
        # self.chart = BaseChart("Temperature")
        self.chart = SinWaveChart()

        self.chart_view = QChartView(self.chart, self)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.chart_view)
        self.setLayout(self.layout)
        self.resize(800, 400)


# data = [
#     {'time': '2022-01-01 00:00:00', 'temperature': 25.0, 'humidity': 50.0},
#     {'time': '2022-01-01 00:01:00', 'temperature': 26.0, 'humidity': 51.0},
#     {'time': '2022-01-01 00:02:00', 'temperature': 27.0, 'humidity': 52.0},
#         self.ui.label_2.setText(str(self.air_temperature) + "°C")


class GlobalData:
    # https://blog.csdn.net/m0_48442491/article/details/128705183
    title = QObject.tr("物联网智慧蔬菜大棚管理系统", "Village Green System")
    icon_path = "img/hand-holding-seedling.svg"
    web_url = "http://192.168.52.133"  # 视频地址
    stream_url = 'http://192.168.52.133:81/stream'  # 视频流地址
    week = {"Mon": "星期一", "Tue": "星期二", "Wed": "星期三", "Thu": "星期四", "Fri": "星期五", "Sat": "星期六",
            "Sun": "星期日"}

    def __init__(self):
        pass

    class EnvironmentalData:
        def __init__(self):
            self.air_humidity = 0.0
            self.air_temperature = 0.0
            self.soil_humidity = 0.0
            self.soil_temperature = 0.0
            self.water_pump_status = 0
            self.fan_status = 0
            self.light_status = 0
            self.air_humidity_status = 0
            self.soil_humidity_status = 0
            self.air_temperature_status = 0
            self.soil_temperature_status = 0
            self.water_pump_status_str = "关闭"
            self.fan_status_str = "关闭"
            self.light_status_str = "关闭"
            self.air_humidity_status_str = "正常"
            self.soil_humidity_status_str = "正常"
            self.air_temperature_status_str = "正常"
            self.soil_temperature_status_str = "正常"
            self.air_humidity_warning = 0
            self.soil_humidity_warning = 0
            self.air_temperature_warning = 0

    def update_data(self):
        pass

    def create_json(self):
        pass


class PageManage(QFrame):
    def __init__(self, parent_obj=None):
        super().__init__()
        self.page = Ui_Form()
        self.page.setupUi(self)
        # self.chart = MainWindow()
        # self.setLayout(QGridLayout(self))
        # self.layout().addWidget(self.chart)


class MainWidget(QFrame, PartAnimation):
    def __init__(self):
        super().__init__()
        self.global_data = GlobalData()
        self.setWindowTitle(self.global_data.title)
        self.setWindowIcon(gf_to_icon(self.global_data.icon_path))
        # apply_stylesheet(self, theme='theme/dark.xml')
        # apply_stylesheet(self, theme='theme/light.xml')
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.page_left = PageLeft(self)     # 46 32
        self.page_communication = PageCommunication(self)
        self.page_data_view = PageDataView(self)
        self.page_data_analysis = PageDataAnalysis(self)
        self.page_manage = PageManage(self)
        self.stacked_pages = QStackedWidget(self)
        self.stacked_pages.addWidget(self.page_communication)
        self.stacked_pages.addWidget(self.page_data_view)
        self.stacked_pages.addWidget(self.page_data_analysis)
        self.stacked_pages.addWidget(self.page_manage)
        self.page_left.page_index_changed.connect(self.stacked_pages.setCurrentIndex)  # 将左、右侧页面的切换信号作关联
        layout = QHBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(3, 0, 0, 0)
        layout.addWidget(self.page_left)
        layout.addWidget(self.stacked_pages)
        self.resize(1280, 720)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_F2:
            if self.page_left.isHidden():
                self.page_left.show()
            else:
                self.page_left.setHidden(True)

    # def showEvent(self, event) -> None:
    #     self.show_animation()
    #
    # def closeEvent(self, event):
    #     self.close_animation(event)


# print(''.join([str1, str2]))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())
