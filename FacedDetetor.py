# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\FacedDetetor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Result = QtWidgets.QLabel(self.centralwidget)
        self.label_Result.setGeometry(QtCore.QRect(140, 50, 211, 201))
        self.label_Result.setAutoFillBackground(False)
        self.label_Result.setObjectName("label_Result")
        self.btn_video = QtWidgets.QPushButton(self.centralwidget)
        self.btn_video.setGeometry(QtCore.QRect(120, 350, 81, 31))
        self.btn_video.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_video.setObjectName("btn_video")
        self.btn_pic = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pic.setGeometry(QtCore.QRect(210, 300, 81, 31))
        self.btn_pic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pic.setObjectName("btn_pic")
        self.btn_camare = QtWidgets.QPushButton(self.centralwidget)
        self.btn_camare.setGeometry(QtCore.QRect(300, 350, 81, 31))
        self.btn_camare.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_camare.setObjectName("btn_camare")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Result.setText(_translate("MainWindow", "???????????????/????????????????????????????????????\n   ??????????????????????????????????????????\n     ?????????????????????output???"))
        self.btn_video.setText(_translate("MainWindow", "????????????"))
        self.btn_pic.setText(_translate("MainWindow", "????????????"))
        self.btn_camare.setText(_translate("MainWindow", "???????????????"))

