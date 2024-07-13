from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QGraphicsScene, QGraphicsPixmapItem, \
    QGraphicsView
from PySide6.QtCore import Qt, QPropertyAnimation, QPointF, QByteArray
from ui_untitled import *


class MainWindow(QWidget):
    class CardWidget(QWidget):
        def __init__(self, title, color):
            super().__init__()
            self.layout = QVBoxLayout(self)
            self.initUI(title, color)

        def initUI(self, title, color):
            self.setStyleSheet(f"background-color: {color};")
            self.setFixedHeight(100)  # 假设每个卡片的高度固定
            self.layout.setAlignment(Qt.AlignCenter)
            label = QLabel(title, self)
            self.layout.addWidget(label)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Card Widgets')
        self.setGeometry(100, 100, 400, 400)  # 设置窗口位置和大小

        layout = QVBoxLayout(self)

        # 创建四个卡片并添加到布局中
        cards = [
            self.CardWidget("Card Title 1", "pink"),
            self.CardWidget("Card Title 2", "lightblue"),
            self.CardWidget("Card Title 3", "lavender"),
            self.CardWidget("Card Title 4", "plum")
        ]

        for card in cards:
            layout.addWidget(card)

            # 如果你想要添加间距或边距，可以这样做：
        # layout.addSpacing(10)  # 在卡片之间添加间距
        # 或者在CardWidget中设置边距

        self.setLayout(layout)


class Window1(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 加载图片
        pixmap = QPixmap("1.png")
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setFixedSize(pixmap.size())  # 设置标签大小与图片相同
        # label.setFixedSize(100, 100)

        # 初始位置
        self.original_pos = label.pos()

        # 布局（虽然这里只有一个标签，但为了清晰起见还是使用了布局）
        layout = QVBoxLayout(self)
        layout.addWidget(label)

        # 启用鼠标跟踪
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        # 这里只是检测鼠标是否在窗口内，实际上你可能需要更精细的检测
        if self.rect().contains(event.position().toPoint()):
            # 假设我们想要标签在鼠标进入时上移50像素
            new_pos = self.original_pos + QPoint(0, -50)
            # 使用QPropertyAnimation进行平滑移动（可选）
            animation = QPropertyAnimation(self.findChild(QLabel, ''), b"pos")
            animation.setDuration(500)  # 动画持续时间（毫秒）
            animation.setStartValue(self.original_pos)
            animation.setEndValue(new_pos)
            animation.start(QPropertyAnimation.DeleteWhenStopped)
            # 注意：这里没有处理鼠标离开时的情况，因为示例中只展示了上移效果


class GraphicsView(QGraphicsView):
    class MovablePixmapItem(QGraphicsPixmapItem):
        def __init__(self, pixmap, parent=None):
            super().__init__(pixmap, parent)
            self.original_pos = self.pos()
            self.original_transform = QTransform()
            self.setAcceptHoverEvents(True)  # 允许悬停事件

        def hoverEnterEvent(self, event):
            # 假设我们想要标签在鼠标进入时上移50像素
            transform = QTransform().translate(0, -50)
            self.setTransform(transform)

        def hoverLeaveEvent(self, event):
            # 恢复原始位置和变换
            self.setPos(self.original_pos)
            self.setTransform(self.original_transform)

    class HoverPixmapItemOld(QGraphicsPixmapItem):
        def __init__(self, pixmap, parent=None):
            super().__init__(pixmap, parent)
            self.original_pos = self.pos()
            self.hovered = False
            self.setAcceptHoverEvents(True)  # 允许悬停事件

        def hoverEnterEvent(self, event):
            self.hovered = True
            self.move_up()

        def hoverLeaveEvent(self, event):
            self.hovered = False
            self.reset_position()

        def move_up(self):
            # 假设我们想要标签在鼠标进入时上移50像素
            new_pos = self.pos() + QPointF(0, -50)
            self.setPos(new_pos)

        def reset_position(self):
            # 恢复原始位置
            self.setPos(self.original_pos)

    class HoverPixmapItem(QGraphicsPixmapItem):
        def __init__(self, pixmap, parent=None):
            super().__init__(pixmap, parent)
            self.original_pos = self.pos()
            self.hovered = False
            self.setAcceptHoverEvents(True)  # 允许悬停事件
            self.hover_animation = None

        def hoverEnterEvent(self, event):
            if not self.hovered:
                self.hovered = True
                self.start_hover_animation(True)

        def hoverLeaveEvent(self, event):
            if self.hovered:
                self.hovered = False
                self.start_hover_animation(False)

        def start_hover_animation(self, hover_in):
            # if self.hover_animation and self.hover_animation.state() == QPropertyAnimation.Running:
            #     self.hover_animation.stop()

            if hover_in:
                # 假设我们想要标签在鼠标进入时上移50像素
                end_pos = self.pos() + QPointF(0, -50)
            else:
                end_pos = self.original_pos

            # 简化为直接使用字符串
            print(type(b"pos"))
            # self.hover_animation = QPropertyAnimation(self, "pos")
            # self.hover_animation = QPropertyAnimation(self, QByteArray(b"pos"))
            self.hover_animation = QPropertyAnimation(self, self.pos())
            # self.hover_animation = QPropertyAnimation(self, self.pos)
            self.hover_animation.setDuration(200)  # 设置动画持续时间，例如200毫秒
            self.hover_animation.setStartValue(self.pos())
            self.hover_animation.setEndValue(end_pos)
            self.hover_animation.setEasingCurve(Qt.Linear)  # 或使用其他缓动曲线
            self.hover_animation.start(QPropertyAnimation.DeleteWhenStopped)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个QGraphicsScene
        self.scene = QGraphicsScene(self)
        # 加载图片并创建一个QGraphicsPixmapItem
        pixmap = QPixmap("img.png")
        item = self.MovablePixmapItem(pixmap)
        # item = self.HoverPixmapItemOld(pixmap)
        # item = self.HoverPixmapItem(pixmap)
        # 将项目添加到场景中
        self.scene.addItem(item)
        # 设置场景到视图
        self.setScene(self.scene)
        # 启用鼠标跟踪
        self.setMouseTracking(True)


if __name__ == '__main__':
    app = QApplication([])
    # ex = MainWindow()
    # ex = Window1()
    # ex = MyWidget()
    ex = GraphicsView()
    ex.show()
    app.exec()
