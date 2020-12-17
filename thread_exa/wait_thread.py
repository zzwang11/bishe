from PyQt5.QtCore import QTime,QThread,pyqtSignal,QMutex,QWaitCondition,pyqtSignal
import time
# import win32con
# 线程锁
qmute = QMutex()
condi = QWaitCondition()
class myThread(QThread):
    mySig = pyqtSignal(int)
    mySig1 = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.working = True
        self.flag = False

    # def __del__(self):
    #     self.working = False
    #     # self.quit()

    def pause(self):
        self.flag = True

    def goon(self):
        self.flag = False
        condi.wakeAll()

    def run(self):
        i = 1
        with open('./save/1.txt', 'w') as f:
            f.write('')

        while self.working:
            i += 1
            time.sleep(1)

            with open('./save/1.txt','a') as f:
                f.write(str(i)+'\n')
            if self.flag:
                qmute.lock()
                condi.wait(qmute)
                qmute.unlock()

            self.mySig.emit(i%10)
            self.mySig1.emit()









