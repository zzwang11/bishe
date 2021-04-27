from tools.read_conf import ReadConfig
from PyQt5.QtCore import QThread


class writeThread(QThread):
    def __init__(self,sec, path='', mod='', add='', ip='', start='', stop='', averages='', power='', edelay='', ifband='',
                 points='',
                 outputfile=''):
        super().__init__()
        self.sec = sec
        self.path = path
        self.mod = mod
        self.add = add
        self.ip = ip
        self.startp = start
        self.stop = stop
        self.averages = averages
        self.power = power
        self.edelay = edelay
        self.ifband = ifband
        self.points = points
        self.outputfile = outputfile



    def run(self):
        conf = ReadConfig()
        if self.mod != '':
            conf.setter(self.sec, 'mod', self.mod)
        if self.add != '':
            conf.setter(self.sec, 'add', self.add)
        if self.stop != '':
            conf.setter(self.sec, 'stop', self.stop)
        if self.ip != '':
            conf.setter(self.sec, 'ip', self.ip)
        if self.startp != '':
            conf.setter(self.sec, 'start', self.startp)
        if self.averages != '':
            conf.setter(self.sec, 'averages', self.averages)
        if self.power != '':
            conf.setter(self.sec, 'power', self.power)
        if self.edelay != '':
            conf.setter(self.sec, 'edelay', self.edelay)
        if self.ifband != '':
            conf.setter(self.sec, 'ifband', self.ifband)
        if self.points != '':
            conf.setter(self.sec, 'points', self.points)
        if self.outputfile != '':
            conf.setter(self.sec, 'outputfile', self.outputfile)


