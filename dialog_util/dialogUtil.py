from PyQt5.QtWidgets import QMessageBox


def fail_dialog(self,title,message):
    a = QMessageBox()
    a.warning(self, title, message, QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Yes)


def success_dialog(self,title,message):
    a = QMessageBox()
    a.information(self, title, message, QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Yes)