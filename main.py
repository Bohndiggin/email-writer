from tkinter import *
from tkinter import ttk
from disp import *

v_num = 0.01

root = Tk()
root.title(f"email_crafter {v_num}")
root.minsize(900, 700)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def main():
    window = MainWindow(root=root)

if __name__ == '__main__':
    main()
    root.mainloop()