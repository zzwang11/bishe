import os
from PyQt5.QtCore import QThread,pyqtSignal


class Js(QThread):
    myOut = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        with open('./save/1.txt', 'r') as f:
            a = f.read().split()
        with open('./save/2.txt', 'r') as f:
            b = f.read().split()
        with open('./save/3.txt', 'r') as f:
            c = f.read().split()
        with open('./save/4.txt', 'r') as f:
            d = f.read().split()
        with open('./save/5.txt', 'r') as f:
            e = f.read().split()
        with open('./save/6.txt', 'r') as f:
            g = f.read().split()
        li = []
        for i in range(len(a)):
            li.append(max(eval(b[i]),eval(a[i]),eval(c[i])))

        self.myOut.emit(li)