from PyQt5.QtCore import QTime,QThread,pyqtSignal,QMutex,QWaitCondition
import time
# import win32con
# 线程锁
qmute = QMutex()
condi = QWaitCondition()
class myThread(QThread):
    def __init__(self):
        super().__init__()
        self.working = True
        self.flag = False

    # def __del__(self):
    #     self.working = False
    #     # self.quit()

    def pause(self):
        self.flag = True
    def run(self):

        i = 1
        while self.working:
            i += 1
            time.sleep(1)
            print(i)
            with open('./save/1.txt','a') as f:
                f.write('hahaha\n')
            if(self.flag):
                qmute.lock()
                condi.wait(qmute)
                qmute.unlock()




