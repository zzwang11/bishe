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
        b = a.split()
        c = [int(i) for i in b]
        self.myOut.emit(c)