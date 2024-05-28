from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtGui import QPainter
from PySide6.QtCore import *
from PySide6.QtCore import Qt
import math
import random


class WaveformWidget(QWidget):
    # https://mp.weixin.qq.com/s/xDf5Mlg2VyeFR3zwqQHTZQ?poc_token=HAyDS2ajf4wvpPm7v6ZyaqSl-gxxq5--Xe7o154g
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("渐变封闭折线波形图")
        # self.setAttribute(Qt.WA_StyledBackground, True)  # 设置背景为透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 设置背景透明
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.lineColor = Qt.black  # 折线颜色
        # self.lineColor = Qt.blue       # 折线颜色
        self.waveformData = []  # 存储波形数据点
        self.normalizedData = []  # 归一化后的数据点
        self.gradientThreshold = 0.2  # 渐变起始高度

    def save_image(self, filename: str):
        pixmap = QPixmap(self.size())
        pixmap.fill(Qt.transparent)  # 背景透明
        self.render(pixmap)
        # painter = QPainter(pixmap)
        # self.render(painter)
        # painter.end()
        # is_success = pixmap.save(filename)
        is_success = pixmap.save("G://Python/PySide_QT6/output/waveform.png", "PNG")
        print("is_success: ", is_success)
        if is_success:
            print("save image to:", filename)

    def set_gradient_threshold(self, threshold: float):
        self.gradientThreshold = threshold
        self.update()

    def set_line_color(self, color: QColor):
        self.lineColor = color
        self.update()

    def set_waveform_data(self, original_data: list[QPointF]):
        self.waveformData = original_data
        self.normalizedData = []

    def normalize_data(self):
        # 归一化数据
        self.normalizedData.clear()
        maxX = self.waveformData[-1].x()
        maxY = 0
        for point in self.waveformData:
            if point.y() > maxY:
                maxY = point.y()
        for point in self.waveformData:
            self.normalizedData.append(
                QPointF(point.x() / maxX * self.width(), self.height() - (point.y() / maxY * self.height())))

    def resizeEvent(self, event: QResizeEvent):
        self.normalize_data()
        self.update()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # 根据 gradientThreshold 计算渐变色的实际起始和结束位置
        gradientStart = self.gradientThreshold * self.height()
        # 创建渐变
        gradient = QLinearGradient(0, gradientStart, 0, self.height())
        gradient.setColorAt(0, QColor(0, 0, 255))
        gradient.setColorAt(1, QColor(255, 0, 0))

        # pen = QPen(self.lineColor, width=2)
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(self.lineColor)
        painter.setPen(pen)

        if len(self.normalizedData) > 1:
            path = QPainterPath()
            path.moveTo(self.normalizedData[0])

            # 绘制平滑曲线
            for i in range(1, len(self.normalizedData) - 1):
                # midPoint = QPointF((self.normalizedData[i - 1].x() + self.normalizedData[i].x()) / 2, (self.normalizedData[i - 1].y() + self.normalizedData[i].y()) / 2)
                # path.quadTo(self.normalizedData[i - 1], midPoint)
                midPoint = QPointF((self.normalizedData[i] + self.normalizedData[i + 1]) / 2)
                path.quadTo(self.normalizedData[i], midPoint)
            # draw last point
            path.lineTo(self.normalizedData[-1])

            # 将渐变填充应用到路径下方
            fillpath = QPainterPath(path)
            # fillpath.setFillRule(Qt.WindingFill)
            fillpath.lineTo(self.normalizedData[-1].x(), self.height())
            fillpath.lineTo(self.normalizedData[0].x(), self.height())
            fillpath.closeSubpath()

            # fill path with gradient
            painter.fillPath(fillpath, gradient)

            # draw path
            painter.drawPath(path)


def generate_random_points1():
    # 参数设置
    num_points = 100  # 点的数量
    frequency = 1.0  # 频率
    amplitude = 100.0  # 振幅
    phase = 0.0  # 相位
    x_offset = 0.0  # x轴偏移
    y_offset = 100.0  # y轴偏移
    noise_scale = 10.0  # 噪声的缩放比例
    # 生成x值（等差数列）
    x_values = [i * (2 * math.pi / num_points) for i in range(num_points)]
    # 生成y值（正弦波 + 噪声）
    y_values = [amplitude * math.sin(x + phase) + y_offset + random.uniform(-noise_scale, noise_scale) for x in x_values]
    # 生成y值（正弦波）
    # y_values = [amplitude * math.sin(x + phase) + y_offset for x in x_values]
    # 生成QPointF列表
    points = [QPointF(x_offset + i * (2 * math.pi / (num_points - 1)), y) for i, y in enumerate(y_values)]
    return points


def test_waveform_widget():
    app = QApplication([])
    widget = WaveformWidget()
    widget.waveformData = generate_random_points1()
    widget.show()
    app.exec()


test_waveform_widget()
