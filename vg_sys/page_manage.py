from import_modules import *
from ui.ui_page_dev import *
from py_gf.render_svg_to_pixmap import gf_to_icon


class PageManage(QFrame):
    thresholds = Signal(list)

    def __init__(self, parent_obj=None):
        super().__init__()
        self.page = Ui_Form()
        self.page.setupUi(self)
        self.page.label_img_waterPump.setPixmap(gf_to_icon("img/水泵.svg", QSize(50, 50)))
        self.page.label_img_fan.setPixmap(gf_to_icon("img/fan.svg", QSize(50, 50)))
        self.page.label_img_light.setPixmap(gf_to_icon("img/lightbulb-idea-person.svg", QSize(50, 50)))
        self.page.label_img_InsectKillingLamp.setPixmap(gf_to_icon("img/杀虫灯.svg", QSize(50, 50)))
        self.page.label_img_beep.setPixmap(gf_to_icon("img/报警器.svg", QSize(50, 50)))

        self.page.spinBox_max_waterPump.setRange(0, 100)
        self.page.spinBox_max_fan.setRange(0, 50)
        self.page.spinBox_max_light.setRange(0, 3500)
        self.page.spinBox_max_InsectKillingLamp.setRange(0, 100)
        self.page.spinBox_max_beep.setRange(0, 100)

        self.page.horizontalSlider_waterPump.setRange(self.page.spinBox_max_waterPump.minimum(), self.page.spinBox_max_waterPump.maximum())
        self.page.horizontalSlider_fan.setRange(0, 50)
        self.page.horizontalSlider_light.setRange(0, 3500)
        self.page.horizontalSlider_InsectKillingLamp.setRange(0, 100)
        self.page.horizontalSlider_beep.setRange(0, 100)

        self.page.spinBox_max_waterPump.setValue(100)
        self.page.spinBox_max_fan.setValue(50)
        self.page.spinBox_max_light.setValue(3500)
        self.page.spinBox_max_InsectKillingLamp.setValue(100)
        self.page.spinBox_max_beep.setValue(100)

        self.page.horizontalSlider_waterPump.setValue(20)
        self.page.horizontalSlider_fan.setValue(33)
        self.page.horizontalSlider_light.setValue(500)
        self.page.horizontalSlider_InsectKillingLamp.setValue(0)
        self.page.horizontalSlider_beep.setValue(0)

        self.page.comboBox_waterPump.setCurrentIndex(4)  # 下拉框默认选项
        self.page.comboBox_fan.setCurrentIndex(1)
        self.page.comboBox_light.setCurrentIndex(5)
        self.page.comboBox_InsectKillingLamp.setCurrentIndex(6)
        self.page.comboBox_beep.setCurrentIndex(0)

        self.page.horizontalSlider_waterPump.valueChanged.connect(self.slider_value_changed)
        self.page.horizontalSlider_fan.valueChanged.connect(self.slider_value_changed)
        self.page.horizontalSlider_light.valueChanged.connect(self.slider_value_changed)
        self.page.horizontalSlider_InsectKillingLamp.valueChanged.connect(self.slider_value_changed)
        self.page.horizontalSlider_beep.valueChanged.connect(self.slider_value_changed)

        self.page.horizontalSlider_waterPump.setPageStep(1)  # 滚轮增减步长
        self.page.horizontalSlider_fan.setPageStep(1)
        self.page.horizontalSlider_light.setPageStep(1)
        self.page.horizontalSlider_InsectKillingLamp.setPageStep(1)
        self.page.horizontalSlider_beep.setPageStep(1)

        self.threshold_list = []

    def slider_value_changed(self):
        self.threshold_list.clear()
        self.threshold_list.append(self.page.horizontalSlider_fan.value())
        self.threshold_list.append(self.page.horizontalSlider_waterPump.value())
        self.threshold_list.append(self.page.horizontalSlider_light.value())
        self.threshold_list.append(self.page.horizontalSlider_InsectKillingLamp.value())
        self.threshold_list.append(self.page.horizontalSlider_beep.value())
        self.thresholds.emit(self.threshold_list)
