from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLabel, QAction, qApp, QMainWindow, QMenu
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QProgressBar, QComboBox, QStyleFactory, QFontDialog
from PyQt5.QtWidgets import QCalendarWidget, QColorDialog, QTextEdit, QFileDialog
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QColor

class SimpleClass(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(100, 100, 800, 500)
		self.setWindowTitle("My Programmes")
		self.setWindowIcon(QIcon('Icon.png'))

		#Main Menu
		#This is Main Menu in the Appliacation
		action = QAction('&Exit',self)
		action.setShortcut('Ctrl+Q')
		action.setStatusTip("Exit Application")
		action.triggered.connect(self.close_application)

		action2 = QAction('&Edit',self)
		action2.setShortcut('Ctrl+E')
		action2.setStatusTip("Edit Operation")
		action2.triggered.connect(self.editor)

		#SubMenu
		#THis is used for Adding subMenu in Menu
		impt = QMenu('Import',self)
		impt1 = QAction('import form phone',self)
		impt2 = QAction('import form hard-drive',self)
		impt.addAction(impt1)
		impt.addAction(impt2)

		Help = QAction('Help',self)
		Help.setShortcut('Ctrl+H')
		Help.setStatusTip('Helper Class')
		Help.triggered.connect(self.helper)

		self.statusBar()

		#main Menu Design is Done

		#Main Menu is applied form here
		mainMenu = self.menuBar()
		file = mainMenu.addMenu('&File')
		file.addAction(action)
		file.addAction(action2)
		#Adding SubMenu into Main Menu 
		file.addMenu(impt)
		# submenu = file.addMenu('Import',self)

		#Creating New Menu
		file1 = mainMenu.addMenu('&Help')
		file1.addAction(Help)

		
		#ToolBar Here
		#content for the ToolBar Here
		action3 = QAction(QIcon("Icon.png"),'This is Gona End',self)
		action3.triggered.connect(self.close_application)

		#Font Picker
		#Start
		#A Declaration of the Font by this chicking Action take Place
		fontchoice = QAction('Fonts',self)
		fontchoice.triggered.connect(self.font_choice)

		#ToolBar In the Application
		self.toolbar = self.addToolBar('Exxit')
		self.toolbar.addAction(action3)
		#Added to the ToolBar But YOu Can add where ever u want
		self.toolbar.addAction(fontchoice)

		#Color Picker
		#set a deafult Color
		color = QColor(0, 0, 0)
		#Declaration of Color Picker
		fontcolor = QAction("Font Color",self)
		fontcolor.triggered.connect(self.color_picker) 

		#Added to ToolBar is not Manditary
		self.toolbar.addAction(fontcolor)

		#Calendar Widgets
		cal = QCalendarWidget(self)
		#Calendar Position in Gui
		cal.move(250,230)
		#Display OF the Calendar Size
		cal.resize(200,200)

		#Editor For Writting the Stuff
		#Declaration Of the Editor
				# openEditor = QAction("Editor",self)
				# openEditor.setShortcut("Ctrl+E")
				# openEditor.setStatusTip("Editing")
				# openEditor.triggered.connect(self.editor)

				# #Adding into the Main Menu
				# edit = mainMenu.addMenu("Edit")
				# edit.addAction(openEditor)
		

		#Open A Fie in Application
		#Declaration of the MEnu
		openf = QAction('&Open',self)
		openf.setShortcut('Ctrl+O')
		openf.setStatusTip("Open File")
		openf.triggered.connect(self.openfile)
		#Added to the MenuBar
		file.addAction(openf)

		saveFile = QAction('&Save',self)
		saveFile.setShortcut('Ctrl+S')
		saveFile.setStatusTip("Save File")
		saveFile.triggered.connect(self.saveFi)

		file.addAction(saveFile)


		self.initUi()

	def saveFi(self):
		name = QFileDialog.getSaveFileName(self,"Save File")
		if type(name) not in [str]:
			pass
		else:
			file = open(name,"w")
			text = self.textEditor.toPlaintext()
			file.write(text)
			file.close()

	#Open File Controller in the App
	def openfile(self):
		#name = QFileDialog.getOpenFileName(self,"Open File")
		#print(name)
		file, filter = QFileDialog.getOpenFileName(self, 'Open file')
		if type(file) not in [str,tuple]:
			pass
		else:
			file = open(file,"r")
			self.editor()
			with file:
				#Added the Text to Editor For Editing
				text = file.read()
				self.textEditor.setText(text)

	def editor(self):
		self.textEditor = QTextEdit()
		self.setCentralWidget(self.textEditor)

	#Main Controller of Color Picker and it's Action
	def color_picker(self):
		#Color Picker DialogWidgets
		col =  QColorDialog.getColor()
		#Operation use Here is Change Label Background Color
		self.selectchoice.setStyleSheet("QWidget {background : %s}" % col.name())

	#Contoller of the Font Pick
	def font_choice(self):
		font ,valid = QFontDialog.getFont()
		if valid:
			self.selectchoice.setFont(font)


	def helper(self):
		self.lbl.setText("You Have Chicked On Helper Event")
		self.lbl.adjustSize()

	def edit_application(self):
		self.lbl.setText("You Have Chicked On Edit")
		self.lbl.adjustSize()

	def close_application(self):
		#THis is a Popup Message for the pop up Message;
		choice = QMessageBox.question(self, "Quit!!!",
		 "Are You Sure To Quit!!!",QMessageBox.Yes | QMessageBox.No)
		#qApp.quit()
		if choice == QMessageBox.Yes:
			qApp.quit()
		else:
			pass

	def initUi(self):
		#Design Ui From Here
		# cb = QCheckBox("Change Label Name",self)
		# cb.toggle()
		# cb.stateChanged.connect(self.ChangeLabel)
		# cb.move(60, 100)

		self.lbl = QLabel(self)
		self.lbl.setText("Status of CheckBox")
		self.lbl.move(60, 80)

		cb = QCheckBox("Change Label Name",self)
		cb.toggle()
		cb.stateChanged.connect(self.ChangeLabel)
		cb.move(60, 150)

		# Working With THe ProgressBar

		#It is not The Correct Declaration OF the ProgressBar
		#self.progress  = QProgressBar('Installing',self)

		#THis is the Correct ProgressBar Declaration
		self.progress = QProgressBar(self)
		self.progress.setGeometry(200,100,300,20)

		#setGeometry(x,y,w,h)
		# x -> x-coordinate
		# y -> y-coordinate
		# w -> Width of that Gui
		# h -> Height of that Gui

		# Progress Bar Is controlled by the Button as Down HEre
		self.down = QtWidgets.QPushButton("Download",self)
		self.down.move(250,150)
		self.down.clicked.connect(self.Download)

		#DropDown Menu in Gui
		#THis will Print the Gui Default set
		print(self.style().objectName())

		#This Lable is not Manditary It is used For Showing
		self.selectchoice = QLabel("Windows Vista",self)
		
		#List Wich will Contains the All Elements
		comboBox  = QComboBox(self)
		comboBox.addItem("motif")
		comboBox.addItem("Windows")
		comboBox.addItem("cde")
		comboBox.addItem("Plastique")
		comboBox.addItem("Cleanlooks")
		comboBox.addItem("Windowsvista")

		#This is the Position Value in THe Gui
		comboBox.move(50,230)
		self.selectchoice.move(50,330)

		#This is the Controller of the Drop Down MEnu in Gui
		comboBox.activated[str].connect(self.set_window_type)

		self.show()

	#This is the Controller Logic of the DropDown Menu
	def set_window_type(self,text):
		self.selectchoice.setText(text)
		QApplication.setStyle(QStyleFactory.create(text))

	#Controller OF the ProgressBAr
	def Download(self):
		self.completed = 0
		while self.completed < 100:
			self.completed +=0.00002
			self.progress.setValue(self.completed)
		self.lbl.setText("Download is completed")
		self.lbl.adjustSize()

	#Funtion of the Change Lable
	def ChangeLabel(self,stauts):
		#Operation To Be Perform
		if stauts == Qt.Checked:
			self.lbl.setText("Status is Checked")
			self.lbl.adjustSize()        
		else:
			self.lbl.setText("Status is UnChecked")
			self.lbl.adjustSize()

if __name__ == '__main__':
    
	app = QApplication(sys.argv)
	ex = SimpleClass()
	sys.exit(app.exec_())