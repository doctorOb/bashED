from java.lang import System
from javax.swing import JPanel
from javax.swing import BorderFactory
from java.awt import Color
from java.awt import Point
from java.awt.event import MouseAdapter
from java.awt.event import MouseEvent
from java.awt.event import MouseMotionAdapter
from javax.swing import SwingUtilities
from net.miginfocom.swing import MigLayout

class Panel(JPanel):
	def __init__(self, migLayoutSettings = ""):
		self.setLayout(MigLayout(migLayoutSettings))

		self.initialClick = Point(0, 0)
		self.setOpaque(False)
		self.setBackground(Color(0,30,0, 40))
		#self.setBorder(BorderFactory.createLineBorder(Color.RED))

		self.initUI()
		self.addUI()

		class MouseAdap(MouseAdapter):
			def mousePressed(ms, m):
				self.initialClick = m.getPoint()
		class MouseMotionAdap(MouseMotionAdapter):
			def mouseDragged(ms, m):
				window = SwingUtilities.getWindowAncestor(self)
				x = window.getLocation().x
				y = window.getLocation().y
				xm = (x + m.getX()) - (x + self.initialClick.x)
				ym = (y + m.getY()) - (y + self.initialClick.y)
				window.setLocation(x + xm, y + ym)

		self.addMouseListener(MouseAdap())
		self.addMouseMotionListener(MouseMotionAdap())

		self.setVisible(True)

	def initUI(self):
		pass

	def addUI(self):
		pass

	def mousePressed(m):
		print "mouse"