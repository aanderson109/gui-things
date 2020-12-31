import tkinter
import os
from tkinter import Tk, Text, Menu, Scrollbar, Frame, Text, N, S, E, W, RIGHT, Y, END

class Notepad(Frame):

    def __init__(self):
        super().__init__()
        self.initNotepad()

    def initNotepad(self):
        self.master.title("Notepad Clone (GUI Madness: Tkinter Edition)")

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        # Text Area
        self.text_area = Text(self.master, padx=0)
        self.text_area.pack()
        self.text_area.grid(sticky = N + E + S + W)


        # Menu Bar
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        # File Menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=None, accelerator="Ctrl+N")
        file_menu.add_command(label="New Window", command=None, accelerator="Ctrl+Shift+N")
        file_menu.add_command(label="Open...", command=None, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=None, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As...", command=None, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Page Setup...", command=None)
        file_menu.add_command(label="Print...", command=None, accelerator="Ctrl+P")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=None)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit Menu
        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=None, accelerator="Ctrl+Z")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=None, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=None, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=None, accelerator="Ctrl+V")
        edit_menu.add_command(label="Delete", command=None, accelerator="Del")
        edit_menu.add_separator()
        edit_menu.add_command(label="Search With Being", command=None, accelerator="Ctrl+E")
        edit_menu.add_command(label="Find...", command=None, accelerator="Ctrl+F")
        edit_menu.add_command(label="Find Next", command=None, accelerator="F3")
        edit_menu.add_command(label="Find Previous", command=None, accelerator="Shift+F3")
        edit_menu.add_command(label="Replace...", command=None, accelerator="Ctrl+H")
        edit_menu.add_command(label="Go To...", command=None, accelerator="Ctrl+G")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=None, accelerator="Ctrl+A")
        edit_menu.add_command(label="Time/Date", command=None, accelerator="F5")
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Format Menu
        format_menu = Menu(menu_bar, tearoff=0)
        format_menu.add_command(label="Word Wrap", command=None)
        format_menu.add_command(label="Font...", command=None)
        menu_bar.add_cascade(label="Format", menu=format_menu)

        # View Menu
        view_menu = Menu(menu_bar, tearoff=0)
        zoom_menu = Menu(menu_bar, tearoff=0)
        view_menu.add_cascade(label="Zoom", menu=zoom_menu)
        zoom_menu.add_command(label="Zoom In", command=None, accelerator="Ctrl+Plus")
        zoom_menu.add_command(label="Zoom Out", command=None, accelerator="Ctrl+Minus")
        view_menu.add_checkbutton(label="Status Bar", onvalue=1, offvalue=0)
        menu_bar.add_cascade(label="View", menu=view_menu)

        # Help Menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_cascade(label="View Help", command=None)
        help_menu.add_cascade(label="Send Feedback", command=None)
        help_menu.add_separator()
        help_menu.add_cascade(label="About Notepad", command=None)
        menu_bar.add_cascade(label="Help", menu=help_menu)


def main():
    root = Tk()
    app = Notepad()
    root.mainloop()


if __name__ == '__main__':
    main()
