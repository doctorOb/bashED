

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

from javax.swing import JLabel
from javax.swing import JPanel
from javax.swing import JTextPane
from javax.swing import JTextField

import threading
import time

import sys

from console import *

class FakeOut():
	def __init__(self,outText):
		self.outText = outText

	def fileno(self):
		return 3
	def write(self,text):
		#dont print in here
		self.outText.setText(self.outText.getText() + text)

class ConsolePanel(Panel):

	def __init__(self):
		
		self.console = None
		self.outText = None
		self.inText = None
		self.outTextScroller = None
		self.nestedInputPanel = None
		self.directoryText = None
		Panel.__init__(self, "insets 0 0 0 0")

	def sendCommand(self, command):
		print str(self)
		oldText = self.inText.getText()
		self.inText.setText(command)

		self.inText.getActionListeners()[0].actionPerformed(None)
		self.inText.setText(oldText)

	def setDirectoryText(self, dirText):
		self.directoryText.setText(dirText)
		self.nestedInputPanel.revalidate()

	def write_out(self,text):
		if not self.outText:
			return
		self.outText.setText(self.outText.getText() + text)

	def initUI(self):

		font = Font("Courier New", Font.BOLD, 14)

		#create the output text panel
		self.outText = JTextPane()
		self.outText.setEditable(False)
		self.outText.setFont(font)
		#self.outText.setLineWrap(True)
		#self.outText.setWrapStyleWord(True)
		class NoGhostScroller(JScrollPane):
			def paintComponent(self, g):
				
				g.setColor(self.getBackground())
				g.fillRect(0, 0, self.getWidth(), self.getHeight())
				#super(NoGhostScroller, self).paintComponent(g)

		self.outTextScroller = JScrollPane(self.outText)
		#self.outText.setOpaque(False)
		self.outText.setBackground(Color(0, 20, 0, 220))
		self.outText.setForeground(Color.WHITE)

		#self.outTextScroller.setOpaque(False)
		self.outTextScroller.setBackground(Color(0, 20, 0, 200))

		#self.outText.repaint()

		#self.layered = JLayeredPane()
		#self.layered.setLayer(self.outTextScroller, 0)

		#create the input text box
		self.inText = JTextField()
		self.inText.setFocusTraversalKeysEnabled(False)
		self.inText.setFont(font)
		self.inText.setBackground(Color(0, 20, 0))
		self.inText.setForeground(Color.WHITE)

		class Cursor(thread.Thread):
			def __init__(thrd):
				threading.Thread.__init__(thrd)
				thrd.state = True
			def run(thrd):
				thrd.state = !thrd.state
				time.sleep(.2)

		Cursor().start()

		self.nestedInputPanel = Panel("Insets 0 0 0 0")

		#create the directory text box
		self.directoryText = JTextField()
		self.directoryText.setEditable(False)
		self.directoryText.setFont(font)
		self.directoryText.setBackground(Color(0, 20, 0))
		self.directoryText.setForeground(Color.WHITE)
		#set up the console
		sys.stdout = FakeOut(self.outText)
		self.console = BashED_Console(stdout=sys.stdout)
		self.directoryText.setText(self.console.get_prompt())
		self.revalidate();


		dirTex = self.directoryText;

		#create the listener that fires when the 'return' key is pressed
		class InputTextActionListener(ActionListener):
			def __init__(self,parent,inp,out,console):
				self.parent = parent
				self.inp = inp
				self.out = out
				self.console = console

			def actionPerformed(self, e):
				#print self.getCommandText()
				# print(self.console.get_prompt())
				# self.console.onecmd(self.inp.getText())
				# self.parent.write_out("\n" + self.inp.getText())
				# dirTex.setText(self.console.get_prompt())
				# self.inp.setText("")
				self.parent.write_out(self.console.get_prompt() + self.inp.getText() + '\n')
				if 'clear' in self.inp.getText().split(' ')[0]:
					self.out.setText("") #clear the screen
				else:
					self.console.onecmd(self.inp.getText())
				
				dirTex.setText(self.console.get_prompt())
				self.inp.setText("")

		#create the listener that fires whenever a user hits a key
		class InputKeyActionListener(KeyAdapter):
			def __init__(self,parent,inp,out,console):
				self.parent = parent
				self.inp = inp
				self.out = out
				self.console = console

			def keyReleased(self, k):
				inp = self.inp.getText()
				if k.getKeyCode() == 9: #tab character
					autos = self.console.tabcomplete(self.inp.getText())
					if len(autos) == 1:
						self.inp.setText(autos[0])
					else:
						i = 0
						for option in autos:
							self.parent.write_out(option)
							if i % 3 == 0:
								print('\n')
							else:
								print('\t')
				hist = None
				if k.getKeyCode() == 38:
					hist = self.console.next_hist()
				if k.getKeyCode() == 40:
					hist = self.console.last_hist()

				if hist:
					self.inp.setText(hist.rstrip('\n'))#prevent from firing

		self.inText.addActionListener(InputTextActionListener(self,self.inText,self.outText,self.console))
		self.inText.addKeyListener(InputKeyActionListener(self,self.inText,self.outText,self.console))




	def addUI(self):
		
		self.add(self.outTextScroller, "cell 0 0, push, grow")
		self.add(self.nestedInputPanel, "cell 0 1, pushx, growx")
		self.nestedInputPanel.add(self.directoryText, "cell 0 0")
		self.nestedInputPanel.add(self.inText, "cell 1 0, spanx, pushx, growx")

