import database as db
import messagebox as mbox
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
        backgroundlmage = QImage('image/회원가입.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(backgroundlmage))
        self.setWindowIcon(QIcon('image/아이콘.png'))
        self.setWindowTitle('회원가입')
        self.setPalette(palette)
        self.resize(300, 500)
        self.show()

    def Check(self,sign):
        if sign==0:
            ID=self.id.text()
            LEN=len(ID)
            if LEN>=5 and LEN<=10:
                for i in range(len(ID)):
                    if not((ID[i]>='a' and ID[i]<='z') or (ID[i]>='0' and ID[i]<='9')):
                        self.label.setText("5~10자의 영어 소문자, 숫자만 가능합니다.")
                        self.join=1
                        return
                sql = 'select ID from login'
                b = db.Database(sql,1)
                for i in range(len(b)):
                    if b[i][0].strip()==self.id.text():
                        self.label.setText("아이디가 중복입니다.")
                        self.join = 1
                        return
                self.label.setText("사용 가능합니다.")
                self.join = 0
            else:
                self.label.setText("5~10자의 영어 소문자, 숫자만 가능합니다.")
                self.join = 1
        else:
            PWD = self.pwd.text()
            LEN = len(PWD)
            if LEN >= 8 and LEN <= 16:
                for i in range(LEN):
                    if not ((PWD[i] >= 'a' and PWD[i] <= 'z') or (PWD[i] >= '0' and PWD[i] <= '9') or PWD[i]=='!'):
                        self.label2.setText("8~16자의 영어 소문자, 숫자, !만 가능합니다.")
                        self.join = 1
                        return
                self.label2.setText("사용 가능합니다.")
                self.join=0
            else:
                self.label2.setText("8~16자의 영어 소문자, 숫자, !만 가능합니다.")
                self.join = 1
    def complete(self):
        if self.join==0 and self.checkbox.isChecked()==True:
            sql = 'insert into login values(' + "'" + self.id.text() + "'," + "'" + self.pwd.text() + "'," + "'" + self.name.text() + "'," + "'" + self.phone.text() + "')"
            db.Database(sql,0)
            self.setVisible(False)
        else:
            mbox.Messagebox(self,"가입 조건을 만족시키지 못했습니다.")