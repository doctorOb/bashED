from java.lang import System
from javax.swing import JPanel
from javax.swing import BorderFactory
from java.awt import Color
from java.awt.event import ActionListener
from java.awt.event import ActionEvent

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
		self.outText.setEditable(False)


		self.inText = JTextField()
		self.inText.setText("")
		
		inT = self.inText
		outT = self.outText
		class InputTextAction(ActionListener):
			def actionPerformed(self, e):
				print inT.getText()
				outT.setText(outT.getText() + "\n" + inT.getText())
				inT.setText("")

		self.inText.addActionListener(InputTextAction())



	def addUI(self):
		self.add(self.title, "cell 0 0")
		self.add(self.outText, "cell 0 1, push, grow")
		self.add(self.inText, "cell 0 2, pushx, growx")