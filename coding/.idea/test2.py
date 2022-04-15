from PyQt5 import QtCore, QtGui, QtWidgets
import sys 
from PyQt5.QtWidgets import QMainWindow,QApplication
class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin,self).__init__()
        self.setWindowTitle("One")
        self.resize(800,800)
        self.status=self.statusBar()
        self.status.showMessage("111",5000)
if __name__=="__main":
    app = QApplication(sys.argv)
    main= FirstMainWin()
    main.show()
    #sys.exit(app.exec_())