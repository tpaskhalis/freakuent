import os, sys
from PyQt4 import QtCore, QtGui

from mainwindow import Ui_MainWindow

class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QtGui.QApplication(sys.argv)
window = Window()
window.show()
app.exec_()
