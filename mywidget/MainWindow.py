# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 490, 624, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(21, 21, 581, 451))
        self.graphicsView.setObjectName("graphicsView")
        self.formGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.formGroupBox.setGeometry(QtCore.QRect(660, 20, 321, 461))
        self.formGroupBox.setObjectName("formGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.formGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.formGroupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.LineEdit_5 = QtWidgets.QLineEdit(self.formGroupBox)
        self.LineEdit_5.setObjectName("LineEdit_5")
        self.gridLayout.addWidget(self.LineEdit_5, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.formGroupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 2, 1, 1)
        self.Label_3 = QtWidgets.QLabel(self.formGroupBox)
        self.Label_3.setObjectName("Label_3")
        self.gridLayout.addWidget(self.Label_3, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.formGroupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 2, 1, 1)
        self.Label_10 = QtWidgets.QLabel(self.formGroupBox)
        self.Label_10.setObjectName("Label_10")
        self.gridLayout.addWidget(self.Label_10, 10, 0, 1, 1)
        self.LineEdit_2 = QtWidgets.QLineEdit(self.formGroupBox)
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.gridLayout.addWidget(self.LineEdit_2, 1, 1, 1, 1)
        self.Label_2 = QtWidgets.QLabel(self.formGroupBox)
        self.Label_2.setObjectName("Label_2")
        self.gridLayout.addWidget(self.Label_2, 1, 0, 1, 1)
        self.Label_5 = QtWidgets.QLabel(self.formGroupBox)
        self.Label_5.setObjectName("Label_5")
        self.gridLayout.addWidget(self.Label_5, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.formGroupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 2, 1, 1)
        self.Label = QtWidgets.QLabel(self.formGroupBox)
        self.Label.setObjectName("Label")
        self.gridLayout.addWidget(self.Label, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.formGroupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 2, 1, 1)
        self.LineEdit_6 = QtWidgets.QLineEdit(self.formGroupBox)
        self.LineEdit_6.setObjectName("LineEdit_6")
        self.gridLayout.addWidget(self.LineEdit_6, 5, 1, 1, 1)
        self.LineEdit_4 = QtWidgets.QLineEdit(self.formGroupBox)
        self.LineEdit_4.setObjectName("LineEdit_4")
        self.gridLayout.addWidget(self.LineEdit_4, 3, 1, 1, 1)
        self.Label_8 = QtWidgets.QLabel(self.formGroupBox)
        self.Label_8.setObjectName("Label_8")
        self.gridLayout.addWidget(self.Label_8, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.formGroupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.Label_9 = QtWidgets.QLabel(self.formGroupBox)
        self.Label_9.setObjectName("Label_9")
        self.gridLayout.addWidget(self.Label_9, 9, 0, 1, 1)
        self.LineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.LineEdit.setObjectName("LineEdit")
        self.gridLayout.addWidget(self.LineEdit, 0, 1, 1, 1)
        self.Label_7 = QtWidgets.QLabel(self.formGroupBox)
        self.Label_7.setObjectName("Label_7")
        self.gridLayout.addWidget(self.Label_7, 6, 0, 1, 1)
        self.LineEdit_8 = QtWidgets.QLineEdit(self.formGroupBox)
        self.LineEdit_8.setObjectName("LineEdit_8")
        self.gridLayout.addWidget(self.LineEdit_8, 7, 1, 1, 1)
        self.LineEdit_3 = QtWidgets.QLineEdit(self.formGroupBox)
        self.LineEdit_3.setObjectName("LineEdit_3")
        self.gridLayout.addWidget(self.LineEdit_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.formGroupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.Label_4 = QtWidgets.QLabel(self.formGroupBox)
        self.Label_4.setObjectName("Label_4")
        self.gridLayout.addWidget(self.Label_4, 3, 0, 1, 1)
        self.Label_6 = QtWidgets.QLabel(self.formGroupBox)
        self.Label_6.setObjectName("Label_6")
        self.gridLayout.addWidget(self.Label_6, 5, 0, 1, 1)
        self.LineEdit_7 = QtWidgets.QLineEdit(self.formGroupBox)
        self.LineEdit_7.setObjectName("LineEdit_7")
        self.gridLayout.addWidget(self.LineEdit_7, 6, 1, 1, 1)
        self.LineEdit_10 = QtWidgets.QLineEdit(self.formGroupBox)
        self.LineEdit_10.setObjectName("LineEdit_10")
        self.gridLayout.addWidget(self.LineEdit_10, 10, 1, 1, 1)
        self.LineEdit_9 = QtWidgets.QLineEdit(self.formGroupBox)
        self.LineEdit_9.setObjectName("LineEdit_9")
        self.gridLayout.addWidget(self.LineEdit_9, 9, 1, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(660, 500, 321, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setEnabled(False)
        self.line.setGeometry(QtCore.QRect(630, -10, 20, 591))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 510, 581, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(22, 526, 581, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(660, 590, 321, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 570, 1011, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1018, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.action5 = QtWidgets.QAction(MainWindow)
        self.action5.setObjectName("action5")
        self.action1_2 = QtWidgets.QAction(MainWindow)
        self.action1_2.setObjectName("action1_2")
        self.action2_2 = QtWidgets.QAction(MainWindow)
        self.action2_2.setObjectName("action2_2")
        self.action3_2 = QtWidgets.QAction(MainWindow)
        self.action3_2.setObjectName("action3_2")
        self.action4_2 = QtWidgets.QAction(MainWindow)
        self.action4_2.setObjectName("action4_2")
        self.action5_2 = QtWidgets.QAction(MainWindow)
        self.action5_2.setObjectName("action5_2")
        self.actionconnect = QtWidgets.QAction(MainWindow)
        self.actionconnect.setObjectName("actionconnect")
        self.actiondisconnect = QtWidgets.QAction(MainWindow)
        self.actiondisconnect.setObjectName("actiondisconnect")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setCheckable(False)
        self.actionopen.setObjectName("actionopen")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action1_3 = QtWidgets.QAction(MainWindow)
        self.action1_3.setObjectName("action1_3")
        self.action1_4 = QtWidgets.QAction(MainWindow)
        self.action1_4.setObjectName("action1_4")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.actionopen)
        self.menu.addSeparator()
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action3)
        self.menu.addSeparator()
        self.menu.addAction(self.action4)
        self.menu.addSeparator()
        self.menu.addAction(self.action5)
        self.menu_3.addAction(self.actionhelp)
        self.menu_4.addAction(self.actionconnect)
        self.menu_4.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.LineEdit, self.LineEdit_2)
        MainWindow.setTabOrder(self.LineEdit_2, self.LineEdit_3)
        MainWindow.setTabOrder(self.LineEdit_3, self.LineEdit_4)
        MainWindow.setTabOrder(self.LineEdit_4, self.LineEdit_5)
        MainWindow.setTabOrder(self.LineEdit_5, self.LineEdit_6)
        MainWindow.setTabOrder(self.LineEdit_6, self.LineEdit_7)
        MainWindow.setTabOrder(self.LineEdit_7, self.LineEdit_8)
        MainWindow.setTabOrder(self.LineEdit_8, self.LineEdit_9)
        MainWindow.setTabOrder(self.LineEdit_9, self.LineEdit_10)
        MainWindow.setTabOrder(self.LineEdit_10, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.graphicsView)
        MainWindow.setTabOrder(self.graphicsView, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "kHz"))
        self.label_5.setText(_translate("MainWindow", "次"))
        self.Label_3.setText(_translate("MainWindow", "宽度:"))
        self.label_6.setText(_translate("MainWindow", "dbm"))
        self.Label_10.setText(_translate("MainWindow", "文件名:"))
        self.Label_2.setText(_translate("MainWindow", "中心频率:"))
        self.Label_5.setText(_translate("MainWindow", "温度:"))
        self.label_7.setText(_translate("MainWindow", "ns"))
        self.Label.setText(_translate("MainWindow", "IP:"))
        self.label.setText(_translate("MainWindow", "GHz"))
        self.Label_8.setText(_translate("MainWindow", "电延时:"))
        self.label_2.setText(_translate("MainWindow", "GHz"))
        self.Label_9.setText(_translate("MainWindow", "点数:"))
        self.Label_7.setText(_translate("MainWindow", "功率:"))
        self.label_4.setText(_translate("MainWindow", "mk"))
        self.Label_4.setText(_translate("MainWindow", "带宽:"))
        self.Label_6.setText(_translate("MainWindow", "平均次数:"))
        self.pushButton_6.setText(_translate("MainWindow", "保存设置"))
        self.pushButton_7.setText(_translate("MainWindow", "取消"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.pushButton_2.setText(_translate("MainWindow", "暂停"))
        self.pushButton_4.setText(_translate("MainWindow", "继续"))
        self.pushButton_3.setText(_translate("MainWindow", "结束"))
        self.pushButton_5.setText(_translate("MainWindow", "保存结果"))
        self.menu.setTitle(_translate("MainWindow", "开始"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.menu_4.setTitle(_translate("MainWindow", "设置"))
        self.action1.setText(_translate("MainWindow", "开始"))
        self.action2.setText(_translate("MainWindow", "暂停"))
        self.action3.setText(_translate("MainWindow", "结束"))
        self.action4.setText(_translate("MainWindow", "保存测量结果"))
        self.action5.setText(_translate("MainWindow", "退出"))
        self.action1_2.setText(_translate("MainWindow", "1"))
        self.action2_2.setText(_translate("MainWindow", "2"))
        self.action3_2.setText(_translate("MainWindow", "3"))
        self.action4_2.setText(_translate("MainWindow", "4"))
        self.action5_2.setText(_translate("MainWindow", "5"))
        self.actionconnect.setText(_translate("MainWindow", "连接设置"))
        self.actiondisconnect.setText(_translate("MainWindow", "断开连接"))
        self.actionhelp.setText(_translate("MainWindow", "帮助信息"))
        self.actionopen.setText(_translate("MainWindow", "打开文件"))
        self.action.setText(_translate("MainWindow", "继续"))
        self.action1_3.setText(_translate("MainWindow", "1"))
        self.action1_4.setText(_translate("MainWindow", "1"))
        self.action_3.setText(_translate("MainWindow", "保存设置"))
