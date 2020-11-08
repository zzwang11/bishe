from PyQt5.QtCore import QTime,QThread,pyqtSignal,QMutex
import time
# import win32con

qmute = QMutex()
class myThread(QThread):
    def __init__(self):
        super().__init__()
        self.working = True

    # def __del__(self):
    #     self.working = False
    #     # self.quit()


    def run(self):
        # qmute.lock()
        i = 1
        while self.working:
            i += 1
            time.sleep(1)
            print(i)
            with open('./save/1.txt','a') as f:
                f.write('hahaha\n')
        # qmute.unlock()


