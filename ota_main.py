import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QStatusBar, QSplitter
from mywidget.MainWindowT import Ui_MainWindow
from PyQt5.QtCore import QCoreApplication, pyqtSignal, QTimer,QMutex,QThread,QWaitCondition,Qt
from PyQt5 import QtGui
from mywidget import connectPic, helpPage
from tools import write_conf,read_conf
from dialog_util.dialogUtil import *
from control_vna.control_suit import suit_cla
from thread_exa.wait_thread import myThread
import time
import pyqtgraph as pg
import numpy as np
import math


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))

        self.setupUi(self)
        # 状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('123456',10000)
        self.preSet()
        # self.qss()
        self.pushButton_5.setStyleSheet('''QPushButton{background:rgb(100,149,237);border-radius:15px;}\
        QPushButton:hover{background:rgb(65,105,225);border-radius:15px;}''')
        # self.split = QSplitter(Qt.Horizontal)
        # self.split.addWidget(self.)
        # pg.setConfigOption('background', '#F8F8FF')
        # pg.setConfigOption('foreground', 'd')
        self.pyqtgraph1.setBackground('#F8F8FF')
        self.draw1()





        # 实现测量开始、暂停、继续、停止
        self.pushButton.clicked.connect(self.measure)
        self.pushButton_2.clicked.connect(self.pause)
        self.pushButton_3.clicked.connect(self.terminate_m)
        self.pushButton_4.clicked.connect(self.go_on)

        # 实现测量所需数据的保存和读取
        self.pushButton_6.clicked.connect(self.writeconf)
        self.pushButton_7.clicked.connect(self.readconf)


        self.actionconnect.triggered.connect(self.con_pic)
        self.action5.triggered.connect(QCoreApplication.instance().quit)
        self.actionhelp.triggered.connect(self.helppage)

    def draw1(self):
        self.pyqtgraph1.clear()
        plt2 = self.pyqtgraph1.addPlot(title='绘制多条线')
        plt2.plot(np.random.normal(size=150), pen=pg.mkPen(color='r', width=2),
                  name="Red curve")
        plt2.plot(np.random.normal(size=110) + 5, pen=(0, 255, 0), name="Green curve")
        plt2.plot(np.random.normal(size=120) + 10, pen=(0, 0, 255), name="Blue curve")

    def preSet(self):
        # self.LineEdit.setInputMask('999.999.999.999;_')
        self.readconf()
    #
    # def qss(self):


    def save_file(self):
        save_path, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "./", "All Files (*);;Text Files (*.txt)")
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
        self.statusBar.showMessage('测量中......',10**8)
        self.pushButton.setEnabled(False)
        self.thread1 = myThread()
        self.thread1.start()
        # print(QThread.currentThread())

    def pause(self):
        self.thread1.pause()
        self.statusBar.showMessage('暂停测量',10**8)

    def go_on(self):
        self.thread1.goon()
        self.statusBar.showMessage('测量中......',10**8)

    def terminate_m(self):
        self.thread1.terminate()
        self.thread1.wait()
        self.pushButton.setEnabled(True)
        self.statusBar.showMessage('测量结束！',10**8)

    def writeconf(self):
        IP = self.LineEdit.text()
        centerf = self.LineEdit_2.text()
        span = self.LineEdit_3.text()
        ifband = self.LineEdit_4.text()
        temp = self.LineEdit_5.text()
        averages = self.LineEdit_6.text()
        power = self.LineEdit_7.text()
        edelay = self.LineEdit_8.text()
        points = self.LineEdit_9.text()
        outputfile = self.LineEdit_10.text()
        self.wr = write_conf.writeThread(IP, centerf, span, temp, averages, power, edelay, ifband, points, outputfile)
        self.wr.start()
        self.statusBar.showMessage('保存配置成功！',10**5)

    def readconf(self):
        self.rd = read_conf.MyTh('test_all')
        self.rd.myOut.connect(self.set_text)
        self.rd.start()
        self.statusBar.showMessage('从本地读取配置成功', 10**4)

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
