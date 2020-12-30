'''

拖动控件之间的边界（QSplitter）

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import os

class Splitter(QWidget):
    def __init__(self):
        super(Splitter, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        self.setWindowTitle('帮助')
        self.width = QApplication.desktop().screenGeometry().width()
        self.height = QApplication.desktop().screenGeometry().height()
        self.resize(int(self.width//1.5), int(self.height/1.5))
        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(['列表'])
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'OTA')

        child1 = QTreeWidgetItem(root)
        child1.setText(0, '场地系统衰减测试')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, '静区纹波测试')

        root1 = QTreeWidgetItem(self.tree)
        root1.setText(0, 'EMC')

        child3 = QTreeWidgetItem(root1)
        child3.setText(0, '归一化场地衰减测试')

        child4 = QTreeWidgetItem(root1)
        child4.setText(0, '场地电压驻波比测试')

        self.tree.clicked.connect(self.onTreeClicked)

        self.splitter1 = QSplitter(Qt.Horizontal)
        # self.textedit = QTextEdit()
        # self.textedit.setFocusPolicy(Qt.NoFocus)
        # self.textedit.setText('')

        self.browser = QWebEngineView()

        self.splitter1.addWidget(self.tree)
        self.splitter1.addWidget(self.browser)
        self.splitter1.setSizes([200, 500])

        hbox.addWidget(self.splitter1)
        self.setLayout(hbox)

    def onTreeClicked(self):
        item = self.tree.currentItem()
        if item.text(0) == '场地系统衰减测试':
            url = os.getcwd() + '/file/1.htm'
        elif item.text(0) == '静区纹波测试':
            url = os.getcwd() + '/file/2.htm'
        elif item.text(0) == '归一化场地衰减测试':
            url = os.getcwd() + '/file/3.htm'
        elif item.text(0) == '场地电压驻波比测试':
            url = os.getcwd() + '/file/4.htm'
        else:
            url = os.getcwd() + '/file/5.htm'
        self.browser.load(QUrl.fromLocalFile(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Splitter()
    demo.show()
    sys.exit(app.exec_())

