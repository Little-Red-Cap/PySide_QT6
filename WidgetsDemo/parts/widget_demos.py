from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGraphicsEllipseItem, QGraphicsView, \
    QGraphicsScene, QMainWindow, QPushButton, QSplitter, QScrollBar, QHBoxLayout
from PySide6.QtGui import QPainter, QColor, QPen, QRadialGradient, QEnterEvent, QMouseEvent, QBrush, QPixmap, \
    QLinearGradient
from PySide6.QtCore import Qt, QPoint, QEvent, QPointF, QTimer, QRect
import sys


class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)  # 跟踪鼠标事件
        self.circle_center: QPoint = QPoint()
        self.draw_circle: bool = False  # 添加一个标志位来跟踪是否绘制圆形

        self.label = QLabel('Hello World', self)  # 创建一个QLabel并设置文本
        self.label.setMouseTracking(True)  # 跟踪鼠标事件
        self.label.setAlignment(Qt.AlignCenter)  # 设置文本居中
        self.label.setStyleSheet("QLabel { font-size: 32px; color: red; }")  # 设置文本样式
        # 设置布局并将QLabel居中
        layout = QVBoxLayout(self)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.resize(680, 400)
        # self.label.installEventFilter(self)  # 安装事件过滤器

    # def eventFilter(self, obj, event):
    #     if obj is self.label and event.type() == QEvent.MouseMove:
    #         # 转发鼠标移动事件给CustomWidget
    #         self.mouseMoveEvent(event)
    #         print('mouse move event from label')
    #         return True  # 表示事件已被处理
    #     return super().eventFilter(obj, event)

    def enterEvent(self, event: QEnterEvent) -> None:
        self.draw_circle = True  # 当鼠标进入 widget 时，设置标志位为 True
        self.update()

    def leaveEvent(self, event: QEvent):
        self.draw_circle = False  # 当鼠标离开 widget 时，设置标志位为 False
        self.update()

    def mouseMoveEvent(self, event: QMouseEvent):
        # print(type(event))
        self.circle_center = event.position().toPoint()
        self.draw_circle = True  # 当鼠标在 widget 内部移动时，也设置标志位为 True
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 启用抗锯齿
        painter.fillRect(self.rect(), QColor('white'))  # 清除背景（如果需要）
        if self.draw_circle:  # 检查是否应该绘制矩形
            radius = 150  # 设定圆形的半径
            gradient = QRadialGradient(self.circle_center, radius)  # 创建一个从中心向边缘的渐变
            gradient.setColorAt(0, QColor(0, 110, 255))  # 中心颜色
            gradient.setColorAt(1, QColor(0, 0, 0, 0))  # 边缘颜色（透明）
            painter.setPen(QPen(Qt.NoPen))  # 使用无画笔，即不绘制边框
            painter.setBrush(gradient)  # 应用渐变
            painter.drawEllipse(self.circle_center, radius, radius)  # 绘制圆形


class GraphicsViewWidget(QGraphicsView):
    class CircleItem(QGraphicsEllipseItem):
        def __init__(self, radius=50, parent=None):
            super().__init__(0, 0, radius * 2, radius * 2, parent)
            self.setBrush(QBrush(QColor(0, 110, 255, 100)))
            self.setPen(QPen(Qt.NoPen))
            self.setVisible(False)  # 默认不显示

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)  # 跟踪鼠标事件
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)  # 全更新视窗
        # self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)  # 仅更新变化的视窗
        # self.setViewportUpdateMode(QGraphicsView.MinimalViewportUpdate)  # 仅更新变化的视窗（仅限于移动）
        self.setRenderHint(QPainter.Antialiasing)
        self.scene = QGraphicsScene(self)
        self.circle = self.CircleItem(radius=50)
        self.scene.addItem(self.circle)
        self.setScene(self.scene)
        self.circle_visible = False
        self.resize(680, 400)

    def enterEvent(self, event: QEvent):
        super().enterEvent(event)
        if not self.circle_visible:
            self.circle_visible = True
            self.circle.setVisible(True)

    def leaveEvent(self, event: QEvent):
        super().leaveEvent(event)
        self.circle_visible = False
        self.circle.setVisible(False)

    def mouseMoveEvent(self, event: QMouseEvent):
        super().mouseMoveEvent(event)
        if self.circle_visible:
            scene_pos = self.mapToScene(event.position().toPoint())  # 转换鼠标位置到场景坐标
            self.circle.setPos(
                scene_pos - QPointF(self.circle.boundingRect().width() / 2, self.circle.boundingRect().height() / 2))


class ScrollableImageWidget(QWidget):
    def __init__(self, image_paths, parent=None):
        super().__init__(parent)
        self.image_paths = image_paths
        self.images = [QPixmap(path) for path in image_paths]
        self.image_width = self.images[0].width()
        self.scroll_offset = 0
        self.scrollbar = QScrollBar(Qt.Horizontal, self)
        self.scrollbar.setRange(-(len(self.images) - 1) * self.image_width, 0)
        self.scrollbar.valueChanged.connect(self.on_scroll_value_changed)

        layout = QHBoxLayout(self)
        layout.addWidget(self.scrollbar)
        layout.setContentsMargins(0, 0, 0, 0)

    def on_scroll_value_changed(self, value):
        self.scroll_offset = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        # 计算淡化的范围
        fade_range = 100
        fade_start = fade_range
        fade_end = self.width() - fade_range

        # 绘制图片
        for img in self.images:
            x = self.scroll_offset + (self.image_width * self.images.index(img))
            if x < self.width():
                # 检查图片是否在可视区域内
                if x + img.width() > 0:
                    # # 计算透明度
                    # opacity = 1.0
                    # if x < fade_start:
                    #     opacity = (x - fade_start) / fade_range
                    # elif x + img.width() > fade_end:
                    #     opacity = 1 - ((x + img.width() - fade_end) / fade_range)
                    # if opacity < 0:
                    #     opacity = 0
                    # if opacity > 1:
                    #     opacity = 1
                    #
                    #     # 设置渐变效果
                    # if opacity < 1:
                    #     gradient = QLinearGradient(x, 0, x + img.width(), 0)
                    #     gradient.setColorAt(0, QColor(255, 255, 255, int(opacity * 255)))
                    #     gradient.setColorAt(1, QColor(255, 255, 255, 0))
                    #     painter.setBrush(QBrush(gradient))
                    #     painter.drawRect(x, 0, img.width(), self.height())
                    #
                    #     # 绘制图片
                    # painter.setOpacity(opacity)
                    painter.drawPixmap(x, 0, img)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.scrollbar.setPageStep(self.width())


class ScrollableImageWidget1(QWidget):
    def __init__(self, image_paths, scroll_speed=1, parent=None):
        super().__init__(parent)
        self.image_paths = image_paths
        # self.images = [QPixmap(path) for path in image_paths]
        self.images = []
        self.image_size = 500, 500
        for path in image_paths:
            pixmap = QPixmap(path)
            pixmap = pixmap.scaled(*self.image_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.images.append(pixmap)

        self.image_width = self.images[0].width()
        self.scroll_offset = 0
        self.total_width = len(self.images) * self.image_width
        self.scroll_speed = scroll_speed  # 滚动速度（像素/秒）

        # 滚动条不需要交互，因此可以隐藏它
        self.scrollbar = QScrollBar(Qt.Horizontal, self)
        self.scrollbar.setRange(0, self.total_width - self.width())
        self.scrollbar.setVisible(False)  # 隐藏滚动条

        # 设置定时器进行自动滚动
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scroll_images)
        self.timer.start(10 // scroll_speed)  # 根据滚动速度设置定时器间隔

        # 布局等初始化代码...

    def scroll_images(self):
        # 更新滚动偏移量
        self.scroll_offset -= self.scroll_speed
        # 处理循环滚动
        # if self.scroll_offset < -self.total_width + self.width():
        #     self.scroll_offset = 0
        # 提前重置滚动偏移量，以避免卡顿
        if self.scroll_offset + self.width() < 0:
            self.scroll_offset = self.total_width
        # 强制重绘
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        # 绘制图片
        for i, img in enumerate(self.images):
            x = self.scroll_offset + (self.image_width * i)
            if self.rect().intersects(QRect(x, 0, img.width(), img.height())):
                painter.drawPixmap(x, 0, img)


class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.image_widget = ScrollableImageWidget(['1.png', '2.png', '3.png', '4.png'])
        self.image_widget = ScrollableImageWidget1(['1.png', '2.png', '3.png', '4.png'])
        self.setCentralWidget(self.image_widget)
        self.resize(1280, 680)


if __name__ == "__main__":
    # 模仿效果来着下面这个网站：
    # https://www.jetbrains.com/zh-cn/aqua/
    app = QApplication(sys.argv)
    # widget = CustomWidget()
    # widget = GraphicsViewWidget()
    widget = MainWindow1()
    widget.show()
    sys.exit(app.exec())
