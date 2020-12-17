from control_vna.control import getdata
from tools.read_conf import ReadConfig
from PyQt5.QtCore import QThread,QMutex,QWaitCondition,pyqtSignal
import math
qmute = QMutex()
condi = QWaitCondition()


class suit_cla(QThread):
    mySig = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.flag = False

    def run(self):
        conf = ReadConfig()
        ip = conf.get('test_config','ip')
        stop = conf.get('test_config','stop')
        start = conf.get('test_config','start')
        averages = conf.get('test_config','averages')
        power = conf.get('test_config', 'power')
        edelay = conf.get('test_config', 'edelay')
        ifband = conf.get('test_config', 'ifband')
        points = conf.get('test_config', 'points')
        outputfile = conf.get('test_config', 'outputfile')
        inst = f'TCPIP::{ip}::inst0::INSTR'
        file_list = []
        if stop >3000:
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
                    file_list.append(getdata(inst, start0, stop0, averages, power, edelay, ifband, points, outputfile))
                except:
                    print("test fail")
                start0 += span
                stop0 += span
                j = j+span
                i = math.floor((j/(stop - start))*100)
                self.mySig.emit(i)
            file_list.append(getdata(inst, stop0, stop, averages, power, edelay, ifband, points, outputfile))
            self.mySig.emit(100)

        else:
            try:
                file_list.append(getdata(inst, start, stop, averages, power, edelay, ifband, points, outputfile))
            except:
                print("test fail")
            self.mySig.emit(100)


    def pause(self):
        self.flag = True

    def goon(self):
        self.flag = False
        condi.wakeOne()



