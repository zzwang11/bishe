from control_vna.control import getdata
from tools.read_conf import ReadConfig
from PyQt5.QtCore import QThread,QMutex,QWaitCondition,pyqtSignal

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
        span = conf.get('test_config','span')
        centerf = conf.get('test_config','centerf')
        temp = conf.get('test_config','temp')
        averages = conf.get('test_config','averages')
        power = conf.get('test_config', 'power')
        edelay = conf.get('test_config', 'edelay')
        ifband = conf.get('test_config', 'ifband')
        points = conf.get('test_config', 'points')
        outputfile = conf.get('test_config', 'outputfile')
        inst = f'TCPIP::{ip}::inst0::INSTR'
        file_list = []
        errormsg = 0
        if span > 200:
            ad = centerf-span/2
            while ad<centerf+span/2:
                if self.flag:
                    qmute.lock()
                    condi.wait(qmute)
                    qmute.unlock()
                try:
                    file_list.append(getdata(inst, ad+100, 200, temp, averages, power, edelay, ifband, points, outputfile))
                except:
                    errormsg = 1
                ad += 200
        else:
            try:
                file_list.append(getdata(inst, centerf, span, temp, averages, power, edelay, ifband, points, outputfile))
            except:
                errormsg = 1
        self.mySig.emit(errormsg)

    def pause(self):
        self.flag = True

    def goon(self):
        self.flag = False
        condi.wakeOne()



