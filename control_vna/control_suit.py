from control_vna.control import getdata
from tools.read_conf import ReadConfig
from PyQt5.QtCore import QThread


class suit_cla(QThread):
    def __init__(self):
        super().__init__()
    def run(self):
        suit()


def suit():
    conf = ReadConfig()
    span = conf.get('test_config','span')
    inst = conf.get('test_config','inst')
    centerf = conf.get('test_config','conterf')
    temp = conf.get('test_config','temp')
    averages = conf.get('test_config','averages')
    power = conf.get('test_config', 'power')
    edelay = conf.get('test_config', 'edelay')
    ifband = conf.get('test_config', 'ifband')
    points = conf.get('test_config', 'points')
    outputfile = conf.get('test_config', 'outputfile')
    file_list = []
    if span > 200:
        ad = centerf-span/2
        while ad<centerf+span/2:
            file_list.append(getdata(inst, ad+100, 200, temp, averages, power, edelay, ifband, points, outputfile))
            ad += 200
    else:
        file_list.append(getdata(inst, centerf, span, temp, averages, power, edelay, ifband, points, outputfile))



