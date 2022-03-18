import sys, datetime
from PyQt5.QtWidgets import *

class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog=None
        self.txt_id=QLineEdit(self)
        self.txt_pwd = QLineEdit(self)
        self.initUI()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
