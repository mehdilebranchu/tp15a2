from PySide2.QtWidgets import *
from buttons import buttonsPanel

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("SQL client")
        self.setMinimumSize(600,400)
        self.__layout = QVBoxLayout()
        self.__buttonsPanel = buttonsPanel()
        self.__layout.addWidget(self.__buttonsPanel)
        self.setLayout(self.__layout)




if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
