import sys
import typing
import csv
import json
from json import JSONEncoder

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
        self.actionSave_Set_As.triggered.connect(self.save_set)
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

    def make_author(self, name, lines: list, document_type: str):
        new_author = AuthorStyle(name, lines, document_type)
        # self.authors.append(new_author)
        return new_author

    def load_document(self, name, description, authors):
        new_document = DocumentType(name, description, authors)
        # self.documents.append(new_document)
        return new_document
        
    # def make_new_document(self, name, description):
    #     new_document = DocumentType(name, description)
    #     self.documents.append(new_document)

    # def make_recipient(self, name, fillables_dictionary):
    #     new_recipient = Recipient(name, fillables_dictionary=fillables_dictionary)
    #     self.recipients.append(new_recipient)


            

    def load_batch(self, filepath=None):
        if not filepath:
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
        else:
             with open(filepath, mode='r', newline='') as f:
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

    def save_set(self, filepath=None):
        if not filepath:
            self.dialog = QFileDialog()
            self.dialog.setFileMode(QFileDialog.FileMode.AnyFile)
            if self.dialog.exec():
                selected_files = self.dialog.selectedFiles()
            with open(selected_files[0], mode='w') as f:
                json_data = {'documents': self.documents, 'authors': self.authors}
                json.dump(json_data, f, ensure_ascii=False, indent=4, cls=CustomEncoder)
        else:
            with open(filepath, mode='w') as f:
                json_data = {'documents': self.documents, 'authors': self.authors}
                json.dump(json_data, f, ensure_ascii=False, indent=4, cls=CustomEncoder)

    def open_set(self, filepath=None):
        self.authors = []
        self.documents = []
        def load_json_data(data):
            for i in data['authors']:
                self.authors.append(AuthorStyle(i['author_name'], i['lines'], i['document_writes']))
            for i in data['documents']:
                author_list = []
                for j in self.authors:
                    if i['doc_name'] == j.document_writes:
                        author_list.append(j)
                self.documents.append(DocumentType(i['doc_name'], i['description'], author_list))
            
        if not filepath:
            self.dialog = QFileDialog()
            self.dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
            if self.dialog.exec():
                selected_files = self.dialog.selectedFiles()
            with open(selected_files[0], mode='r') as f:
                loaded_json = json.load(f)
                load_json_data(loaded_json)
        else:
            with open(filepath, mode='r') as f:
                loaded_json = json.load(f)
                load_json_data(loaded_json)

    def test_set(self):
        self.authors.append(self.make_author('Joe', [['huh', 'how'], ['are', 'you'], ['doing', 'me', 'favor']], 'testdoc'))
        self.authors.append(self.make_author('Joe2', [['huh', 'how'], ['are', 'you'], ['doing', 'me', 'favor']], 'testdoc'))
        self.documents.append(self.load_document('testdoc', 'this is a test', self.authors))

    def test(self):
        self.test_set()
        self.load_batch(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/test1.csv')
        self.save_set(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/test1.json')
        self.open_set(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/test1.json')
        self.save_set(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/test2.json')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    win.test()
    sys.exit(app.exec())
