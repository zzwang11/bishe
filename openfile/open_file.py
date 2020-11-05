from PyQt5.QtWidgets import QFileDialog


def open_event():
    directory1, ok1 = QFileDialog.getOpenFileName(None, "选择文件", "/save/")
    print(directory1)  # 打印文件夹路径ok1
    path = directory1
    if path:
        try:
            with open(file=path, mode='r+', encoding='utf-8') as file:
                # self.text_value.setPlainText(file.read())
                print(file.read())
        except:
            print('not exist or not txt')