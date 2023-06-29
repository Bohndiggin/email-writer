import csv
import random
from json import JSONEncoder
from typing import Any

document_types = []

class AuthorStyle:
    def __init__(self, name, lines: list, document_type):
        if 'Author: ' == name[0:8]:
            self.author_name = name
        else:
            self.author_name = 'Author: ' + name
        self.lines = lines
        document_type.doc_authors.append(self)

    def export_style(self):
        pass # makes csv of the style

    def write(self, recipient):
        document = []
        for i in self.lines:
            line = random.choice(i)
            document.append(line)
        assembled_document = ' '.join(document) + '\n\nThis Email was made with email-writer: https://github.com/Bohndiggin/email-writer'
        formatted_document = assembled_document.format(**recipient.fillables_dictionary).replace('\\n', '\n')
        return formatted_document

    def __repr__(self) -> str:
        return f'{self.author_name} is an author Style'

class DocumentType:
    def __init__(self, name, description) -> None:
        if 'Document: ' == name[0:10]:
            self.doc_name = name
        else:
            self.doc_name = 'Document: ' + name
        self.description = description
        self.doc_authors = [] # A list of author styles since they'll be only for one document
    
    def __repr__(self) -> str:
        return f'{self.doc_name}: {self.description}'
    
    def build_fillables(self):
        pass # will build a list of fillables based on self.authors???

    def remove_author(self, author):
        self.doc_authors.pop(self.doc_authors.index(author))
        print(self.doc_authors)

class Recipient:
    def __init__(self, name, fillables_dictionary: dict) -> None:
        self.name = name
        self.fillables_dictionary = fillables_dictionary

    def __repr__(self) -> str:
        return f'{self.name}: a recipient.'

class CustomEncoder(JSONEncoder):
    def default(self, o) -> Any:
        return o.__dict__