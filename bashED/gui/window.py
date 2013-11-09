from java.lang import System

from javax.swing import JFrame
from java.awt import Dimension
from java.awt import Toolkit
from java.awt import Color



from panel import Panel
from mainPanel import MainPanel

from javax.swing import JRootPane
from javax.swing import BorderFactory
from javax.swing.border import Border
from javax.swing import UIManager
from javax.swing import ImageIcon
#from console import BashED_Console

#props = System.getProperties()
#userDir = props['user.dir'];
#print "User dir " + str(userDir)

class Window(JFrame):
    def __init__(self):

        UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());

        size = Dimension(800, 800)
        self.setPreferredSize(size)

        screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        self.setLocation(screenSize.getSize().width/2 - size.width/2, 100)
        self.setTitle("bashED Terminal HQ EXTREME");

        self.setUndecorated(True)
        self.getRootPane().setOpaque(False)
        #self.getRootPane().setWindowDecorationStyle(JRootPane.FRAME);
        self.setBackground(Color(0,128,0, 198))


        self.setIconImage(ImageIcon("icon.png").getImage())

        mp = MainPanel()
        self.add(mp)
        bb = BorderFactory.createLineBorder(Color.BLACK, 5)
        bw1 = BorderFactory.createLineBorder(Color.WHITE, 1)
        bw2 = BorderFactory.createLineBorder(Color.WHITE, 1)

        mp.setBorder( BorderFactory.createCompoundBorder( bw1, BorderFactory.createCompoundBorder(bb, bw2) ))


        #make the window viewable
        self.defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        self.pack()
        self.setVisible(True)



x = Window()

