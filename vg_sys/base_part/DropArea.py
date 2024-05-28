

class DropArea(QLabel):
    # https://mp.weixin.qq.com/s/hoT67rqMSjgeoj53sFLUjw
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setText("Drop files here")
        self.setAlignment(Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.setScaledContents(True)
        self.resize(QSize(640, 480))
        self.setWindowTitle("拖放功能 实现一个图像拖入与显示")

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasImage() | event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent):
        event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        mime_data = event.mimeData()
        if mime_data.hasImage():
            print("drop image")
            image = QImage(mime_data.imageData())
            pixmap = QPixmap.fromImage(image)
            self.setPixmap(pixmap)
        elif mime_data.hasUrls():
            print("drop urls")
            urls = mime_data.urls()
            for url in urls:
                file_path = url.toLocalFile()
                if file_path.endswith(('.jpg', '.png', '.jpeg', '.gif')):
                    image = QImage(file_path)
                    pixmap = QPixmap.fromImage(image)
                    self.setPixmap(pixmap)
        event.acceptProposedAction()
