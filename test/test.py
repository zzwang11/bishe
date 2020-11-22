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

'''

绘制不同类型的直线



'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine,self).__init__()
        self.resize(300,300)
        self.setWindowTitle('设置Pen的样式')

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)


        pen = QPen(Qt.red,3,Qt.SolidLine)

        painter.setPen(pen)
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,10,5,8])
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)


        size = self.size()



        painter.end()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()
    sys.exit(app.exec_())