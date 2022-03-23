import database as db
import main
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#management home
class Management_list(QDialog):
    def __init__(self,date):
        super().__init__()
        self.date=date
        self.dialog=None
        self.table = QTableWidget(self)
        self.initUI()
    def initUI(self):
        label=QLabel(self.date,self)
        label.setGeometry(185,110,180,35)
        label.setFont(QFont('HY헤드라인M',18))
        btn=QPushButton("",self)
        btn.setGeometry(5,400,80,100)
        btn.setStyleSheet('color:white; border:0px;')
        btn.clicked.connect(self.back)
        self.table.setGeometry(17,150,465,250)
        self.table.setColumnCount(5)
        self.table.setColumnWidth(0,145)
        self.table.setHorizontalHeaderLabels(('예약 시간','경기장','예약 종목','전화번호','이름'))
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 130)
        self.table.setColumnWidth(2, 60)
        self.table.setColumnWidth(3, 150)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setWindowIcon(QIcon('image/아이콘.png'))
        self.setWindowTitle('예약자 명단')
        self.table.setFont(QFont('HY견고딕',10))
        backgroundlmage = QImage('image/관리자모드.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(backgroundlmage))
        self.setPalette(palette)
        self.resize(500, 500)
        self.show()
        sentance="where l.id=r.id and i.num=r.rnum and TO_CHAR(rdate,'yyyy-mm-dd')="+"'"+self.date+"' order by rtime,rnum"
        sql="select rtime,i.name,game,l.phone,l.name from login l,reserve r, information i "+sentance
        b=db.Database(sql,1)
        self.table.setRowCount(len(b))
        for i in range(len(b)):
            time = b[i][0].strip()
            location = b[i][1].strip()
            game=b[i][2].strip()
            phone='0'+str(b[i][3])
            ph="-".join([phone[:3],phone[3:7],phone[7:11]])
            name=b[i][4].strip()
            self.table.setItem(i, 0, QTableWidgetItem(time))
            self.table.item(i, 0).setTextAlignment(132|128)
            self.table.setItem(i, 1, QTableWidgetItem(location))
            self.table.item(i, 1).setTextAlignment(132 | 128)
            self.table.setItem(i, 2, QTableWidgetItem(game))
            self.table.item(i, 2).setTextAlignment(132 | 128)
            self.table.setItem(i, 3, QTableWidgetItem(ph))
            self.table.item(i, 3).setTextAlignment(132 | 128)
            self.table.setItem(i, 4, QTableWidgetItem(name))
            self.table.item(i, 4).setTextAlignment(132 | 128)
    def back(self):
        self.setVisible(False)
        self.dialog=Management()
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
        backgroundlmage = QImage('image/관리자모드.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(backgroundlmage))
        self.setWindowIcon(QIcon('image/아이콘.png'))
        self.setWindowTitle('날짜 선택')
        self.setPalette(palette)
        self.resize(500, 500)
        self.show()
    def back(self):
        self.setVisible(False)
        self.dialog=main.Login()
    def Rlist(self):
        self.setVisible(False)
        temp = self.Date.selectedDate().toString('yyyy-MM-dd')
        self.dialog=Management_list(temp)