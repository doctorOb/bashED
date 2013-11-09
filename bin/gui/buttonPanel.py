from javax.swing import JButton
from java.lang import System
from java.awt import Color
from java.awt import Dimension
from javax.swing import ImageIcon
from java.awt.event import ActionListener
from java.awt.event import ActionEvent
from java.awt.event import MouseEvent
from java.awt.event import MouseAdapter
#import bashed_run
from panel import Panel


class ButtonPanel(Panel):
	
	playButton = None
	helpButton = None
	resetButton = None
	exitButton = None

	def __init__(self, inconsolePanel,dialogPanel):
		self.consolePanel = inconsolePanel
		self.dialogPanel = dialogPanel
		Panel.__init__(self, "gap 1px 1px, insets 0 0 0 0, flowy")

	def initUI(self):

		self.setBackground(Color(0, 50, 0))

		self.playButtonS = ImageIcon('bin/gui/media/' + "playButton.png")
		self.helpButtonS = ImageIcon('bin/gui/media/' + "helpButton.png")
		self.resetButtonS = ImageIcon('bin/gui/media/' + "resetButton.png")
		self.exitButtonS = ImageIcon('bin/gui/media/' + "exitButton.png")
		self.playButtonU = ImageIcon('bin/gui/media/' + "playButton_unselected.png")
		self.helpButtonU = ImageIcon('bin/gui/media/' + "helpButton_unselected.png")
		self.resetButtonU = ImageIcon('bin/gui/media/' + "resetButton_unselected.png")
		self.exitButtonU = ImageIcon('bin/gui/media/' + "exitButton_unselected.png")

		class MouseHoverAdap(MouseAdapter):
			def __init__(self, butt, entImage, leaImage):
				self.entImage = entImage
				self.leaImage = leaImage
				self.butt = butt
				self.butt.setIcon(self.leaImage)
			def mouseEntered(self, m):
				self.butt.setIcon(self.entImage)
				#self.butt.repaint()
			def mouseExited(self, m):
				self.butt.setIcon(self.leaImage)
				#self.butt.repaint()


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
		
		# self.playButton.addMouseListener(MouseHoverAdap(self.playButton, self.playButtonS, self.playButtonU))
		# self.helpButton.addMouseListener(MouseHoverAdap(self.helpButton, self.helpButtonS, self.helpButtonU))
		# self.resetButton.addMouseListener(MouseHoverAdap(self.resetButton, self.resetButtonS, self.resetButtonU))
		# self.exitButton.addMouseListener(MouseHoverAdap(self.exitButton, self.exitButtonS, self.exitButtonU))


		class PlayButtonActionListener(ActionListener):
			def actionPerformed(button, e):
				self.dialogPanel.speak(self.consolePanel.console.do_play(''))
		self.playButton.addActionListener(PlayButtonActionListener())

		class HelpBUttonActionListener(ActionListener):
			def actionPerformed(button, e):
				self.dialogPanel.speak(self.consolePanel.console.do_hint(''))
		self.helpButton.addActionListener(HelpBUttonActionListener())

		class ResetButtonActionListener(ActionListener):
			def actionPerformed(button, e):
				self.dialogPanel.speak(self.consolePanel.console.do_reset(''))
		self.resetButton.addActionListener(ResetButtonActionListener())

		class ExitButtonActionListener(ActionListener):
			def actionPerformed(button, e):
				System.exit(0)
		self.exitButton.addActionListener(ExitButtonActionListener())





	def addUI(self):
		self.add(self.playButton, "push, grow")
		self.add(self.helpButton, "push, grow")
		self.add(self.resetButton, "push, grow")
		self.add(self.exitButton, "push, grow")
