from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtGui import QGradient
from PySide6.QtCore import *
from PySide6.QtCore import Qt
from PySide6.QtCharts import *
from PySide6.QtCharts import QScatterSeries, QLineSeries, QChart


class LineChartWithGradient(QChartView):
    # https://mp.weixin.qq.com/s/c2-B5RDlXb2oKV202h1vsg
    def __init__(self, parent=None):
        self.chart = QChart(parent)
        super().__init__(self.chart, parent)

        self.areaSeries = QAreaSeries(self)
        self.markerSeries = QScatterSeries(self)  # 专门用于标记的散点系列
        self.series = QLineSeries(self)
        self.areaSeries.setUpperSeries(self.series)  # 设置上层系列为折线系列
        # 设置散点系列的形状、大小和颜色
        self.markerSeries.setMarkerShape(QScatterSeries.MarkerShapeCircle)
        self.markerSeries.setMarkerSize(10.0)
        self.markerSeries.setColor(QColor(255, 0, 0))
        # self.m_markerSeries.setBorderColor(QColor(255, 0, 0))
        # 将系列添加到图表
        self.chart.addSeries(self.areaSeries)
        self.chart.addSeries(self.series)
        self.chart.addSeries(self.markerSeries)  # 确保散点系列被添加到图表
        self.setup_chart()

        self.chart.createDefaultAxes()  # 创建默认坐标轴
        self.chart.setTheme(QChart.ChartThemeDark)  # 设置主题
        self.chart.legend().hide()  # 隐藏图例

    def set_data(self, points: list[QPointF]):
        self.series.replace(points)
        self.markerSeries.replace(points)  # 刷新散点系列 保证散点系列与折线系列的点一致
        self.apply_gradient()  # 应用渐变效果
        self.chart.update()  # 更新图表

    def set_x_min_maxvalue(self, min_value, max_value):
        self.chart.axes(Qt.Horizontal)[0].setRange(min_value, max_value)

    def set_y_min_maxvalue(self, min_value, max_value):
        self.chart.axes(Qt.Vertical)[0].setRange(min_value, max_value)

    def setup_chart(self):
        self.chart.setTitle("Line Chart with Gradient")
        pen = QPen(Qt.red)
        pen.setWidth(2)
        self.series.setPen(pen)
        self.apply_gradient()

    def apply_gradient(self):
        # gradient = QLinearGradient(0, 0, 0, self.chart.plotArea().height())
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setColorAt(0.0, QColor(255, 0, 0, 127))  # 起始颜色
        gradient.setColorAt(0.5, QColor(255, 255, 0, 127))  # 中间颜色
        gradient.setColorAt(1.0, QColor(0, 255, 0, 127))  # 结束颜色
        # gradient.setCoordinateMode(QGradient.StretchToDeviceMode)  #
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)  #
        # self.areaSeries.setBrush(QBrush(gradient))  # 设置渐变填充
        self.areaSeries.setBrush(gradient)  # 设置渐变填充
        self.areaSeries.setPen(Qt.NoPen)


def test_line_chart_with_gradient():
    app = QApplication([])
    widget = LineChartWithGradient()
    widget.setWindowTitle("散点渐变折线图")
    widget.set_data([QPointF(i, i * i) for i in range(10)])
    widget.set_x_min_maxvalue(0, 9)
    widget.set_y_min_maxvalue(0, 81)
    widget.resize(680, 400)
    widget.show()
    app.exec()


test_line_chart_with_gradient()
