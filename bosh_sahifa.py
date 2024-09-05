from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize

class BoshMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.v_main=QVBoxLayout()
        self.lbl=QLabel("Kumushlar")
        

if __name__ == "__main__":
    app = QApplication([])
    win = BoshMenu()
    win.show()
    app.exec_()