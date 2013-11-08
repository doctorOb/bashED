from java.lang import System

from javax.swing import JFrame
from java.awt import Dimension
from java.awt import Toolkit


#props = System.getProperties()
#userDir = props['user.dir'];
#print "User dir " + str(userDir)

class Window(JFrame):
    def __init__(self):

        size = Dimension(700, 500)
        self.setPreferredSize(size)

        screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        self.setLocation(screenSize.getSize().width/2 - size.width/2, 100)


        self.setTitle("bashED Terminal HQ EXTREME");

        #make the window viewable
        self.defaultCloseOperation=JFrame.EXIT_ON_CLOSE
        self.pack()
        self.setVisible(True)



x = Window()

print "end, YOU BITCH";
