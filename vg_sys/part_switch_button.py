from PySide6.QtCore import Qt, QRect, QVariantAnimation, QPoint, Signal
from PySide6.QtGui import QPainter, QFont, QBrush, QColor, QPen
from PySide6.QtWidgets import QWidget


class SwitchButton(QWidget):
    bt_changed = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 30)
        self.checked = False
        self.setCursor(Qt.PointingHandCursor)
        self.animation = QVariantAnimation()
        self.animation.setDuration(80)  # 动画持续时间
        self.animation.setStartValue(0)
        self.animation.setEndValue(20)
        self.animation.valueChanged.connect(self.update)
        self.animation.finished.connect(self.onAnimationFinished)

    def setText(self, value):
        pass

    def isChecked(self):
        return self.checked

    def setChecked(self, check):
        self.checked = check
        self.animation.setDirection(
            QVariantAnimation.Forward if self.checked else QVariantAnimation.Backward)
        self.animation.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        if self.checked:
            painter.setBrush(QColor('#07c160'))  # 选中颜色
        else:
            painter.setBrush(QColor('#d5d5d5'))  # 未选中颜色

        # 绘制外框
        painter.drawRoundedRect(QRect(0, 0, self.width(), self.height()), 15, 15)

        # 按钮位置
        offset = self.animation.currentValue()

        # 绘制按钮
        painter.setBrush(QColor(255, 255, 255))
        painter.drawEllipse(QPoint(15 + offset, 15), 12, 12)

    def mouseReleaseEvent(self, event) -> None:
        if event.button() == Qt.LeftButton:
            self.checked = not self.checked
            self.animation.setDirection(
                QVariantAnimation.Forward if self.checked else QVariantAnimation.Backward)
            self.animation.start()

    def onAnimationFinished(self):
        pass


# class SwitchButton(QWidget):
#     def __init__(self, parent=None):
#         super(SwitchButton, self).__init__(parent)
#         self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#         # self.resize(70, 30)
#         # SwitchButtonstate：True is ON，False is OFF
#         self.state = False
#         self.setFixedSize(80, 40)
#
#     def mousePressEvent(self, event):
#         super(SwitchButton, self).mousePressEvent(event)
#         self.state = False if self.state else True
#         self.update()
#
#     def paintEvent(self, event):
#         super(SwitchButton, self).paintEvent(event)
#
#         # Create a renderer and set anti-aliasing and smooth transitions
#         painter = QPainter(self)
#         painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
#         # Defining font styles
#         font = QFont("Arial")
#         font.setPixelSize(self.height() // 3)
#         painter.setFont(font)
#         # SwitchButton state：ON
#         if self.state:
#             # Drawing background
#             painter.setPen(Qt.NoPen)
#             brush = QBrush(QColor('#bd93f9'))
#             painter.setBrush(brush)
#             # Top left corner of the rectangle coordinate
#             rect_x = 0
#             rect_y = 0
#             rect_width = self.width()
#             rect_height = self.height()
#             rect_radius = self.height() // 2
#             painter.drawRoundedRect(rect_x, rect_y, rect_width, rect_height, rect_radius, rect_radius)
#             # Drawing slides circle
#             painter.setPen(Qt.NoPen)
#             brush.setColor(QColor('#ffffff'))
#             painter.setBrush(brush)
#             # Phase difference pixel point
#             # Top left corner of the rectangle coordinate
#             diff_pix = 3
#             rect_x = self.width() - diff_pix - (self.height() - 2 * diff_pix)
#             rect_y = diff_pix
#             rect_width = (self.height() - 2 * diff_pix)
#             rect_height = (self.height() - 2 * diff_pix)
#             rect_radius = (self.height() - 2 * diff_pix) // 2
#             painter.drawRoundedRect(rect_x, rect_y, rect_width, rect_height, rect_radius, rect_radius)
#
#             # ON txt set
#             painter.setPen(QPen(QColor('#ffffff')))
#             painter.setBrush(Qt.NoBrush)
#             painter.drawText(QRect(int(self.height() / 3), int(self.height() / 3.5), 50, 20), Qt.AlignLeft, 'ON')
#         # SwitchButton state：OFF
#         else:
#             # Drawing background
#             painter.setPen(Qt.NoPen)
#             brush = QBrush(QColor('#525555'))
#             painter.setBrush(brush)
#             # Top left corner of the rectangle coordinate
#             rect_x = 0
#             rect_y = 0
#             rect_width = self.width()
#             rect_height = self.height()
#             rect_radius = self.height() // 2
#             painter.drawRoundedRect(rect_x, rect_y, rect_width, rect_height, rect_radius, rect_radius)
#
#             # Drawing slides circle
#             pen = QPen(QColor('#999999'))
#             pen.setWidth(1)
#             painter.setPen(pen)
#             # Phase difference pixel point
#             diff_pix = 3
#             # Top left corner of the rectangle coordinate
#             rect_x = diff_pix
#             rect_y = diff_pix
#             rect_width = (self.height() - 2 * diff_pix)
#             rect_height = (self.height() - 2 * diff_pix)
#             rect_radius = (self.height() - 2 * diff_pix) // 2
#             painter.drawRoundedRect(rect_x, rect_y, rect_width, rect_height, rect_radius, rect_radius)
#
#             # OFF txt set
#             painter.setBrush(Qt.NoBrush)
#             painter.drawText(QRect(int(self.width() * 1 / 2), int(self.height() / 3.5), 50, 20), Qt.AlignLeft, 'OFF')


