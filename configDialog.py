from labeledTextField import *


class configDial(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.layout = QVBoxLayout()
        self.setWindowTitle("configuration")
        self.__1 = labeledTextField('IP adress')
        self.__2 = labeledTextField('User')
        self.__3 = labeledTextField('Password')
        self.layout.addWidget(self.__1)
        self.layout.addWidget(self.__2)
        self.layout.addWidget(self.__3)
        self.setLayout(self.layout)
