# This Python file uses the following encoding: utf-8
# from WidgetsDemo.base.page_left import PageLeft
from base.base_window import *


class MainWidget(BaseWindow):
    # title = QObject.tr("物联网智慧蔬菜大棚管理系统", "Village Green System")
    title = "Widgets Demo"
    icon_path = "img/hand-holding-seedling.svg"
    starting = Signal(bool)

    class StatrPage(QMainWindow):

        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.label = QLabel(self)
            self.label.setText("欢迎使用Widgets Demo")
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setStyleSheet("font-size: 24px;")
            self.setCentralWidget(self.label)
            self.resize(400, 300)

        def showEvent(self, event: QShowEvent) -> None:
            animation = QPropertyAnimation(self, b"windowOpacity")  # setWindowOpacity(self)
            animation.setDuration(500)  # 设置动画时长为500毫秒
            animation.setStartValue(0.0)  # 设置动画起始值为透明
            animation.setEndValue(1.0)  # 设置动画结束值为不透明
            animation.setEasingCurve(QEasingCurve.InQuad)  # 设置动画曲线为先加速后减速
            animation.start()  # 启动动画

    def __init__(self):
        super().__init__()
        self.start_page = self.StatrPage(self)
        # start_page.show()
        self.start_page.show()
        # QTimer.singleShot(1000, lambda: start_page.close())
        # QTimer.singleShot(1000, lambda: self.loaded(True))
        # self.starting.connect(start_page.close)
        self.starting.connect(self.loading)
        # self.starting.connect(lambda is_loaded: start_page.show() if is_loaded else start_page.close())
        # self.starting.connect(lambda is_loaded: print("not loaded") if is_loaded else print("loaded") and self.show())
        self.starting.emit(True)
        QTimer.singleShot(2000, lambda: self.starting.emit(False))

        self.setWindowTitle(self.title)
        # self.setWindowIcon(gf_to_icon(self.icon_path))
        # self.page_left = PageLeft(self)  # 46 32
        self.stacked_pages = QStackedWidget(self)
        layout = QHBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(3, 0, 0, 0)
        # layout.addWidget(self.page_left)
        layout.addWidget(self.stacked_pages)
        self.resize(1280, 720)

    def loading(self, is_loaded: bool) -> None:
        pass
        # if is_loaded:
        #     print("not loaded")
        #     self.start_page.show()
        # else:
        #     print("loaded")
        #     self.start_page.close()
        #     self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec())
