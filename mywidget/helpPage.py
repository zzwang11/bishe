import sys
from PyQt5.QtWidgets import *


class mainwindow(QMainWindow):
    def __init__(self, parent=None):
        super(mainwindow,self).__init__(parent)
        self.setWindowTitle('treeWidget')
        self.resize(800,600)
        self.tree = QTreeWidget()
        root = QTreeWidgetItem(self.tree)
        root.setText(0,'root')
        son1 = QTreeWidgetItem(root)
        son1.setText(0, 'son1')
        son2 = QTreeWidgetItem(root)
        son2.setText(0,'son2')

        root1 = QTreeWidgetItem(self.tree)
        root1.setText(0,'root1')
        son11 = QTreeWidgetItem(root1)
        son11.setText(0, 'son11')
        son21 = QTreeWidgetItem(root1)
        son21.setText(0,'son21')

        self.tree.addTopLevelItem(root)
        self.setCentralWidget(self.tree)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mainwindow()
    w.show()
    sys.exit(app.exec_())
