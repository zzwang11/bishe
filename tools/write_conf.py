from tools.read_conf import ReadConfig
from PyQt5.QtCore import QThread


class writeThread(QThread):
    def __init__(self, mod='', add='', ip='', start='', stop='', averages='', power='', edelay='', ifband='', points='',
                 outputfile='', distance='', r='', degree=''):
        super().__init__()
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
        self.distance = distance
        self.r = r
        self.degree = degree

    def run(self):
        conf = ReadConfig()
        if self.mod != '':
            conf.setter('test_config', 'mod', self.mod)
        if self.add != '':
            conf.setter('test_config', 'add', self.add)
        if self.stop != '':
            conf.setter('test_config', 'stop', self.stop)
        if self.ip != '':
            conf.setter('test_config', 'ip', self.ip)
        if self.startp != '':
            conf.setter('test_config', 'start', self.start)
        if self.averages != '':
            conf.setter('test_config', 'averages', self.averages)
        if self.power != '':
            conf.setter('test_config', 'power', self.power)
        if self.edelay != '':
            conf.setter('test_config', 'edelay', self.edelay)
        if self.ifband != '':
            conf.setter('test_config', 'ifband', self.ifband)
        if self.points != '':
            conf.setter('test_config', 'points', self.points)
        if self.outputfile != '':
            conf.setter('test_config', 'outputfile', self.outputfile)
        if self.distance != '':
            conf.setter('test_config', 'distance', self.distance)
        if self.r != '':
            conf.setter('test_config', 'r', self.r)
        if self.degree != '':
            conf.setter('test_config', 'degree', self.degree)