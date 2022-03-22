import sys, datetime
import database
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


#Main home interface
class reserve(QDialog):
    def __init__(self,id):
        super().__init__()
        self.dialog=None
        self.id = id
        self.btselect=QPushButton('',self)
        self.select="축구"
        self.initUI()
    def initUI(self):
        btn1 = QPushButton('', self)
        btn1.setGeometry(6, 130, 120, 40)
        btn1.clicked.connect(lambda:self.Image('축구'))
        btn1.setStyleSheet('''
              QPushButton{background-image: url(soccer.png); border:0px;} 
              QPushButton:hover{background-image: url(soccer2.png); border:0px;}
              ''')
        btn2 = QPushButton('', self)
        btn2.setGeometry(128, 130, 120, 40)
        btn2.clicked.connect(lambda:self.Image('풋살'))
        btn2.setStyleSheet('''
               QPushButton{background-image: url(foot.png); border:0px;} 
               QPushButton:hover{background-image: url(foot2.png); border:0px;}
               ''')
        btn3 = QPushButton('', self)
        btn3.setGeometry(250, 130, 120, 40)
        btn3.clicked.connect(lambda:self.Image('족구'))
        btn3.setStyleSheet('''
               QPushButton{background-image: url(gu.png); border:0px;} 
               QPushButton:hover{background-image: url(gu2.png); border:0px;}
               ''')
        btn4 = QPushButton('', self)
        btn4.setGeometry(372, 130, 120, 40)
        btn4.clicked.connect(lambda:self.Image('농구'))
        btn4.setStyleSheet('''
               QPushButton{background-image: url(bask.png); border:0px;} 
               QPushButton:hover{background-image: url(bask2.png); border:0px;}
               ''')
        btnr=QPushButton('',self)
        btnr.setStyleSheet('''
                       QPushButton{background-image: url(예약조회.png); border:0px;} 
                       QPushButton:hover{background-image: url(예약조회2.png); border:0px;}
                       ''')
        btnr.setGeometry(170,430,156,50)
        btnr.clicked.connect(self.Inquiry2)

        self.btselect.setGeometry(4,170,492,245)
        self.btselect.clicked.connect(self.detail)
        self.btselect.setStyleSheet('background-image : url(축구.png);')
        backgroundlmage = QImage('init.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(backgroundlmage))
        self.setWindowIcon(QIcon('아이콘.png'))
        self.setWindowTitle('종목 선택')
        self.Timeout()
        self.setPalette(palette)
        self.resize(500,500)
        self.show()

    #Sign an hour ago
    def Timeout(self):
        Day = datetime.datetime.now()
        Hour=Day.time().hour
        Min=Day.time().minute
        date=str(Day.date())
        sql = 'select RTIME from reserve where id=' + "'" + self.id + "' and TO_CHAR(RDATE,"+"'yyyy-mm-dd')="+"'"+date+"'"
        b=Database(sql,1)
        list_a=[]
        list_b=[]
        for i in range(len(b)):
            list_a.append(b[i][0].strip())
        for i in range(len(list_a)):
            a=list_a[i].split(" ")
            r_hour=int(a[0].split(":")[0])
            r_min=int(a[0].split(":")[1])
            if r_hour>=Hour:
                a=(r_hour-Hour)*60
                b=r_min-Min
                if b<0:
                    b+=60
                    a-=60
                if a+b<=60 and a+b>=0:
                    temp=str(r_hour)+":"+"00"+" ~ "+str(r_hour+1)+":"+"00"
                    list_b.append(temp)
        if len(list_b)!=0:
            STR=""
            for i in range(len(list_b)):
                sql = 'select r.GAME,i.NAME,i.PHONE from reserve r, information i where r.RNUM=i.NUM and id=' + "'" + self.id + "' and TO_CHAR(RDATE,"+"'yyyy-mm-dd')="+"'"+date+"' and RTIME="+"'"+list_b[i]+"'"
                b=Database(sql,1)
                STR+=b[0][1].split()[0]+"("+b[0][0].split()[0]+")"+" 예약이 1시간 전입니다!\n문의사항 : 0"+str(b[0][2])+'\n'
            a=Messagebox(self,STR)
            a.move(470,320)
   #image load
    def Image(self,type):
        self.select=type
        if type=='축구':
            self.btselect.setStyleSheet('background-image : url(축구.png);')
        elif type=='풋살':
            self.btselect.setStyleSheet('background-image : url(풋살.png);')
        elif type=='농구':
            self.btselect.setStyleSheet('background-image : url(농구.png);')
        elif type=='족구':
            self.btselect.setStyleSheet('background-image : url(족구.png);')

