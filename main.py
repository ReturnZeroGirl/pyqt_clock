import sys
from PyQt6.QtWidgets import *

from datetime import *
import time as t
from mainwin import Ui_MainWindow
import threading
stop=0
def updatetime(win):
    while True:
        now = datetime.now()
        h = now.hour
        m = now.minute
        s = now.second
        time = f"{h}:{m}:{s}"
        win.lcdNumber.display(time)
        t.sleep(0.1)
        if stop == 1:
            return
def updatedate(win):
    while True:
        today = datetime.today()

        # 分别存入年、月、日三个变量
        y = today.year
        m = today.month
        d = today.day
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
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber_2.setDigitCount(10)
        threading.Thread(target=updatetime,args=(self,)).start()
        threading.Thread(target=updatedate, args=(self,)).start()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    app.exec()
    stop = 1
    main.close()

    sys.exit(0)