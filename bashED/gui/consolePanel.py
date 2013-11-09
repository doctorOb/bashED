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
	
	title = None
	outText = None
	outTextScroller = None
	inText = None
	

	def __init__(self):
		Panel.__init__(self)
		self.console = None
		


	def initUI(self):
		self.title = JLabel("bashED")
		self.outText = JTextPane()
		self.outText.setEditable(False)

		#d = Dimension(50, 50)
		#self.outText.setMaximumSize(d)
		self.outTextScroller = JScrollPane(self.outText)


		self.inText = JTextField()
		self.inText.setFocusTraversalKeysEnabled(False)

		self.inText.setText("")
		self.new_out = FakeOut(self.outText)
		import sys
		sys.stdout = self.new_out
		self.console = BashED_Console(stdin=None,stdout=self.new_out)

		inT = self.inText
		outT = self.outText
		class InputTextActionListener(ActionListener):

			def __init__(self,console):
				self.console = console
			def actionPerformed(self, e):
				outT.setText(outT.getText() + "\n" + inT.getText())
				self.console.onecmd(inT.getText())
				inT.setText(self.console.prompt)
		class InputKeyActionListener(KeyAdapter):
			def __init__(self,console):
				self.console = console
			def keyReleased(self, k):
				if k.getKeyCode() == 9: #tab character
					inT.setText(self.console.tabcomplete(self,inT.getText()))
		self.inText.addActionListener(InputTextActionListener(self.console))
		self.inText.addKeyListener(InputKeyActionListener(self.console))


	def addUI(self):
		self.add(self.title, "cell 0 0")
		self.add(self.outTextScroller, "cell 0 1, push, grow")
		self.add(self.inText, "cell 0 2, pushx, growx")