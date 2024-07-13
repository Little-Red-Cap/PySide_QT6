from PySide6.QtCore import QPointF, QRectF, QTimeLine
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsItemAnimation, QApplication

# 创建应用程序对象
app = QApplication([])

# 创建场景和视图
scene = QGraphicsScene()
view = QGraphicsView(scene)

# 创建并添加QGraphicsPixmapItem到场景中
pixmap = QPixmap("img.png")
pixmap_item = QGraphicsPixmapItem(pixmap)
scene.addItem(pixmap_item)

# 创建动画
animation = QGraphicsItemAnimation()
animation.setItem(pixmap_item)

timeline = QTimeLine(1000)  # 设置动画持续时间为1000毫秒
timeline.setFrameRange(0, 100)  # 设置帧范围

# 设置动画起始和结束位置
start_pos = QPointF(0, 0)  # 设置起始位置
end_pos = QPointF(0, -100)  # 设置结束位置
for i in range(0, 101, 10):  # 从0到100逐步设置位置
    animation.setPosAt(i / 100, start_pos + (end_pos - start_pos) * i / 100)

animation.setTimeLine(timeline)

# 启动动画
timeline.start()

# 显示视图
view.show()

# 运行应用程序
app.exec()
