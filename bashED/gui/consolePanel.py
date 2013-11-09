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

	def write(self,text):
		#dont print in here
		self.outText.setText(self.outText.getText() + text)

class ConsolePanel(Panel):
	
	outText = None
	outTextScroller = None
	nestedInputPanel = None
	inText = None
	directoryText = None

	def __init__(self):
		Panel.__init__(self)
		self.console = None
		


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

		#set up the console
		import sys
		sys.stdout = FakeOut(self.outText)
		self.console = BashED_Console(stdout=sys.stdout)
		self.directoryText.setText(self.console.get_prompt())

		#create the listener that fires when the 'return' key is pressed
		class InputTextActionListener(ActionListener):
			def __init__(self,console):
				self.console = console

			def actionPerformed(selfBtn, e):
				#print self.getCommandText()
				selfBtn.console.onecmd(self.inText.getText())
				self.outText.setText(self.outText.getText() + "\n" + self.inText.getText())

				self.setDirectoryText(selfBtn.console.get_prompt())
				self.inText.setText("")

		#create the listener that fires whenever a user hits a key
		class InputKeyActionListener(KeyAdapter):
			def __init__(self,console):
				self.console = console

			def keyReleased(selfBtn, k):
				if k.getKeyCode() == 9: #tab character
					inT.setText(selfBtn.console.tabcomplete(self,inT.getText()))
		self.inText.addActionListener(InputTextActionListener(self.console))
		self.inText.addKeyListener(InputKeyActionListener(self.console))


		#create a nested panel that will house the directory and the input text box
		self.nestedInputPanel = Panel("Insets 0 0 0 0")



	def addUI(self):
		self.add(self.outTextScroller, "cell 0 0, push, grow")
		self.add(self.nestedInputPanel, "cell 0 1, pushx, growx")
		self.nestedInputPanel.add(self.directoryText, "cell 0 0")
		self.nestedInputPanel.add(self.inText, "cell 1 0, spanx, pushx, growx")

	def setDirectoryText(self, dirText):
		self.directoryText.setText(dirText)
		self.nestedInputPanel.revalidate()
