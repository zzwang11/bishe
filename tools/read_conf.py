import configparser
import os
from PyQt5.QtCore import QThread,pyqtSignal


class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            self.configpath = filepath
        else:
            # root_dir = os.path.dirname(os.path.abspath('.'))
            root_dir = 'e://bishe'
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
        self.cf.set(*param)
        self.cf.write(open(self.configpath,'w'))



# if __name__ == '__main__':
#     a = ReadConfig()
#     print(a.get('test_config', 'ip'))
#     a.set('test_config', 'temp', '44445')


class myth(QThread):
    myOut = pyqtSignal(str)

    def __init__(self, *param):
        super().__init__()
        self.param = param

    def run(self):
        a = ReadConfig()
        b = []
        if self.param == ('test_all',):
            b.append(a.get('test_config','ip'))
            b.append(a.get('test_config','centerf'))
            b.append(a.get('test_config','span'))
            b.append(a.get('test_config', 'ifband'))
            b.append(a.get('test_config','temp'))
            b.append(a.get('test_config','averages'))
            b.append(a.get('test_config', 'power'))
            b.append(a.get('test_config', 'edelay'))
            b.append(a.get('test_config', 'points'))
            b.append(a.get('test_config', 'outputfile'))
        else:
            b.append(a.get(*self.param))
        self.myOut.emit(b)


