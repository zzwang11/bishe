from tools.read_conf import ReadConfig
from PyQt5.QtCore import QThread


class writeThread(QThread):
    def __init__(self,):
        super().__init__()

    def run(self):
        self.wri()

    def wri(self, inst, centerf, span, temp, averages, power, edelay, ifband, points, outputfile):
        write(inst, centerf, span, temp, averages, power, edelay, ifband, points, outputfile)

def write(inst, centerf, span, temp, averages, power, edelay, ifband, points, outputfile):
    conf = ReadConfig()
    conf.set('test_config','span',span)
    conf.set('test_config','inst',inst)
    conf.set('test_config','conterf',centerf)
    conf.set('test_config','temp',temp)
    conf.set('test_config','averages',averages)
    conf.set('test_config', 'power',power)
    conf.set('test_config', 'edelay',edelay)
    conf.set('test_config', 'ifband',ifband)
    conf.set('test_config', 'points',points)
    conf.set('test_config', 'outputfile',outputfile)
