import sys

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
        # self.connectSignalsSlots()

    # def connectSignalsSlots(self):
    #     self.action_Exit.triggered.connect(self.close)
    #     self.action_Find_Replace.triggered.connect(self.findAndReplace)
    #     self.action_About.triggered.connect(self.about)

    # def about(self):
    #     QMessageBox.about(
    #         self,
    #         "About Sample Editor",
    #         "<p>A sample text editor app built with:</p>"
    #         "<p>- PyQt</p>"
    #         "<p>- Qt Designer</p>"
    #         "<p>- Python</p>",
    #     )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
