import os
from PyQt5.QtCore import QThread,pyqtSignal


class Result(QThread):
    myOut = pyqtSignal(list)

    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath

    def run(self):
        with open(self.filepath, 'r') as f:
            a = f.read()
        s = a.split()

        l = []
        # li = []
        # while i < len(s):
        #     if i % 2 == 0:
        #         l.append(float(s[i]))
        #     else:
        #         li.append(float(s[i]))
        #     i+=1
        #
        # self.myOut.emit(l,li)
        for i in s:
            l.append(eval(i))
        self.myOut.emit(l)