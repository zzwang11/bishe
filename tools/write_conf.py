from tools.read_conf import ReadConfig


def write(inst, centerf, span, temp, averages, power, edelay, ifband, points, outputfile):
    conf = ReadConfig()
    conf.set('test_config','span',span)
    conf.set('test_config','inst',inst)
    conf.set('test_config','conterf',centerf)
    conf.set('test_config','temp',temp)
    conf.set('test_config','averages')
    conf.set('test_config', 'power')
    conf.set('test_config', 'edelay')
    conf.set('test_config', 'ifband')
    conf.set('test_config', 'points')
    conf.set('test_config', 'outputfile')