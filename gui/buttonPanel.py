from panel import Panel
from javax.swing import JButton

class ButtonPanel(Panel):
	
	playButton = None
	helpButton = None
	resetButton = None

	def __init__(self):
		Panel.__init__(self, "insets 0 0 0 0, flowy")

	def initUI(self):
		self.playButton = JButton("PLAY")
		self.helpButton = JButton("HELP")
		self.resetButton = JButton("RESET")

	def addUI(self):
		self.add(self.playButton, "cell 0 0, pushx, growx, top")
		self.add(self.helpButton, "cell 0 0, pushx, growx")
		self.add(self.resetButton, "cell 0 0, pushx, growx, bottom")