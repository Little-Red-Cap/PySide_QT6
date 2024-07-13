from PySide6.QtCore import QPointF, QTimeLine, QPropertyAnimation
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsItemAnimation, QApplication


class GraphicsViewOld(QGraphicsView):
    class HoverableGraphicsPixmapItem(QGraphicsPixmapItem):
        def __init__(self, pixmap, parent=None):
            super().__init__(parent)
            self.setAcceptHoverEvents(True)  # 允许悬停事件
            self.setPixmap(pixmap)

            move_pixel = 100
            # 创建动画
            self.animation = QGraphicsItemAnimation()
            self.animation.setItem(self)

            self.timeline = QTimeLine(1000)  # 设置动画持续时间为1000毫秒
            self.timeline.setFrameRange(0, move_pixel)  # 设置帧范围

            # 设置动画起始和结束位置
            self.start_pos = QPointF(0, 0)  # 设置起始位置
            end_pos = QPointF(0, -move_pixel)  # 设置结束位置
            for i in range(0, 101, 10):  # 从0到100逐步设置位置
                self.animation.setPosAt(i / move_pixel, self.start_pos + (end_pos - self.start_pos) * i / move_pixel)
            self.animation.setTimeLine(self.timeline)

        def hoverEnterEvent(self, event):
            # 当鼠标进入图片显示范围时，显示上移动动画
            self.timeline.start()

        def hoverLeaveEvent(self, event):
            # 当鼠标离开时，取消上移并以动画效果恢复到原来的位置
            self.timeline.stop()

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)  # 开启鼠标跟踪功能
        self.setScene(QGraphicsScene(self))
        # 创建并添加QGraphicsPixmapItem到场景中
        pixmap = QPixmap("img.png")
        self.pixmap_item = self.HoverableGraphicsPixmapItem(pixmap)
        self.scene().addItem(self.pixmap_item)


class HoverableGraphicsPixmapItem(QGraphicsPixmapItem):
    def __init__(self, pixmap, parent=None):
        super().__init__(pixmap, parent)
        self.setAcceptHoverEvents(True)  # 允许悬停事件
        self.start_pos = QPointF(0, 0)  # 设置起始位置
        self.end_pos = QPointF(0, -100)  # 设置结束位置

        self.animation = QGraphicsItemAnimation()
        self.animation.setItem(self)
        self.timeline = QTimeLine(1000)  # 设置动画持续时间为1000毫秒
        self.timeline.setFrameRange(0, 100)  # 设置帧范围
        self.setupAnimation()

    def setupAnimation(self):
        for i in range(0, 101, 10):  # 从0到100逐步设置位置
            self.animation.setPosAt(i / 100, self.start_pos + (self.end_pos - self.start_pos) * i / 100)

    def hoverEnterEvent(self, event):
        # 当鼠标进入图片显示范围时，显示上移动画
        self.timeline.start()

    def hoverLeaveEvent(self, event):
        # 当鼠标离开时，取消上移并以动画效果恢复到原来的位置
        self.timeline.stop()
        self.setPos(self.start_pos)

        # 实现45度倾斜的效果
        transform = QTransform()
        transform.rotate(45)
        transform.translate(-self.pixmap().width() / 2, -self.pixmap().height() / 2)
        self.setTransform(transform)


class GraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)  # 开启鼠标跟踪功能
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        # 创建并添加HoverableGraphicsPixmapItem到场景中
        pixmap = QPixmap("img.png")
        self.pixmap_item = HoverableGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmap_item)


if __name__ == '__main__':
    app = QApplication([])
    window = GraphicsView()
    window.show()
    app.exec()
