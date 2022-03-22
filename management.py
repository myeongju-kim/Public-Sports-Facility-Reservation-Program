import sys, datetime
import database
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#management home
class Management(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog=None
        self.Date = QCalendarWidget(self)
        self.initUI()
    def initUI(self):
        btn=QPushButton("",self)
        btn.setGeometry(5,400,80,100)
        btn.setStyleSheet('color:white; border:0px;')
        btn.clicked.connect(self.back)
        self.Date.setGeometry(60, 120, 380, 300)
        self.Date.setGridVisible(True)
        self.Date.activated.connect(self.Rlist)
        backgroundlmage = QImage('관리자모드.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(backgroundlmage))
        self.setWindowIcon(QIcon('아이콘.png'))
        self.setWindowTitle('날짜 선택')
        self.setPalette(palette)
        self.resize(500, 500)
        self.show()
    def back(self):
        self.setVisible(False)
        self.dialog=Login()
