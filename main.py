import sys
import csv
import json
import typing
import smtplib
from dotenv import load_dotenv
import os

from PyQt6 import QtCore

from utils import *

from PyQt6.QtWidgets import (
    QApplication, QFileDialog, QMainWindow, QDialog, QWidget
)
from PyQt6.uic import loadUi
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QTextCursor

from ui import Ui_MainWindow
from uidiag import Ui_Dialog
import uidiag2
import uidiag3


class AddDocumentDialog(QDialog, Ui_Dialog):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setupUi(self)

    def get_data(self):
        data = [self.lineEdit.text(), self.lineEdit_2.text()]
        return data

class AddAuthorStyleDialog(QDialog, uidiag2.Ui_Dialog):
    def __init__(self, parent: QWidget, documents_to_write) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.comboBox.addItems(documents_to_write)

    def get_data(self):
        data = [self.lineEdit.text(), self.comboBox.currentIndex()]
        return data
    
class RemoveAuthorDialog(QDialog, uidiag3.Ui_Dialog):
    def __init__(self, parent: QWidget, author_list: list) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.comboBox.addItems(author_list)

    def get_data(self):
        data = [self.comboBox.currentIndex()]
        return data
    
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.documents = []
        self.recipients = []
        self.disp_model = QStandardItemModel()
        self.parentItem = self.disp_model.invisibleRootItem()
        self.doc_item_list = []
        self.save_location = ''
        self.author_count = 0
        self.columnView.setModel(self.disp_model)
        self.doc_selected = 0
        self.author_selected_index = 0
        self.author_selected = None
        self.emails = []
        self.text_cursor = QTextCursor(self.textEdit.document())
        self.selected_document_viewing = 0


    def connectSignalsSlots(self):
        self.actionNew_Set.triggered.connect(self.placeholder_command)
        self.actionOpen_Set.triggered.connect(self.open_set)
        self.actionSave_Set.triggered.connect(self.quicksave)
        self.actionSave_Set_As.triggered.connect(self.save_set)
        self.actionLoad_Batch.triggered.connect(self.load_batch)
        self.actionWrite_Emails.triggered.connect(self.write_emails)
        
        self.actionAdd_Document_Type.triggered.connect(self.new_doc_type)
        self.actionAdd_Document_Set.triggered.connect(self.placeholder_command)
        self.actionAdd_Author_Style.triggered.connect(self.new_author_style)
        self.actionRemove_Author_Style.triggered.connect(self.delete_author)
        self.actionAssign_Author_Style.triggered.connect(self.placeholder_command)
        self.actionHook_Up_API.triggered.connect(self.placeholder_command)
        self.actionAttach.triggered.connect(self.placeholder_command)
        # self.action.triggered.connect(self.placeholder_command)
        
        # self.pushButtonAttach.clicked.connect(self.placeholder_command)
        self.pushButtonPrev.clicked.connect(self.previous_document)
        self.pushButtonSend.clicked.connect(self.send_email)
        self.pushButtonNext.clicked.connect(self.next_document)
        # self.pushButtonSend.clicked.connect(self.placeholder_command)
        self.columnView.clicked.connect(self.on_columnView_clicked)  

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
        self.author_count += 1
        new_author = AuthorStyle(name, lines, document_type)
        self.sync_list_and_objects()
        return new_author

    def make_document(self, name, description):
        self.documents.append(DocumentType(name, description))
        new_list_item = QStandardItem(name)
        self.doc_item_list.append(new_list_item)
        self.parentItem.appendRow(new_list_item)
        self.columnView.setModel(self.disp_model)
        self.sync_list_and_objects()
        
    def load_batch(self, filepath=None):
        if not filepath:
            self.dialog = QFileDialog()
            self.dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
            if self.dialog.exec():
                selected_files = self.dialog.selectedFiles()
            try:
                with open(selected_files[0], mode='r', newline='') as f:
                    csvreader = csv.DictReader(f)
                    self.recipients = []
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
            except Exception as e:
                print(e)
        else:
             with open(filepath, mode='r', newline='') as f:
                csvreader = csv.DictReader(f)
                self.recipients = []
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
            try:
                with open(selected_files[0], mode='w') as f:
                    json_data = {'save_location': self.save_location, 'documents': self.documents}
                    json.dump(json_data, f, ensure_ascii=False, indent=4, cls=CustomEncoder)
            except Exception as e:
                print(e)
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
                for j in i['doc_authors']:
                    AuthorStyle(j['author_name'], j['lines'], new_doc)
                self.documents.append(new_doc)
        if not filepath:
            self.dialog = QFileDialog()
            self.dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
            if self.dialog.exec():
                selected_files = self.dialog.selectedFiles()
            try:
                with open(selected_files[0], mode='r') as f:
                    loaded_json = json.load(f)
                    load_json_data(loaded_json)
            except Exception as e:
                print(e)
        else:
            with open(filepath, mode='r') as f:
                loaded_json = json.load(f)
                load_json_data(loaded_json)
        print(self.documents)
        self.sync_list_and_objects()

    def test_set(self):
        self.make_document('testdoc', 'this is a test')
        self.make_author('Joe', [['huh', 'how'], ['are', 'you'], ['doing', 'me', 'favor']], self.documents[0])
        self.make_author('Joe2', [['huh', 'how'], ['are', 'you'], ['doing', 'me', 'favor']], self.documents[0])

    def test(self):
        # self.test_set()
        self.load_batch(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/test1.csv')
        # self.save_set(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/test1.json')
        self.open_set(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/testWORK.json')
        # self.save_set(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/test2.json')
        # self.make_author('james', [['I', 'Me'], ['no', 'dont'], ['speak', 'talk']], self.documents[0])
        # self.quicksave()
        # self.make_document('sss', 'ssa')
        # self.quicksave()
        # self.new_author_style(filepath='C:/Users/bohnd/Documents/email-tool-2/ignore/test1_author_style.csv')
        # self.quicksave()
        # pass
    
    def new_doc_type(self):
        self.dialog = AddDocumentDialog(self)
        self.dialog.setModal(True)
        if self.dialog.exec() == QDialog.DialogCode.Accepted:
            data_recieved = self.dialog.get_data()
        self.make_document(data_recieved[0], data_recieved[1])

    def new_author_style(self, filepath=None):
        def author_extract(style_lines):
            output = []
            for row in style_lines:
                cleaned_row = [i for i in row if i != '']
                output.append(cleaned_row)
            doc_names_list = [str(x) for x in self.documents]
            self.dialog = AddAuthorStyleDialog(self, doc_names_list)
            self.dialog.setModal(True)
            if self.dialog.exec() == QDialog.DialogCode.Accepted:
                data_recieved = self.dialog.get_data()
            self.make_author(data_recieved[0], output, self.documents[data_recieved[1]])
        if not filepath:
            self.dialog = QFileDialog()
            self.dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
            if self.dialog.exec():
                selected_files = self.dialog.selectedFiles()
            try:
                with open(selected_files[0], 'r') as f:
                    style_lines = csv.reader(f)
                    author_extract(style_lines)
            except Exception as e:
                print(e)
        else:
            try:
                with open(filepath, 'r') as f:
                    style_lines = csv.reader(f)
                    author_extract(style_lines)
            except Exception as e:
                print(e)

    def write_emails(self):
        # print(self.columnView.selectionModel().selectedIndexes())
        try:
            index = [self.doc_selected, self.author_selected_index]
            self.author_selected = self.documents[index[0]].doc_authors[index[1]]
            self.emails = []
            if self.recipients == []:
                print('No Recipients!!')
            else:
                for i in self.recipients:
                    self.emails.append(self.author_selected.write(i))
                self.show_document()
        except Exception as e:
            print(e)
        
    def on_columnView_clicked(self, index):
        print(index.data())
        string_selcted = index.data()
        if 'Author: ' == string_selcted[0:8]:
            self.author_selected_index = index.row()
        elif 'Document: ' == string_selcted[0:10]:
            self.doc_selected = index.row()
        else:
            print('oops')
    
    def show_document(self):
        self.textEdit.clear()
        try:
            self.textEdit.insertPlainText(self.emails[self.selected_document_viewing])
        except Exception as e:
            print(e)

    def previous_document(self):
        if self.selected_document_viewing > 0:
            self.selected_document_viewing -= 1
        else:
            pass
        self.show_document()
    
    def next_document(self):
        if self.selected_document_viewing < len(self.emails)-1:
            self.selected_document_viewing += 1
        else:
            pass
        self.show_document()

    def send_email(self):
        index_of_email = self.selected_document_viewing
        email_to_send = self.emails[index_of_email]
        recipient_to_recieve = self.recipients[index_of_email]
        target_email = recipient_to_recieve.fillables_dictionary['email_address']
        subject = self.documents[self.doc_selected].doc_name[9:]
        sent_address = os.getenv('EMAIL_ADDRESS')
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sent_address, os.getenv('EMAIL_SECRET'))
            server.sendmail(sent_address, target_email, f"Subject: {subject}\n\n{email_to_send}")
            server.quit()
            print("Email sent successfully")
        except Exception as e:
            print(f"Error: {e}")

    def delete_author(self):
        author_list = []
        for i in self.documents:
            for j in i.doc_authors:
                author_list.append(j)
        author_list = [str(x) for x in author_list]
        self.dialog = RemoveAuthorDialog(self, author_list=author_list)
        self.dialog.setModal(True)
        if self.dialog.exec() == QDialog.DialogCode.Accepted:
            data_recieved = self.dialog.get_data()
        for i in self.documents:
            for j in i.doc_authors:
                if author_list[data_recieved[0]][:-19] == j.author_name:
                    i.remove_author(j)
                    break

    def delete_document(self):
        pass

        
if __name__ == '__main__':
    load_dotenv()
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    # win.test()
    sys.exit(app.exec())
