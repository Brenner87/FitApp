#!/usr/local/bin/python3
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget



class Window(QWidget):
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle("my thirst app")
		self.home()

	def home(self):
		btn=QtWidgets.QPushButton("Quite",self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())
		btn.move(0,0)
		self.show()

	def close_application(self):
		print("We are closing")
		sys.exit()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    GUI=Window()
    sys.exit(app.exec_())