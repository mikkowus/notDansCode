#IMPORTS
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class WindowClassOne(QWidget):
    def __init__(self):
        super(WindowClassOne,self).__init__()
        #SET THE DEFAULT FONT FOR APP
        self.setFont(QFont('consolas',11))
        #SET DEFUALT MINIMUM SIZE OF WINDOW
        self.setMinimumSize(100,100)
        
        #INSTANTIATE AN OUTER LAYOUT (master layout); STEP 1
        self.outerLayout = QHBoxLayout()
        
        #ADD THE MAIN WINDOWS OUTER LAYOUT (MASTER LAYOUT); STEP 2
        self.setLayout(self.outerLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion') 
    window = WindowClassOne()
    window.show()
    sys.exit(app.exec_())

    