import sys
from PyQt5.QtWidgets import QApplication
from mywidget.connect_test_win import ConnectTest
# import bwipo
import nsa
import field_sys
import start
import svswr

app = QApplication(sys.argv)
window1 = field_sys.MyMainWindow()
window3 = nsa.MyMainWindow()
window4 = svswr.MyMainWindow()
win1 = start.Choice(window1, window3, window4)
# demo = ConnectTest(win1=win1)
# demo.show()
win1.show()
sys.exit(app.exec_())
