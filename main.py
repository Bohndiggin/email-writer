import sys
import csv
import json
from json import JSONEncoder

from PyQt6 import QtCore
from utils import *

from PyQt6.QtWidgets import (
    QApplication, QDialog, QFileDialog, QMainWindow, QMessageBox, QWidget, QColumnView
)
from PyQt6.QtCore import QStringListModel
from PyQt6.uic import loadUi
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from ui import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        # self.authors = []
        self.documents = []
        self.recipients = []
        self.disp_model = QStandardItemModel()
        self.parentItem = self.disp_model.invisibleRootItem()
        self.doc_item_list = []
        self.save_location = ''
        self.columnView.setModel(self.disp_model)

    def connectSignalsSlots(self):
        self.actionNew_Set.triggered.connect(self.placeholder_command)
        self.actionOpen_Set.triggered.connect(self.open_set)
        self.actionSave_Set.triggered.connect(self.quicksave)
        self.actionSave_Set_As.triggered.connect(self.save_set)
        self.actionLoad_Batch.triggered.connect(self.load_batch)
        self.actionWrite_Emails.triggered.connect(self.placeholder_command)
        
        self.actionAdd_Document_Type.triggered.connect(self.placeholder_command)
        self.actionAdd_Document_Set.triggered.connect(self.placeholder_command)
        self.actionAdd_Author_Style.triggered.connect(self.placeholder_command)
        self.actionAssign_Author_Style.triggered.connect(self.placeholder_command)
        self.actionHook_Up_API.triggered.connect(self.placeholder_command)
        self.actionAttach.triggered.connect(self.placeholder_command)
        # self.action.triggered.connect(self.placeholder_command)
        
        # self.pushButtonAttach.clicked.connect(self.placeholder_command)
        self.pushButtonPrev.clicked.connect(self.placeholder_command)
        self.pushButtonSend.clicked.connect(self.placeholder_command)
        self.pushButtonNext.clicked.connect(self.placeholder_command)
        # self.pushButtonSend.clicked.connect(self.placeholder_command)     

    def placeholder_command(self):
        print('event triggered')

    def sync_list_and_objects(self):
        self.disp_model = QStandardItemModel()
        self.parentItem = self.disp_model.invisibleRootItem()
        for i in self.documents:
            new_list_item = QStandardItem(i.doc_name)
            self.parentItem.appendRow(new_list_item)
            for j in i.doc_authors:
                new_list_item.appendRow(QStandardItem(j.author_name))
        self.columnView.setModel(self.disp_model)


    def make_author(self, name, lines: list, document_type):
        new_author = AuthorStyle(name, lines, document_type)
        # self.authors_model.insertRow(self.authors_model.rowCount())
        # self.authors_model.setData(self.authors_model.index(self.authors_model.rowCount() -1)
        self.sync_list_and_objects()
        return new_author

    def load_document(self, name, description):
        new_document = DocumentType(name, description)
        new_list_item = QStandardItem(name)
        self.doc_item_list.append(new_list_item)
        self.parentItem.appendRow(new_list_item)
        # for i in authors:
        #     new_list_item.appendRow(QStandardItem(i.author_name))
        self.columnView.setModel(self.disp_model)
        return new_document
        
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
            self.save_location = selected_files[0]
            with open(selected_files[0], mode='w') as f:
                json_data = {'save_location': self.save_location, 'documents': self.documents}
                json.dump(json_data, f, ensure_ascii=False, indent=4, cls=CustomEncoder)
        else:
            self.save_location = filepath
            with open(filepath, mode='w') as f:
                json_data = {'save_location': self.save_location, 'documents': self.documents}
                json.dump(json_data, f, ensure_ascii=False, indent=4, cls=CustomEncoder)

    def quicksave(self):
        try:
            print(self.save_location)
            self.save_set(filepath=self.save_location)
        except Exception as e:
            print(e)
        finally:
            pass

    def open_set(self, filepath=None):
        self.documents = []
        def load_json_data(data):
            for i in data['documents']:
                new_doc = DocumentType(i['doc_name'], i['description'])
                self.documents.append(new_doc)
            
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
        self.documents.append(self.load_document('testdoc', 'this is a test'))
        self.make_author('Joe', [['huh', 'how'], ['are', 'you'], ['doing', 'me', 'favor']], self.documents[-1])
        self.make_author('Joe2', [['huh', 'how'], ['are', 'you'], ['doing', 'me', 'favor']], self.documents[-1])

# make it so that when it makes a new author it attaches them to a document. Docs first, authors second!

    def test(self):
        self.test_set()
        self.load_batch(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/test1.csv')
        self.save_set(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/test1.json')
        self.open_set(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/test1.json')
        self.save_set(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/test2.json')
        self.make_author('james', [['I', 'Me'], ['no', 'dont'], ['speak', 'talk']], self.documents[-1])
        self.quicksave()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    win.test()
    sys.exit(app.exec())
