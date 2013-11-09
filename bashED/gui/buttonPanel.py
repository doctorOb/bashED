from panel import Panel
from javax.swing import JButton
from java.lang import System
from java.awt import Color

from java.awt.event import ActionListener
from java.awt.event import ActionEvent

class ButtonPanel(Panel):
	
	playButton = None
	helpButton = None
	resetButton = None
	exitButton = None

	def __init__(self):
		Panel.__init__(self, "insets 0 0 0 0, flowy")

	def initUI(self):

		self.setBackground(Color(0, 50, 0))

		self.playButton = JButton("PLAY")
		self.playButton.setForeground(Color(0, 255, 0))
		#self.playButton.setBackground(Color(125, 125, 25))
		self.playButton.setContentAreaFilled(False)

		self.helpButton = JButton("HELP")
		self.helpButton.setForeground(Color(0, 255, 0))
		self.helpButton.setContentAreaFilled(False)

		self.resetButton = JButton("RESET")
		self.resetButton.setForeground(Color(0, 255, 0))
		self.resetButton.setContentAreaFilled(False)

		self.exitButton = JButton("EXIT")
		self.exitButton.setForeground(Color(0, 255, 0))
		self.exitButton.setContentAreaFilled(False)


		class ExitButtonActionListener(ActionListener):
			def actionPerformed(button, e):
				System.exit(0)
		self.exitButton.addActionListener(ExitButtonActionListener())

	def addUI(self):
		self.add(self.playButton, "cell 0 0, pushx, growx, top")
		self.add(self.helpButton, "cell 0 0, pushx, growx")
		self.add(self.resetButton, "cell 0 0, pushx, growx, bottom")
		self.add(self.exitButton, "cell 0 0, pushx, growx")