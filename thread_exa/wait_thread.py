from PyQt5.QtCore import QTime,QThread,pyqtSignal,QMutex,QWaitCondition,pyqtSignal
import time
# import win32con
# 线程锁
qmute = QMutex()
condi = QWaitCondition()


class myThread(QThread):
    mySig = pyqtSignal(int)
    mySig1 = pyqtSignal()
    mySig2 = pyqtSignal()
    def __init__(self,state):
        super().__init__()
        self.working = True
        self.flag = False
        self.state = state

    # def __del__(self):
    #     self.working = False
    #     # self.quit()

    def pause(self):
        self.flag = True

    def goon(self):
        self.flag = False
        condi.wakeAll()

    def fun(self,i,a):
        if a == 1:
            return i*5
        else:
            return i**2
    def run(self):
        i = 1
        if self.state == "线缆连接测量":
            path = './save/1.txt'
            s = 1
        else:
            path = './save/2.txt'
            s = 2
        with open(path, 'w') as f:
            f.write('')

        while self.working:
            i += 1
            time.sleep(1)

            with open(path,'a') as f:
                f.write(str(self.fun(i,s))+'\n')
            if self.flag:
                qmute.lock()
                condi.wait(qmute)
                qmute.unlock()

            self.mySig.emit(i%10)
            self.mySig1.emit()
            if i == 10:
                self.mySig2.emit()
                break









