import sys
from utils import *

from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt6.uic import loadUi

from ui import Ui_MainWindow

def main():
    window = Ui_MainWindow()

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.actionOpen_Set.triggered.connect(self.placeholder_command)
        self.actionSave_Set.triggered.connect(self.placeholder_command)
        self.actionSave_Set_As.triggered.connect(self.placeholder_command)
        self.actionLoad_Batch.triggered.connect(self.placeholder_command)
        self.actionWrite_Emails.triggered.connect(self.placeholder_command)
        
        self.actionAdd_Document_Type.triggered.connect(self.placeholder_command)
        self.actionAdd_Document_Set.triggered.connect(self.placeholder_command)
        self.actionAdd_Author_Style.triggered.connect(self.placeholder_command)
        self.actionAssign_Author_Style.triggered.connect(self.placeholder_command)
        self.actionHook_Up_API.triggered.connect(self.placeholder_command)
        # self.action.triggered.connect(self.placeholder_command)
        
        self.pushButtonAttach.clicked.connect(self.placeholder_command)
        self.pushButtonPrev.clicked.connect(self.placeholder_command)
        self.pushButtonSend.clicked.connect(self.placeholder_command)
        self.pushButtonNext.clicked.connect(self.placeholder_command)
        # self.pushButtonSend.clicked.connect(self.placeholder_command)

    def placeholder_command(self):
        print('event triggered')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
