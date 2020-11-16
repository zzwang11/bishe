from tools.read_conf import ReadConfig
from PyQt5.QtCore import QThread


class writeThread(QThread):
    def __init__(self,ip, centerf, span, temp, averages, power, edelay, ifband, points, outputfile):
        super().__init__()
        self.ip = ip
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
        conf = ReadConfig()
        if self.span != '':
            conf.set('test_config','span',self.span)
        if self.ip != '':
            conf.set('test_config','ip',self.ip)
        if self.centerf != '':
            conf.set('test_config','centerf',self.centerf)
        if self.temp != '':
            conf.set('test_config','temp',self.temp)
        if self.averages != '':
            conf.set('test_config','averages',self.averages)
        if self.power != '':
            conf.set('test_config', 'power',self.power)
        if self.edelay != '':
            conf.set('test_config', 'edelay',self.edelay)
        if self.ifband != '':
            conf.set('test_config', 'ifband',self.ifband)
        if self.points != '':
            conf.set('test_config', 'points',self.points)
        if self.outputfile != '':
            conf.set('test_config', 'outputfile',self.outputfile)
