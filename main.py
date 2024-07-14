import sys
from PyQt6.QtWidgets import *

from datetime import *
import time as t
from mainwin import Ui_MainWindow
import threading
stop=0
def updatetime_ms(win):
    while True:
        now = datetime.now()
        h = str(now.hour)
        m = str(now.minute)
        s = str(now.second)
        ms = str(now.microsecond // 1000)
        if(len(h) == 1):
            h = "0" + h
        if (len(m) == 1):
            m = "0" + m
        if (len(s) == 1):
            s = "0" + s
        if(len(ms) == 1):
            ms = "00" + ms
        if(len(ms) == 2):
            ms = "0" + ms
        time = f"{h}:{m}:{s}:{ms}"
        win.lcdNumber.display(time)
        t.sleep(0.001)
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
        self.show()
        self.lcdNumber.setDigitCount(12)
        self.lcdNumber_2.setDigitCount(10)
        threading.Thread(target=updatetime_ms,args=(self,)).start()
        threading.Thread(target=updatedate, args=(self,)).start()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    app.exec()
    stop = 1
    main.close()

    sys.exit(0)