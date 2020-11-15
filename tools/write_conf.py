from tools.read_conf import ReadConfig
from PyQt5.QtCore import QThread


class writeThread(QThread):
    def __init__(self,inst, centerf, span, temp, averages, power, edelay, ifband, points, outputfile):
        super().__init__()
        self.inst = inst
        self.centerf = centerf
        self.span = span
        self.temp = temp
        self.averages = averages
        self.power = power
        self.edelay = edelay
        self.ifband = ifband
        self.points = points
        self.outputfile = outputfile


    def run(self):
        self.write(self.inst, self.centerf, self.span, self.temp, self.averages, self.power, self.edelay, self.ifband, self.points, self.outputfile)

    def write(self,inst, centerf, span, temp, averages, power, edelay, ifband, points, outputfile):
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
