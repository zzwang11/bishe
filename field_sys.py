import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QStatusBar
from mywidget.field_sys_win import Ui_MainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtGui
from mywidget import field_pic, helpPage, connect_test_win
from tools import write_conf, read_conf, test_connect, result
from dialog_util.dialogUtil import *
from tools.control_vna import control_suit

import os
import pyqtgraph as pg
import tools.set_pic
import shutil
import random, math
import pyvisa
import numpy as np
import pathlib


local_path = 'h:/bishe/'
icon = './img/icon.ico'


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon(icon))
        self.rm = pyvisa.ResourceManager()
        # self.instru = self.rm.open_resource('TCPIP::192.6.94.9::inst0::INSTR')
        # self.instru = self.rm.open_resource('TCPIP::192.6.94.10::inst0::INSTR')
        # self.instru = self.rm.open_resource('TCPIP::192.168.48.149::inst0::INSTR')
        self.setupUi(self)
        self.staus0 = 3
        # 状态栏
        self.rere = 0
        self.mak = 0
        self.blueBtn = '''QPushButton{background:rgb(100,149,237);border-radius:10px;border-width:3px;border-color:gray;}\
        QPushButton:hover{background:rgb(65,105,225);border-radius:10px;}'''
        self.blueBtn1 = '''QPushButton{background:rgb(100,149,237);border-radius:2px;}\
        QPushButton:hover{background:rgb(65,105,225);border-radius:2px;}'''
        self.redBtn = '''QPushButton{background:rgb(255,192,203);border-radius:10px;}\
                QPushButton:hover{background:rgb(255,182,193);border-radius:10px;}'''
        self.preSet()
        self.qss()
        self.name_list = []
        self.filepath = self.LineEdit_10.text()

        # 实现测量开始、暂停、继续、停止
        self.pushButton.clicked.connect(self.measure)


        # 实现测量所需数据的保存和读取
        self.pushButton_5.clicked.connect(self.save_result)
        self.pushButton_6.clicked.connect(self.writeconf)
        self.pushButton_7.clicked.connect(self.readconf)
        self.pushButton_8.clicked.connect(self.read_result)
        self.pushButton_9.clicked.connect(self.save_config)
        self.pushButton_11.clicked.connect(self.restart)
        self.pushButton_12.clicked.connect(self.next1)
        self.pushButton_13.clicked.connect(self.pre2)
        self.pushButton_14.clicked.connect(self.next2)
        self.pushButton_15.clicked.connect(self.next0)
        self.pushButton_16.clicked.connect(self.pre3)
        self.pushButton_17.clicked.connect(self.next3)
        self.pushButton_18.clicked.connect(self.pre4)
        self.pushButton_19.clicked.connect(self.next4)
        self.pushButton_27.clicked.connect(self.save_result)
        self.pushbutton_22.clicked.connect(self.xuanze)
        self.pbtn1.clicked.connect(self.test_con)
        self.actionconnect.triggered.connect(self.test_con1)
        self.actionopen.triggered.connect(self.read_result)
        self.action1.triggered.connect(self.measure)

        self.action4.triggered.connect(self.save_result)
        self.action7.triggered.connect(self.restart)

        self.action5.triggered.connect(QCoreApplication.instance().quit)
        self.actionhelp.triggered.connect(self.helppage)

    def next1(self):
        self.widget1.show()
        self.widget3.hide()
        self.staus0 = 3
        self.label_8.setText('测量RX线缆')

    def next0(self):
        self.widget1.hide()
        self.pyqtgraph1.clear()
        if self.staus0 == 3:
            self.widget4.show()
        elif self.staus0 == 4:
            self.widget5.show()
        elif self.staus0 == 5:
            self.widget6.show()
            self.LineEdit_11.setText('S12')
        elif self.staus0 == 6:
            self.widget7.show()

    def pre2(self):
        self.widget4.hide()
        self.widget3.show()
        self.staus0 = 3

    def next2(self):
        self.widget4.hide()
        self.widget1.show()
        self.pyqtgraph1.clear()
        self.staus0 = 4
        self.label_8.setText('测量TX线缆')

    def next3(self):
        self.widget5.hide()
        self.widget1.show()
        self.pyqtgraph1.clear()
        self.staus0 = 5
        self.label_8.setText('参考天线测量Rx')

    def pre3(self):
        self.widget5.hide()
        self.widget4.show()
        self.staus0 = 4

    def next4(self):
        self.widget6.hide()
        self.widget1.show()
        self.pyqtgraph1.clear()
        self.staus0 = 6
        self.label_8.setText('参考天线测量Tx')

    def pre4(self):
        self.widget6.hide()
        self.widget5.show()
        self.staus0 = 5

    def restart(self):
        self.pyqtgraph1.clear()
        self.widget1.hide()
        self.widget5.hide()
        self.widget4.hide()
        self.widget6.hide()
        self.widget7.hide()
        self.widget3.show()

    def read_result(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./save/", "All Files (*);;Text Files (*.txt)")
        self.widget1.hide()
        self.widget5.hide()
        self.widget4.hide()
        self.widget6.hide()
        self.widget7.show()
        self.widget3.hide()
        self.pyqtgraph1.clear()
        with open(fileName1, 'r') as f:
            a = f.read().split('\n')
        tx = []
        rx = []
        freq = []
        if len(a[0].split()) == 3:
            for i in a:
                c = i.split()
                if len(c) == 0:
                    break
                freq.append(eval(c[0]))
                tx.append(eval(c[2]))
                rx.append(eval(c[1]))
        elif len(a[0].split()) == 2:
            for i in a:
                c = i.split()
                if len(c) == 0:
                    break
                freq.append(eval(c[0]))
                rx.append(eval(c[1]))
        elif len(a[0].split()) == 1:
            for i in a:
                c = i.split()
                print(c)
                if len(c) == 0:
                    break
                rx.append(eval(c[0]))
            aaa = fileName1.rfind('/')
            name = fileName1[aaa + 1:]
            n1 = name.find('_')
            n2 = name[n1 + 1:].find('_')
            n3 = name[n2 + 1:].find('_')
            if name[n1 + 1] == '+':
                start = eval(name[n1 + 2:n2 + n1 + 1])
                stop = eval(name[n2 + 2:n3 + n2 + 1])
            else:
                start = eval(name[n1 + 1:n2 + n1 + 1])
                stop = eval(name[n2 + 1:n3 + n2 + 1])
            freq = np.linspace(float(start), float(stop), len(rx))

        self.pyqtgraph2.clear()
        self.c = self.pyqtgraph2.addPlot(title='', pen=pg.mkPen(color='b'))
        self.c.setLabel('left', "S21", units='dB')
        self.c.setLabel('bottom', "频率", units='MHz')
        self.c.setLogMode(x=False, y=False)
        # freq = np.linspace(float(self.LineEdit_2.text()), float(self.LineEdit_3.text()), len(xx))
        self.c.plot(x=freq, y=rx, pen=pg.mkPen(color='r', width=1))
        if len(tx) != 0:
            self.c.plot(x=freq, y=tx, pen=pg.mkPen(color='g', width=1))

    def save_result(self):
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "./", "Text Files (*.txt)")
        try:
            shutil.copy(self.result_path, fileName2)
            information_dialog(self, '提示', '保存成功')
        except:
            information_dialog(self, '提示', '保存失败')

    def jisuan(self):
        with open(self.name_list[0], 'r') as f:
            a = f.read().split()
        with open(self.name_list[1], 'r') as f:
            b = f.read().split()
        with open(self.name_list[2], 'r') as f:
            c = f.read().split()
        with open(self.name_list[3], 'r') as f:
            d = f.read().split()
        aa = []
        bb = []
        fr = []
        i = 0
        while i < len(a) - 2:
            aa.append(eval(c[i]) - eval(a[i]))
            bb.append(eval(d[i]) - eval(b[i]))
            i += 3

        freq = np.linspace(float(self.LineEdit_2.text()), float(self.LineEdit_3.text()), len(aa))
        for j in freq:
            fr.append(j)
        self.result_path = self.LineEdit_10.text() + '/result.txt'
        with open(self.result_path, 'w') as f:
            i = 0
            while i < len(aa):
                f.write(str(fr[i]) + ' ' + str(aa[i]) + ' ' + str(bb[i]) + '\n')
                i += 1
        self.pyqtgraph1.clear()
        self.c = self.pyqtgraph1.addPlot(title='最终结果', pen=pg.mkPen(color='b'))
        self.c.setLabel('left', "loss", units='dB')
        self.c.setLabel('bottom', "频率", units='MHz')
        self.c.setLogMode(x=False, y=False)
        self.c.plot(x=freq, y=aa, pen=pg.mkPen(color='r', width=1), name='Rx')
        self.c.plot(x=freq, y=bb, pen=pg.mkPen(color='g', width=1), name='Tx')

    def preSet(self):
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.progressBar.setValue(100)
        self.readdefconf()

    def test_con(self):
        self.test = connect_test_win.ConnectTest(self.rm)
        self.test.setWindowIcon(QtGui.QIcon(icon))
        self.test.show()
        self.test.setFocus()
        self.test.myout.connect(self.connect)
        self.test.myout1.connect(self.set)

    def set(self,ins):
        self.LineEdit.setText(ins)
        self.instru = self.rm.open_resource(ins)

    def test_con1(self):
        self.test1 = test_connect.TestCon(self.LineEdit.text(), self.rm)
        self.test1.start()
        self.test1.myOut.connect(self.connect)


    def connect(self, i):
        if i == 1:
            jpg5 = QtGui.QPixmap('./img/dui.jpg').scaled(48, 48)
            information_dialog(self, '成功', '连接成功')
            self.lab1.setPixmap(jpg5)
            self.lab2.setText('检测连接成功')
            self.lab2.setStyleSheet("QLabel{color:rgb(0,255,0)}")
        else:
            jpg5 = QtGui.QPixmap('./img/cha.jpg').scaled(48, 48)
            information_dialog(self, '失败', '连接失败')
            self.lab1.setPixmap(jpg5)
            self.lab2.setText('检测到未成功')
            self.lab2.setStyleSheet("QLabel{color:rgb(255,0,0)}")

    def con_pic(self):
        self.pic = field_pic.picture()
        self.pic.setWindowIcon(QtGui.QIcon(icon))
        self.pic.show()

    def helppage(self):
        self.help_page = helpPage.Splitter()
        self.help_page.setWindowIcon(QtGui.QIcon(icon))
        self.help_page.show()

    def get_con(self):
        mod = self.LineEdit_11.text()
        add = self.LineEdit_12.text()
        IP = self.LineEdit.text()
        start = self.LineEdit_2.text()
        stop = self.LineEdit_3.text()
        ifband = self.LineEdit_4.text()
        averages = self.LineEdit_6.text()
        power = self.LineEdit_7.text()
        edelay = self.LineEdit_8.text()
        points = self.LineEdit_9.text()
        outputfile = self.LineEdit_10.text()
        li = [mod, add, IP, start, stop, ifband, averages, power, edelay, points, outputfile]
        return li

    def measure(self):
        self.name_list = []
        if pathlib.Path(self.LineEdit_10.text()).is_dir():
            pass
        else:
            os.mkdir(self.LineEdit_10.text())
        li = self.get_con()
        self.LineEdit_11.setText('S21')
        try:
            self.thread1 = control_suit.suit_cla(li, 'mag', self.instru)
            self.thread1.start()
            self.thread1.mySig.connect(self.setbar)
            self.thread1.mySig1.connect(self.mat)
            self.thread1.mySig2.connect(self.succ_dialog)
            self.thread1.mySig2.connect(self.finish)
        except:
            self.fail_dialog()
        self.pyqtgraph1.clear()
        self.c = self.pyqtgraph1.addPlot(title='结果', pen=pg.mkPen(color='r', width=1))
        self.c.setLabel('left', "S21", units='dB')
        self.c.setLabel('bottom', "频率", units='MHz')
        self.c.setLogMode(x=False, y=False)
        self.statusBar.showMessage('测量中......', 10 ** 8)


    def finish(self):
        self.mak += 1
        self.pushButton.setEnabled(True)
        self.statusBar.showMessage('测量完成', 10 ** 8)

    def mat(self, ss):
        self.name_list.append(ss)
        with open(ss, 'r') as f:
            a = f.read().split()
        xx = []
        i = 0
        while i < len(a) - 2:
            xx.append(eval(a[i + 1]))
            i += 3
        freq = np.linspace(float(self.LineEdit_2.text()), float(self.LineEdit_3.text()), len(xx))
        self.c.plot(x=freq, y=xx, pen=pg.mkPen(color='r', width=1))

    def xuanze(self):
        directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")  # 起始路径
        self.LineEdit_10.setText(directory1)

    def setbar(self, a):
        self.progressBar.setValue(a)


    def writeconf(self):
        print(self.rere)
        li = self.get_con()
        self.wr = write_conf.writeThread('field',mod=li[0], add=li[1], ip=li[2], start=li[3], stop=li[4],
                                         ifband=li[5], averages=li[6], power=li[7], edelay=li[8], points=li[9],
                                         outputfile=li[10])
        self.wr.start()
        self.statusBar.showMessage('保存配置成功！', 10 ** 5)

    def save_config(self):

        self.writeconf()
        fileName2, ok2 = QFileDialog.getSaveFileName(self, "保存设置", "./config/", "Setting Files (*.ini)")
        if fileName2:
            shutil.copy('./config.ini', fileName2)
        else:
            pass

    def readdefconf(self):
        self.rd = read_conf.MyTh('field')
        self.rd.myOut.connect(self.set_text)
        self.rd.start()
        self.statusBar.showMessage('从本地读取配置成功', 10 ** 4)

    def readconf(self):
        directory1, filetype = QFileDialog.getOpenFileName(self,
                                                           "选取文件",
                                                           "./config/",
                                                           "Setting Files (*.ini)")
        self.rd = read_conf.MyTh('field', directory1)
        self.rd.myOut.connect(self.set_text)
        self.rd.start()
        self.statusBar.showMessage('从本地读取配置成功', 10 ** 4)

    def set_text(self, a):
        self.LineEdit_11.setText(a[0])
        self.LineEdit_12.setText(a[1])
        self.LineEdit.setText(a[2])
        self.LineEdit_2.setText(a[3])
        self.LineEdit_3.setText(a[4])
        self.LineEdit_4.setText(a[5])
        self.LineEdit_6.setText(a[6])
        self.LineEdit_7.setText(a[7])
        self.LineEdit_8.setText(a[8])
        self.LineEdit_9.setText(a[9])
        self.LineEdit_10.setText(a[10])

    def fail_dialog(self):
        warning_dialog(self, '失败', '连接失败')

    def succ_dialog(self):
        information_dialog(self, '成功', '测量完成')

    def qss(self):
        self.pushButton_5.setStyleSheet(self.blueBtn)
        self.pushButton_8.setStyleSheet(self.blueBtn)
        self.pushButton_11.setStyleSheet(self.redBtn)
        self.pbtn1.setStyleSheet(self.blueBtn)

        # self.pushButton.setStyleSheet(self.blueBtn1)
        # self.pushButton_2.setStyleSheet(self.blueBtn1)
        # self.pushButton_3.setStyleSheet(self.blueBtn1)
        # self.pushButton_4.setStyleSheet(self.blueBtn1)
        # self.pushButton_6.setStyleSheet(self.blueBtn1)
        # self.pushButton_7.setStyleSheet(self.blueBtn1)
        # self.pushButton_9.setStyleSheet(self.blueBtn1)
        # self.widget1.setStyleSheet('''
        #   QPushButton{border:none;color:white;}
        #   QPushButton#left_label{
        #     border:none;
        #     border-bottom:1px solid white;
        #     font-size:18px;
        #     font-weight:700;
        #     font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        #   }
        #   QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        # ''')

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    # QApplication.processEvents()实现页面刷新


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
