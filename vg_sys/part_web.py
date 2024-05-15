import os

from PySide6.QtCore import QObject, QUrl
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow


# https://blog.csdn.net/zheng19880607/article/details/134302577
class WebObject(QObject):
    m_nativeText = str

    def  nativeText(self):
        return self.m_nativeText

    # 在C++中定义的信号，可以在JS端监听此信号接收消息
    def nativeTextChanged(self, text):
        # 槽函数，JS端调用此函数时，会传入一个参数text
        print("nativeTextChanged:", text)
    # C + + 端的公共槽函数，可以在JS端调用。
    def setNativeText(self, text):
        m_nativeText = text
        self.nativeTextChanged(text)



class test_web(QMainWindow):
    def __init__(self):
        # self.web_view = QWebEngineView()
        #
        # self.setWindowTitle('Web Engine View Example')
        # self.setGeometry(100, 100, 800, 600)
        #
        # self.setCentralWidget(self.web_view)
        #
        # # self.web_view.load(QUrl("https://www.baidu.com"))
        # self.web_view.load(QUrl("https://www.baidu.com"))
        # self.web_view.show()
        super().__init__()
        self.setWindowTitle('Web Engine View Example')
        self.setGeometry(100, 100, 800, 600)

        # 创建 QWebEngineView 实例
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # 获取当前 Python 文件的目录
        html_file = "test.html"
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(current_dir, html_file)
        self.browser.load(QUrl.fromLocalFile(html_path))        # 加载HTML
        # self.browser.load(QUrl('https://www.baidu.com'))        # 加载网页
        # self.browser.connect(self.browser, SIGNAL('loadFinished(bool)'), wait_load_finished)
        self.browser.loadFinished.connect(self.wait_load_finished)

    def web_callback(self):
        print("Web callback called")

    def wait_load_finished(self):
        print("网页加载完成")
        # jsCode = "showalert('%s')" % "Hello QtWebEngine!"
        # self.browser.page().runJavaScript(jsCode)
        # jsCode = "getJsData()"
        # self.browser.page().runJavaScript(jsCode, 1, self.web_callback)

        # while not self.browser.loadFinished():
        #     pass

        m_pWebObj = WebObject()
        pWebChannel = QWebChannel()
        # 注册C + +对象到QWebChannel，这样远端的QWebChannel也会生成一个对应的JS对象
        # pWebChannel->registerObject("nativeObj", m_pWebObj)
        pWebChannel.registerObject("nativeObj", m_pWebObj)
        # ui->webview->page()->setWebChannel(pWebChannel)
        self.browser.page().setWebChannel(pWebChannel)
