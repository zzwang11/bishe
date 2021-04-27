from tools.control_vna.control1 import getdata
from tools.read_conf import ReadConfig
from PyQt5.QtCore import QThread, QMutex, QWaitCondition, pyqtSignal
import math

qmute = QMutex()
condi = QWaitCondition()


class suit_cla(QThread):
    mySig = pyqtSignal(int)
    mySig1 = pyqtSignal(str)
    mySig2 = pyqtSignal()

    def __init__(self, li,data, inst):
        super().__init__()
        self.flag = False
        self.li = li
        self.data = data
        self.inst = inst

    def run(self):

        mod = self.li[0]

        stop = float(self.li[4])
        start = float(self.li[3])
        averages = int(self.li[6])
        power = float(self.li[7])
        edelay = float(self.li[8])
        ifband = float(self.li[5])
        points = int(self.li[9])
        outputfile = self.li[10]
        # inst = f'TCPIP::{ip}::inst0::INSTR'
        # inst = ip


        ss = getdata(self.inst, mod, self.data, start, stop, averages, power, edelay, ifband, points,outputfile)
        self.mySig.emit(100)
        self.mySig1.emit(ss)
        self.mySig2.emit()




