import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

'''
连接器件的图片教程页面
'''


class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()

        self.resize(910, 500)
        self.setWindowTitle("选择连接模式")
        self.setMaximumSize(910, 500)
        self.setMinimumSize(910, 500)
        self.label = QLabel(self)
        self.label.setText("显示图片")
        self.label.setFixedSize(900, 420)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}"
                                 "QLabel{alignment:AlignHCenter,AlignVCenter}"
                                 )

        btn = QPushButton(self)
        btn.resize(200,60)
        btn.setText("关闭")
        btn.clicked.connect(self.close)
        self.openimage('线缆连接测量')

        comb = QtWidgets.QComboBox(self)
        comb.addItems(['线缆连接测量','天线连接测量'])
        comb.activated[str].connect(self.openimage)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(comb)
        vbox1.addWidget(self.label)

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(vbox1)
        vbox.addWidget(btn, alignment=Qt.AlignRight)
        self.setLayout(vbox)

    def openimage(self,s):

        d = {'线缆连接测量':'zhijie.png', '天线连接测量':'tianxian.png'}
        imgName = './img/'+d[s]
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())