from functools import partial
from PySide6.QtCore import Signal, QSize, Qt, Property, QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QApplication, QSpacerItem, QSizePolicy
from py_gf.render_svg_to_pixmap import gf_to_icon


class PageLeft(QFrame):
    page_index_changed = Signal(int)
    animation = None
    bar_width = 46

    class ButtonInfo:
        def __init__(self, icon_path, tip, func):
            self.icon_path = icon_path
            self.tip = tip
            self.func = func

    def __init__(self):
        super().__init__()
        # frame = QFrame()
        # layout = QVBoxLayout(frame)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 30, -1, 40)
        self.setMaximumSize(self.bar_width, 17280)
        # self.setMinimumWidth(self.bar_width)
        self.buttons = []
        btn_infos = [
            # PageLeft.ButtonInfo("img/indent-right.svg", "隐藏菜单", self.hide),
            PageLeft.ButtonInfo("img/indent-right.svg", "隐藏菜单", self.toggle_animation),
            PageLeft.ButtonInfo("img/settings_icon.svg", "配置", lambda: self.page_index_changed.emit(0)),
            PageLeft.ButtonInfo("img/bar-chart.png", "可视化", lambda: self.page_index_changed.emit(1)),
            PageLeft.ButtonInfo("img/play-movie.svg", "图像处理", lambda: self.page_index_changed.emit(2)),
            PageLeft.ButtonInfo("img/horizontal-sliders-dots.svg", "数据分析", lambda: self.page_index_changed.emit(3)),
            PageLeft.ButtonInfo("img/exit.svg", "退出程序", QApplication.instance().quit),
        ]
        for item in range(6):
            button = QPushButton()
            button.setObjectName(f"Button{item}")
            button.setFixedSize(QSize(40, 40))
            button.setIconSize(QSize(30, 30))
            button.setIcon(gf_to_icon(btn_infos[item].icon_path))
            button.setToolTip(btn_infos[item].tip)
            if btn_infos[item].func is not None:
                button.clicked.connect(btn_infos[item].func)
            self.buttons.append(button)
            # layout.addWidget(button, 0, Qt.AlignHCenter)
            layout.addWidget(button, 0, Qt.AlignCenter | Qt.AlignLeft)
            # if 0 <= item <= 6:
            #     # 连接信号到槽函数，这里使用了functools.partial来传递额外的参数
            #     button.clicked.connect(partial(self.on_button_clicked, button))

        layout.insertItem(1, QSpacerItem(20, 0, QSizePolicy.Fixed, QSizePolicy.Expanding))
        layout.insertItem(layout.count() - 1, QSpacerItem(20, 0, QSizePolicy.Fixed, QSizePolicy.Expanding))
        self.setLayout(layout)
        with open('theme/PageLeft.qss', 'r') as file:
            self.setStyleSheet(file.read())
        # index = Property(int, self.on_button_clicked)
        # QToolTip.setFont(QFont("SansSerif", 10));

    def on_button_clicked(self, button):
        page_index = int(button.objectName()[-1])
        if page_index >= 1:
            page_index -= 1
        self.page_index_changed.emit(page_index)

    def toggle_animation(self):
        self.animation = QPropertyAnimation(self, b"minimumWidth")
        self.animation.stop()
        if self.width() == self.bar_width:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(240)
            self.buttons[0].setIcon(gf_to_icon("img/indent-left.svg"))
        else:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self.bar_width)
            self.buttons[0].setIcon(gf_to_icon("img/indent-right.svg"))
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(500)
        self.animation.start()

    def hide_animation(self):
        self.animation = QPropertyAnimation(self, b"minimumWidth")
        self.animation.stop()
        self.animation.setStartValue(self.width())
        self.animation.setEndValue(0)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(500)
        # 当动画结束时隐藏左边页面
        self.animation.finished.connect(lambda: self.hide() if self.animation.endValue() == 0 else None)
        # 开始动画
        self.animation.start()
