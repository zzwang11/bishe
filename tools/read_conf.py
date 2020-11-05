import configparser
import os


class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            self.configpath = filepath
        else:
            root_dir = os.path.dirname(os.path.abspath('.'))
            self.configpath = os.path.join(root_dir, "config.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(self.configpath)

    def get(self, *param):
        value = self.cf.get(*param)
        return value

    def set(self, *param):
        self.cf.set(*param)
        self.cf.write(open(self.configpath,'w'))




