import os
from PyQt5.QtCore import QThread,pyqtSignal
import pyvisa


class TestCon(QThread):
    myOut = pyqtSignal(int)

    def __init__(self, ip,rm):
        super().__init__()
        self.ip = ip
        self.rm = rm

    def run(self):

        try:
            self.inst = self.rm.open_resource(self.ip)
            if self.inst.query('*IDN?'):
                self.myOut.emit(1)
            else:
                self.myOut.emit(0)
        except:
            self.myOut.emit(0)

