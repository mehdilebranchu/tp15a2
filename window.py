from buttons import buttonsPanel
from configDialog import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("SQL client")
        self.setMinimumSize(600,400)
        self.__layout = QVBoxLayout()
        self.__buttonsPanel = buttonsPanel()
        self.__notificationPanel = QTextEdit()
        self.__resultTable = QTableWidget(5,3)
        self.__resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.__layout.addWidget(self.__buttonsPanel)
        self.__layout.addWidget(self.__notificationPanel)
        self.__layout.addWidget(self.__resultTable)
        self.setLayout(self.__layout)




if __name__ == "__main__":
   app = QApplication([])
   dial = configDial()
   win = Window()
   win.show()
   dial.show()
   app.exec_()
