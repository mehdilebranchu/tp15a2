from PySide2.QtWidgets import *


class labeledTextField(QWidget):

    def __init__(self,text):
        QWidget.__init__(self)
        self.__text = text
        self.layout = QHBoxLayout()
        self.label = QLabel(self.__text)
        self.textZone = QTextEdit()
        self.textZone.setMaximumHeight(50)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textZone)
        self.setLayout(self.layout)



