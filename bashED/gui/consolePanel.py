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

class ConsolePanel(Panel):
	
	title = None
	outText = None
	outTextScroller = None
	inText = None
	

	def __init__(self):
		Panel.__init__(self)
		


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
		
		inT = self.inText
		outT = self.outText
		class InputTextActionListener(ActionListener):
			def actionPerformed(self, e):
				print inT.getText()
				outT.setText(outT.getText() + "\n" + inT.getText())
				inT.setText("")
		class InputKeyActionListener(KeyAdapter):
			def keyReleased(self, k):
				print str(k.getKeyCode()) + ":\t" + k.getKeyChar()

		self.inText.addActionListener(InputTextActionListener())
		self.inText.addKeyListener(InputKeyActionListener())


	def addUI(self):
		self.add(self.title, "cell 0 0")
		self.add(self.outTextScroller, "cell 0 1, push, grow")
		self.add(self.inText, "cell 0 2, pushx, growx")