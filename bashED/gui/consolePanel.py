from java.lang import System
from javax.swing import JPanel
from javax.swing import BorderFactory
from javax.swing import JScrollPane

from java.awt import Dimension
from java.awt import Color

from java.awt.event import ActionListener
from java.awt.event import KeyListener
from java.awt.event import ActionEvent
from java.awt.event import KeyEvent
from java.awt.event import KeyAdapter

from net.miginfocom.swing import MigLayout
from panel import Panel


from javax.swing import JLabel
from javax.swing import JPanel
from javax.swing import JTextPane
from javax.swing import JTextField

from console import *
import sys

class FakeOut():
	def __init__(self,outText):
		self.outText = outText

	def fileno(self):
		return 3
	def write(self,text):
		#dont print in here
		self.outText.setText(self.outText.getText() + text)

class ConsolePanel(Panel):

	def __init__(self):
		Panel.__init__(self)
		self.console = None
		self.outText = None
		self.inText = None
		self.outTextScroller = None
		self.nestedInputPanel = None
		self.directoryText = None

	def setDirectoryText(self, dirText):
		self.directoryText.setText(dirText)
		self.nestedInputPanel.revalidate()

	def write_out(self,text):
		if not self.outText:
			return
		self.outText.setText(self.outText.getText() + text)

	def initUI(self):

		#create the output text panel
		self.outText = JTextPane()
		self.outText.setEditable(False)
		self.outTextScroller = JScrollPane(self.outText)

		#create the input text box
		self.inText = JTextField()
		self.inText.setFocusTraversalKeysEnabled(False)

		#create the directory text box
		self.directoryText = JTextField()
		self.directoryText.setEditable(False)
		self.nestedInputPanel = Panel("Insets 0 0 0 0")
		#set up the console
		import sys
		sys.stdout = FakeOut(self.outText)
		self.console = BashED_Console(stdout=sys.stdout)
		self.setDirectoryText(self.console.get_prompt())


		dirTex = self.directoryText;

		#create the listener that fires when the 'return' key is pressed
		class InputTextActionListener(ActionListener):
			def __init__(self,parent,inp,out,console):
				self.parent = parent
				self.inp = inp
				self.out = out
				self.console = console

			def actionPerformed(self, e):
				#print self.getCommandText()
				print(self.console.get_prompt())
				self.console.onecmd(self.inp.getText())
				self.parent.write_out("\n" + self.inp.getText())
				dirTex.setText(self.console.get_prompt())
				self.inp.setText("")

		#create the listener that fires whenever a user hits a key
		class InputKeyActionListener(KeyAdapter):
			def __init__(self,parent,inp,out,console):
				self.parent = parent
				self.inp = inp
				self.out = out
				self.console = console

			def keyReleased(self, k):
				inp = self.inp.getText()
				if k.getKeyCode() == 9: #tab character
					autos = self.console.tabcomplete(self.inp.getText())
					if len(autos) == 1:
						self.inp.setText(autos[0])
					else:
						for option in autos:
							self.parent.write_out(option)
				hist = None
				if k.getKeyCode() == 38:
					hist = self.console.next_hist()
				if k.getKeyCode() == 40:
					hist = self.console.last_hist()

				if hist:
					self.inp.setText(hist)

		self.inText.addActionListener(InputTextActionListener(self,self.inText,self.outText,self.console))
		self.inText.addKeyListener(InputKeyActionListener(self,self.inText,self.outText,self.console))


		#create a nested panel that will house the directory and the input text box
		



	def addUI(self):
		self.add(self.outTextScroller, "cell 0 0, push, grow")
		self.add(self.nestedInputPanel, "cell 0 1, pushx, growx")
		self.nestedInputPanel.add(self.directoryText, "cell 0 0")
		self.nestedInputPanel.add(self.inText, "cell 1 0, spanx, pushx, growx")

