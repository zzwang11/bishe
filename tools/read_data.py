import os
from PyQt5.QtCore import QThread,pyqtSignal


class MyRD(QThread):
    myOut = pyqtSignal(list)

    def __init__(self, filepath,name):
        super().__init__()
        self.filepath = os.path.join(filepath, f"{name}.txt")

    def run(self):
        with open(self.filepath, 'r') as f:
            a = f.read()
        b = a.split()
        c = [int(i) for i in b]
        self.myOut.emit(c)
