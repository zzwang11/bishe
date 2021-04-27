import pyvisa

class scpi():
    def get_S21(self):
        self.rm = pyvisa.ResourceManager()
        self.myfieldBox = self.rm.open_resource('TCPIP::192.6.94.10::inst0::INSTR')
        print(self.myfieldBox.query("*IDN?"))

        self.myfieldBox.write('SOUR:POW1 -30 dBm')
        self.myfieldBox.query("*OPC?")
        self.myfieldBox.write("SENS:FREQ:23.5e9")
        self.myfieldBox.write("SENS:FREQ:28.5e9")
        self.myfieldBox.write("SENS:FREQ 5001")
        self.myfieldBox.write("INIT")
        self.myfieldBox.write('CALC:PAR:SEL"MEAS1"')
        a = self.myfieldBox.query("CALC:DATA?FDATA")
        print(a)
        self.myfieldBox.write('CALC:PAR:SEL"MEAS2"')
        b = self.myfieldBox.query("CALC:DATA?FDATA")
        print(b)
if __name__ == '__main__':
    scpi = scpi()
    scpi.get_S21()
