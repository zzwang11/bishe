from tools.read_conf import ReadConfig
from PyQt5.QtCore import QThread


class writeThread(QThread):
    def __init__(self, path='', mod='', add='', ip='', start='', stop='', averages='', power='', edelay='', ifband='',
                 points='',
                 outputfile=''):
        super().__init__()
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
            conf.setter('field', 'mod', self.mod)
        if self.add != '':
            conf.setter('field', 'add', self.add)
        if self.stop != '':
            conf.setter('field', 'stop', self.stop)
        if self.ip != '':
            conf.setter('field', 'ip', self.ip)
        if self.startp != '':
            conf.setter('field', 'start', self.startp)
        if self.averages != '':
            conf.setter('field', 'averages', self.averages)
        if self.power != '':
            conf.setter('field', 'power', self.power)
        if self.edelay != '':
            conf.setter('field', 'edelay', self.edelay)
        if self.ifband != '':
            conf.setter('field', 'ifband', self.ifband)
        if self.points != '':
            conf.setter('field', 'points', self.points)
        if self.outputfile != '':
            conf.setter('field', 'outputfile', self.outputfile)
        # if self.distance != '':
        #     conf.setter('field', 'distance', self.distance)

