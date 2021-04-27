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
    pna.write('DISPlay:WINDow1:STATE ON')
    pna.write('DISPlay:WINDow1:TRACe1:FEED \'Meas\'')
    pna.write('DISPlay:WINDow1:TRACe2:FEED \'Meas\'')
    # set parameters for sweep
    pna.write('SENSe1:SWEep:POINts {}'.format(points))
    pna.write('SENSe1:FREQuency:START {}MHZ'.format(start))
    pna.write('SENSe1:FREQuency:STOP {}MHZ'.format(stop))
    pna.write('SENSe1:BANDwidth {}HZ'.format(ifband))
    pna.write('SENSe1:SWEep:TIME:AUTO ON')
    pna.write('SOUR:POW1 {}'.format(power))
    pna.write('CALCulate1:CORRection:EDELay:TIME {}NS'.format(edelay))
    pna.write('SENSe1:AVERage:STATe ON')

    # ensure at least 10 averages are taken
    # if(averages < 10):
    #    averages = 10
    if averages < 1:
        averages = 1
    averages = averages // 1
    pna.write('SENSe1:AVERage:Count {}'.format(averages))


def read_data(path11,pna, data, points, outputfile, power):
    """
    function to read in data from the pna and output it into a file
    """
    # date = time.strftime('%Y-%m-%d', time.localtime())
    # path1 = 'h:/bishe/save/'


    # read in frequency
    start = str(pna.query('SENSe1:FREQuency:START?'))[:6]
    stop = str(pna.query('SENSe1:FREQuency:STOP?'))[:6]
    # for i in range(10):
    # # read in phase
    # if data == 'mag':
    #     pna.write('CALCulate1:FORMat PHASe')
    # else:
    #     pna.write('CALCulate1:FORMat REAL')
    # re = pna.query_ascii_values('CALCulate1:DATA? FDATA', container=np.array)
    # time.sleep(2)
    # # with open('h:/save/xiangwei.txt','w') as f:
    # #     for i in re:
    # #         f.write(i)
    # # read in mag
    # if data == 'mag':
    #     pna.write('CALCulate1:FORMat MLOG')
    # else:
    #     pna.write('CALCulate1:FORMat IMAGinary')
    # im = pna.query_ascii_values('CALCulate1:DATA? FDATA', container=np.array)
    pna.write('CALCulate1:FORMat  SMIT')
    im = pna.query_ascii_values('CALCulate1:DATA? FDATA', container=np.array)
    filess = path11+'fudu_'+start+'_'+stop+'_'+str(time.strftime("%H-%M-%S", time.localtime()))+'.txt'
    with open(filess,'w') as f:
        for i in range(len(im)):
            # f.write(str(im[i])+','+str(re[i])+'\n')
            f.write(str(im[i]) + '  ' + '\n')
        # time.sleep(1)

    # open output file and put data points into the file
    # file1 = path1 + outputfile[0:-4] + '_' + str(power) + 'dB' + time.strftime('%H-%M-%S', time.localtime()) + '.txt'
    # file = open(file1, "a")
    # count = 0
    # freq = np.linspace(float(pna.query('SENSe1:FREQuency:START?')), float(pna.query('SENSe1:FREQuency:STOP?')), points)
    # for i in freq:
    #     file.write(str(re[count]) + ' ' + str(im[count]) + '\n')
    #     count = count + 1
    # file.close()

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

    # wait until the averages are done being taken then read in the data
    # count = 10000000
    # while count > 0:
    #     count = count - 1
    time.sleep(2)
    # while True:
    #     if inst.query('STAT:OPER:AVER1:COND?')[1] != "0":
    #         break

    file1 = read_data(outputfile, inst, data, points, outputfile, power)

    inst.write("trace:clear; trace:feed:control next")
    # inst.close()
    return file1



