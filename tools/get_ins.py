import os
from PyQt5.QtCore import QThread,pyqtSignal
import pyvisa


class GetCon(QThread):
    myOut = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()


    def run(self):
        rm = pyvisa.ResourceManager()
        try:
            inst = rm.list_resources()
            self.myOut.emit(inst)
        except:
            a = tuple()
            self.myOut.emit(a)