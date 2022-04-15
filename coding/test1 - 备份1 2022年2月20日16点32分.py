# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import pyqtgraph as pg
import serial
import serial.tools.list_ports


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1038, 900)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(1038, 0))
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setMouseTracking(False)
        self.centralwidget.setTabletTracking(False)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)#设置为垂直布局
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget.addTab(self.main, "")
        self.plot = QtWidgets.QWidget()
        self.plot.setObjectName("plot")
        self.tabWidget.addTab(self.plot, "")
        self.figure = QtWidgets.QWidget()
        self.figure.setObjectName("figure")
        self.tabWidget.addTab(self.figure, "")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.figure)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.plot)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.pushButton_3 = QtWidgets.QPushButton(self.figure)
        # self.pushButton_3.setObjectName("绘图botton")
        # self.horizontalLayout.addWidget(self.pushButton_3)
 
        # self.pushButton = QtWidgets.QPushButton(self.plot)
        # self.pushButton.setObjectName("pushButton")
        # self.horizontalLayout_2.addWidget(self.pushButton)
       
        self.gridLayout = QtWidgets.QGridLayout(self.main)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_8 = QtWidgets.QPushButton(self.main)
        self.pushButton_8.setObjectName("手动发送")
        self.gridLayout.addWidget(self.pushButton_8, 11, 1, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.main)
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout.addWidget(self.comboBox_7, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.main)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.main)
        self.comboBox_8.setObjectName("comboBox_8")
        self.gridLayout.addWidget(self.comboBox_8, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.main)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1) 
        self.comboBox_2 = QtWidgets.QComboBox(self.main)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.main)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.main)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.main)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.main)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 11, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.main)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.main)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 12, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.main)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 12, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.main)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.main)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.main)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 11, 2, 3, 1)
        self.textEdit = QtWidgets.QTextEdit(self.main)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 2, 7, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.main)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.main)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
         
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1038, 26))
        self.menubar.setObjectName("menubar")
        self.menumain = QtWidgets.QMenu(self.menubar)
        self.menumain.setObjectName("menumain")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menumain.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2018级自动化1班刘宇辰毕业设计"))
        self.pushButton_8.setText(_translate("MainWindow", "手动发送"))
        self.label.setText(_translate("MainWindow", "端口"))
        self.label_7.setText(_translate("MainWindow", "数据位"))
        self.label_2.setText(_translate("MainWindow", "波特率"))
        self.pushButton_7.setText(_translate("MainWindow", "清空接受区"))
        self.label_8.setText(_translate("MainWindow", "停止位"))
        self.checkBox.setText(_translate("MainWindow", "十六进制"))
        self.checkBox_2.setText(_translate("MainWindow", "十六进制"))
        self.pushButton_2.setText(_translate("MainWindow", "打开串口"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "校验位"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("MainWindow", "主要信息"))
        # self.pushButton.setText(_translate("MainWindow", "2222"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plot), _translate("MainWindow", "绘图"))
        # self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.figure), _translate("MainWindow", "数据库"))
        #self.menumain.setTitle(_translate("MainWindow", "主窗口"))
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
