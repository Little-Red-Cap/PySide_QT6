from import_modules import *
from ui.ui_page_chart import *
from py_gf.render_svg_to_pixmap import gf_to_icon


class PageDataView(QWidget):
    def __init__(self, parent_obj=None):
        super().__init__()
        self.parent_obj = parent_obj
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
        # current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss A")
        # self.data_view.label_time.setText(current_time)
        self.data_view.label_time_date.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd"))
        self.data_view.label_time_time.setText(QDateTime.currentDateTime().toString("hh:mm:ss A"))
        self.data_view.label_time_week.setText(self.parent_obj.global_data.week[QDateTime.currentDateTime().toString("ddd")])
