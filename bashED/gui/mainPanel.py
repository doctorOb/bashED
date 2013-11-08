from java.lang import System
from javax.swing import JPanel
from javax.swing import BorderFactory
from java.awt import Color
from net.miginfocom.swing import MigLayout

class Panel(JPanel):
	def __init__(self):
		self.setLayout(MigLayout())

		
		self.setBorder(BorderFactory.createLineBorder(Color.RED))

		self.initUI()
		self.addUI()

		self.setVisible(True)
		print "panel"

	def initUI(self):
		pass

	def addUI(self):
		pass