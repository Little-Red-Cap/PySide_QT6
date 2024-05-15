import os
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPainter, QPixmap, QIcon
from PySide6.QtSvg import QSvgRenderer

# def render_svg_to_pixmap(svg_file_path, size):
#     renderer = QSvgRenderer(svg_file_path)      # 创建一个SVG渲染器
#     pixmap = QPixmap(size)          # 创建一个QPixmap
#     pixmap.fill(Qt.transparent)     # 设置透明背景
#     painter = QPainter(pixmap)      # 创建一个QPainter并绑定到QPixmap上
#     renderer.render(painter)        # 使用渲染器将SVG渲染到QPainter中
#     painter.end()       # 结束绘制
#     return pixmap


def gf_to_icon(file_path, size=QSize(32, 32), size_factor=False):
    """
        This function is used to convert an SVG file to a QIcon or QPixmap.
        If the file is a PNG file, it will return a QIcon with the specified size.
        If the file is an SVG file, it will return a QPixmap with the specified size.
        If the file is not supported, it will return an empty QPixmap.
    """
    _, suffix = os.path.splitext(file_path)

    # if suffix.lower() == '.png' || suffix.lower() == '.jpg' || suffix.lower() == '.jpeg':
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
