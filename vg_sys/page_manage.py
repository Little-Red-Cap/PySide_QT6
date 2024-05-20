from import_modules import *
from ui.ui_page_dev import *


class PageManage(QFrame):
    def __init__(self, parent_obj=None):
        super().__init__()
        self.page = Ui_Form()
        self.page.setupUi(self)
        # self.chart = MainWindow()
        # self.setLayout(QGridLayout(self))
        # self.layout().addWidget(self.chart)
