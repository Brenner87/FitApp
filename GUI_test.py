#!/usr/local/bin/python3
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox



class Window(QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle("my thirst app")
		extractAction=QtWidgets.QAction("&GET TO THE CHOPPAH!!", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Leave The App')
		extractAction.triggered.connect(self.close_application)
		extractAction2=QtWidgets.QAction("&Whisper me something", self)
		extractAction2.setShortcut("Ctrl+S")
		extractAction2.setStatusTip('here are you')
		extractAction2.triggered.connect(self.day_menu)
		self.statusBar()
		mainMenu=self.menuBar()
		fileMenu=mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		fileMenu.addAction(extractAction2)
		#sayMenu=mainMenu.addMenu('&Say')
		#fileMenu.addAction(extractAction2)

		self.home()

	def home(self):
		btn=QtWidgets.QPushButton("Quite",self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.minimumSizeHint())
		btn.move(0,100)
		extractAction=QtWidgets.QAction(QtGui.QIcon('1486016084_Streamline-83.png'), 'Flee the scene',self)
		extractAction.triggered.connect(self.close_application)
		extractAction2=QtWidgets.QAction(QtGui.QIcon('1486016580_Streamline-25.png'), 'Something new',self)
		extractAction2.triggered.connect(self.day_menu)
		self.toolbar=self.addToolBar("Extraction")
		self.toolbar.addAction(extractAction)
		self.toolbar.addAction(extractAction2)
		checkBox=QtWidgets.QCheckBox('Enlarge Window',self)
		checkBox.move(100,25)
		checkBox.toggle()
		checkBox.stateChanged.connect(self.enlarge_Window)
		self.show()

	def enlarge_Window(self, state):
		if state==QtCore.Qt.Checked:
			self.setGeometry(50,50,1000,600)
		else:
			self.setGeometry(50,50,500,300)

	def close_application(self):
		choice=QMessageBox.question(self,'Extract!', 
									     "Are you sure?", 
										  QMessageBox.Yes|QMessageBox.No)
		if choice==QMessageBox.Yes:
			print("YOOOOOOHOOOOOOO!!!")
			sys.exit()
		else:
			pass

	def day_menu(self):
		print("Another button added!!!!!")


def run():
	app = QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()
    
    