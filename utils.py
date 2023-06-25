import csv
from json import JSONEncoder
from typing import Any

document_types = []

class AuthorStyle:
    def __init__(self, name, lines: list, document_type):
        self.author_name = name
        self.lines = lines
        document_type.doc_authors.append(self)

    def export_style(self):
        pass # makes csv of the style

    def __repr__(self) -> str:
        return f'{self.author_name} is an author Style'

class DocumentType:
    def __init__(self, name, description) -> None:
        self.doc_name = name
        self.description = description
        self.doc_authors = [] # A list of author styles since they'll be only for one document
        # self.form_fillables = []
        # print(self.doc_authors)
    
    def __repr__(self) -> str:
        return f'{self.doc_name}: {self.description}'
    
    def build_fillables(self):
        pass # will build a list of fillables based on self.authors???
    
    def export_document(self):
        pass

class Recipient:
    def __init__(self, name, fillables_dictionary: dict) -> None:
        self.name = name
        self.fillables_dictionary = fillables_dictionary

    def __repr__(self) -> str:
        return f'{self.name}: a recipient.'

class CustomEncoder(JSONEncoder):
    def default(self, o) -> Any:
        return o.__dict__

def read_in_author_style():
    pass

def read_in_recipient_data():
    pass #Builds list of recipients and fills the dictionary with the form fillables

def author(doc, style, recipient):
    pass # Take doc type, fill recipient data, build using style

def broker(doc, style, recipients):
    pass # Will call author for each document needed to be written, should/can be multiprocessed??

