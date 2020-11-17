import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from mywidget.MainWindow import Ui_MainWindow
from PyQt5.QtCore import QCoreApplication, pyqtSignal, QTimer,QMutex,QThread,QWaitCondition
from PyQt5 import QtGui
from mywidget import connectPic, helpPage
from tools import write_conf,read_conf
from dialog_util.dialogUtil import *
from control_vna.control_suit import suit_cla
from thread_exa.wait_thread import myThread
import time


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.setupUi(self)
        self.preSet()





        self.pushButton.clicked.connect(self.measure)
        self.pushButton_2.clicked.connect(self.pause)
        self.pushButton_3.clicked.connect(self.terminate_m)
        self.pushButton_4.clicked.connect(self.go_on)

        self.pushButton_6.clicked.connect(self.writeconf)
        self.pushButton_7.clicked.connect(self.readconf)
        self.actionconnect.triggered.connect(self.con_pic)
        self.action5.triggered.connect(QCoreApplication.instance().quit)
        self.actionhelp.triggered.connect(self.helppage)

    def preSet(self):
        # self.LineEdit.setInputMask('999.999.999.999;_')
        self.readconf()

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
        self.help_page = helpPage.mainwindow()
        self.help_page.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.help_page.show()

    def measure(self):
        # thread_exa = suit_cla()
        # thread_exa.start()
        self.pushButton.setEnabled(False)
        self.thread1 = myThread()
        self.thread1.start()
        # print(QThread.currentThread())

    def pause(self):
        self.thread1.pause()


    def go_on(self):
        self.thread1.goon()

    def terminate_m(self):
        self.thread1.terminate()
        self.thread1.wait()
        self.pushButton.setEnabled(True)

    def writeconf(self):
        IP = self.LineEdit.text()
        centerf = self.LineEdit_2.text()
        span = self.LineEdit_3.text()
        ifband = self.LineEdit_4.text()
        temp = self.LineEdit_5.text()
        averages = self.LineEdit_6.text()
        power = self.LineEdit_7.text()
        edelay = self.LineEdit_7.text()
        points = self.LineEdit_8.text()
        outputfile = self.LineEdit_9.text()
        self.wr = write_conf.writeThread(IP, centerf, span, temp, averages, power, edelay, ifband, points, outputfile)
        self.wr.start()

    def readconf(self):
        self.rd = read_conf.myth('test_all')
        self.rd.myOut.connect(self.set_text)
        self.rd.start()

    def set_text(self,a):
        self.LineEdit.setText(a[0])
        self.LineEdit_2.setText(a[1])
        self.LineEdit_3.setText(a[2])
        self.LineEdit_4.setText(a[3])
        self.LineEdit_5.setText(a[4])
        self.LineEdit_6.setText(a[5])
        self.LineEdit_7.setText(a[6])
        self.LineEdit_8.setText(a[7])
        self.LineEdit_9.setText(a[8])
        self.LineEdit_10.setText(a[9])

    def fail_dialog(self):
        warning_dialog(self,'shibai','you fail')

    def succ_dialog(self):
        information_dialog(self, 'cheng gong', 'you success')

    # QApplication.processEvents()实现页面刷新





if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
