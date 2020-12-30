from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from tools.test_connect import TestCon
from tools.get_ins import GetCon
from dialog_util.dialogUtil import *

class connect_Test(QWidget):
    def __init__(self):
        super(connect_Test, self).__init__()
        self.initUI()

    def initUI(self):

        vbox = QGridLayout(self)
        self.setWindowTitle('连接')
        # self.width = QApplication.desktop().screenGeometry().width()
        # self.height = QApplication.desktop().screenGeometry().height()
        # self.resize(int(self.width//5), int(self.height/3))
        self.resize(400,180)
        self.setMaximumSize(400,180)
        self.setMinimumSize(400,180)

        self.radioButton = QtWidgets.QRadioButton()
        self.radioButton.setText("USB连接")
        vbox.addWidget(self.radioButton,0,0,1,1)
        self.radioButton_1 = QtWidgets.QRadioButton()
        self.radioButton_1.setText("GPIB连接")
        vbox.addWidget(self.radioButton_1,0,1,1,1)
        self.radioButton_2 = QtWidgets.QRadioButton()
        self.radioButton_2.setText("网线连接")

        vbox.addWidget(self.radioButton_2,0,2,1,1)
        self.pushButton1 = QtWidgets.QPushButton()
        self.pushButton1.setText('自动查询')
        vbox.addWidget(self.pushButton1,0,3,1,1)

        self.line = QtWidgets.QFrame()
        self.line.setEnabled(False)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        vbox.addWidget(self.line,1,0,1,4)
        self.comb = QtWidgets.QComboBox(self)
        self.comb.addItems([])
        vbox.addWidget(self.comb,2,0,1,4)

        self.label = QLabel()
        self.label.setText('手动输入:')
        vbox.addWidget(self.label,3,0,1,1)
        self.textlin = QLineEdit()
        vbox.addWidget(self.textlin,3,1,1,3)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setText('测试连接')
        vbox.addWidget(self.pushButton,4,3,1,1)

        self.setLayout(vbox)

        self.radioButton.toggled.connect(self.buttonState)
        self.radioButton_1.toggled.connect(self.buttonState)
        self.radioButton_2.toggled.connect(self.buttonState)
        self.pushButton.clicked.connect(self.conn)
        self.pushButton1.clicked.connect(self.conn1)
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
            self.comb.addItems(['TCPIP::192.168.0.5::inst0::INSTR'])

    def suan(self, j):
        self.comb.addItems(j)

    def select(self, s):
        self.ins = s
        self.textlin.setText(self.ins)

    def buttonState(self):
        radioButton = self.sender()
        self.comb.clear()
        if radioButton.isChecked():
            self.state=radioButton.text()



    def conn(self):
        self.a = TestCon(self.textlin.text())
        self.a.start()
        self.a.myOut.connect(self.jug)

    def jug(self, i):
        if i == 1:
            information_dialog(self, '成功', '连接成功')
        else:
            information_dialog(self, '失败', '连接失败')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = connect_Test()
    demo.show()
    sys.exit(app.exec_())