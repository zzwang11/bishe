import numpy as np
import pyvisa
import time
import os
import math


def pna_setup(pna, mod, points: int, start: float, stop: float, ifband: float, power: float, edelay: float, averages: int):
    """
    set parameters for the PNA for the sweep (number of points, center frequency, span of frequencies,
    IF bandwidth, power, electrical delay and number of averages)
    """

    # initial setup for measurement
    # if pna.query('CALC:PAR:CAT:EXT?') != f'"Meas,{mod}"\n':
    pna.write(f'CALCulate1:PARameter:DEFine:EXT \'Meas\',{mod}')

    pna.write(f'CALCulate1:PARameter:DEFine:EXT \'Meas2\',{mod}')

    pna.write('DISPlay:WINDow1:STATE ON')
    pna.write('DISPlay:WIND:TRACe1:FEED \'Meas\'')
    pna.write('DISPlay:WIND:TRACe2:FEED \'Meas2\'')
    # set parameters for sweep
    pna.write('SENSe1:SWEep:POINts {}'.format(points))
    pna.write('SENSe1:FREQuency:START {}MHZ'.format(start))
    pna.write('SENSe1:FREQuency:STOP {}MHZ'.format(stop))
    pna.write('SENSe1:BANDwidth {}HZ'.format(ifband))
    pna.write('SENSe1:SWEep:TIME:AUTO ON')
    # pna.write('SENSe1:SWEep:TRI:AUTO OFF')
    pna.write('SOUR:POW1 {}'.format(power))
    # pna.write('CALCulate1:CORRection:EDELay:TIME {}NS'.format(edelay))
    pna.write('SENSe1:AVERage:STATe ON')

    if averages < 1:
        averages = 1
    averages = averages // 1
    pna.write('SENSe1:AVERage:Count {}'.format(averages))


def read_data(path11,pna, start,stop):
    """
    function to read in data from the pna and output it into a file
    """

    time.sleep(30)
    pna.write('CALCulate1:PAR:SEL "Meas"')
    pna.write('CALCulate1:FORMat MLOG')
    ml = pna.query_ascii_values('CALCulate1:DATA? FDATA')
    pna.write('CALCulate1:PAR:SEL "Meas2"')
    pna.write('CALCulate1:FORMat PHAS')
    ph = pna.query_ascii_values('CALCulate1:DATA? FDATA')
    ll = []
    freq = np.linspace(float(start), float(stop), len(ml))
    for i in freq:
        ll.append(i)

    filess = path11+'/fudu_'+start+'_'+stop+'_'+str(time.strftime("%H-%M-%S", time.localtime()))+'.txt'
    with open(filess, 'w') as f:
        for i in range(len(ml)):
            f.write(str(ll[i])+' '+str(ml[i])+' '+str(ph[i])+'\n')

    return filess


def getdata(inst: str, mod: str, data: str, start: float, stop: float, averages: int, power: float,
            edelay: float, ifband: float, points: int, outputfile: str = "results.csv"):
    """
    function to get data and put it into a user specified file
    """
    # addr = '192.168.0.1'
    # tcp_addr = 'TCPIP::"192.168.0.1"::inst0::INSTR'
    # gpib_addr = 'GPIB0::12::INSTR'

    # set up the PNA to measure s21 for the specific instrument GPIB0::16::INSTR
    # rm = pyvisa.ResourceManager()
    # try:
    #     inst = rm.open_resource(inst)
    # except Exception:
    #     return 0
    pna_setup(inst, mod, points, start, stop, ifband, power, edelay, averages)

    # start taking data for S21
    inst.write('CALCulate1:PARameter:SELect \'Meas\'')
    inst.write('FORMat ASCII')
    inst.write('CALCulate1:PARameter:SELect \'Meas2\'')
    inst.write('FORMat ASCII')

    # wait until the averages are done being taken then read in the data
    # count = 10000000
    # while count > 0:
    #     count = count - 1
    time.sleep(2)
    # while True:
    #     if inst.query('STAT:OPER:AVER1:COND?')[1] != "0":
    #         break


    file1 = read_data(outputfile, inst, start,stop)

    inst.write("SYST:FPR")
    inst.write("CALC:PAR:DEL:ALL")
    # inst.close()
    return file1


if __name__ == '__main__':

    mod = 'S21'
    add = 20

    start = 23500
    stop = 24500
    ifband = 100
    averages = 10
    power = -30
    edelay = 20
    points = 1001
    outputfile = 'h:/bishe/save/270cm/'
    rm = pyvisa.ResourceManager()
    instru = rm.open_resource('TCPIP::192.6.94.10::inst0::INSTR')
    ss = getdata(instru, mod,'mag', start, stop, averages, power, edelay, ifband, points,outputfile)


