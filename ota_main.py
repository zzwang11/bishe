import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from mywidget.MainWindow import Ui_MainWindow
from PyQt5.QtCore import QCoreApplication, pyqtSignal, QTimer
from PyQt5 import QtGui
from mywidget import connectPic, helpPage
from tools import write_conf
from dialog_util.dialogUtil import *

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
        self.pushButton_6.clicked.connect(self.writeConf)
        self.pushButton_7.clicked.connect(self.faildialog)

    def save_file(self):
        save_path, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "./", "All Files (*);;Text Files (*.txt)")
        print(save_path)
        if save_path:
            with open(file=save_path, mode='a+', encoding='utf-8') as file:
                file.write('wen jian')

    def conn(self):
        a = connectPic.picture()
        a.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        a.show()

    def helppage(self):
        a = helpPage.mainwindow()
        a.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        a.show()

    def connect(self):
        self.con_vna = suit()

    def writeConf(self):
        inst = self.LineEdit.Text()
        centerf = self.LineEdit_2.Text()
        span = self.LineEdit_3.Text()
        ifband = self.LineEdit_4.Text()
        temp = self.LineEdit_5.Text()
        averages = self.LineEdit_6.Text()
        power = self.LineEdit_7.Text()
        edelay = self.LineEdit_7.Text()
        points = self.LineEdit_8.Text()
        outputfile = self.LineEdit_9.Text()
        write_conf.write(inst, centerf, span, temp, averages, power, edelay, ifband, points, outputfile)

    def faildialog(self):
        fail_dialog(self,'shibai','you lose')


    def succDialog(self):
        a = QMessageBox()
        a.information(self, '成功', 'success', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Yes)

    # QApplication.processEvents()实现页面刷新



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
