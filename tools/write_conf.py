from tools.read_conf import ReadConfig
from PyQt5.QtCore import QThread


class writeThread(QThread):
    def __init__(self, mod, add='', ip='', start='', stop='', averages='', power='', edelay='', ifband='', points='',
                 outputfile='', distance='', r='', degree=''):
        super().__init__()
        self.mod = mod
        self.add = add
        self.ip = ip
        self.start = start
        self.span = stop
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
            conf.set('test_config', 'mod', self.mod)
        if self.add != '':
            conf.set('test_config', 'add', self.add)
        if self.stop != '':
            conf.set('test_config', 'stop', self.stop)
        if self.ip != '':
            conf.set('test_config', 'ip', self.ip)
        if self.start != '':
            conf.set('test_config', 'start', self.start)
        if self.averages != '':
            conf.set('test_config', 'averages', self.averages)
        if self.power != '':
            conf.set('test_config', 'power', self.power)
        if self.edelay != '':
            conf.set('test_config', 'edelay', self.edelay)
        if self.ifband != '':
            conf.set('test_config', 'ifband', self.ifband)
        if self.points != '':
            conf.set('test_config', 'points', self.points)
        if self.outputfile != '':
            conf.set('test_config', 'outputfile', self.outputfile)
        if self.distance != '':
            conf.set('test_config', 'outputfile', self.distance)
        if self.r != '':
            conf.set('test_config', 'outputfile', self.r)
        if self.degree != '':
            conf.set('test_config', 'outputfile', self.degree)