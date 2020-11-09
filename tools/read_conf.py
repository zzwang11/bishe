import configparser
import os
from PyQt5.QtCore import QThread

class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            self.configpath = filepath
        else:
            # root_dir = os.path.dirname(os.path.abspath('.'))
            root_dir = 'd://bishe'
            self.configpath = os.path.join(root_dir, "config.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(self.configpath)

    def get(self, *param):
        value = self.cf.get(*param)
        return value

    def set(self, *param):
        self.cf.set(*param)
        self.cf.write(open(self.configpath,'w'))




class myth(QThread):
    def __init__(self,*param):
        super().__init__()
        self.param = param


    def run(self):
        a = ReadConfig()
        a.get(*self.param)


