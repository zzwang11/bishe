import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QStatusBar
from mywidget.field_sys_win import Ui_MainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtGui, QtCore
from mywidget import field_pic, helpPage, connect_test_win
from tools import write_conf, read_conf, read_data, test_connect
from dialog_util.dialogUtil import *
from control_vna.control_suit import suit_cla
from thread_exa.wait_thread import myThread
import os
import pyqtgraph as pg
import tools.setcon
import shutil

icon = 'e:/bishe/img/icon.ico'


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon(icon))
        self.setupUi(self)
        # 状态栏
        self.mak = 0
        self.blueBtn = '''QPushButton{background:rgb(100,149,237);border-radius:10px;}\
        QPushButton:hover{background:rgb(65,105,225);border-radius:10px;}'''
        self.blueBtn1 = '''QPushButton{background:rgb(100,149,237);border-radius:2px;}\
        QPushButton:hover{background:rgb(65,105,225);border-radius:2px;}'''
        self.redBtn = '''QPushButton{background:rgb(255,192,203);border-radius:10px;}\
                QPushButton:hover{background:rgb(255,182,193);border-radius:10px;}'''
        self.preSet()
        self.qss()

        self.test_con()
        # 绑定模式
        self.radioButton.toggled.connect(self.buttonState)
        self.radioButton_2.toggled.connect(self.buttonState)

        # 实现测量开始、暂停、继续、停止
        self.pushButton.clicked.connect(self.measure)
        self.pushButton_2.clicked.connect(self.pause)
        self.pushButton_3.clicked.connect(self.terminate_m)
        self.pushButton_4.clicked.connect(self.go_on)

        # 实现测量所需数据的保存和读取
        self.pushButton_5.clicked.connect(self.save_result)
        self.pushButton_6.clicked.connect(self.writeconf)
        self.pushButton_7.clicked.connect(self.readconf)
        self.pushButton_8.clicked.connect(self.read_result)
        self.pushButton_9.clicked.connect(self.test_con)
        self.pushButton_11.clicked.connect(self.jisuan)
        self.actionconnect.triggered.connect(self.con_pic)
        self.actionopen.triggered.connect(self.read_result)
        self.action1.triggered.connect(self.measure)
        self.action2.triggered.connect(self.pause)
        self.action3.triggered.connect(self.terminate_m)
        self.action4.triggered.connect(self.save_result)
        self.action.triggered.connect(self.go_on)
        self.action5.triggered.connect(QCoreApplication.instance().quit)
        self.actionhelp.triggered.connect(self.helppage)

    def read_result(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./save/", "All Files (*);;Text Files (*.txt)")
        with open(fileName1, 'r') as f:
            a = f.read().split()
        c = []
        for i in a:
            c.append(eval(i))
        self.result = c
        self.pyqtgraph1.clear()
        self.c = self.pyqtgraph1.addPlot(title='最终的结果', pen=pg.mkPen(color='b'))
        self.c.setLabel('left', "PL", units='dB')
        self.c.setLabel('bottom', "频率", units='MHz')
        self.c.setLogMode(x=False, y=False)
        self.c.plot(y=c, pen=pg.mkPen(color='r', width=2))

    def save_result(self):
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "./", "Text Files (*.txt)")
        try:
            shutil.copy('e:/bishe/save/3.txt', fileName2)
            information_dialog(self, '提示', '保存成功')
        except:
            information_dialog(self, '提示', '保存失败')

    def buttonState(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.state = radioButton.text()
            information_dialog(self, '提示', '请先进行连线测量，再进行天线测量')
            self.con_pic()
            self.pyqtgraph1.clear()
            self.c = self.pyqtgraph1.addPlot(title=self.state, pen=pg.mkPen(color='b'))
            self.c.setLabel('left', "S21", units='dB')
            self.c.setLabel('bottom', "频率", units='MHz')
            self.c.setLogMode(x=False, y=False)

    def jisuan(self):
        with open('./save/1.txt', 'r') as f:
            a = f.read().split()
        with open('./save/2.txt', 'r') as f:
            b = f.read().split()
        c = []
        for i in range(len(a)):
            c.append(eval(b[i]) - eval(a[i]) - eval(self.LineEdit_12))
        with open('./save/3.txt', 'w') as f:
            for i in c:
                f.write(str(i) + '\n')
        self.pyqtgraph1.clear()
        self.c = self.pyqtgraph1.addPlot(title='最终结果', pen=pg.mkPen(color='b'))
        self.c.setLabel('left', "PL", units='dB')
        self.c.setLabel('bottom', "频率", units='MHz')
        self.c.setLogMode(x=False, y=False)
        self.c.plot(y=c, pen=pg.mkPen(color='r', width=2))

    def set_2d(self, a):
        tools.setcon.pic_2d(self, a)

    def preSet(self):
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.progressBar.setValue(0)
        self.readconf()
        self.path = './save'
        self.state = "线缆连接测量"
        self.save_path = 'd://save//'
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)

    def test_con(self):
        self.test = connect_test_win.ConnectTest()
        self.test.setWindowIcon(QtGui.QIcon(icon))
        self.test.show()
        self.test.setFocus()
        self.test.myout.connect(lambda i: self.LineEdit.setText(i))

    def con_pic(self):
        self.pic = field_pic.picture()
        self.pic.setWindowIcon(QtGui.QIcon(icon))
        self.pic.show()

    def helppage(self):
        self.help_page = helpPage.Splitter()
        self.help_page.setWindowIcon(QtGui.QIcon(icon))
        self.help_page.show()

    def get_con(self):
        try:
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
        except:
            li = []
            print('read error!')
        return li

    def measure(self):

        # self.thread_exa = suit_cla()
        # self.thread_exa.start()
        # self.thread_exa.mySig.connect(self.mat)

        self.select_change(1)
        self.pyqtgraph1.clear()
        self.c = self.pyqtgraph1.addPlot(title=self.state, pen=pg.mkPen(color='r', width=2))
        self.c.setLabel('left', "S21", units='dB')
        self.c.setLabel('bottom', "频率", units='MHz')
        self.c.setLogMode(x=False, y=False)

        self.statusBar.showMessage('测量中......', 10 ** 8)
        self.pushButton.setEnabled(False)
        self.thread1 = myThread(self.state)
        self.thread1.start()
        # self.thread1.mySig.connect(lambda i:self.progressBar.setValue(i))
        self.thread1.mySig.connect(self.setbar)
        self.thread1.mySig1.connect(self.mat)
        self.thread1.mySig2.connect(self.succ_dialog)
        self.thread1.mySig2.connect(self.finish)

    def finish(self):
        self.mak += 1
        self.pushButton.setEnabled(True)
        self.statusBar.showMessage('测量完成', 10 ** 8)

    def mat(self):
        if self.state == "线缆连接测量":
            path = './save/1.txt'
        else:
            path = './save/2.txt'

        with open(path, 'r') as f:
            a = f.read().split()
        li = []
        for i in a:
            li.append(eval(i))

        self.c.plot(y=li, pen=pg.mkPen(color='r', width=2))

    def setbar(self, a):
        self.progressBar.setValue(a * 10)

    def pause(self):
        self.thread1.pause()
        self.statusBar.showMessage('暂停测量', 10 ** 8)
        self.graph.show()

    def go_on(self):
        self.thread1.goon()
        self.statusBar.showMessage('测量中......', 10 ** 8)

    def terminate_m(self):
        self.thread1.terminate()
        self.thread1.wait()
        self.pushButton.setEnabled(True)
        self.statusBar.showMessage('测量结束！', 10 ** 8)

    def writeconf(self):
        li = self.get_con()
        self.wr = write_conf.writeThread(mod=li[0], add=li[1], ip=li[2], start=li[3], stop=li[4],
                                         ifband=li[5], averages=li[6], power=li[7], edelay=li[8], points=li[9],
                                         outputfile=li[10])
        self.wr.start()
        self.statusBar.showMessage('保存配置成功！', 10 ** 5)

    def readconf(self):
        self.rd = read_conf.MyTh('test_all')
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
        warning_dialog(self, '失败', '失败')

    def succ_dialog(self):
        information_dialog(self, '成功', '测量完成')

    def qss(self):
        self.pushButton_5.setStyleSheet(self.blueBtn)
        self.pushButton_8.setStyleSheet(self.blueBtn)
        self.pushButton_11.setStyleSheet(self.redBtn)

        # self.pushButton.setStyleSheet(self.blueBtn1)
        # self.pushButton_2.setStyleSheet(self.blueBtn1)
        # self.pushButton_3.setStyleSheet(self.blueBtn1)
        # self.pushButton_4.setStyleSheet(self.blueBtn1)
        # self.pushButton_6.setStyleSheet(self.blueBtn1)
        # self.pushButton_7.setStyleSheet(self.blueBtn1)
        # self.pushButton_9.setStyleSheet(self.blueBtn1)

    # QApplication.processEvents()实现页面刷新


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
