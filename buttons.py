from PySide2.QtWidgets import *

class buttonsPanel(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.layout = QHBoxLayout()
        self.button1 = QPushButton("configure")
        self.button2 = QPushButton("connect")
        self.button3 = QPushButton("disconnect")
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.setLayout(self.layout)
