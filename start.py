from ota_main import MyMainWindow
import sys
from PyQt5.QtWidgets import QApplication






app = QApplication(sys.argv)
myWin = MyMainWindow()
myWin.show()
sys.exit(app.exec_())