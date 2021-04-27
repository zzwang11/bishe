from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from tools.test_connect import TestCon
from tools.get_ins import GetCon
from tools import write_conf
from dialog_util.dialogUtil import *

import nsa
import field_sys
import start
import svswr


class ConnectTest(QWidget):
    myout = pyqtSignal(int)
    myout1 = pyqtSignal(str)

    def __init__(self, rm):
        super(ConnectTest, self).__init__()
        self.initUI()
        # self.win1 = win1
        self.rm = rm

    def initUI(self):
        self.setWindowIcon(QtGui.QIcon('h:/bishe/img/icon.ico'))
        gbox = QGridLayout(self)
        self.setWindowTitle('连接')

        self.resize(800, 400)
        self.setMaximumSize(800, 400)
        self.setMinimumSize(800, 400)

        self.label = QLabel(self)
        self.label.setText("显示图片")
        self.label.setFixedSize(780, 200)
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}"
                                 "QLabel{alignment:AlignHCenter,AlignVCenter}"
                                 )
        gbox.addWidget(self.label, 0, 0, 2, 4)
        jpg = QtGui.QPixmap('h:/bishe/img/disconn.jpg')
        self.label.setPixmap(jpg)

        self.radioButton = QtWidgets.QRadioButton()
        self.radioButton.setText("USB连接")
        gbox.addWidget(self.radioButton, 2, 0, 1, 1)
        self.radioButton_1 = QtWidgets.QRadioButton()
        self.radioButton_1.setText("GPIB连接")
        gbox.addWidget(self.radioButton_1, 2, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton()
        self.radioButton_2.setText("网线连接")
        gbox.addWidget(self.radioButton_2, 2, 2, 1, 1)
        self.pushButton1 = QtWidgets.QPushButton()
        self.pushButton1.setText('查询')
        gbox.addWidget(self.pushButton1, 2, 3, 1, 1)

        self.line = QtWidgets.QFrame()
        self.line.setEnabled(False)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        gbox.addWidget(self.line, 3, 0, 1, 4)
        self.comb = QtWidgets.QComboBox(self)
        self.comb.addItems([])
        gbox.addWidget(self.comb, 4, 0, 1, 4)

        self.label1 = QLabel()
        self.label1.setText('手动输入:')
        gbox.addWidget(self.label1, 5, 0, 1, 1)
        self.textlin = QLineEdit()
        gbox.addWidget(self.textlin, 5, 1, 1, 3)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setText('测试连接')
        gbox.addWidget(self.pushButton, 6, 2, 1, 1)
        self.pushButton2 = QtWidgets.QPushButton()
        self.pushButton2.setText('保存地址')
        gbox.addWidget(self.pushButton2, 6, 3, 1, 1)

        self.setLayout(gbox)
        self.pushButton1.setEnabled(False)

        self.radioButton.toggled.connect(self.buttonState)
        self.radioButton_1.toggled.connect(self.buttonState)
        self.radioButton_2.toggled.connect(self.buttonState)
        self.pushButton.clicked.connect(self.conn)
        self.pushButton1.clicked.connect(self.conn1)
        self.pushButton2.clicked.connect(self.savepath)
        self.comb.activated[str].connect(self.select)

    def conn1(self):
        self.inst = GetCon()
        self.inst.start()
        self.inst.myOut.connect(self.suan)
        if self.state == "USB连接":
            self.comb.addItems(['USB::0x1234::125::A22-5::INSTR'])
        elif self.state == "GPIB连接":
            self.comb.addItems(["GPIB::1::0::INSTR"])
        elif self.state == "网线连接":
            self.comb.addItems(['TCPIP::192.6.94.9::inst0::INSTR'])

    def suan(self, j):
        self.comb.addItems(j)

    def select(self, s):
        self.ins = s
        self.textlin.setText(self.ins)

    def buttonState(self):
        self.pushButton1.setEnabled(True)
        radioButton = self.sender()
        self.comb.clear()
        if radioButton.isChecked():
            self.state = radioButton.text()

    def conn(self):
        self.a = TestCon(self.textlin.text(),self.rm)
        self.a.start()
        self.a.myOut.connect(self.jug)

    def jug(self, i):
        if i == 1:
            information_dialog(self, '成功', '连接成功')
            self.myout.emit(1)
            self.myout1.emit(self.textlin.text())
            jpg = QtGui.QPixmap('h:/bishe/img/connect.jpg')
            self.label.setPixmap(QPixmap(""))
            self.label.setPixmap(jpg)

        else:
            information_dialog(self, '失败', '连接失败')
            self.myout.emit(0)
            jpg = QtGui.QPixmap('h:/bishe/img/disconn.jpg')
            self.label.setPixmap(QPixmap(""))
            self.label.setPixmap(jpg)

    def savepath(self):
        aa = self.textlin.text()
        self.wr = write_conf.writeThread(ip=aa)
        self.wr.start()
        if self.win1:
            self.win1.show()
        self.close()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window1 = field_sys.MyMainWindow()
#     window3 = nsa.MyMainWindow()
#     window4 = svswr.MyMainWindow()
#     win1 = start.Choice(window1, window3, window4)
#     demo = ConnectTest(win1)
#     demo.show()
#     sys.exit(app.exec_())
