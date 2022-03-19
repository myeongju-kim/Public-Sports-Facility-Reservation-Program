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

    def initUI(self):
        self.id.setGeometry(80, 95, 130, 25)
        self.label.setFont(QFont('고딕', 8))
        self.label.setStyleSheet('color : red;')
        self.label.setGeometry(20, 122, 250, 25)
        check = QPushButton("확인", self)
        check.setGeometry(220, 95, 60, 25)
        check.clicked.connect(lambda: self.Check(0))
        self.label2.setFont(QFont('고딕', 8))
        self.label2.setStyleSheet('color : red;')
        self.label2.setGeometry(20, 177, 300, 25)
        self.pwd.setGeometry(80, 150, 130, 25)
        self.pwd.setEchoMode(2)
        check2 = QPushButton("확인", self)
        check2.setGeometry(220, 150, 60, 25)
        check2.clicked.connect(lambda: self.Check(1))
        self.name.setGeometry(80, 205, 130, 25)
        self.phone.setGeometry(80, 262, 130, 25)
        label3 = QLabel("'-' 생략", self)
        label3.setStyleSheet('color : red;')
        label3.setGeometry(80, 290, 300, 25)
        self.checkbox.setGeometry(20, 330, 200, 50)
        btn = QPushButton("가입", self)
        btn.setGeometry(100, 400, 100, 50)
        btn.clicked.connect(self.complete)
        backgroundlmage = QImage('회원가입.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(backgroundlmage))
        self.setWindowIcon(QIcon('아이콘.png'))
        self.setWindowTitle('회원가입')
        self.setPalette(palette)
        self.resize(300, 500)
        self.show()

    def Check(self, sign):
        return 0
    def complete(self):
        return 0