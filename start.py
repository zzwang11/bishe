import field_sys

import nsa
import svswr
import sys
from mywidget import connect_test_win
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Choice(QDialog):

    def __init__(self,win1,win3,win4):
        super(Choice, self).__init__()
        self.initUI()
        self.win1 = win1
        self.win3 = win3
        self.win4 = win4

    def initUI(self):
        self.setWindowTitle('选择测试项目')
        self.setWindowIcon(QIcon('e:/bishe/img/icon.ico'))
        layout = QGridLayout()




        self.button2 = QPushButton('场地系统衰减测试')
        self.button2.clicked.connect(lambda: self.whichButton('field'))
        layout.addWidget(self.button2, 0, 0)



        self.button3 = QPushButton('归一化场地衰减测试')
        self.button3.clicked.connect(lambda: self.whichButton('guiyi'))
        layout.addWidget(self.button3, 1, 0)

        self.button4 = QPushButton('场地电压驻波比测试')
        self.button4.clicked.connect(lambda: self.whichButton('vswr'))
        layout.addWidget(self.button4, 2, 0)

        self.button2.setMaximumWidth(200)
        self.button3.setMaximumWidth(200)
        self.button4.setMaximumWidth(200)

        self.setLayout(layout)
        self.resize(300, 150)
        self.setMaximumSize(300, 150)
        self.setMinimumSize(300, 150)

    def whichButton(self, b):
        # win5.show()
        if b == 'field':
            self.win1.show()
        # elif b == 'bwipo':
        #     self.win2.show()
        elif b == 'guiyi':
            self.win3.show()
        elif b == 'vswr':
            self.win4.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Choice()
    main.show()
    sys.exit(app.exec_())
