# This Python file uses the following encoding: utf-8
from import_modules import *

from part_animation import *
from page_left import *
from page_communi import *
from page_data_analysis import *
from page_data_view import *
from page_manage import *

# from ultralytics import YOLO
# model = YOLO('yolov8n.pt')


# data = [
#     {'time': '2022-01-01 00:00:00', 'temperature': 25.0, 'humidity': 50.0},
#     {'time': '2022-01-01 00:01:00', 'temperature': 26.0, 'humidity': 51.0},
#     {'time': '2022-01-01 00:02:00', 'temperature': 27.0, 'humidity': 52.0},


class GlobalData:
    web_url = "http://192.168.65.133"  # 视频地址
    stream_url = 'http://192.168.65.133:81/stream'  # 视频流地址
    items = {}

    def update_josn_data(self, json_data):
        # json_string = json.dumps(self.items, indent=4)  # 字典转字符串
        self.items = json.loads(json_data)  # 字符串转字典
        temperature = self.items['environment']['airTemperature']
        print(f"air temperature: {temperature}°C")
        # humidity = self.items['environment']['airHumidity']


class MainWidget(QFrame, PartAnimation):
    # https://doc.qt.io/qt-6/qt.html
    # https://doc.qt.io/qtforpython-6/
    # https://blog.csdn.net/eiilpux17/article/details/124776295
    # https://blog.csdn.net/m0_48442491/article/details/128705183
    # https://blog.csdn.net/GoForwardToStep/article/details/68938965
    title = QObject.tr("物联网智慧蔬菜大棚管理系统", "Village Green System")
    icon_path = "img/hand-holding-seedling.svg"

    def __init__(self):
        super().__init__()
        self.global_data = GlobalData()
        self.setWindowTitle(self.title)
        self.setWindowIcon(gf_to_icon(self.icon_path))
        # apply_stylesheet(self, theme='theme/dark.xml')
        # apply_stylesheet(self, theme='theme/light.xml')
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
        # self.page_communication.update_json.connect(self.global_data.update_josn_data)  # 接收Json数据
        self.page_communication.json_dict.connect(self.page_data_view.update_data_view)
        self.page_data_view.dev_message.connect(self.page_communication.send_data)
        layout = QHBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(3, 0, 0, 0)
        layout.addWidget(self.page_left)
        layout.addWidget(self.stacked_pages)
        self.resize(1280, 720)
        self.opacity_value = 1.0  # 初始值
        self.opacity_step = 0.01  # 步长
        self.window_infos = []
        self.stacked_pages.setCurrentIndex(1)
        self.is_on_top = False
        self.show_event_flag = False

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_F10:
            self.is_on_top = not self.is_on_top
            self.setWindowFlag(Qt.WindowStaysOnTopHint, self.is_on_top)
            self.show()

        if event.key() == Qt.Key_F12:
            if self.page_left.isHidden() and self.isFullScreen():
                self.page_left.show()
                self.setWindowState(self.window_infos[0])
                self.setWindowFlags(self.window_infos[1])
                self.show()
            else:
                self.page_left.setHidden(True)
                self.window_infos = [self.windowState(), self.windowFlags()]
                # self.setWindowState(Qt.WindowNoState)  # 隐藏状态栏
                self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
                self.showFullScreen()
        if event.modifiers() & Qt.ControlModifier and event.key() == Qt.Key_Tab:
            self.stacked_pages.setCurrentIndex((self.stacked_pages.currentIndex() + 1) % self.stacked_pages.count())
        elif event.modifiers() & Qt.ControlModifier and event.key() == Qt.Key_QuoteLeft:
            self.page_left.show() if self.page_left.isHidden() else self.page_left.setHidden(True)
        else:
            super().keyPressEvent(event)

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() & Qt.ControlModifier:  # 检查是否按下了Ctrl键
            if event.angleDelta().y() > 0:  # 向上滚动
                if self.opacity_value < 1.0:
                    self.opacity_value += self.opacity_step
                    self.opacity_value = min(self.opacity_value, 1.0)  # 确保值不超过1.0
            else:  # 向下滚动
                if self.opacity_value > 0.01:
                    self.opacity_value -= self.opacity_step
                    self.opacity_value = max(self.opacity_value, 0.01)  # 确保值不小于0.
            self.setWindowOpacity(self.opacity_value)
        super().wheelEvent(event)

    def showEvent(self, event) -> None:
        if not self.show_event_flag:
            self.show_animation()
            self.show_event_flag = True

    def closeEvent(self, event):
        self.close_animation(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())
