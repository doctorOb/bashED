from java.lang import System

from java.awt import Dimension

from javax.swing import JButton

from panel import Panel 
from consolePanel import ConsolePanel
from dialogPanel import DialogPanel

class MainPanel(Panel):

	dialogsPanel = None
	consolePanel = None

	playButton = None
	helpButton = None
	resetButton = None

	def __init__(self):
		Panel.__init__(self)

	def initUI(self):
		self.consolePanel = ConsolePanel()

		self.dialogsPanel = DialogPanel()
		self.dialogsPanel.setMinimumSize(Dimension(1, 112))
		self.dialogsPanel.setMaximumSize(Dimension(9999, 112))

		self.playButton = JButton("PLAY")
		self.helpButton = JButton("HELP")
		self.resetButton = JButton("RESET")


	def addUI(self):
		self.add(self.dialogsPanel, "cell 0 0, growx, pushx")
		self.add(self.consolePanel, "cell 0 1, grow, push")