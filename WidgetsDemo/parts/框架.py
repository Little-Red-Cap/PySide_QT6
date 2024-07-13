from PySide6.QtWidgets import QWidget


class MainWidget(QWidget):
    def __init__(self, parent=None, enable_start_ui: bool = True):
        super(MainWidget, self).__init__(parent)

    def insert_widget(self, widget: QWidget, menu: QWidget = None, icon: str = None, index: int = -1, before: bool = False):
        pass


