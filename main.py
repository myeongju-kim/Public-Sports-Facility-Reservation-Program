import sys, datetime
import database as db
import messagebox as mbox
import management as mn
import signup as su
import reserve as rs
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class ID_find(QDialog):
    def __init__(self):
        super().__init__()
        self.name=QLineEdit("",self)
        self.phone=QLineEdit("",self)
        self.initUI()
    def initUI(self):
        self.name.setGeometry(85,95,160,25)
        self.phone.setGeometry(85,150,160,25)
        btn=QPushButton("아이디 찾기",self)
        btn.setGeometry(100,230,100,50)
        btn.clicked.connect(self.find)
        backgroundlmage = QImage('image/아이디찾기.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(backgroundlmage))
        self.setWindowIcon(QIcon('image/아이콘.png'))
        self.setWindowTitle('아이디 찾기')
        self.setPalette(palette)
        self.resize(300, 320)
        self.show()
    def find(self):
        Phone=self.phone.text()
        for i in Phone:
            try:
                int(i)
            except:
                Phone="0"
        sql = 'select id from LOGIN where name=' + "'" + self.name.text() + "' and phone="+"'"+Phone+"'"
        a=db.Database(sql,1)
        if a==[]:
            mbox.Messagebox(self,"정보가 없습니다.")
        else:
            mbox.Messagebox(self,"아이디는 "+a[0][0]+"\n문의사항 : 055-753-0000")
class Pwd_Find(QDialog):
    def __init__(self):
        super().__init__()
        self.txt=QLineEdit("",self)
        self.name=QLineEdit("",self)
        self.initUI()
    def initUI(self):
        self.txt.setGeometry(75,95,160,25)
        self.name.setGeometry(75,150,160,25)
        btn=QPushButton("비밀번호 찾기",self)
        btn.setGeometry(100,230,100,50)
        btn.clicked.connect(self.find)
        backgroundlmage = QImage('image/비번찾기.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(backgroundlmage))
        self.setWindowIcon(QIcon('image/아이콘.png'))
        self.setWindowTitle('비밀번호 찾기')
        self.setPalette(palette)
        self.resize(300, 320)
        self.show()
    def find(self):
        sql = 'select password from LOGIN where id=' + "'" + self.txt.text() + "' and name="+"'"+self.name.text()+"'"
        a=db.Database(sql,1)
        if a==[]:
            mbox.Messagebox(self,"정보가 없습니다.")
        else:
            STR=a[0][0]
            STR=STR.replace(STR[3],'*')
            mbox.Messagebox(self,"비밀번호는 "+STR+"\n문의사항 : 055-753-0000")
class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog=None
        self.txt_id=QLineEdit(self)
        self.txt_pwd = QLineEdit(self)
        self.initUI()
    def initUI(self):
        self.txt_id.setGeometry(190,195,250,30)
        self.txt_id.setFont(QFont("고딕",15))
        self.txt_id.setStyleSheet('border:0px;')
        self.txt_pwd.setGeometry(190,295,250,30)
        self.txt_pwd.setFont(QFont("고딕", 15))
        self.txt_pwd.setEchoMode(2)
        self.txt_pwd.setStyleSheet('border:0px;')
        font=QFont('고딕',10)
        font.setBold(True)
        btn=QPushButton('',self)
        btn.setGeometry(140, 360, 230, 50)
        btn.clicked.connect(self.into)
        btn.setStyleSheet('background-image:url(image/로그인버튼.png);')
        btn1 = QPushButton('회원가입', self)
        btn1.setGeometry(120, 400, 100, 45)
        btn1.clicked.connect(self.join)
        btn1.setFont(font)
        btn1.setStyleSheet('color:gray; border:0px;')
        btn2 = QPushButton('ID 찾기', self)
        btn2.setGeometry(190, 400, 100, 45)
        btn2.clicked.connect(self.find_id)
        btn2.setFont(font)
        btn2.setStyleSheet('color:gray; border:0px;')
        btn3 = QPushButton('비밀번호 찾기', self)
        btn3.setGeometry(270, 400, 100, 45)
        btn3.clicked.connect(self.find_pwd)
        btn3.setFont(font)
        btn3.setStyleSheet('color:gray; border:0px;')
        btn4=QPushButton(self)
        btn4.setGeometry(220,441,60,50)
        btn4.clicked.connect(self.management)
        btn4.setStyleSheet('border:0px;')
        btn4.setFont(font)
        backgroundlmage = QImage('image/입력창.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(backgroundlmage))
        self.setWindowIcon(QIcon('image/아이콘.png'))
        self.setWindowTitle('로그인 화면')
        self.setPalette(palette)
        self.resize(500,500)
        self.show()
    def management(self):
        self.dialog=QDialog()
        self.dialog.setWindowIcon(QIcon('image/아이콘.png'))
        self.dialog.setWindowTitle("관리자 접속")
        a=self.dialog
        txt=QLineEdit("",a)
        txt.setEchoMode(2)
        txt.setGeometry(43,110,120,30)
        btn=QPushButton("접속",a)
        btn.setFont(QFont("HY견고딕",15))
        btn.setGeometry(62,160,80,30)
        self.m_pwd = txt.text()
        btn.clicked.connect(lambda :self.a(txt.text()))
        backgroundlmage = QImage('image/관리자비밀번호.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(backgroundlmage))
        a.setPalette(palette)
        a.resize(200,200)
        a.show()
    def a(self,m_pwd):
        if m_pwd=="0000":
            self.dialog.setVisible(False)
            self.setVisible(False)
            self.dialog=mn.Management()
    def join(self):
        self.dialog=su.Join()
    def into(self):
        sql = 'select password from LOGIN where id='+"'"+self.txt_id.text()+"'"
        b=db.Database(sql,1)
        try:
            a=b[0][0]
            if a.strip() == self.txt_pwd.text():
                self.setVisible(False)
                self.dialog = rs.reserve(self.txt_id.text())
            else:
                self.txt_pwd.setText("")
                mbox.Messagebox(self,"비밀 번호가 옳지 않습니다.")
        except:
            mbox.Messagebox(self,"등록된 아이디가 존재하지 않습니다.")
    def find_id(self):
        self.dialog=ID_find()
    def find_pwd(self):
        self.dialog=Pwd_Find()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
