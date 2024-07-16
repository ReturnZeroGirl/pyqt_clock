import sys
import time

from PyQt6.QtWidgets import *

from datetime import *
import time as t
from mainwin import Ui_MainWindow
import threading


stop = 0
tm_stop = 0
tmstatus = 0
tmts = 0


def updatetime_ms(win):
    while True:
        now = datetime.now()
        h = str(now.hour)
        m = str(now.minute)
        s = str(now.second)
        ms = str(now.microsecond // 1000)
        if (len(h) == 1):
            h = "0" + h
        if (len(m) == 1):
            m = "0" + m
        if (len(s) == 1):
            s = "0" + s
        if (len(ms) == 1):
            ms = "00" + ms
        if (len(ms) == 2):
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


def updateweekday(win):
    while True:
        now = datetime.now()

        # 获取当前是星期几，返回值是一个整数（0代表星期一，1代表星期二，...，6代表星期日）
        weekday = now.weekday()

        # 将返回的整数转换为实际的星期几名称
        weekdays = ['1', '2', '3', '4', '5', '6', '8']
        current_weekday = weekdays[weekday]

        win.lcdNumber_3.display(current_weekday)
        t.sleep(0.1)
        if stop == 1:
            return


def starttime(win):
    global tmts
    while True:
        t.sleep(1)
        if (tm_stop == 1 or stop == 1):
            return
        tmts += 1
        timeh = tmts // 3600
        timem = tmts % 3600 // 60
        times = tmts % 60
        time = f"{timeh}:{timem}:{times}"
        l = len(str(time))
        win.lcdNumber_4.setDigitCount(l)
        win.lcdNumber_4.display(time)


class MainWidget(QMainWindow, Ui_MainWindow):
    def bc(self):
        global tmstatus
        global tm_stop
        tmstatus += 1
        if (tmstatus % 2 == 0):
            self.pushButton.setText("启动秒表")
            self.pushButton_2.setEnabled(True)
            tm_stop = 1
        if (tmstatus % 2 != 0):
            self.pushButton.setText("停止秒表")
            self.pushButton_2.setEnabled(False)
            tm_stop = 0
            threading.Thread(target=starttime, args=(self,)).start()

    def resetz(self):
        global tmts
        tmts = 0
        self.lcdNumber_4.display(tmts)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.lcdNumber.setDigitCount(12)
        self.lcdNumber_2.setDigitCount(10)
        self.lcdNumber_3.setDigitCount(1)
        self.lcdNumber_4.setDigitCount(5)
        self.lcdNumber_4.display("0:0:0")
        self.pushButton.clicked.connect(self.bc)
        self.pushButton_2.clicked.connect(self.resetz)
        threading.Thread(target=updatetime_ms, args=(self,)).start()
        threading.Thread(target=updatedate, args=(self,)).start()
        threading.Thread(target=updateweekday, args=(self,)).start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    main.setFixedSize(350, 300)
    app.exec()
    stop = 1
    main.close()
    sys.exit(0)
