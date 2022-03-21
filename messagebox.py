from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def Messagebox(durl,message):
    msgBox = QMessageBox(durl)
    msgBox.setWindowTitle("알림창")
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(message)
    msgBox.setFont(QFont('HY헤드라인M', 12))
    msgBox.setStandardButtons(QMessageBox.Cancel)
    msgBox.show()
    return msgBox