import os
from PyQt5.QtCore import QThread,pyqtSignal
import pyvisa


class TestCon(QThread):
    myOut = pyqtSignal(int)

    def __init__(self, ins):
        super().__init__()
        self.ins = ins

    def run(self):
        rm = pyvisa.ResourceManager()
        try:
            inst = rm.open_resource(self.ins)
            if inst.query('*IDN?'):
                self.myOut.emit(1)
            else:
                self.myOut.emit(0)
        except:
            self.myOut.emit(0)