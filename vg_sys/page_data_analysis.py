from import_modules import *
# TODO: 去掉这里的parent_obj依赖


class PageDataAnalysis(QSplitter):
    key_pressed = Signal(QKeyEvent)

    def __init__(self, parent_obj=None):
        super().__init__()
        self.parent_obj = parent_obj
        self.page_setting = self.Browser(parent_obj)
        self.page_setting.setMaximumWidth(380)
        self.page_video_stream = self.VideoStream(parent_obj)
        self.addWidget(self.page_setting)
        self.addWidget(self.page_video_stream)
        self.page_setting.loadFinished.connect(self.wait_load_finished)

    class Browser(QWebEngineView):
        def __init__(self, parent_obj=None):
            super().__init__()
            self.parent_obj = parent_obj
            html_file = "test.html"
            current_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前 Python 文件的目录
            html_path = os.path.join(current_dir, html_file)
            # self.browser.load(QUrl.fromLocalFile(html_path))        # 加载HTML
            self.load(QUrl(self.parent_obj.web_url))

        def keyPressEvent(self, event: QKeyEvent):
            if event.key() == Qt.Key_F5:
                self.load(QUrl(self.parent_obj.web_url))
                # self.reload()

    class OpenCV:
        def __init__(self, parent_obj=None):
            self.parent_obj = parent_obj
            cap = cv2.VideoCapture(self.parent_obj.stream_url)   # 打开视频流
            while True:
                ret, frame = cap.read()  # 读取一帧视频
                if ret:     # 如果读取成功，显示帧
                    cv2.imshow('Video Stream', frame)
                # 按 'q' 退出循环
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                # 按 'p' 保存当前帧
                if cv2.waitKey(1) & 0xFF == ord('p'):
                    cv2.imwrite('frame.jpg', frame)
            cap.release()   # 释放摄像头资源q
            cv2.destroyAllWindows()  # 销毁所有窗口

    class VideoStream(QLabel):
        # 参考 https://blog.csdn.net/m0_48442491/article/details/128705183
        # GET请求参考 https://blog.51cto.com/u_12968/10279479 （未实现）
        def __init__(self, parent_obj=None):
            super().__init__()
            self.parent_obj = parent_obj
            self.cap = None
            self.setText("Key F6 to start/stop video stream")
            self.setAlignment(Qt.AlignCenter)
            self.timer = QTimer(self)
            self.timer.setInterval(30)  # 设置定时器的间隔时间为 30ms
            self.timer.timeout.connect(self.update_frame)

        def update_frame(self):
            ret, frame = self.cap.read()
            if ret:
                # rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # OpenCV 使用 BGR，但 Qt 使用 RGB，所以需要转换
                # h, w, ch = rgb_image.shape  # OpenCV 使用 numpy 数组，Qt 使用 QImage，所以需要转换
                # bytes_per_line = ch * w
                # convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
                h, w, ch = frame.shape  # OpenCV 使用 numpy 数组，Qt 使用 QImage，所以需要转换
                bytes_per_line = ch * w
                convert_to_Qt_format = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
                pixmap = QPixmap.fromImage(convert_to_Qt_format, Qt.AutoColor)    # 将 QImage 转换为 QPixmap 以在 QLabel 上显示
                self.setPixmap(pixmap)

        def keyPressEvent(self, event: QKeyEvent):
            if event.key() == Qt.Key_F6:
                if self.timer.isActive():
                    self.cap.release()  # 释放摄像头资源
                    self.timer.stop()
                    self.clear()
                    self.setText("Key F6 to start/stop video stream")
                else:
                    self.cap = cv2.VideoCapture(self.parent_obj.stream_url)   # 打开视频流
                    self.timer.start()

    def wait_load_finished(self):
        # self.page_video_stream.timer.start()
        pass

    def keyPressEvent(self, event: QKeyEvent):
        super().keyPressEvent(event)
        self.Browser.keyPressEvent(self.page_setting, event)
        self.VideoStream.keyPressEvent(self.page_video_stream, event)
        # self.key_pressed.emit(event)

    def closeEvent(self, event):
        self.page_video_stream.timer.stop()
        self.page_video_stream.cap.release()
        super().closeEvent(event)
