import datetime
import database
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Inquiry(QDialog):
    def __init__(self,id):
        super().__init__()
        self.id = id
        self.table = QTableWidget()
        self.row=None
        self.dialog=None
        self.initUI()
    def initUI(self):
        date=str(datetime.datetime.now().date())
        sql = 'select r.RDATE, r.RTIME, r.GAME, i.NAME, i.ADDRESS, i.PHONE from reserve r, information i where RDATE>='+"'"+date+"' and id="+"'"+self.id+"' and r.RNUM=i.NUM order by r.RDATE,r.RTIME"
        b=Database(sql,1)
        delbtn=QPushButton("",self)
        delbtn.setStyleSheet('background-image: url(삭제.png);')
        delbtn.setFixedSize(97,45)
        delbtn.clicked.connect(self.Delete)
        backbtn=QPushButton("",self)
        backbtn.setStyleSheet('background-image: url(이전.png);')
        backbtn.setFixedSize(113,45)
        backbtn.clicked.connect(self.Back)
        self.table.setColumnCount(6)
        self.table.setRowCount(100)
        self.table.setHorizontalHeaderLabels(('날짜','시간','종목','경기장','경기장 주소','경기장 연락처'))
        self.table.setColumnWidth(2, 40)
        self.table.setColumnWidth(4, 200)
        self.table.setColumnWidth(5, 100)
        self.table.cellClicked.connect(self.ROW)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFont(QFont('고딕', 10))
        for i in range(len(b)):
            for j in range(6):
                if j==0:
                    STR=str(b[i][j]).split(" ")[0]
                elif j==5:
                    STR=str(b[i][j])
                    list_a=list(STR)
                    list_a.insert(0,'0')
                    list_a.insert(3,'-')
                    list_a.insert(7,'-')
                    STR="".join(list_a)
                else:
                    STR=b[i][j].strip()
                self.table.setItem(i,j,QTableWidgetItem(STR))
                self.table.item(i, j).setTextAlignment(132 | 128)
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(delbtn)
        layout.addWidget(backbtn)
        backgroundlmage = QImage('init.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(backgroundlmage))
        self.setWindowIcon(QIcon('아이콘.png'))
        self.setWindowTitle('예약 조회')
        self.setPalette(palette)
        self.setLayout(layout)
        self.resize(500, 500)
        self.show()
    def Back(self):
        self.setVisible(False)
        reserve(self.id)
    def Delete(self):
        try:
            date=self.table.item(self.row,0).text()
            time=self.table.item(self.row,1).text()
            game=self.table.item(self.row,2).text()
            sign=0
            R_hour=int(time.split(":")[0])
            R_min=int(time.split(":")[2])
            Day = datetime.datetime.now()
            now_date=str(Day.date())
            Hour = Day.time().hour
            Min = Day.time().minute
            if date==now_date:
                if R_hour >= Hour:
                    a = (R_hour - Hour) * 60
                    b = R_min - Min
                    if b < 0:
                        b += 60
                        a -= 60
                    if a + b <= 60 :
                        sign=1
                else:
                    sign=1
            else:
                sign=0
            if sign==1:
                Messagebox(self,"예약 취소가 불가합니다.")
            else:
                self.dialog=Check(self.id,date,time,game)
        except:
            Messagebox(self,"빈 셀을 선택했습니다.")
    def ROW(self):
        self.row=self.table.currentRow()

class Detail(QDialog):
    date_tuple=('09:00 ~ 10:00','10:00 ~ 11:00','11:00 ~ 12:00','12:00 ~ 13:00','13:00 ~ 14:00','14:00 ~ 15:00','15:00 ~ 16:00','16:00 ~ 17:00','17:00 ~ 18:00')
    def __init__(self,game,id,num,date):
        super().__init__()
        self.dialog = None
        self.game=game
        self.id=id
        self.num=num
        self.date=date
        self.table = QTableWidget()
        self.initUI()
    def initUI(self):
        self.table.setColumnCount(1)
        self.table.setColumnWidth(0,145)
        self.table.setRowCount(9)
        self.table.setHorizontalHeaderLabels(('예약자 성명',))
        self.table.setVerticalHeaderLabels(self.date_tuple)
        self.table.cellDoubleClicked.connect(self.cli)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFont(QFont('HY견고딕',10))
        sentance = 'r.game=' + "'" + self.game + "'" + ' and r.RNUM=' + "'" + str(self.num) + "'" + " and TO_CHAR(r.RDATE, 'yyyy-mm-dd')=" + "'" + self.date + "'"
        sql = 'select r.rtime,l.name from reserve r, login l where r.id=l.id and ' + sentance
        b = Database(sql,1)
        for i in range(len(b)):
            DATE = b[i][0].strip()
            STR = b[i][1].strip()
            for j in range(len(self.date_tuple)):
                if self.date_tuple[j] == DATE:
                    self.table.setItem(j, 0, QTableWidgetItem(STR.replace(STR[1], '*')))
                    self.table.item(j, 0).setTextAlignment(132 | 128)
                    self.table.item(j, 0).setBackground(QColor(255, 148, 153))
        back = QPushButton('', self)
        back.clicked.connect(self.back)
        back.setFixedSize(277,30)
        back.setStyleSheet('background-image : url(BACK.png);')
        layout=QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(back)
        self.setLayout(layout)
        palette = QPalette()
        palette.setBrush(10, QColor(244, 249, 255))
        self.setWindowIcon(QIcon('아이콘.png'))
        self.setWindowTitle('세부 사항')
        self.setPalette(palette)
        self.resize(300, 300)
        self.show()
    def Sametime(self):
        Time=self.date_tuple[self.table.currentRow()]
        sql = "select id from reserve where TO_CHAR(RDATE,'yyyy-mm-dd')=" + "'" + self.date + "'" + ' and RTIME=' + "'" + Time + "'"+"and ID="+"'"+self.id+"'"
        same = Database(sql,1)
        if same == []:
            return False
        else:
            return True
    def overlap(self):
        sql="select id from reserve where TO_CHAR(RDATE,'yyyy-mm-dd')="+"'"+self.date+"'"+' and GAME='+"'"+self.game+"'"+" and ID="+"'"+self.id+"'"
        over=Database(sql,2)
        if over==[]:
            return False
        else:
            return True
    def cli(self):
        if self.table.currentItem()==None:
            if self.overlap()==True:
                Messagebox(self,"이미 예약 되었습니다.")
            else:
                if self.Sametime()==True:
                    Messagebox(self,"같은 시간대에 다른 종목이 예약되어 있습니다.")
                else:
                    now_date=str(datetime.datetime.now().date())
                    if now_date==self.date:
                        now_time = datetime.datetime.now().time()
                        now_hour = now_time.hour
                        re_hour = self.date_tuple[self.table.currentRow()]
                        temp = re_hour.split(" ")[0].split(":")[0]
                        if now_hour>=int(temp):
                            signal=0
                        else:
                            signal=1
                    else:
                        signal=1

                    if signal==0:
                        text="이미 시간이 지난 예약입니다."
                    else:
                        sql='insert into reserve values('+"'"+self.id+"',"+"'"+self.game+"',"+"'"+self.date_tuple[self.table.currentRow()]+"',"+"'"+self.date+"',"+"'"+str(self.num)+"')"
                        Database(sql,0)
                        text = "예약되었습니다."
                    Messagebox(self,text)
        else:
            Messagebox(self,"이미 예약자가 존재합니다.")
    def back(self):
        self.setVisible(False)
        self.dialog=Date_Select(self.game,self.id,self.num)
class Date_Select(QDialog):
    def __init__(self,game,id,num):
        super().__init__()
        self.dialog = None
        self.game=game
        self.id=id
        self.num=num
        self.Date = QCalendarWidget(self)
        self.initUI()
    def initUI(self):
        self.Date.setGeometry(10,10,280,280)
        self.Date.setGridVisible(True)
        self.Date.activated.connect(self.plan)
        palette = QPalette()
        palette.setBrush(10, QColor(244, 249,255))
        self.setWindowIcon(QIcon('아이콘.png'))
        self.setWindowTitle('날짜 선택')
        self.setPalette(palette)
        self.resize(300, 300)
        self.show()
    def plan(self):
        cur=datetime.datetime.now().date()
        temp=self.Date.selectedDate().toString('yyyy-MM-dd').split('-')
        if int(temp[0])<cur.year:
            signal=0
        elif int(temp[0])==cur.year:
            if int(temp[1])<cur.month:
                signal=0
            elif int(temp[1])==cur.month:
                if int(temp[2])<cur.day:
                    signal=0
                else:
                    if int(temp[2])<=cur.day+14:
                        signal=1
                    else:
                        signal=0
            else:
                if int(temp[1])-cur.month==1:
                    total=14+cur.day
                    if cur.month==2:
                        var=28
                    elif cur.month==4 or cur.month==6 or cur.month==9 or cur.month==11:
                        var=30
                    else:
                        var=31
                    if total>=var:
                        total-=var
                        if total>=int(temp[2]):
                            signal=1
                        else:
                            signal=0
                    else:
                        signal=0
                else:
                    signal=0
        else:
            if cur.month==12 and int(temp[1])==1 and int(temp[0])-cur.year==1:
                total=14+cur.day
                if total>=31:
                    total-=31
                    if total>=int(temp[2]):
                        signal=1
                    else:
                        signal=0
                else:
                    signal=0
            else:
                signal=0
        if signal==0:
            Messagebox(self,"예약할 수 없는 날짜 입니다.")
        else:
            self.setVisible(False)
            self.dialog=Detail(self.game,self.id,self.num,self.Date.selectedDate().toString('yyyy-MM-dd'))
class reserve_d(QDialog):
    def __init__(self, type,id):
        super().__init__()
        self.dialog=None
        self.type = type
        self.id=id
        self.Date=None
        self.initUI()
    def initUI(self):
        label=QLabel(self.type,self)
        label.setGeometry(230,5,100,50)
        label.setFont(QFont('HY헤드라인M',20))
        btn1 = QPushButton('', self)
        btn1.setStyleSheet('background-image:url(스포츠파크.png);')
        btn1.setGeometry(30, 70, 200, 180)
        btn1.clicked.connect(lambda:self.select(1))
        label1=QLabel('스포츠파크(문산)',self)
        label1.setGeometry(82,255,120,20)
        label1.setFont(QFont('HY견고딕',10))
        btn2 = QPushButton('', self)
        btn2.setGeometry(265, 70, 200, 180)
        btn2.setStyleSheet('background-image:url(종합경기장.png);')
        btn2.clicked.connect(lambda: self.select(2))
        label2=QLabel('종합경기장(충무공동)',self)
        label2.setGeometry(305,255,140,20)
        label2.setFont(QFont('HY견고딕',10))
        btn3 = QPushButton('', self)
        btn3.setGeometry(30, 280, 200, 180)
        btn3.setStyleSheet('background-image:url(모덕구장.png);')
        btn3.clicked.connect(lambda: self.select(3))
        label3=QLabel('모덕체육구장(상대동)',self)
        label3.setGeometry(70,465,130,20)
        label3.setFont(QFont('HY견고딕',10))
        btn4 = QPushButton('', self)
        btn4.setGeometry(265, 280, 200, 180)
        btn4.setStyleSheet('background-image:url(와룡지구.png);')
        btn4.clicked.connect(lambda: self.select(4))
        label4=QLabel('와룡지구체육시설(금산)',self)
        label4.setGeometry(295,465,150,20)
        label4.setFont(QFont('HY견고딕',10))
        if self.type=='농구':
            btn3.setStyleSheet('background-image:url(모덕사용불가.png);')
            label3.setText('모덕체육구장(X)')
            label3.setGeometry(82, 465, 130, 20)
            btn4.setStyleSheet('background-image:url(와룡사용불가.png);')
            label4.setText('와룡지구체육시설(X)')
            label4.setGeometry(300,465,150,20)
            btn3.setEnabled(False)
            btn4.setEnabled(False)
        elif self.type=='족구':
            btn1.setStyleSheet('background-image:url(파크사용불가.png);')
            label1.setText('스포츠파크(X)')
            label1.setGeometry(87, 255, 120, 20)
            btn2.setStyleSheet('background-image:url(종합사용불가.png);')
            label2.setText('종합경기장(X)')
            label2.setGeometry(325, 255, 140, 20)
            btn1.setEnabled(False)
            btn2.setEnabled(False)
        back=QPushButton('',self)
        back.setGeometry(0,0,46,36)
        back.clicked.connect(self.back)
        back.setStyleSheet('''
                       QPushButton{background-image: url(뒤로가기.png); border:0px;} 
                       QPushButton:hover{background-image: url(뒤로가기2.png); border:0px;}
                       ''')
        lmage = QImage('white.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(lmage))
        self.setWindowIcon(QIcon('아이콘.png'))
        self.setWindowTitle('경기장 선택')
        self.setPalette(palette)
        self.resize(500,500)
        self.show()
    def select(self,num):
        self.Date=Date_Select(self.type,self.id,num)
    def back(self):
        self.setVisible(False)
        self.dialog=reserve(self.id)
class Check(QDialog):
    def __init__(self, id,date,time,game):
        super().__init__()
        self.id = id
        self.date=date
        self.time=time
        self.game=game
        self.tet=QLineEdit("", self)
        self.initUI()
    def initUI(self):
        self.tet.setGeometry(130, 63, 120, 25)
        self.tet.setEchoMode(2)
        btn = QPushButton("", self)
        btn.setGeometry(90, 140, 113, 45)
        btn.clicked.connect(self.boan)
        btn.setStyleSheet('background-image: url(취소.png);')
        backgroundlmage = QImage('취소확인.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(backgroundlmage))
        self.setWindowIcon(QIcon('아이콘.png'))
        self.setWindowTitle('취소 화면')
        self.setPalette(palette)
        self.resize(300, 200)
        self.show()
    def boan(self):
        sql = 'select password from login where id='+"'"+self.id+"'"
        a=Database(sql,1)
        b=a[0][0].strip()
        if b==self.tet.text():
            sql = 'delete reserve where TO_CHAR(RDATE,' + "'yyyy-mm-dd')=" + "'" + self.date + "' and RTIME=" + "'" + self.time + "' and GAME=" + "'" + self.game + "'"
            Database(sql,0)
            self.setVisible(False)
        else:
            Messagebox(self,"비밀번호가 틀렸습니다.")

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
    def Inquiry2(self):
        self.dialog=Inquiry(self.id)
        self.setVisible(False)
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
    def detail(self):
        self.setVisible(False)
        self.dialog=reserve_d(self.select,self.id)

