import ota_main
import sys
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)
myWin = ota_main.MyMainWindow()
myWin.show()
sys.exit(app.exec_())