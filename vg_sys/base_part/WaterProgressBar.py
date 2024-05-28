from math import sin
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtGui import QPainter
from PySide6.QtCore import *
from PySide6.QtCore import Qt


class WaterProgressBar(QWidget):
    # https://mp.weixin.qq.com/s?__biz=MzkxNDY0MDg1Mw==&mid=2247484246&idx=3&sn=a946f04434330ed0f22cf0451ac5a922&chksm=c043c3be1f2cde9ae88c87997b0dfbc6701220666dd8ce807a4a37c42bb0be3e606cb6972368&scene=132&exptype=timeline_recommend_article_extendread_samebiz&show_related_article=1&subscene=0&scene=132#wechat_redirect

    def __init__(self, parent: QWidget = None, water_color=QColor(90, 175, 233), bg_color=QColor(50, 50, 50), value=50.0, radius=100, offset=50, animation=True):
        super().__init__(parent)
        self.setWindowTitle("圆形水波动画进度条")
        self.waterColor = water_color   # 水的颜色
        self.bg_color = bg_color        # 背景颜色
        self.offset = offset            # 动画偏移量
        self.value = value              # 进度值
        self.radius = radius            # 圆形半径

        self.timer = QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.timer_update)
        if animation:
            self.timer.start()

    def timer_update(self):
        self.offset += 5
        if self.offset == 100:
            self.offset = 50
        self.update()

    def get_value(self):  # 获取当前进度值
        return self.value

    def get_radius(self):  # 获取圆形进度条的半径
        return self.radius

    def get_water_color(self):  # 获取水的颜色
        return self.waterColor

    def get_bg_color(self):  # 获取背景颜色
        return self.bg_color

    def start(self):  # 开始水波动画
        self.timer.start()

    def stop(self):  # 停止水波动画
        self.timer.stop()

    def set_value(self, value: int):  # 设置进度值
        self.value = value
        self.repaint()

    def set_radius(self, radius: int):  # 设置圆形进度条的半径
        self.radius = radius
        self.repaint()

    def set_water_color(self, color: QColor):  # 设置水的颜色
        self.waterColor = color
        self.repaint()

    def set_bg_color(self, color: QColor):  # 设置背景颜色
        self.bg_color = color
        self.repaint()

    def paintEvent(self, event: QPaintEvent):  # 绘制事件处理
        width = self.width()
        height = self.height()
        side = min(width, height)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing | QPainter.TextAntialiasing)
        painter.translate(width / 2, height / 2)
        painter.scale(side / 200, side / 200)

        self.draw_bg(painter)
        self.draw_water(painter)
        self.draw_text(painter)
        super().paintEvent(event)

    def draw_water(self, painter: QPainter):  # 绘制水波
        sinA = 2.5  # 波幅
        sinAlpha = 0.1  # 波长
        rect = QRect(-self.radius, -self.radius, self.radius * 2, self.radius * 2)
        startX = -self.radius
        startY = -self.radius
        endX = self.radius
        endY = self.radius
        height = self.radius - ((self.value * self.radius) / 50)

        water_path1 = QPainterPath()
        water_path1.moveTo(startX, endY)
        water_path2 = QPainterPath()
        water_path2.moveTo(startX, endY)

        for i in range(startX, endY):
            y1 = sinA * sin(i * sinAlpha + self.offset) + height
            y2 = sinA * sin(i * sinAlpha + self.offset + 60) + height

            if self.value == 0:
                y1 = y2 = endY
            elif self.value == 100:
                y1 = y2 = -endY

            water_path1.lineTo(i, y1)
            water_path2.lineTo(i, y2)

        water_path1.lineTo(endX, endY)
        water_path2.lineTo(endX, endY)

        big_path = QPainterPath()
        big_path.addEllipse(rect)
        water_path1 = big_path.intersected(water_path1)
        water_path2 = big_path.intersected(water_path2)
        painter.save()
        painter.setPen(Qt.NoPen)
        self.waterColor.setAlpha(180)
        painter.setBrush(self.waterColor)
        painter.drawPath(water_path2)
        self.waterColor.setAlpha(100)
        painter.setBrush(self.waterColor)
        painter.drawPath(water_path1)
        painter.restore()

    def draw_text(self, painter: QPainter):  # 绘制文本
        painter.save()
        text = str(self.value) + "%"
        font = painter.font()
        font.setPixelSize(30)
        painter.setFont(font)
        pen = painter.pen()
        pen.setColor(Qt.white)
        pen.setWidth(4)
        painter.setPen(pen)
        rect = QRect(-self.radius, -self.radius, self.radius * 2, self.radius * 2)
        painter.drawText(rect, Qt.AlignCenter, text)
        painter.restore()

    def draw_bg(self, painter: QPainter):  # 绘制背景圆形
        painter.save()
        painter.setPen(Qt.NoPen)
        # painter.setBrush(QColor(self.bgColor))
        painter.setBrush(self.bg_color)
        rect = QRect(-self.radius, -self.radius, self.radius * 2, self.radius * 2)
        painter.drawEllipse(rect)
        painter.restore()
