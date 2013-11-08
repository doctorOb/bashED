from java.lang import System

from javax.swing import JFrame
from java.awt import Dimension
from java.awt import Toolkit
from java.awt import Color

from panel import Panel
from mainPanel import MainPanel

from javax.swing import UIManager

#from console import BashED_Console

#props = System.getProperties()
#userDir = props['user.dir'];
#print "User dir " + str(userDir)

class Window(JFrame):
    def __init__(self):

        UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());

        size = Dimension(700, 400)
        self.setPreferredSize(size)

        screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        self.setLocation(screenSize.getSize().width/2 - size.width/2, 100)
        self.setTitle("bashED Terminal HQ EXTREME");

        #self.setUndecorated(True)

        self.setBackground(Color(255,0,0))

        mp = MainPanel()
        self.add(mp)

        #make the window viewable
        self.defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        self.pack()
        self.setVisible(True)



x = Window()

