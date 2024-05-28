from import_modules import *
from ui.ui_page_chart import *
from py_gf.render_svg_to_pixmap import gf_to_icon


class PageDataView(QFrame):
    dev_message = Signal(str)
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
            # self.setAutoFillBackground(True)

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

        def mousePressEvent(self, event):
            # Ctrl+左键点击 显示图片
            if event.button() == Qt.LeftButton and event.modifiers() & Qt.ControlModifier:
                dialog = QDialog()  # 创建一个临时对话框来显示QLabel
                label = QLabel(dialog)    # 创建一个QLabel来显示图片
                label.setPixmap(QPixmap("img/PixPin.png"))
                layout = QVBoxLayout(dialog)
                layout.addWidget(label)
                dialog.exec()  # 显示对话框，等待用户关闭
            super().mousePressEvent(event)  # 确保其他事件处理正常进行

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
        self.data_view.label_img_InsectKillingLamp.setPixmap(gf_to_icon("img/杀虫灯.svg", QSize(50, 50)))
        self.data_view.label_img_beep.setPixmap(gf_to_icon("img/报警器.svg", QSize(50, 50)))
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

        self.data_view.button_fan.animation.finished.connect(lambda: self.send_command(self.data_view.button_fan))
        self.data_view.button_waterPump.animation.finished.connect(lambda: self.send_command(self.data_view.button_waterPump))
        self.data_view.button_light.animation.finished.connect(lambda: self.send_command(self.data_view.button_light))
        self.data_view.button_InsectKillingLamp.animation.finished.connect(lambda: self.send_command(self.data_view.button_InsectKillingLamp))
        self.data_view.button_beep.animation.finished.connect(lambda: self.send_command(self.data_view.button_beep))
        self.data_view.pushButton_ctrl.clicked.connect(lambda: self.send_command(self.data_view.pushButton_ctrl))
        self.pushButton_ctrl_state = False  # default state of pushButton_ctrl: auto mode
        self.dev_info_list = [0, 0, 0, 0, 0, 0, 33, 20, 500, 0]  # en, s1, s2, s3, s4, s5, at, ah, li, ap
        # self.dev_message.connect(lambda msg: print("msg: " + msg))

        def generate_random_points(num_points=100, x_range=(-100, 100), y_range=(-100, 100)):
            # 生成100个随机QPointF的列表
            points = [QPointF(random.uniform(x_range[0], x_range[1]), random.uniform(y_range[0], y_range[1]))
                      for _ in range(num_points)]
            return points

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

    def send_command(self, obj: QObject):
        if obj.objectName() == "pushButton_ctrl":
            self.pushButton_ctrl_state = not self.pushButton_ctrl_state
            self.data_view.pushButton_ctrl.setText("当前模式: 手动" if self.pushButton_ctrl_state else "当前模式: 自动")
            self.dev_info_list[0] = 1 if self.pushButton_ctrl_state else 0
        else:
            names = ["pushButton_ctrl", "button_waterPump", "button_fan", "button_light", "button_InsectKillingLamp", "button_beep"]
            try:
                index = names.index(obj.objectName())
                self.dev_info_list[index] = 1 if obj.checked else 0
            except ValueError:
                pass
            # self.dev_info_list[int(obj.objectName().split("_")[1])] = obj.checked()  # name: button_1 -> 1
            formatted_lst = [int(i) if isinstance(i, bool) else str(i) for i in self.dev_info_list]  # 格式化数据
            formatted_str = ';'.join(formatted_lst)  # 使用分号作为分隔符连接字符串
            formatted_str += ';'
            self.dev_message.emit(formatted_str)

    def update_thresholds(self, data):
        self.dev_info_list[6: 9] = data[0: 3]  # at, ah, li
        print(self.dev_info_list)

    def update_time(self):
        self.data_view.label_time_date.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd"))
        self.data_view.label_time_time.setText(QDateTime.currentDateTime().toString("hh:mm:ss A"))
        self.data_view.label_time_week.setText(self.week[QDateTime.currentDateTime().toString("ddd")])

    def update_data_view(self, json_dict: dict):
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
