import sys
import os
from PyQt5.QtWidgets import QWidget, QFileDialog, QPushButton, QGridLayout, QApplication, QFormLayout, QLineEdit


class win(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.btnOpen = QPushButton('open path')
        self.btnSave = QPushButton('save path')
        self.btnOk = QPushButton('ok')
        self.btnOpen.clicked.connect(self.openFile)
        self.btnSave.clicked.connect(self.saveFile)
        self.btnOk.clicked.connect(self.ok)
        self.openLine = QLineEdit()
        self.saveLine = QLineEdit()
        self.formlayout = QFormLayout()
        self.formlayout.addRow('打开路径', self.openLine)
        self.formlayout.addRow('保存路径', self.saveLine)
        self.grid = QGridLayout()
        self.grid.addItem(self.formlayout, 0, 0)
        self.grid.addWidget(self.btnOpen, 1, 0)
        self.grid.addWidget(self.btnSave, 2, 0)
        self.grid.addWidget(self.btnOk, 3, 0)
        self.setLayout(self.grid)
        self.show()

    def openFile(self):
        self.file, fileType = QFileDialog.getOpenFileName(self, 'open file', './', "ALL (*.*)")
        if self.file:
            self.openLine.setText(str(self.file))

    def saveFile(self):
        self.fname, ftype = QFileDialog.getSaveFileName(self, 'save file', './', "ALL (*.*)")
        if self.fname:
            self.saveLine.setText(self.fname)

    def ok(self):
        if self.fname:
            if os.path.exists(self.file):
                with open(self.file, 'r') as f:
                    content = f.read()
                    with open(self.fname, 'w') as fn:
                        fn.write(content)
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = win()
    window.show()
    sys.exit(app.exec_())