from PySide6.QtWidgets import QFrame, QSplitter, QLabel


class WidgetAbout(QFrame):
    def __init__(self):
        super().__init__()
        self.splitter = QSplitter(self)
        self.label = QLabel(self)
        self.label.setText("<h1><a href=\"http://www.baidu.com\">百度一下</a></h1>");
        self.label.setOpenExternalLinks(True)
        self.splitter.addWidget(self.label)
