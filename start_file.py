import field_sys
import sys
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)
myWin = field_sys.MyMainWindow()
myWin.show()
sys.exit(app.exec_())