import field_sys
import bwipo
import nsa
import vswr
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Choice(QDialog) :
    def __init__(self):
        super(Choice,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('选择测试项目')
        self.setWindowIcon(QIcon('./img/cartoon4.ico'))
        layout = QGridLayout()

        self.label = QLabel('OTA')
        layout.addWidget(self.label,0,0)
        # self.label.setMaximumSize(40,30)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}"
                                 "QLabel{alignment:AlignHCenter,AlignVCenter}"
                                 )
        self.button1 = QPushButton()
        self.button1.setText('纹波测试')
        self.button1.clicked.connect(lambda :self.whichButton('bwipo'))
        layout.addWidget(self.button1,1,0)

        self.button2 = QPushButton('场地系统衰减测试')
        self.button2.clicked.connect(lambda:self.whichButton('field'))
        layout.addWidget(self.button2,2,0)

        self.label1 = QLabel('EMC')
        self.label1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # self.label1.setMaximumSize(40,30)
        self.label1.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}"
                                 "QLabel{alignment:AlignHCenter,AlignVCenter}"
                                 )

        layout.addWidget(self.label1,0,1)

        self.button3 = QPushButton('归一化场地衰减测试')
        self.button3.clicked.connect(lambda:self.whichButton('guiyi'))
        layout.addWidget(self.button3,1,1)

        self.button4 = QPushButton('场地电压驻波比测试')
        self.button4.clicked.connect(lambda:self.whichButton('vswr'))
        layout.addWidget(self.button4,2,1)

        self.setLayout(layout)
        self.resize(400,150)
        self.setMaximumSize(400,150)
        self.setMinimumSize(400,150)

    def whichButton(self,b):
        if b == 'field':
            window1.show()
        elif b == 'bwipo':
            window2.show()
        elif b == 'guiyi':
            window3.show()
        elif b == 'vswr':
            window4.show()

        main.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window1 = field_sys.MyMainWindow()
    window2 = bwipo.MyMainWindow()
    window3 = nsa.MyMainWindow()
    window4 = vswr.MyMainWindow()

    main = Choice()
    main.show()
    sys.exit(app.exec_())

