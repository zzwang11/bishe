import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from mywidget.MainWindow import Ui_MainWindow
from PyQt5.QtCore import QCoreApplication,pyqtSignal,QTimer
from PyQt5 import QtGui
from mywidget import connectPic, helpPage
from control_vna.control_suit import suit
from control_vna.test import xee
from control_vna.control_suit import suit

import time

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.setupUi(self)
        self.pushButton_5.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_4.clicked.connect(self.connect)
        self.actionconnect.triggered.connect(self.conn)
        self.action5.triggered.connect(QCoreApplication.instance().quit)
        self.actionhelp.triggered.connect(self.helppage)

    def save_file(self):
        save_path, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "./", "All Files (*);;Text Files (*.txt)")
        print(save_path)
        if save_path:
            with open(file=save_path, mode='a+', encoding='utf-8') as file:
                file.write('wen jian')

    def conn(self):
        self.a = connectPic.picture()
        self.a.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.a.show()

    def helppage(self):
        self.b = helpPage.mainwindow()
        self.a.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.b.show()

    def connect(self):
        self.con_vna = suit()


    # QApplication.processEvents()实现页面刷新
    # def duo(self):
    #     for i in range(100000):
    #         # QApplication.processEvents()
    #         # QTimer.time.sleep(0.1)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())