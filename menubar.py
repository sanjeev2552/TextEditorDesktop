from tkinter import *
from tkinter.ttk import *


class MenuBar:
    def __init__(self, master=None, **kw):
        self.__master = master
        self.__menubar = Menu(self.__master)
        self.__selectAll = kw['selectAll']

        self.__File = Menu(self.__menubar, tearoff=0, name="file")
        self.__Edit = Menu(self.__menubar, tearoff=0, name="edit")
        self.__Format = Menu(self.__menubar, tearoff=0, name="format")
        self.__Help = Menu(self.__menubar, tearoff=0, name="help")

        self.__menubar.add_cascade(label="File", menu=self.__File, underline=0)
        self.__menubar.add_cascade(label="Edit", menu=self.__Edit, underline=0)
        self.__menubar.add_cascade(label="Format",
                                   menu=self.__Format,
                                   underline=1)
        self.__menubar.add_cascade(label="Help", menu=self.__Help, underline=0)

        # This specifies the submenu of FILE option
        self.__File.add_command(label="New",
                                accelerator="Ctrl+N",
                                underline=0,
                                command=kw['newFile'])
        self.__File.add_command(label="Open...",
                                accelerator="Ctrl+O",
                                underline=0,
                                command=kw['openFile'])
        self.__File.add_command(label="Save",
                                accelerator="Ctrl+S",
                                underline=0,
                                command=kw['save'])
        self.__File.add_command(label="Save As...",
                                accelerator="Ctrl+Shift+S",
                                underline=5,
                                command=kw['saveAs'])
        self.__File.add_separator()
        self.__File.add_command(label="Exit",
                                underline=1,
                                command=kw['exitApplication'])

        # This specifies the submenu of EDIT option
        self.__Edit.add_command(label="Undo",
                                accelerator="Ctrl+Z",
                                underline=0)
        self.__Edit.add_separator()
        self.__Edit.add_command(label="Cut", accelerator="Ctrl+X", underline=2)
        self.__Edit.add_command(label="Copy",
                                accelerator="Ctrl+C",
                                underline=0)
        self.__Edit.add_command(label="Paste",
                                accelerator="Ctrl+V",
                                underline=0)
        self.__Edit.add_separator()
        self.__Edit.add_command(label="Replace",
                                accelerator="Ctrl+H",
                                underline=0)
        self.__Edit.add_separator()
        self.__Edit.add_command(label="Select All",
                                accelerator="Ctrl+A",
                                underline=7,
                                command=kw['selectAll'])
        self.__Edit.add_command(label="Time/Date",
                                accelerator="F5",
                                underline=5,
                                command=kw['pushDateAndTime'])

        # This specifies the submenu of FORMAT option
        self.__checkVariable = BooleanVar(self.__Format, value=FALSE)
        self.__Format.add_checkbutton(label="Word Wrap",
                                      underline=0,
                                      variable=self.__checkVariable,
                                      command=lambda: kw['setWrap']
                                      (self, kw['textArea']))
        self.__Format.add_command(label="Font...",
                                  underline=0,
                                  command=lambda: kw['fontChooser']
                                  (self.__master))

        self.__master.config(menu=self.__menubar)

    def getEditMenu(self):
        return self.__Edit

    def getCheckValue(self):
        return self.__checkVariable.get()

    # Function to show CONTEXT MENU
    def showContextMenu(self, event):
        popupMenu = Menu(self.__master, tearoff=0)
        popupMenu.add_command(label="Undo")
        popupMenu.add_separator()
        popupMenu.add_command(label="Cut")
        popupMenu.add_command(label="Copy")
        popupMenu.add_command(label="Paste")
        popupMenu.add_command(label="Select All", command=self.__selectAll)

        popupMenu.tk_popup(event.x_root, event.y_root)