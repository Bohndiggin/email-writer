from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as font
from utils import *


class MainWindow:
    def __init__(self, root) -> None:
        self.root = root

        self.style = ttk.Style()
        self.style.configure('my.TButton', font=('helvetica', 35))
        # self.large_button_font = font.Font(size=35)

        # Frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame['padding'] = 5
        self.main_frame.pack()

        # Menu Stuff
        root.option_add('*tearOff', FALSE)
        self.menubar = Menu(root)
        root['menu'] = self.menubar

        # File Menu
        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menu_file.add_command(label='Open Set...', command=self.placeholder_command)
        self.menu_file.add_command(label='Save Set', command=self.placeholder_command)
        self.menu_file.add_command(label='Save Set As...', command=self.placeholder_command)

        # Documents Submenu
        self.menu_documents = Menu(self.menu_file)
        self.menu_documents.add_command(label='Add Document Type...', command=self.placeholder_command)
        self.menu_documents.add_command(label='Add Document Set...', command=self.placeholder_command)
        self.menu_documents.add_command(label='Remove Document Type', command=self.placeholder_command)
        
        # Authors Submenu
        self.menu_authors = Menu(self.menu_file)
        self.menu_authors.add_command(label='Add Author Style...', command=self.placeholder_command)
        self.menu_authors.add_command(label='Assign Author Style...', command=self.placeholder_command)

        # Adding Submenus to File Menu
        self.menu_file.add_cascade(label='Document Types', menu=self.menu_documents)
        self.menu_file.add_cascade(label='Author Styles', menu=self.menu_authors)

        # Edit Menu
        self.menu_edit = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_edit, label='Edit')
        self.menu_edit.add_command(label='Generate', command=self.placeholder_command)
        
        # GUI - Frames 

        self.gui_listboxes_frame_doc = ttk.Frame(self.main_frame)
        self.gui_listboxes_frame_doc.grid(column=0, row=0, sticky=NSEW)
        self.gui_listboxes_frame_author = ttk.Frame(self.main_frame)
        self.gui_listboxes_frame_author.grid(column=1, row=0, sticky=NSEW)

        self.output_gui_frame = ttk.Frame(self.main_frame)
        self.output_gui_frame.grid(column=2, row=0, sticky=NSEW)

        self.controls_outer_frame = ttk.Frame(self.main_frame)
        self.controls_outer_frame.grid(column=0, row=2, columnspan=3, sticky=NSEW)
        

        self.doc_list_frame = ttk.Frame(self.gui_listboxes_frame_doc)
        self.doc_list_frame.pack()
        self.author_list_frame = ttk.Frame(self.gui_listboxes_frame_author)
        self.author_list_frame.pack(side=RIGHT)
        self.output_frame = ttk.Frame(self.output_gui_frame)
        self.output_frame.pack(side=RIGHT)

        # GUI - Doc List
        self.doc_list_label = ttk.Label(self.doc_list_frame, text='List of Documents')
        self.doc_list_label.pack()
        self.doc_list_listbox = Listbox(self.doc_list_frame, height=20)
        self.doc_list_listbox.pack()

        # GUI - Author List
        self.author_list_label = ttk.Label(self.author_list_frame, text='List of Authors')
        self.author_list_label.pack()
        self.author_list_listbox = Listbox(self.author_list_frame, height=20)
        self.author_list_listbox.pack()

        # GUI - Output
        self.output_label = ttk.Label(self.output_frame, text='OUTPUT')
        self.output_label.pack()
        self.output_textbox = Text(self.output_frame, width=60, height=20)
        self.output_textbox.pack()

        # GUI - Controls
        self.generate_button = ttk.Button(self.controls_outer_frame, text="WRITE", command=self.placeholder_command, padding=15, style='my.TButton')
        self.generate_button.pack(side=LEFT)


    def placeholder_command(self):
        pass