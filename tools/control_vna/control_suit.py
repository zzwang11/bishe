from tools.control_vna.control import getdata
from tools.read_conf import ReadConfig
from PyQt5.QtCore import QThread, QMutex, QWaitCondition, pyqtSignal
import math

qmute = QMutex()
condi = QWaitCondition()


class suit_cla(QThread):
    mySig = pyqtSignal(int)
    mySig1 = pyqtSignal()

    def __init__(self, data):
        super().__init__()
        self.flag = False
        self.data = data

    def run(self):
        conf = ReadConfig()
        try:
            mod = conf.get('test_config', 'mod')
            ip = conf.get('test_config', 'ip')
            stop = float(conf.get('test_config', 'stop'))
            start = float(conf.get('test_config', 'start'))
            averages = int(conf.get('test_config', 'averages'))
            power = float(conf.get('test_config', 'power'))
            edelay = float(conf.get('test_config', 'edelay'))
            ifband = float(conf.get('test_config', 'ifband'))
            points = int(conf.get('test_config', 'points'))
            outputfile = conf.get('test_config', 'outputfile')
            inst = f'TCPIP::{ip}::inst0::INSTR'
        except:
            self.mySig1.emit()
            return
        file_list = []
        if stop > 3000:
            span = 200
        else:
            span = 50
        if stop - start > span:
            j = 0
            start0 = start
            stop0 = start + span
            while stop0 < stop:

                if self.flag:
                    qmute.lock()
                    condi.wait(qmute)
                    qmute.unlock()
                try:
                    file_list.append(
                        getdata(inst, mod, self.data, start0, stop0, averages, power, edelay, ifband, points,
                                outputfile))
                except:
                    print("test fail")
                start0 += span
                stop0 += span
                j = j + span
                i = math.floor((j / (stop - start)) * 100)
                self.mySig.emit(i)
            file_list.append(
                getdata(inst, mod, self.data, stop0, stop, averages, power, edelay, ifband, points, outputfile))
            self.mySig.emit(100)

        else:
            try:
                file_list.append(
                    getdata(inst, mod, self.data, start, stop, averages, power, edelay, ifband, points, outputfile))
            except:
                print("test fail")
            self.mySig.emit(100)

    def pause(self):
        self.flag = True

    def goon(self):
        self.flag = False
        condi.wakeOne()
