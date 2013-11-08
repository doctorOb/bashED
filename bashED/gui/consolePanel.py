from java.lang import System
from javax.swing import JPanel
from javax.swing import BorderFactory
from javax.swing import JScrollPane

from java.awt import Dimension
from java.awt import Color
from java.awt import Font

from java.awt.event import ActionListener
from java.awt.event import KeyListener
from java.awt.event import ActionEvent
from java.awt.event import KeyEvent
from java.awt.event import KeyAdapter

from net.miginfocom.swing import MigLayout
from panel import Panel

from javax.swing import JPanel
from javax.swing import JTextPane
from javax.swing import JTextField

class ConsolePanel(Panel):
	
	outText = None
	outTextScroller = None
	nestedInputPanel = None
	inText = None
	directoryText = None

	def __init__(self):
		Panel.__init__(self, "insets 0 0 0 0")
		


	def initUI(self):

		font = Font("Courier", Font.PLAIN, 14)

		#create the output text panel
		self.outText = JTextPane()
		self.outText.setEditable(False)
		self.outText.setFont(font)
		self.outTextScroller = JScrollPane(self.outText)


		#create the input text box
		self.inText = JTextField()
		self.inText.setFocusTraversalKeysEnabled(False)
		self.inText.setFont(font)

		#create the directory text box
		self.directoryText = JTextField()
		self.directoryText.setEditable(False)
		self.directoryText.setFont(font)
		self.directoryText.setText("~/agent")

		#create the listener that fires when the 'return' key is pressed
		class InputTextActionListener(ActionListener):
			def actionPerformed(selfButton, e):
				#print self.getCommandText()
				self.outText.setText(self.outText.getText() + "\n" + self.inText.getText())
				self.setDirectoryText(self.outText.getText())
				self.inText.setText("")

		#create the listener that fires whenever a user hits a key
		class InputKeyActionListener(KeyAdapter):
			def keyReleased(self, k):
				print str(k.getKeyCode()) + ":\t" + k.getKeyChar()

		#register the listeners
		self.inText.addActionListener(InputTextActionListener())
		self.inText.addKeyListener(InputKeyActionListener())

		#create a nested panel that will house the directory and the input text box
		self.nestedInputPanel = Panel("Insets 0 0 0 0")



	def addUI(self):
		self.add(self.outTextScroller, "cell 0 0, push, grow")
		self.add(self.nestedInputPanel, "cell 0 1, pushx, growx")
		self.nestedInputPanel.add(self.directoryText, "cell 0 0")
		self.nestedInputPanel.add(self.inText, "cell 1 0, spanx, pushx, growx")

	def setDirectoryText(self, dirText):
		self.directoryText.setText(dirText)
		self.nestedInputPanel.revalidate()
