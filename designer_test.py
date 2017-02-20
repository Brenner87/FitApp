#!/usr/local/bin/python3
import sys
from PyQt5.QtWidgets import  QApplication,QWidget,QDialog

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(273, 66)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spell_this = QtWidgets.QPushButton(self.centralwidget)
        self.spell_this.setGeometry(QtCore.QRect(180, 0, 75, 23))
        self.spell_this.setObjectName("spell_this")

        self.product_input = QtWidgets.QLineEdit(self.centralwidget)
        self.product_input.setGeometry(QtCore.QRect(0, 0, 111, 20))
        self.product_input.setObjectName("product_input")
        self.product_waight = QtWidgets.QLineEdit(self.centralwidget)
        self.product_waight.setGeometry(QtCore.QRect(120, 0, 51, 20))
        self.product_waight.setObjectName("product_waight")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 273, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.spell_this.clicked.connect(self.get_data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.spell_this.setText(_translate("MainWindow", "Spell this"))


    def get_data(self):
        product_name=self.product_input.text()
        product_waight=self.product_waight.text()
        print('Name: {0}, Waight: {1}'.format(product_name, product_waight))


class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

app=QApplication(sys.argv)
w=AppWindow()
w.show()
sys.exit(app.exec_())
