from panel import Panel
from javax.swing import JButton
from java.lang import System
from java.awt import Color
from java.awt import Dimension
from javax.swing import ImageIcon
from java.awt.event import ActionListener
from java.awt.event import ActionEvent
from java.awt.event import MouseEvent
from java.awt.event import MouseAdapter

class ButtonPanel(Panel):
	
	playButton = None
	helpButton = None
	resetButton = None
	exitButton = None

	def __init__(self, inconsolePanel):
		self.consolePanel = inconsolePanel
		Panel.__init__(self, "gap 1px 1px, insets 0 0 0 0, flowy")

	def initUI(self):

		self.setBackground(Color(0, 50, 0))

		self.playButtonS = ImageIcon("playButton.png")
		self.helpButtonS = ImageIcon("helpButton.png")
		self.resetButtonS = ImageIcon("resetButton.png")
		self.exitButtonS = ImageIcon("exitButton.png")
		self.playButtonU = ImageIcon("playButton_unselected.png")
		self.helpButtonU = ImageIcon("helpButton_unselected.png")
		self.resetButtonU = ImageIcon("resetButton_unselected.png")
		self.exitButtonU = ImageIcon("exitButton_unselected.png")

		class MouseHoverAdap(MouseAdapter):
			def __init__(self, butt, entImage, leaImage):
				self.entImage = entImage
				self.leaImage = leaImage
				self.butt = butt
			def mouseEntered(self, m):
				print "entered"
				self.butt.setIcon(self.entImage)
				self.butt.repaint()
			def mouseLeave(self, m):
				print "left"
				self.butt.setIcon(self.leaImage)
				self.butt.repaint()


		self.playButton = JButton(self.playButtonS)
		self.playButton.setForeground(Color(0, 245, 0))
		#self.playButton.setPreferredSize(Dimension(playButton.getIconWidth(), playButton.getIconHeight()))
		#self.playButton.setBackground(Color(125, 125, 25))
		self.playButton.setMaximumSize(Dimension(self.playButtonS.getIconWidth(), self.playButtonS.getIconHeight()))
		self.playButton.setContentAreaFilled(False)

		self.helpButton = JButton(self.helpButtonS)
		self.helpButton.setForeground(Color(0, 235, 0))
		self.helpButton.setMaximumSize(Dimension(self.helpButtonS.getIconWidth(), self.helpButtonS.getIconHeight()))
		self.helpButton.setContentAreaFilled(False)

		self.resetButton = JButton(self.resetButtonS)
		self.resetButton.setForeground(Color(0, 225, 0))
		self.resetButton.setMaximumSize(Dimension(self.resetButtonS.getIconWidth(), self.resetButtonS.getIconHeight()))
		self.resetButton.setContentAreaFilled(False)

		self.exitButton = JButton(self.exitButtonS)
		self.exitButton.setForeground(Color(0, 215, 0))
		self.exitButton.setContentAreaFilled(False)
		self.exitButton.setMaximumSize(Dimension(self.exitButtonS.getIconWidth(), self.exitButtonS.getIconHeight()))
		
		self.playButton.addMouseListener(MouseHoverAdap(self.playButton, self.playButtonS, self.playButtonU))
		self.helpButton.addMouseListener(MouseHoverAdap(self.helpButton, self.helpButtonS, self.helpButtonU))
		self.resetButton.addMouseListener(MouseHoverAdap(self.resetButton, self.resetButtonS, self.resetButtonU))
		self.exitButton.addMouseListener(MouseHoverAdap(self.exitButton, self.exitButtonS, self.exitButtonU))


		class PlayButtonActionListener(ActionListener):
			def actionPerformed(button, e):
				self.consolePanel.sendCommand("python bashED.py --help")
		self.playButton.addActionListener(PlayButtonActionListener())

		class HelpBUttonActionListener(ActionListener):
			def actionPerformed(button, e):
				self.consolePanel.sendCommand("dir")
		self.helpButton.addActionListener(HelpBUttonActionListener())

		class ResetButtonActionListener(ActionListener):
			def actionPerformed(button, e):
				self.consolePanel.sendCommand("cls")
		self.resetButton.addActionListener(ResetButtonActionListener())

		class ExitButtonActionListener(ActionListener):
			def actionPerformed(button, e):
				System.exit(0)
		self.exitButton.addActionListener(ExitButtonActionListener())





	def addUI(self):
		self.add(self.playButton, "pushx, growx")
		self.add(self.helpButton, "pushx, growx")
		self.add(self.resetButton, "pushx, growx")
		self.add(self.exitButton, "pushx, growx")