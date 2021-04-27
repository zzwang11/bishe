import configparser
import os
from PyQt5.QtCore import QThread, pyqtSignal


class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            self.configpath = filepath
        else:
            self.configpath = 'h:/bishe/config.ini'
        self.cf = configparser.ConfigParser()
        self.cf.read(self.configpath)

    def get(self, *param):
        try:
            value = self.cf.get(*param)
        except:
            value = "未读取到"
        return value

    def setter(self, *param):
        try:
            self.cf.set(*param)
            self.cf.write(open(self.configpath, 'w'))
            a = 0
        except:
            a = "写入失败"
        return a


class MyTh(QThread):
    myOut = pyqtSignal(list)

    def __init__(self, param, path=None):
        super().__init__()
        self.param = param
        self.path = path

    def run(self):
        a = ReadConfig(self.path)
        b = []
        mod = a.get(self.param, 'mod')
        add = a.get(self.param, 'add')
        ip = a.get(self.param, 'ip')
        start = a.get(self.param, 'start')
        stop = a.get(self.param, 'stop')
        ifband = a.get(self.param, 'ifband')
        averages = a.get(self.param, 'averages')
        power = a.get(self.param, 'power')
        edelay = a.get(self.param, 'edelay')
        points = a.get(self.param, 'points')
        outputfile = a.get(self.param, 'outputfile')

        b.append(mod)
        b.append(add)
        b.append(ip)
        b.append(start)
        b.append(stop)
        b.append(ifband)
        b.append(averages)
        b.append(power)
        b.append(edelay)
        b.append(points)
        b.append(outputfile)

        self.myOut.emit(b)
