from PySide6.QtCore import QPointF, QEasingCurve, QPropertyAnimation
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QApplication

# 创建应用程序对象
app = QApplication()

# 创建场景和视图
scene = QGraphicsScene()
view = QGraphicsView(scene)

# 创建并添加QGraphicsPixmapItem到场景中
pixmap = QPixmap("img.png")
pixmap_item = QGraphicsPixmapItem(pixmap)
scene.addItem(pixmap_item)

# 创建动画
animation = QPropertyAnimation(pixmap_item, b"pos")  # 传递QGraphicsPixmapItem对象而不是名称
animation.setDuration(1000)  # 设置动画持续时间为1000毫秒
animation.setStartValue(pixmap_item.pos())  # 设置起始位置为当前位置
animation.setEndValue(pixmap_item.pos() - QPointF(0, 100))  # 设置结束位置为当前位置向上移动100个单位
animation.setEasingCurve(QEasingCurve.OutBounce)  # 使用弹跳效果

# 启动动画
animation.start()

# 显示视图
view.show()

# 运行应用程序
app.exec()
