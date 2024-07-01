import sys
from PyQt6.QtWidgets import *
from PySide6.QtGui import QGuiApplication

from datetime import *
import time as t
from mainwin import Ui_MainWindow
import threading
stop=0
def updatetime(win):
    while True:
        now = datetime.now()
        h = str(now.hour)
        m = str(now.minute)
        s = str(now.second)
        if(len(h) == 1):
            h = "0" + h
        if (len(m) == 1):
            m = "0" + m
        if (len(s) == 1):
            s = "0" + s
        time = f"{h}:{m}:{s}"
        win.lcdNumber.display(time)
        t.sleep(0.1)
        if stop == 1:
            return
def updatedate(win):
    while True:
        today = datetime.today()

        # 分别存入年、月、日三个变量
        y = str(today.year)
        m = str(today.month)
        d = str(today.day)
        if (len(y) == 1):
            y = "0" + y
        if (len(m) == 1):
            m = "0" + m
        if (len(d) == 1):
            d = "0" + d
        time = f"{y}-{m}-{d}"
        win.lcdNumber_2.display(time)
        t.sleep(0.1)
        if stop == 1:
            return
class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("background-color: #161616;")
        self.showFullScreen()
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber_2.setDigitCount(10)
        threading.Thread(target=updatetime,args=(self,)).start()
        threading.Thread(target=updatedate, args=(self,)).start()
        self.lcdNumber_2.setStyleSheet("color:#eeeeee")
        self.lcdNumber.setStyleSheet("color:#eeeeee")
    def resizeEvent(self, event):
        screen = QGuiApplication.primaryScreen().geometry()
        width = screen.width()  # 获取屏幕的宽
        height = screen.height()  # 获取屏幕的高
        print(width,height)
        self.lcdNumber_2.setGeometry(0,0,width,int(height/2))
        self.lcdNumber.setGeometry(0,int(height/2),width,int(height/2))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    app.exec()
    stop = 1
    main.close()

    sys.exit(0)