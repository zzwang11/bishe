import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from mywidget.MainWindow import Ui_MainWindow
from PyQt5.QtCore import QCoreApplication, pyqtSignal, QTimer,QMutex,QThread
from PyQt5 import QtGui
from mywidget import connectPic, helpPage
from tools import write_conf
from dialog_util.dialogUtil import *
from control_vna.control_suit import suit_cla
from thread_exa.wait_thread import myThread
import time


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.setupUi(self)
        self.pushButton_5.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton.clicked.connect(self.measure)
        self.pushButton_3.clicked.connect(self.terminate_m)
        self.actionconnect.triggered.connect(self.con_pic)
        self.action5.triggered.connect(QCoreApplication.instance().quit)
        self.actionhelp.triggered.connect(self.helppage)
        self.pushButton_6.clicked.connect(self.writeConf)
        self.pushButton_7.clicked.connect(self.fail_dialog)




    def save_file(self):
        save_path, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "./", "All Files (*);;Text Files (*.txt)")
        print(save_path)
        if save_path:
            with open(file=save_path, mode='a+', encoding='utf-8') as file:
                file.write('wen jian')

    def con_pic(self):
        self.a = connectPic.picture()
        self.a.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.a.show()

    def helppage(self):
        self.a = helpPage.mainwindow()
        self.a.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.a.show()

    def measure(self):
        # thread_exa = suit_cla()
        # thread_exa.start()
        self.pushButton.setEnabled(False)
        self.thread1 = myThread()
        self.thread1.start()
        print(QThread.currentThread())

    def pause(self):
        self.thread1.wait()

    def terminate_m(self):
        self.thread1.terminate()
        self.thread1.wait()
        print(QThread.currentThread())
        # del self.thread1
        self.pushButton.setEnabled(True)


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

    def fail_dialog(self):
        fail_dialog(self,'shibai','you lose')


    def succ_dialog(self):
        success_dialog(self, 'cheng gong', 'you win')

    # QApplication.processEvents()实现页面刷新
    def calculate(self):
        print('aaa')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
