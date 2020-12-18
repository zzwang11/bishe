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
        c = []
        for i in range(len(a)):
            c.append(eval(b[i]) - eval(a[i]))
        with open('./save/3.txt', 'w') as f:
            f.write(c)