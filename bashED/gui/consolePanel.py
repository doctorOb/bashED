from java.lang import System
from javax.swing import JPanel
from javax.swing import BorderFactory
from java.awt import Color
from net.miginfocom.swing import MigLayout
from panel import Panel


from javax.swing import JLabel
from javax.swing import JTextPane
from javax.swing import JTextField

class ConsolePanel(Panel):
	
	title = None
	outText = None
	inText = None

	def __init__(self):
		Panel.__init__(self)
		


	def initUI(self):
		self.title = JLabel("bashED")
		self.outText = JTextPane()
		self.inText = JTextField()

	def addUI(self):
		self.add(self.title, "cell 0 0")
		self.add(self.outText, "cell 0 1, push, grow")
		self.add(self.inText, "cell 0 2, pushx, growx")