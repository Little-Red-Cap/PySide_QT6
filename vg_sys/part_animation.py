from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QApplication


class PartAnimation():
    def __init__(self):
        self.animation = None
    # super(PySide6_Window_Animation, self).__init__()
    # self.setWindowFlags(Qt.FramelessWindowHint)
    # self.setAttribute(Qt.WA_TranslucentBackground)
    # self.setWindowOpacity(0.0)
    # self.setGeometry(100, 100, 800, 600)
    # self.setObjectName("obj1")

    def show_animation(self):
        # 创建渐变动画，从不透明到透明
        self.animation = QPropertyAnimation(self, b"windowOpacity")  # setWindowOpacity(self)
        self.animation.setDuration(500)     # 设置动画时长为500毫秒
        self.animation.setStartValue(0.0)   # 设置动画起始值为透明
        self.animation.setEndValue(1.0)     # 设置动画结束值为不透明
        self.animation.setEasingCurve(QEasingCurve.InQuad)  # 设置动画曲线为先加速后减速
        self.animation.start()  # 启动动画

    def close_animation(self, event):
        # 创建渐变动画，从透明到不透明
        self.animation = QPropertyAnimation(self, b"windowOpacity")  # setWindowOpacity(self)
        self.animation.setDuration(500)     # 设置动画时长为500毫秒
        self.animation.setStartValue(1.0)   # 设置动画起始值为不透明
        self.animation.setEndValue(0.0)     # 设置动画结束值为透明
        self.animation.setEasingCurve(QEasingCurve.InQuad)  # 设置动画曲线为先加速后减速
        self.animation.start()  # 启动动画
        # 等待动画结束
        while self.animation.state() == QPropertyAnimation.Running:
            QApplication.processEvents()
        event.accept()  # 动画结束执行关闭窗口事件
