from javax.swing import JTextPane
from javax.swing import JScrollPane

from panel import Panel 
from buttonPanel import ButtonPanel 

class DialogPanel(Panel):

	dialogText = None
	dialogTextScroller = None
	buttonsPanel = None

	def __init__(self):
		Panel.__init__(self, "insets 0 0 0 0")

	def initUI(self):
		self.dialogText = JTextPane()
		self.dialogText.setEditable(False)
		self.dialogTextScroller = JScrollPane(self.dialogText);

		self.buttonsPanel = ButtonPanel()


		self.dialogText.setText("Welcome to BashED!!!")

	def addUI(self):
		self.add(self.buttonsPanel, "cell 0 0")
		self.add(self.dialogTextScroller, "cell 1 0, push, grow")