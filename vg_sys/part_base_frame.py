from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout


class BaseFrame(QFrame):
    def __init__(self, text="N/A", value_type=""):
        super().__init__()
        self.value_type = value_type
        self.label_value = QLabel(self)
        self.label_text = QLabel(self)
        self.label_value.setObjectName("label_value")
        self.label_text.setObjectName("label_text")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.addWidget(self.label_value, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.label_text, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        with open('theme/BaseFrame.qss', 'r') as file:
            self.setStyleSheet(file.read())
        self.update_value(0.0)
        self.update_text(text)

    def update_value(self, value):
        self.label_value.setText(str(value) + self.value_type)

    def update_text(self, text):
        self.label_text.setText(str(text))
