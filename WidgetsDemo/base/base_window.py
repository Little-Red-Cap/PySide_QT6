from WidgetsDemo.import_modules import *
from PySide6.QtGui import QIcon, QPixmap, QPainter
from PySide6.QtCore import QEasingCurve, QPropertyAnimation


class BaseWindow(QFrame):
    def __init__(self):
        super().__init__()
        self.animation = None
        self.show_event_flag = False
        self.opacity_value = 1.0  # 初始值
        self.opacity_step = 0.01  # 步长

    def keyPressEvent(self, event: QKeyEvent):
        if event.modifiers() & Qt.ControlModifier and event.key() == Qt.Key_W:
            self.close()
        super().keyPressEvent(event)

    def showEvent(self, event: QShowEvent) -> None:
        if not self.show_event_flag:
            self.show_animation()
            self.show_event_flag = True
        super().showEvent(event)

    def closeEvent(self, event: QCloseEvent):
        self.close_animation(event)
        super().closeEvent(event)

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

    def gf_to_icon(self, file_path: str, size=QSize(32, 32), size_factor=False):
        """
            This function is used to convert an SVG file to a QIcon or QPixmap.
            If the file is a PNG file, it will return a QIcon with the specified size.
            If the file is an SVG file, it will return a QPixmap with the specified size.
            If the file is not supported, it will return an empty QPixmap.
        """
        _, suffix = os.path.splitext(file_path)
        if suffix.lower() in ['.png', '.jpg', '.jpeg', 'ico']:
            if size_factor:  # 如果指定了大小，则缩放图标
                return QIcon(file_path).pixmap(size)
            else:            # 否则返回原始大小的图标
                return QIcon(file_path)

        elif suffix.lower() == '.svg':
            renderer = QSvgRenderer(file_path)  # 创建一个SVG渲染器
            pixmap = QPixmap(size)          # 创建一个QPixmap
            pixmap.fill(Qt.transparent)     # 设置透明背景
            painter = QPainter(pixmap)      # 创建一个QPainter并绑定到QPixmap上
            renderer.render(painter)        # 使用渲染器将SVG渲染到QPainter中
            painter.end()  # 结束绘制
            return pixmap
        else:
            # 对于其他类型的文件，可以返回一个错误图标或空图标
            print(suffix, 'is not supported')
            return QPixmap()
