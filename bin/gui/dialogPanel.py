

from javax.swing import JTextPane
from javax.swing import JScrollPane
from javax.swing import ImageIcon
from javax.swing import JLabel
from panel import Panel
from buttonPanel import ButtonPanel 
from java.awt import Color
from java.awt import Font
#import bashed_run

import threading
import time

class DialogPanel(Panel):

	manImage = None #image
	manImageSilent = None
	manLabel = None #label
	dialogText = None
	dialogTextScroller = None
	buttonsPanel = None


	def speak(self, text):
		self.dialogText.setText("")
		self.manLabel.setIcon(self.manImage)
		class Typer(threading.Thread):
			def __init__(thrd, text):
				threading.Thread.__init__(thrd)
				thrd.text = text
			def run(thrd):
				for i in range(0, len(thrd.text)):
					#print str(text[i])
					self.dialogText.setText(self.dialogText.getText() + text[i])
					time.sleep(.1)
				self.manLabel.setIcon(self.manImageSilent)
		Typer(text).start()
		

	def __init__(self, inconsolePanel):
		self.consolePanel = inconsolePanel
		Panel.__init__(self, "insets 0 0 0 0")
		self.speak("My name is Captain danglewood! Help me find my lost crew in this hell pit of unix!!!")


	def initUI(self):
		self.manImage = ImageIcon('bin/gui/media/' + "danglewood.gif")
		self.manImageSilent = ImageIcon('bin/gui/media/' + "danglewood-silent.png")
		self.manLabel = JLabel(self.manImage)

		self.dialogText = JTextPane()
		self.dialogText.setEditable(False)
		self.dialogTextScroller = JScrollPane(self.dialogText);

		self.dialogText.setBackground(Color(0, 24, 0))
		self.dialogText.setForeground(Color.WHITE)
		self.dialogText.setFont(Font("Arial", Font.BOLD, 15))

		self.buttonsPanel = ButtonPanel(self.consolePanel,self)


		self.dialogText.setText("Welcome to BashED!!!")

	def addUI(self):
		self.add(self.buttonsPanel, "cell 0 0, pushy, growy")
		self.add(self.dialogTextScroller, "cell 1 0, push, grow")
		self.add(self.manLabel, "cell 2 0")