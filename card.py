from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class Card(QWidget):
    def __init__(self, bosqich="1", place="1", group_place="1", group="Foundation", xp="1"):
        super().__init__()
        self.setStyleSheet("background-color:white")
        self.bosqich = bosqich
        self.group_number_="12"
        self.xp = xp
        self.place = place
        self.group = group
        self.setFixedSize(500,600)
        self.v_main = QVBoxLayout()
        self.h_bosqich = QHBoxLayout()
        self.h_xp = QHBoxLayout()
        self.h_umumiy = QHBoxLayout()
        self.h_group = QHBoxLayout()

        
        font = QFont("Arial", 25) 

        self.lbl_bosqich = QLabel("Bosqich")
        self.lbl_bosqich.setFont(font)
        self.bosqich_lbl = QLabel(self.bosqich)
        self.bosqich_lbl.setFont(font)

        self.indicator = QLabel()
        image = QPixmap("indicator.png").scaled(260, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Iconning o'lchamini kattalashtirish
        self.indicator.setPixmap(image)

        self.xp_lbl = QLabel("XP")
        self.xp_lbl.setFont(font)
        self.xp_count = QLabel(self.xp)
        self.xp_count.setFont(font)

        self.reyting = QLabel("Reyting")
        self.reyting.setFont(font)
        self.umumiy = QLabel("Umumiy")
        self.umumiy.setFont(font)
        self.umumiy_ball = QLabel(self.place)
        self.umumiy_ball.setFont(font)

        self.group_lbl = QLabel(self.group)
        self.group_lbl.setFont(font)
        self.group_number = QLabel(self.group_number_)
        self.group_number.setFont(font)

        self.h_bosqich.addWidget(self.lbl_bosqich)
        self.h_bosqich.addWidget(self.bosqich_lbl)

        self.h_xp.addWidget(self.xp_lbl)
        self.h_xp.addWidget(self.xp_count)

        self.h_umumiy.addWidget(self.umumiy)
        self.h_umumiy.addWidget(self.umumiy_ball)

        self.h_group.addWidget(self.group_lbl)
        self.h_group.addWidget(self.group_number)

        self.v_main.addLayout(self.h_bosqich)
        self.v_main.addWidget(self.indicator)
        self.v_main.addLayout(self.h_xp)
        self.v_main.addLayout(self.h_umumiy)
        self.v_main.addLayout(self.h_group)

        self.setLayout(self.v_main)

if __name__ == "__main__":
    app = QApplication([])
    win = Card()
    win.show()
    app.exec_()
