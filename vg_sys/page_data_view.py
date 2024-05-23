from import_modules import *
from ui.ui_page_chart import *
from py_gf.render_svg_to_pixmap import gf_to_icon

#1;0;0;1;1;1;33;44;55;66;
class PageDataView(QFrame):
    week = {"Mon": "星期一", "Tue": "星期二", "Wed": "星期三", "Thu": "星期四", "Fri": "星期五", "Sat": "星期六", "Sun": "星期日"}

    class BaseChart(QChart):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setAnimationOptions(QChart.SeriesAnimations)  # 开启动画效果
            self.setAnimationDuration(1000)  # 动画持续时间
            self.tick_x = 36    # 时间轴刻度间隔, -3600 * 24
            # 创建X坐标轴
            self.axisX = QDateTimeAxis(self)   # 时间轴
            self.axisX.setRange(QDateTime.currentDateTime().addSecs(-self.tick_x), QDateTime.currentDateTime())
            self.axisX.setMinorGridLineVisible(True)  # 显示小网格线
            self.axisX.setGridLineVisible(True)       # 显示大网格线
            self.axisX.setTickCount(11)  # 11个刻度
            self.axisX.setFormat("mm:ss")
            self.axisX.setLabelsAngle(30)  # 标签倾斜角度
            # 创建Y坐标轴
            self.axisY = QValueAxis(self)
            # self.axisY.setRange(-20, 50)  # 范围
            self.axisY.setMinorGridLineVisible(True)  # 显示小网格线
            self.axisY.setGridLineVisible(True)       # 显示大网格线
            self.addAxis(self.axisX, Qt.AlignBottom)
            self.addAxis(self.axisY, Qt.AlignLeft)
            self.points = []

        def wheelEvent(self, event: QGraphicsSceneWheelEvent):
            if event.modifiers() & Qt.ControlModifier:  # 检查是否按下了Ctrl键
                if event.delta() > 0:  # 向上滚动
                    self.zoomIn()
                else:  # 向下滚动
                    self.zoomOut()
            # super().wheelEvent(event)   # 不传递给父类，避免滚轮事件影响父控件

    class ChartTemp(BaseChart):
        def __init__(self, parent=None):
            super().__init__(parent)
            # 创建序列
            self.series_at = QSplineSeries(self, name="空气温度")
            self.addSeries(self.series_at)
            self.series_at.attachAxis(self.axisX)    # 绑定X轴
            self.series_at.attachAxis(self.axisY)    # 绑定Y轴

            self.series_st = QSplineSeries(self, name="土壤温度")
            self.addSeries(self.series_st)
            self.series_st.attachAxis(self.axisX)    # 绑定X轴
            self.series_st.attachAxis(self.axisY)    # 绑定Y轴

        def update_data(self, json_dict):
            at = json_dict.get('environment', {}).get('airTemperature', 0)
            st = json_dict.get('environment', {}).get('soilTemperature', 0)
            self.points.append(at)
            self.points.append(st)
            self.series_at.append(QPointF(QDateTime.currentDateTime().toMSecsSinceEpoch(), at))
            self.series_st.append(QPointF(QDateTime.currentDateTime().toMSecsSinceEpoch(), st))
            self.axisX.setRange(QDateTime.currentDateTime().addSecs(-36), QDateTime.currentDateTime())
            self.axisY.setRange(min(self.points) * 0.95, max(self.points) * 1.05)
            if len(self.points) > self.tick_x * 2:  # 乘2是因为有两个序列
                self.points.pop(0)  # 删掉第一个数据点，保持数据点数为tick_x的倍数
                self.points.pop(0)  # 索引会变，所以删掉索引为0的点

    class ChartHum(BaseChart):
        def __init__(self, parent=None):
            super().__init__(parent)
            # 创建序列
            self.series_ah = QSplineSeries(self, name="空气湿度")
            self.addSeries(self.series_ah)
            self.series_ah.attachAxis(self.axisX)    # 绑定X轴
            self.series_ah.attachAxis(self.axisY)    # 绑定Y轴

            self.series_sh = QSplineSeries(self, name="土壤湿度")
            self.addSeries(self.series_sh)
            self.series_sh.attachAxis(self.axisX)    # 绑定X轴
            self.series_sh.attachAxis(self.axisY)    # 绑定Y轴

        # TODO: 图像Y轴的自动缩放，有点提前，导致波形峰值会上移，显示不全
        def update_data(self, json_dict):
            ah = json_dict.get('environment', {}).get('airHumidity', 0)
            sh = json_dict.get('environment', {}).get('soilHumidity', 0)
            self.points.append(ah)
            self.points.append(sh)
            self.series_ah.append(QPointF(QDateTime.currentDateTime().toMSecsSinceEpoch(), ah))
            self.series_sh.append(QPointF(QDateTime.currentDateTime().toMSecsSinceEpoch(), sh))
            self.axisX.setRange(QDateTime.currentDateTime().addSecs(-36), QDateTime.currentDateTime())
            self.axisY.setRange(min(self.points) * 0.95, max(self.points) * 1.05)
            # print(len(self.points))
            if len(self.points) > self.tick_x * 2:
                self.points.pop(0)  # 删掉第一个数据点，保持数据点数为tick_x的倍数
                self.points.pop(0)  # 索引会变，所以删掉索引为0的点

    class ChartLight(BaseChart):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.series_li = QSplineSeries(self, name="光照强度")
            self.series_li.dynamicPropertyNames()
            self.axisX.hide()
            self.axisY.setGridLineVisible(False)
            self.addSeries(self.series_li)
            self.series_li.attachAxis(self.axisX)    # 绑定X轴
            self.series_li.attachAxis(self.axisY)    # 绑定Y轴

        def update_data(self, json_dict):
            li = json_dict.get('environment', {}).get('lightIntensity', 0)
            self.points.append(li)
            self.series_li.append(QPointF(QDateTime.currentDateTime().toMSecsSinceEpoch(), float(li)))
            self.axisX.setRange(QDateTime.currentDateTime().addSecs(-36), QDateTime.currentDateTime())
            self.axisY.setRange(min(self.points) * 0.95, max(self.points) * 1.05)
            if len(self.points) > self.tick_x * 2:  # 乘2是因为有两个序列
                self.points.pop(0)  # 删掉第一个数据点，保持数据点数为tick_x的倍数

    class ChartPressure(BaseChart):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.series_ap = QSplineSeries(self, name="大气压力")
            self.axisX.hide()
            self.axisY.setGridLineVisible(False)
            self.addSeries(self.series_ap)
            self.series_ap.attachAxis(self.axisX)    # 绑定X轴
            self.series_ap.attachAxis(self.axisY)    # 绑定Y轴

        def update_data(self, json_dict):
            ap = json_dict.get('environment', {}).get('airPressure', 0)
            self.points.append(ap)
            self.series_ap.append(QPointF(QDateTime.currentDateTime().toMSecsSinceEpoch(), float(ap)))
            self.axisX.setRange(QDateTime.currentDateTime().addSecs(-36), QDateTime.currentDateTime())
            self.axisY.setRange(min(self.points) * 0.95, max(self.points) * 1.05)
            if len(self.points) > self.tick_x * 2:  # 乘2是因为有两个序列
                self.points.pop(0)  # 删掉第一个数据点，保持数据点数为tick_x的倍数

    def __init__(self, parent):
        super().__init__(parent)
        self.data_view = Ui_data_view()
        self.data_view.setupUi(self)
        self.data_view.label_img_at.setPixmap(gf_to_icon("img/大气温度.svg", QSize(50, 50)))
        self.data_view.label_img_ah.setPixmap(gf_to_icon("img/大气湿度.svg", QSize(50, 50)))
        self.data_view.label_img_st.setPixmap(gf_to_icon("img/土壤温度.svg", QSize(50, 50)))
        self.data_view.label_img_sh.setPixmap(gf_to_icon("img/土壤湿度.svg", QSize(50, 50)))
        self.data_view.label_img_waterPump.setPixmap(gf_to_icon("img/水泵.svg", QSize(50, 50)))
        self.data_view.label_img_fan.setPixmap(gf_to_icon("img/fan.svg", QSize(50, 50)))
        self.data_view.label_img_light.setPixmap(gf_to_icon("img/lightbulb-idea-person.svg", QSize(50, 50)))
        self.data_view.label_img_InsectKillingLamp.setPixmap(gf_to_icon("img/fan.svg", QSize(50, 50)))
        self.data_view.label_img_beep.setPixmap(gf_to_icon("img/fan.svg", QSize(50, 50)))
        self.data_view.label_img_li.setPixmap(gf_to_icon("img/lighting.svg", QSize(50, 50)))
        self.data_view.label_img_ap.setPixmap(gf_to_icon("img/大气压力.svg", QSize(60, 60)))
        self.data_view.label_time_img.setPixmap(gf_to_icon("img/calendar-date.svg", QSize(50, 50)))

        self.chart_temp = self.ChartTemp()
        self.data_view.graphicsView_t.setChart(self.chart_temp)
        self.data_view.graphicsView_t.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.chart_hum = self.ChartHum()
        self.data_view.graphicsView_h.setChart(self.chart_hum)
        self.data_view.graphicsView_h.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.chart_light = self.ChartLight()
        self.data_view.graphicsView_li.setChart(self.chart_light)
        self.data_view.graphicsView_li.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.chart_pressure = self.ChartPressure()
        self.data_view.graphicsView_ap.setChart(self.chart_pressure)
        self.data_view.graphicsView_ap.setRenderHint(QPainter.Antialiasing)  # 抗锯齿

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
        self.data_view.label_val_at.setText(f"{json_dict.get('environment', {}).get('airTemperature', ''):.2f}°C")
        self.data_view.label_val_ah.setText(f"{json_dict.get('environment', {}).get('airHumidity', ''):.2f}%RH")
        self.data_view.label_val_st.setText(f"{json_dict.get('environment', {}).get('soilTemperature', ''):.2f}°C")
        self.data_view.label_val_sh.setText(f"{json_dict.get('environment', {}).get('soilHumidity', ''):.2f}%RH")
        self.data_view.label_val_ap.setText(f"{json_dict.get('environment', {}).get('airPressure', ''):.2f}hPa")
        self.data_view.label_val_li.setText(f"{json_dict.get('environment', {}).get('lightIntensity', ''):.2f}lx")
        self.data_view.label_state_waterPump.setText(str(json_dict.get('devices', {}).get('waterPump', {}).get('status', '')).upper())
        self.data_view.label_state_fan.setText(str(json_dict.get('devices', {}).get('fan', {}).get('status', '')).upper())
        self.data_view.label_state_light.setText(str(json_dict.get('devices', {}).get('light', {}).get('status', '')).upper())
        self.data_view.label_state_InsectKillingLamp.setText(str(json_dict.get('devices', {}).get('InsectKillingLamp', {}).get('status', '')).upper())
        self.data_view.label_state_beep.setText(str(json_dict.get('devices', {}).get('beep', {}).get('status', '')).upper())
        self.chart_temp.update_data(json_dict)
        self.chart_hum.update_data(json_dict)
        self.chart_light.update_data(json_dict)
        self.chart_pressure.update_data(json_dict)

    def update_chart(self, data):
        pass
