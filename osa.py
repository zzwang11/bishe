import visa


class OSA:

    def __init__(self):
        # Start communications with Optical Spectrum Analyzer - should check the address before
        self.resmgr = visa.ResourceManager()
        self.instr = self.resmgr.open_resource('GPIB0::1::INSTR')

    # OSA span
    def span(self, spn):
        self.instr.write('SPN%4.1f' % spn)

    # OSA resolution
    def resolution(self, res):
        self.instr.write('RES %1.2f' % res)

        # OSA resolution

    def vbw(self, vbw):
        self.instr.write('VBW %dKHZ' % vbw)

        # OSA yscale

    def yscale(self, yscl):
        self.instr.write('LOG %d' % yscl)

        # OSA reference level

    def reference(self, rlv):
        self.instr.write('RLV %1.1f' % rlv)

        # OSA sampling points

    def sampoint(self, mpt):
        self.instr.write('MPT %d' % mpt)

        # OSA center

    def center(self, cnt):
        self.instr.write('CNT %4.3f' % cnt)

    # OSA single measure
    def single(self):
        self.instr.write('SSI')

    # OSA repeat measure
    def repeat(self):
        self.instr.write('SRT')

    # OSA stop measure
    def stop(self):
        self.instr.write('SST')

    # OSA range measure
    def wlrange(self, srt, stp):
        self.instr.write('WSS%f,%f' % srt % stp)

    # OSA analysis power mode
    def powermode(self):
        self.instr.write('ANA PWR')

    # OSA analysis power mode result
    def anapmr(self):
        self.data = self.instr.query_ascii_values('ANAR?')

    def reads21(self):
        self.instr.write('CALCulate:PARameter:DEFine MySMeaS21,S21')


# Create a OSA instance
osa = OSA()