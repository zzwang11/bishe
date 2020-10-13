import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from MainWindow import Ui_MainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtGui
import connectPic
import helpPage


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.setupUi(self)
        self.pushButton_5.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_4.clicked.connect(self.save_file)
        self.actionconnect.triggered.connect(self.conn)
        self.action5.triggered.connect(QCoreApplication.instance().quit)
        self.actionhelp.triggered.connect(self.helppage)

    def save_file(self):
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "./", "All Files (*);;Text Files (*.txt)")
        save_path = fileName2
        if save_path is not None:
            with open(file=save_path, mode='a+', encoding='utf-8') as file:
                file.write('self.text_value.toPlainText()')
            print('已保存！')

    def conn(self):
        self.a = connectPic.picture()
        self.a.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.a.show()

    def helppage(self):
        self.b = helpPage.mainwindow()
        self.a.setWindowIcon(QtGui.QIcon('./img/cartoon4.ico'))
        self.b.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())