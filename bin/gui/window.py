

from java.lang import System

from javax.swing import JFrame
from java.awt import Dimension
from java.awt import Toolkit
from java.awt import Color
from mainPanel import MainPanel
from panel import Panel

from javax.swing import JRootPane
from javax.swing import BorderFactory
from javax.swing.border import Border
from javax.swing import UIManager
from javax.swing import ImageIcon
from javax.swing import JLayeredPane
from javax.swing import JLabel
from javax.swing import JDesktopPane
#import bashed_run
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


        #j = JDesktopPane()
        #j.setOpaque(False)
        self.setLayout(None)

        self.setIconImage(ImageIcon('bin/gui/media/' + "icon.png").getImage())




        mp = MainPanel()
        self.add(mp)
        mp.setBounds(0, 0, size.width, size.height)


        imageTest = ImageIcon('bin/gui/media/' + "image.png")
        imageTestLabel = JLabel(imageTest)
        self.add(imageTestLabel)
        imageTestLabel.setBounds(0, 0, size.width, size.height)
        #self.getContentPane().add(mp)

        #self.getContentPane().add(JLabel("Iglo"))

        bb = BorderFactory.createLineBorder(Color.BLACK, 5)
        bw1 = BorderFactory.createLineBorder(Color.WHITE, 1)
        bw2 = BorderFactory.createLineBorder(Color.WHITE, 1)

        mp.setBorder( BorderFactory.createCompoundBorder( bw1, BorderFactory.createCompoundBorder(bb, bw2) ))


        #make the window viewable
        self.defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        self.pack()
        self.setVisible(True)



x = Window()

