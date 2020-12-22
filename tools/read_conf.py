import configparser
import os
from PyQt5.QtCore import QThread,pyqtSignal


class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            self.configpath = filepath
        else:
            root_dir = os.path.abspath('.')
            self.configpath = os.path.join(root_dir, "config.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(self.configpath)

    def get(self, *param):
        try:
            value = self.cf.get(*param)
        except:
            value = "未读取到"
        return value

    def set(self, *param):
        try:
            self.cf.set(*param)
            self.cf.write(open(self.configpath,'w'))
            a = 0
        except:
            a = "写入失败"
        return a


class MyTh(QThread):
    myOut = pyqtSignal(list)

    def __init__(self, *param):
        super().__init__()
        self.param = param

    def run(self):
        a = ReadConfig()
        b = []
        if self.param == ('test_all',):
            mod = a.get('test_config', 'mod')
            add = a.get('test_config', 'add')
            ip = a.get('test_config', 'ip')
            start = a.get('test_config', 'start')
            stop = a.get('test_config', 'stop')
            ifband = a.get('test_config', 'ifband')
            averages = a.get('test_config', 'averages')
            power = a.get('test_config', 'power')
            edelay = a.get('test_config', 'edelay')
            points = a.get('test_config', 'points')
            outputfile = a.get('test_config', 'outputfile')
            distance = a.get('test_config', 'distance')
            r = a.get('test_config', 'r')
            degree = a.get('test_config', 'degree')
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
            b.append(distance)
            b.append(r)
            b.append(degree)
        else:
            b.append(a.get(*self.param))
        self.myOut.emit(b)


