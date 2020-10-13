import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from MainWindow import Ui_MainWindow
from PyQt5.QtCore import QCoreApplication
from openfile import MyWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_5.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_4.clicked.connect(self.save_file())

    def save_file(self):
        fileName2, ok2 = QFileDialog.getSaveFileName(self,
                                                     "文件保存",
                                                     "./",
                                                     "All Files (*);;Text Files (*.txt)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())