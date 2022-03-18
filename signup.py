from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Join(QDialog):
    def __init__(self):
        super().__init__()
        self.phone = QLineEdit("", self)
        self.name = QLineEdit("", self)
        self.pwd = QLineEdit("", self)
        self.id = QLineEdit("", self)
        self.join=1
        self.label=QLabel("",self)
        self.label2=QLabel("",self)
        self.checkbox = QCheckBox(' 개인 정보 수집 동의', self)
        self.initUI()
