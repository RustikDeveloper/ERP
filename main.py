from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from card import Card

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:white")
        self.h_info = QHBoxLayout()
        self.h_main = QHBoxLayout()
        self.info = QWidget()
        self.lbl = QLabel("")
        self.rasm = QLabel()
        self.lbl.setFixedHeight(300)
        image = QPixmap("logo.jpg")
        self.rasm.setPixmap(image)

        self.hm_btn = QPushButton("Bosh sahifa", clicked=self.Bosh_sahifa)
        self.hm_btn.setStyleSheet("font-size:20px;color:grey;")
        self.paid_btn = QPushButton("To'lovlarim")
        self.gro_btn = QPushButton("Guruhlarim")    
        self.result_btn = QPushButton("Ko'rsatgichlarim")
        self.raiting_btn = QPushButton("Reyting")
        self.shop_btn = QPushButton("Do'kon")
        self.setting_btn = QPushButton("Sozlamalar")

        self.hm_btn.setIcon(QIcon('home.png')) 
        self.paid_btn.setIcon(QIcon('paid_logo.png'))
        self.gro_btn.setIcon(QIcon('people.png'))
        self.result_btn.setIcon(QIcon('rating_logo.png'))
        self.raiting_btn.setIcon(QIcon('resul_logo.png'))
        self.shop_btn.setIcon(QIcon('shop_logo.jpg'))
        self.setting_btn.setIcon(QIcon('settings.png'))

        icon_size = QSize(32, 32)
        self.hm_btn.setIconSize(icon_size)
        self.paid_btn.setIconSize(icon_size)
        self.gro_btn.setIconSize(icon_size)
        self.result_btn.setIconSize(icon_size)
        self.raiting_btn.setIconSize(icon_size)
        self.shop_btn.setIconSize(icon_size)
        self.setting_btn.setIconSize(icon_size)

        self.size_font(self.hm_btn)
        self.size_font(self.paid_btn)
        self.size_font(self.gro_btn)
        self.size_font(self.result_btn)
        self.size_font(self.raiting_btn)
        self.size_font(self.shop_btn)
        self.size_font(self.setting_btn)

        self.lst_widget = QListWidget()  
        self.btn_lay = QVBoxLayout()
        self.btn_lay.addWidget(self.rasm)
        self.btn_lay.addWidget(self.hm_btn)
        self.btn_lay.addWidget(self.paid_btn)
        self.btn_lay.addWidget(self.gro_btn)
        self.btn_lay.addWidget(self.result_btn)
        self.btn_lay.addWidget(self.raiting_btn)
        self.btn_lay.addWidget(self.shop_btn)
        self.btn_lay.addWidget(self.setting_btn)
        self.btn_lay.addWidget(self.lbl)
        self.h_main.addLayout(self.btn_lay)
        self.h_main.addLayout(self.h_info)
        self.h_info.addWidget(self.lst_widget)  
        self.h_main.addStretch()
        self.setLayout(self.h_main)
        self.resize(800, 600)

    def size_font(self, button):
        button.setFixedSize(200, 60)
        button.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: white;
                padding: 10px;
                border-radius: 5px;
                font-size:  15px;
                text-align: left; 
                padding-left: 50px;
            }
            QPushButton:hover {
                background-color: #D2B48C;
                color: white;
                font-size:20px
            }
        """)

    def Bosh_sahifa(self):
        widget = Card() 
        for i in reversed(range(self.h_info.count())): 
            widget_item = self.h_info.itemAt(i)
            if widget_item is not None:
                widget_item.widget().deleteLater()
        self.h_info.addWidget(widget)

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()
