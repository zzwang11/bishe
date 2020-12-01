import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QStatusBar, QSplitter
from mywidget.MainWindowT import Ui_MainWindow
from PyQt5.QtCore import QCoreApplication, pyqtSignal, QTimer,QMutex,QThread,QWaitCondition,Qt
from PyQt5 import QtGui,QtCore
from mywidget import connectPic, helpPage
from tools import write_conf,read_conf
from dialog_util.dialogUtil import *
from control_vna.control_suit import suit_cla
from thread_exa.wait_thread import myThread
import time
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import tools.setcon
import math
import matplotlib.pyplot as plt


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))

        self.setupUi(self)
        # self.setconf()
        # 状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('123456',10000)
        self.preSet()
        # self.qss()


        # 二维
        # self.pyqtgraph1 = pg.GraphicsLayoutWidget(self.centralwidget)
        # self.pyqtgraph1.setObjectName("pyqtgraph1")
        # self.pyqtgraph1.setBackground('#F8F8FF')
        # self.gridLayout_2.addWidget(self.pyqtgraph1, 4, 0, 1, 1)
        # self.plt2 = self.pyqtgraph1.addPlot(title='绘制多条线')

        # 三维图
        # self.graph = gl.GLViewWidget(self.centralwidget)
        # self.graph.setObjectName("graph")
        # self.graph.setBackgroundColor(QtGui.QColor('white'))
        # self.graph.opts['distance'] = 40
        # self.gx = gl.GLGridItem()
        # self.gx.rotate(90, 0, 1, 0)
        # self.gx.translate(-10, 0, 0)
        # self.gx.setColor(QtGui.QColor('black'))
        # self.graph.addItem(self.gx)
        # self.gy = gl.GLGridItem()
        # self.gy.rotate(90, 1, 0, 0)
        # self.gy.translate(0, -10, 0)
        # self.gy.setColor(QtGui.QColor('black'))
        # self.graph.addItem(self.gy)
        # self.gz = gl.GLGridItem()
        # self.gz.translate(0, 0, -10)
        # self.gz.setColor(QtGui.QColor('black'))
        # self.graph.addItem(self.gz)
        # self.gridLayout_2.addWidget(self.graph, 0, 0, 1, 1)



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

    def set_3d(self):
        tools.setcon.pic_3d(self)

    def set_2d(self):
        tools.setcon.pic_2d(self)

    def preSet(self):
        # self.LineEdit.setInputMask('999.999.999.999;_')
        self.readconf()


    def con_pic(self):
        self.a = connectPic.picture()
        self.a.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.a.show()

    def helppage(self):
        self.help_page = helpPage.mainwindow()
        self.help_page.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.help_page.show()


    def measure(self):
        # self.thread_exa = suit_cla()
        # self.thread_exa.start()
        # self.thread_exa.mySig.connect(self.bar)



        self.statusBar.showMessage('测量中......',10**8)
        self.pushButton.setEnabled(False)
        self.thread1 = myThread()
        self.thread1.start()
        # self.graph.close()
        # self.thread1.mySig.connect(lambda i:self.progressBar.setValue(i))
        self.thread1.mySig.connect(self.settext)

    def settext(self,a):
        self.progressBar.setValue(a*10)
        # x = np.linspace(0,20,200)
        # n = np.sin(a*x)
        # self.plt2.plot(y = n,pen=(a*10,255,0))

    def pause(self):
        self.thread1.pause()
        self.statusBar.showMessage('暂停测量',10**8)
        # self.graph.show()

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

    def qss(self):
        self.pushButton_5.setStyleSheet('''QPushButton{background:rgb(100,149,237);border-radius:15px;}\
        QPushButton:hover{background:rgb(65,105,225);border-radius:15px;}''')
        self.pushButton_8.setStyleSheet('''QPushButton{background:rgb(100,149,237);border-radius:15px;}\
        QPushButton:hover{background:rgb(65,105,225);border-radius:15px;}''')
    # QApplication.processEvents()实现页面刷新




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
