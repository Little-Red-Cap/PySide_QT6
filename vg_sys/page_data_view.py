from import_modules import *
from ui.ui_page_chart import *
from py_gf.render_svg_to_pixmap import gf_to_icon

#1;0;0;1;1;1;33;44;55;66;
class PageDataView(QFrame):
    week = {"Mon": "星期一", "Tue": "星期二", "Wed": "星期三", "Thu": "星期四", "Fri": "星期五", "Sat": "星期六", "Sun": "星期日"}

    class ChartTemp(QChart):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setAnimationOptions(QChart.SeriesAnimations)  # 开启动画效果
            self.setAnimationDuration(1000)  # 动画持续时间
            # 创建X坐标轴
            self.axisX_ = QDateTimeAxis(self)   # 时间轴
            # self.axisX_.setRange(QDateTime.currentDateTime().addSecs(-3600 * 24), QDateTime.currentDateTime())
            self.axisX_.setRange(QDateTime.currentDateTime().addSecs(-36), QDateTime.currentDateTime())
            self.axisX_.setMinorGridLineVisible(True)  # 显示小网格线
            self.axisX_.setGridLineVisible(True)       # 显示大网格线
            self.axisX_.setTickCount(11)  # 11个刻度
            self.axisX_.setFormat("hh:mm:ss")
            self.axisX_.setLabelsAngle(30)  # 标签倾斜角度
            # 创建Y坐标轴
            self.axisY_ = QValueAxis(self)
            self.axisY_.setRange(-20, 50)  # 范围
            self.axisY_.setMinorGridLineVisible(True)  # 显示小网格线
            self.axisY_.setGridLineVisible(True)       # 显示大网格线
            self.addAxis(self.axisX_, Qt.AlignBottom)
            self.addAxis(self.axisY_, Qt.AlignLeft)

            # 创建序列
            self.series_at = QLineSeries(self, name="空气温度")
            self.addSeries(self.series_at)
            self.series_at.attachAxis(self.axisX_)    # 绑定X轴
            self.series_at.attachAxis(self.axisY_)    # 绑定Y轴
            self.points_at = []

            self.series_st = QLineSeries(self, name="土壤温度")
            self.addSeries(self.series_st)
            self.series_st.attachAxis(self.axisX_)    # 绑定X轴
            self.series_st.attachAxis(self.axisY_)    # 绑定Y轴
            self.points_st = []

        def update_data(self, json_dict):
            at = json_dict.get('environment', {}).get('airTemperature', 0)
            st = json_dict.get('environment', {}).get('soilTemperature', 0)
            self.points_st.append(QPointF(QDateTime.currentDateTime().toMSecsSinceEpoch(), st))
            self.series_st.replace(self.points_st)
            # self.series_st.append(self.points_st)
            self.points_at.append(QPointF(QDateTime.currentDateTime().toMSecsSinceEpoch(), at))
            self.series_at.replace(self.points_at)
            self.axisX_.setRange(QDateTime.currentDateTime().addSecs(-36), QDateTime.currentDateTime())

    class ChartHum(QChart):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setAnimationOptions(QChart.SeriesAnimations)  # 开启动画效果
            self.setAnimationDuration(1000)  # 动画持续时间
            # 创建X坐标轴
            self.axisX = QDateTimeAxis(self)   # 时间轴
            # self.axisX_.setRange(QDateTime.currentDateTime().addSecs(-3600 * 24), QDateTime.currentDateTime())
            self.axisX.setRange(QDateTime.currentDateTime().addSecs(-360), QDateTime.currentDateTime())
            self.axisX.setMinorGridLineVisible(True)  # 显示小网格线
            self.axisX.setGridLineVisible(True)       # 显示大网格线
            self.axisX.setTickCount(11)  # 11个刻度
            self.axisX.setFormat("hh:mm:ss")
            self.axisX.setLabelsAngle(30)  # 标签倾斜角度
            # 创建Y坐标轴
            self.axisY = QValueAxis(self)
            self.axisY.setRange(0, 100)  # 范围
            self.axisY.setMinorGridLineVisible(True)  # 显示小网格线
            self.axisY.setGridLineVisible(True)       # 显示大网格线
            self.addAxis(self.axisX, Qt.AlignBottom)
            self.addAxis(self.axisY, Qt.AlignLeft)

            # 创建序列
            self.series_ah = QLineSeries(self, name="空气湿度")
            self.addSeries(self.series_ah)
            self.series_ah.attachAxis(self.axisX)    # 绑定X轴
            self.series_ah.attachAxis(self.axisY)    # 绑定Y轴
            self.points_ah = []

            self.series_sh = QLineSeries(self, name="土壤湿度")
            self.addSeries(self.series_sh)
            self.series_sh.attachAxis(self.axisX)    # 绑定X轴
            self.series_sh.attachAxis(self.axisY)    # 绑定Y轴
            self.points_sh = []

        def update_data(self, json_dict):
            ah = json_dict.get('environment', {}).get('airHumidity', 0)
            self.points_ah.append(QPointF(QDateTime.currentDateTime().toMSecsSinceEpoch(), ah))
            self.series_ah.replace(self.points_ah)
            sh = json_dict.get('environment', {}).get('soilHumidity', 0)
            self.points_sh.append(QPointF(QDateTime.currentDateTime().toMSecsSinceEpoch(), sh))
            self.series_sh.replace(self.points_sh)
            self.axisX.setRange(QDateTime.currentDateTime().addSecs(-36), QDateTime.currentDateTime())


    def __init__(self, parent):
        super().__init__()
        self.data_view = Ui_data_view()
        self.data_view.setupUi(self)
        self.data_view.label_img_at.setPixmap(gf_to_icon("img/大气温度.svg", QSize(50, 50)))
        self.data_view.label_img_ah.setPixmap(gf_to_icon("img/大气湿度.svg", QSize(50, 50)))
        self.data_view.label_img_st.setPixmap(gf_to_icon("img/土壤温度.svg", QSize(50, 50)))
        self.data_view.label_img_sh.setPixmap(gf_to_icon("img/土壤湿度.svg", QSize(50, 50)))
        self.data_view.label_img_dev1.setPixmap(gf_to_icon("img/水泵.svg", QSize(50, 50)))
        self.data_view.label_img_dev2.setPixmap(gf_to_icon("img/fan.svg", QSize(50, 50)))
        self.data_view.label_img_dev3.setPixmap(gf_to_icon("img/fan.svg", QSize(50, 50)))
        self.data_view.label_img_dev4.setPixmap(gf_to_icon("img/fan.svg", QSize(50, 50)))
        self.data_view.label_img_li.setPixmap(gf_to_icon("img/lighting.svg", QSize(50, 50)))
        self.data_view.label_img_ap.setPixmap(gf_to_icon("img/大气压力.svg", QSize(60, 60)))
        self.data_view.label_time_img.setPixmap(gf_to_icon("img/calendar-date.svg", QSize(50, 50)))

        self.chart_temp = self.ChartTemp()
        self.data_view.graphicsView_t.setChart(self.chart_temp)
        self.data_view.graphicsView_t.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        # self.data_view.graphicsView_h.setChart(PageManage())
        self.chart_hum = self.ChartHum()
        self.data_view.graphicsView_h.setChart(self.chart_hum)
        self.data_view.graphicsView_h.setRenderHint(QPainter.Antialiasing)  # 抗锯齿

        #动态列表
        #https://www.bilibili.com/read/cv34228805/

        with open('theme/bgColor.qss', 'r') as file:
            style_sheet = file.read()
            # self.setStyleSheet(style_sheet)

        with open('theme/BaseFrame.qss', 'r') as file:
            style_sheet = file.read()
            # self.setStyleSheet(style_sheet)
            self.data_view.widget_2.setStyleSheet(style_sheet)
            self.data_view.widget.setStyleSheet(style_sheet)
            self.data_view.widget_3.setStyleSheet(style_sheet)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # 1000ms = 1s
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    def update_time(self):
        self.data_view.label_time_date.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd"))
        self.data_view.label_time_time.setText(QDateTime.currentDateTime().toString("hh:mm:ss A"))
        self.data_view.label_time_week.setText(self.week[QDateTime.currentDateTime().toString("ddd")])

    def update_data_view(self, json_dict):
        self.data_view.label_val_at.setText(str(json_dict.get('environment', {}).get('airTemperature', '')) + '°C')
        self.data_view.label_val_ah.setText(str(json_dict.get('environment', {}).get('airHumidity', '')) + '%RH')
        self.data_view.label_val_st.setText(str(json_dict.get('environment', {}).get('soilTemperature', '')) + '°C')
        self.data_view.label_val_sh.setText(str(json_dict.get('environment', {}).get('soilHumidity', '')) + '%RH')
        self.data_view.label_val_ap.setText(str(json_dict.get('environment', {}).get('airPressure', '')) + 'hPa')
        self.data_view.label_val_li.setText(str(json_dict.get('environment', {}).get('lightIntensity', '')) + 'lx')
        self.data_view.label_state_dev1.setText(str(json_dict.get('devices', {}).get('waterPump', {}).get('status', '')))
        self.data_view.label_state_dev2.setText(str(json_dict.get('devices', {}).get('fan', {}).get('status', '')))
        self.data_view.label_state_dev3.setText(str(json_dict.get('devices', {}).get('light', {}).get('status', '')))
        self.data_view.label_state_dev4.setText(str(json_dict.get('devices', {}).get('InsectKillingLamp', {}).get('status', '')))
        self.chart_temp.update_data(json_dict)
        self.chart_hum.update_data(json_dict)

    def update_chart(self, data):
        pass
