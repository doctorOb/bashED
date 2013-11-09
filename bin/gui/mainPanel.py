
#import bashed_run
from java.lang import System

from java.awt import Dimension
from java.awt import Color
from java.awt import Font

from javax.swing import JButton
from javax.swing import JLabel
from panel import Panel
from consolePanel import ConsolePanel
from dialogPanel import DialogPanel
from javax.swing import SwingUtilities
from java.awt.event import MouseAdapter
from java.awt.event import MouseMotionAdapter
from java.awt.event import MouseEvent
from javax.swing import ImageIcon
from os import path



class MainPanel(Panel):

	dialogsPanel = None
	consolePanel = None

	def __init__(self):
		Panel.__init__(self, "insets 20 4 20 4")



	def initUI(self):
		self.consolePanel = ConsolePanel()
		self.dialogsPanel = DialogPanel(self.consolePanel)
		self.dialogsPanel.setMinimumSize(Dimension(1, 112))
		self.dialogsPanel.setMaximumSize(Dimension(9999, 112))
		self.title = JLabel(ImageIcon('bin/gui/media/' + "logo.png"))
		#self.title.setFont(Font("Arial", Font.BOLD, 24))

	def addUI(self):
		self.add(self.title, "cell 0 0")
		self.add(self.dialogsPanel, "cell 0 1, growx, pushx")
		self.add(self.consolePanel, "cell 0 2, grow, push")