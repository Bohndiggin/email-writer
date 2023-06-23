import sys
import typing
import csv
import json

from PyQt6 import QtCore
from utils import *

from PyQt6.QtWidgets import (
    QApplication, QDialog, QFileDialog, QMainWindow, QMessageBox, QWidget
)
from PyQt6.uic import loadUi

from ui import Ui_MainWindow

# class FileLoader(QDialog):
#     def __init__(self, parent=None) -> None:
#         super().__init__(parent)
#         self.setupUi(self)



class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.authors = []
        self.documents = []
        self.recipients = []

    def connectSignalsSlots(self):
        self.actionNew_Set.triggered.connect(self.placeholder_command)
        self.actionOpen_Set.triggered.connect(self.open_set)
        self.actionSave_Set.triggered.connect(self.placeholder_command)
        self.actionSave_Set_As.triggered.connect(self.placeholder_command)
        self.actionLoad_Batch.triggered.connect(self.load_batch)
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

    def make_author(self, name, lines, document_type):
        new_author = AuthorStyle(name, lines, document_type)
        self.authors.append(new_author) 

    def load_document(self, name, description, authors):
        new_document = DocumentType(name, description, authors)
        self.documents.append(new_document) 
        
    # def make_new_document(self, name, description):
    #     new_document = DocumentType(name, description)
    #     self.documents.append(new_document)

    # def make_recipient(self, name, fillables_dictionary):
    #     new_recipient = Recipient(name, fillables_dictionary=fillables_dictionary)
    #     self.recipients.append(new_recipient)


    def open_set(self):
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        if self.dialog.exec():
            selected_files = self.dialog.selectedFiles()
        with open(selected_files[0], mode='r') as f:
            print(f)

    def load_batch(self):
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        if self.dialog.exec():
            selected_files = self.dialog.selectedFiles()
        with open(selected_files[0], mode='r', newline='') as f:
            csvreader = csv.DictReader(f)
            self.recipients = []
            # print(csvreader[0])
            batch = []
            for row in csvreader:
                batch.append(row)
            try:
                for i in batch:
                    self.recipients.append(Recipient(i['name'], fillables_dictionary=i))
            except:
                for i in range(len(batch)):
                    self.recipients.append(Recipient(i, fillables_dictionary=batch[i]))
            finally:
                print(self.recipients[0])
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
