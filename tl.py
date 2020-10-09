# -*- coding: utf-8 -*-
"""
@author: FibLab
"""

import visa
import time
import numpy as np
import OSAtunics
import matplotlib.pyplot


class tunablelaser:

    def __init__(self):
        # Start communications with scope - probably should do some checking here
        self.resmgr = visa.ResourceManager()
        self.instr = self.resmgr.open_resource('GPIB0::10::INSTR')

    # Enable laser
    def enable(self):
        self.instr.write('ENABLE')

    # Stop acquisition
    def disable(self):
        self.instr.write('DISABLE')

    # Set power unit
    def powerunit(self, unit):
        self.instr.write('%s' % unit)

    # Set power
    def power(self, p):
        self.instr.write('P=+%1.2f' % p)

    # Set wavelength
    def wl(self, wavelength):
        self.instr.write('L=%4.3f' % wavelength)

    # Create a tunablelaser instance and initialize


Tunaser = tunablelaser()
Tunaser.enable()
time.sleep(0.5)

Tunaser.power(2.00)
time.sleep(0.5)

# tune parameters
wlstart = input("Input start wavelength(XXXX.XXX nm >=1500 nm):")
wlstop = input("Input stop wavelength(XXXX.XXX nm <=1640 nm):")
step = 0.001
wlrange = np.arange(float(wlstart), float(wlstop), step)

# Create a OSA instance and initialize
osa = OSAtunics.OSA()
osa.span(3.7)
time.sleep(0.5)

osa.powermode()
time.sleep(0.5)

osa.reference(0)
time.sleep(0.5)

osa.yscale(10)
time.sleep(0.5)

osa.resolution(0.03)
time.sleep(0.5)

osa.vbw(1)
time.sleep(0.5)

osa.sampoint(1001)
time.sleep(0.5)

scanmode = input("Choose scan mode [Power mode or Wavelength mode] (P/W?):")

if scanmode == 'W':
    print('Capture the Reference data[Input R]')
    dataprofile = input()

    if dataprofile == 'R':
        # reference capture tune start
        i = 0
        ref_buffer = np.zeros((len(wlrange), 2))
        for wavelength in wlrange:
            Tunaser.wl(wavelength)
            time.sleep(0.1)

            osa.center(wavelength)
            time.sleep(0.1)

            osa.single()
            time.sleep(3)

            osa.anapmr()
            time.sleep(0.1)

            ref_buffer[i] = osa.data
            i = i + 1

    print('Capture the Transmit data[Input T]')
    dataprofile = input()

    if dataprofile == 'T':
        # data capture tune start
        i = 0
        data_buffer = np.zeros((len(wlrange), 2))
        for wavelength in wlrange:
            Tunaser.wl(wavelength)
            time.sleep(0.1)

            osa.center(wavelength)
            time.sleep(0.1)

            osa.single()
            time.sleep(2.5)

            osa.anapmr()
            time.sleep(0.1)

            data_buffer[i] = osa.data
            i = i + 1

        # turnoff laser source
Tunaser.disable()
s21 = data_buffer[:, 0] / ref_buffer[:, 0]

fig = matplotlib.pyplot.figure()
axes = fig.add_subplot(111)
axes.plot(ref_buffer[:, 1], s21)

fig.savefig('FP filter.pdf', dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format='pdf',
            transparent=False, bbox_inches=None, pad_inches=0.1,
            frameon=None)