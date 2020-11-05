from PyQt5.QtCore import QTime,QThread,pyqtSignal
import time

class myThread(QThread):
    sinout = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
    def run(self):
        time.sleep(5)
        self.sinout.emit(print('aaaaa'))
        return