from import_modules import *
from ui.ui_page_chart import *
from py_gf.render_svg_to_pixmap import gf_to_icon


class PageDataView(QFrame):
    week = {"Mon": "星期一", "Tue": "星期二", "Wed": "星期三", "Thu": "星期四", "Fri": "星期五", "Sat": "星期六", "Sun": "星期日"}

    def __init__(self, parent):
        super().__init__()
        # self.chart = PartChart()
        # self.setLayout(QGridLayout(self))
        # self.layout().addWidget(self.chart)
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

        # TODO: 实现数据联动
        # self.data_view.graphicsView_t.setChart(SinWaveChart())
        # self.data_view.graphicsView_h.setChart(SinWaveChart())
        # self.data_view.graphicsView_h.setChart(PageManage())

        #动态列表
        #https://www.bilibili.com/read/cv34228805/

        with open('theme/bgColor.qss', 'r') as file:
            style_sheet = file.read()
            self.setStyleSheet(style_sheet)

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
