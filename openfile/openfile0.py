from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QFileDialog
import sys
from openfile.open_file import open_event

class MyWindow(QtWidgets.QWidget):
    # save_path=''
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(400,300)
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setGeometry(QtCore.QRect(40, 200, 200, 20))
        self.oneBtn = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        self.myButton.clicked.connect(self.msg)
        self.oneBtn.setObjectName("oneButton")
        self.oneBtn.setText("Test1")
        self.oneBtn.clicked.connect(self.save_event)
        self.twoBtn = QtWidgets.QPushButton(self)
        self.twoBtn.setText('Test2')
        self.twoBtn.clicked.connect(open_event)
        cc = QtWidgets.QVBoxLayout()
        cc.addWidget(self.myButton)
        cc.addWidget(self.oneBtn)
        cc.addWidget(self.twoBtn)
        self.setLayout(cc)
        self.show()

    def msg(self):
        # directory1 = QFileDialog.getExistingDirectory(self,
        #                                               "选取文件夹",
        #                                               "./")  # 起始路径
        # print(directory1)
        #
        # fileName1, filetype = QFileDialog.getOpenFileName(self,
        #                                                   "选取文件",
        #                                                   "./",
        #                                                   "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        # print(fileName1, filetype)
        #
        # files, ok1 = QFileDialog.getOpenFileNames(self,
        #                                           "多文件选择",
        #                                           "./",
        #                                           "All Files (*);;Text Files (*.txt)")
        # print(files, ok1)

        fileName2, ok2 = QFileDialog.getSaveFileName(self,
                                                     "文件保存",
                                                     "./",
                                                     "All Files (*);;Text Files (*.txt)")
        print(fileName2,ok2)

    # def open_event(self):
    #     directory1 = None
    #     directory1, ok1 = QFileDialog.getOpenFileName(None, "选择文件", "/")
    #     print(directory1)  # 打印文件夹路径ok1
    #     path = directory1
    #     if path:
    #         try:
    #             with open(file=path, mode='r+', encoding='utf-8') as file:
    #                 # self.text_value.setPlainText(file.read())
    #                 print(file.read())
    #         except:
    #             print('not exist or not txt')

    def save_event(self):
        # global save_path
        # _translate = QtCore.QCoreApplication.translate
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "./","All Files (*);;Text Files (*.txt)")
        print(fileName2)  # 打印保存文件的全部路径（包括文件名和后缀名）
        save_path = fileName2
        # self.save_path_text.setText(_translate("Form", save_path))
        if save_path:
            try:
                with open(file=save_path, mode='a+', encoding='utf-8') as file:
                    file.write('self.text_value.toPlainText()')
                print('已保存！')
            except:
                print('write fail')

    '''
    directory1 = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
    print(directory1)  # 打印文件夹路径
    text.setText(_translate("Form", directory1))
    fileName, filetype = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;Text Files (*.txt)")
    print(fileName, filetype)  # 打印文件全部路径（包括文件名和后缀名）和文件类型
    print(fileName)  # 打印文件全部路径（包括文件名和后缀名）
    text.setText(_translate("Form", fileName))
    fileinfo = QFileInfo(fileName)
    print(fileinfo)  # 打印与系统相关的文件信息，包括文件的名字和在文件系统中位置，文件的访问权限，是否是目录或符合链接，等等。
    file_name = fileinfo.fileName()
    print(file_name)  # 打印文件名和后缀名
    file_suffix = fileinfo.suffix()
    print(file_suffix)  # 打印文件后缀名
    file_path = fileinfo.absolutePath()
    print(file_path)  # 打印文件绝对路径（不包括文件名和后缀名）
    files, ok1 = QFileDialog.getOpenFileNames(self, "多文件选择", "/", "所有文件 (*);;文本文件 (*.txt)")
    print(files, ok1)  # 打印所选文件全部路径（包括文件名和后缀名）和文件类型
    fileName2, ok2 = QFileDialog.getSaveFileName(self, "文件保存", "/", "图片文件 (*.png);;(*.jpeg)")
    print(fileName2)  # 打印保存文件的全部路径（包括文件名和后缀名）
    '''


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())