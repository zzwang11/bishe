# class c:
#     def __init__(self,aa):
#         self.aa = aa
#
#     def d(self):
#         if self.aa:
#             print(123)
#         else:
#             print(456)
#
#
#
# m = c()
# m.d()

# def a(*aa):
#     if aa == ('aaaaaa',):
#         print(222)
#     print(aa)
#     print(*aa)
#
# a('aaaaaa')

# import configparser
#
#
# def read(*a):
#     c = configparser.ConfigParser()
#     c.read('e://bishe//config.ini')
#     b = c.get(*a)
#     print(b)
#     print(type(b))
#
# read('test_config','ip')

# '''
#
# 绘制不同类型的直线
#
#
#
# '''
#
# import sys,math
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import Qt
#
# class DrawMultiLine(QWidget):
#     def __init__(self):
#         super(DrawMultiLine,self).__init__()
#         self.resize(300,300)
#         self.setWindowTitle('设置Pen的样式')
#
#     def paintEvent(self, event):
#         painter = QPainter()
#         painter.begin(self)
#
#
#         pen = QPen(Qt.red,3,Qt.SolidLine)
#
#         painter.setPen(pen)
#         painter.drawLine(20,40,250,40)
#
#         pen.setStyle(Qt.DashLine)
#         painter.setPen(pen)
#         painter.drawLine(20, 80, 250, 80)
#
#         pen.setStyle(Qt.DashDotDotLine)
#         painter.setPen(pen)
#         painter.drawLine(20, 120, 250, 120)
#
#         pen.setStyle(Qt.DotLine)
#         painter.setPen(pen)
#         painter.drawLine(20, 160, 250, 160)
#
#         pen.setStyle(Qt.DashDotDotLine)
#         painter.setPen(pen)
#         painter.drawLine(20, 200, 250, 200)
#
#         pen.setStyle(Qt.CustomDashLine)
#         pen.setDashPattern([1,10,5,8])
#         painter.setPen(pen)
#         painter.drawLine(20, 240, 250, 240)
#
#
#         size = self.size()
#
#
#
#         painter.end()
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = DrawMultiLine()
#     main.show()
#     sys.exit(app.exec_())

# from pyqtgraph.Qt import QtCore, QtGui
# import pyqtgraph as pg
# import scipy.ndimage as ndi
# import numpy as np
#
# Nf = 90     # No. of frames
# Ns = 100    # Signal length
#
# app = QtGui.QApplication([])
#
# Arx = np.zeros([Nf, Ns])
# win = pg.image(Arx)
# win.view.setAspectLocked()
# def update():
#     global Arx
#     Arx = np.roll(Arx, 1, axis=0)
#     Arx[0] = ndi.gaussian_filter(np.random.normal(size=(1,Ns)), (1, 1))
#     win.setImage(Arx.T, autoRange=False)
#
# timer = QtCore.QTimer()
# timer.timeout.connect(update)
# timer.start(30)
#
# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtGui.QApplication.instance().exec_()

# import time
# # a = (i for i in range(1,10,1))
# a = [i for i in range(10)]
# i = 0
# while True:
#     print(a[i])
#     i += 1
#     if i>9:
#         i = 0
#     time.sleep(0.5)
#     d = time.time()
#
#     b = str(d)[10:14]
#     print(time.strftime("%H:%M:%S",time.localtime()),end='')
#     print(str(b))
import sys

ss = 1
print(sys.getsizeof(ss))
with open("../save/1.txt",'r') as f:
    for line in f:
        print(line)
    # a = f.readline()
    # while a:
    #
    #     print(a)
    #     print(sys.getsizeof(a))
    #     a = f.readline()
# b = a.split()
# c = f.readlines(7)
# print(c)
# print(b)
# print(type(a))

# import socket
#
# print("您当前的主机名为" + socket.gethostname())
#
# print("您当前的IP地址为" + socket.gethostbyname(socket.gethostname()))