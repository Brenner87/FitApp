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


		openEditor=QtWidgets.QAction("&Editor",self)
		openEditor.setShortcut("Ctrl+E")
		openEditor.setStatusTip('Open Editor')
		openEditor.triggered.connect(self.editor)

		openFile=QtWidgets.QAction("&Open File",self)
		openFile.setShortcut("Ctrl+O")
		openFile.setStatusTip('Open File')
		openFile.triggered.connect(self.file_open)


		saveFile=QtWidgets.QAction("&Save File",self)
		saveFile.setShortcut("Ctrl+S")
		saveFile.setStatusTip('Save File')
		saveFile.triggered.connect(self.file_save)

		self.statusBar()
		mainMenu=self.menuBar()
		fileMenu=mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		editorMenu=mainMenu.addMenu("&Editor")
		editorMenu.addAction(openEditor)

		fileMenu.addAction(openFile)
		fileMenu.addAction(saveFile)

		#sayMenu=mainMenu.addMenu('&Say')
		#fileMenu.addAction(extractAction2)

		self.home()


	def file_save(self):
		name=QtWidgets.QFileDialog.getSaveFileName(self,'Save File')[0]
		file=open(name,'w')
		text=self.textEdit.toPlainText()
		file.write(text)
		file.close()

	def file_open(self):
		name=QtWidgets.QFileDialog.getOpenFileName(self,'Open File')[0]
		print(name)
		file=open(name,'r')
		print(file)
		self.editor()
		with file:
			text=file.read()
			self.textEdit.setText(text)

	def editor(self):
		self.textEdit=QtWidgets.QTextEdit()
		self.setCentralWidget(self.textEdit)

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

		fontChoice = QtWidgets.QAction(QtGui.QIcon('1486104767_Streamline-27.png'), 'Change fonts', self)
		fontChoice.triggered.connect(self.font_choice)
		#self.toolbar = self.addToolBar("Font")
		self.toolbar.addAction(fontChoice)
		color=QtGui.QColor(0,0,0)
		fontColor=QtWidgets.QAction('Fonts bg Color',self)
		fontColor.triggered.connect(self.color_picker)
		self.toolbar.addAction(fontColor)

		checkBox=QtWidgets.QCheckBox('Enlarge Window',self)
		checkBox.move(300,25)
		checkBox.toggle()
		checkBox.stateChanged.connect(self.enlarge_Window)
		#PROGRESS BAR
		self.progress=QtWidgets.QProgressBar(self)
		self.progress.setGeometry(200,80,250,20)
		self.btn=QtWidgets.QPushButton("Download",self)
		self.btn.move(200,120)
		self.btn.clicked.connect(self.download)
		#DROPDOWN AND STYLES
		print (self.style().objectName())
		self.styleChoice=QtWidgets.QLabel("Windows Vista", self)
		comboBox=QtWidgets.QComboBox(self)
		comboBox.addItem("motif")
		comboBox.addItem("Windows")
		comboBox.addItem("cde")
		comboBox.addItem("Plastique")
		comboBox.addItem("Cleanlooks")
		comboBox.addItem("windowsvista")
		comboBox.move(50, 250)
		self.styleChoice.move(50,150)
		comboBox.activated[str].connect(self.style_choice)
		cal=QtWidgets.QCalendarWidget(self)
		cal.move(500,200)
		cal.resize(200,200)
		self.show()


	def color_picker(self):
		color=QtWidgets.QColorDialog.getColor()
		self.styleChoice.setStyleSheet("QWidget {background-color: %s}" % color.name())

	def font_choice(self):
		font, valid=QtWidgets.QFontDialog.getFont()
		if valid:
			self.styleChoice.setFont(font)


	def style_choice(self, text):
		self.styleChoice.setText(text)
		QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))

	def download(self):
		self.completed=0
		while self.completed < 100:
			self.completed+=0.0001
			self.progress.setValue(self.completed)
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
    
    