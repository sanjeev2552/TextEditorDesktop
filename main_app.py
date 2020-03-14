# Imports
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from datetime import date, datetime

# Constants
DEFAULT_TITLE = "Untitled - TextEditor"
DEFAULT_UNSAVED_TITLE = "*Untitled - TextEditor"
TITLE = DEFAULT_TITLE
PATH_OF_CURRENTLY_OPENED_FILE = None


# Function to demonstrate NEW command
def newFile():
    global TITLE
    textObject = textArea.getTextObject()
    value = textObject.get("1.0", "end-1c")

    if value and TITLE == DEFAULT_TITLE:
        answer = askyesnocancel("TextEditor",
                                "Do you want to save changes to Untitled?")
        if not answer:
            textObject.delete("1.0", "end-1c")
        else:
            saveAs()
    textObject.delete("1.0", "end-1c")
    TITLE = DEFAULT_TITLE
    master.title(TITLE)


# Function to demonstrate OPEN command
def openFile():
    global PATH_OF_CURRENTLY_OPENED_FILE
    filename = askopenfile(mode='r',
                           filetypes=[("Text Document (*.txt)", "*.txt"),
                                      ("All Files", "*.*")])
    if filename is not None:
        global TITLE
        PATH_OF_CURRENTLY_OPENED_FILE = filename
        parts = PATH_OF_CURRENTLY_OPENED_FILE.name.split('/')[-1]
        parts = parts.split('.')[0]
        TITLE = parts
        master.title(TITLE)

        content = PATH_OF_CURRENTLY_OPENED_FILE.read()
        textObject = textArea.getTextObject()
        textObject.delete("1.0", END)
        textObject.insert(END, content)


# Function to demonstrate SAVE command
def save():
    if TITLE == DEFAULT_TITLE:
        saveAs()
    else:
        textObject = textArea.getTextObject()
        value = textObject.get("1.0", "end-1c")
        currentFile = open(PATH_OF_CURRENTLY_OPENED_FILE.name, 'w')
        currentFile.write(value)


# Function to demonstrate SAVEAS command
def saveAs():
    textObject = textArea.getTextObject()
    filesFormat = [
        ("Text Document (*.txt)", "*.txt"),
        ("All Files"),
    ]
    fileToSave = asksaveasfile(filetypes=filesFormat,
                               defaultextension=filesFormat)

    value = textObject.get("1.0", "end-1c")
    if fileToSave:
        fileToSave.write(value)


# Function to demonstrate EXIT command
def exitApplication():
    textObject = textArea.getTextObject()
    value = textObject.get("1.0", "end-1c")

    if value:
        answer = askyesnocancel("TextEditor",
                                "Do you want to save changes to Untitled?")
        if answer:
            saveAs()
    quit()


def undo():
    pass


def cut():
    pass


def copy():
    pass


def paste():
    pass


def replace():
    pass


def selectAll():
    pass


def pushDateAndTime():
    today = date.today().strftime('%d-%m-%Y')
    time = datetime.now().strftime("%H:%M %p")
    print(time, today)


def setWrap(menuBar, textArea):
    value = menuBar.getCheckValue()
    textArea.setWrap(value)


class MenuBar:
    def __init__(self, master=None, textArea=None):
        self.__master = master
        self.__menubar = Menu(self.__master)

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
                                command=newFile)
        self.__File.add_command(label="Open...",
                                accelerator="Ctrl+O",
                                underline=0,
                                command=openFile)
        self.__File.add_command(label="Save",
                                accelerator="Ctrl+S",
                                underline=0,
                                command=save)
        self.__File.add_command(label="Save As...",
                                accelerator="Ctrl+Shift+S",
                                underline=5,
                                command=saveAs)
        self.__File.add_separator()
        self.__File.add_command(label="Exit",
                                underline=1,
                                command=exitApplication)

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
                                underline=7)
        self.__Edit.add_command(label="Time/Date",
                                accelerator="F5",
                                underline=5,
                                command=pushDateAndTime)

        # This specifies the submenu of FORMAT option
        self.__checkVariable = BooleanVar(self.__Format, value=FALSE)
        self.__Format.add_checkbutton(label="Word Wrap",
                                      underline=0,
                                      variable=self.__checkVariable,
                                      command=lambda: setWrap(self, textArea))
        self.__Format.add_command(label="Font...",
                                  underline=0,
                                  command=lambda: FontChooser())

        self.__master.config(menu=self.__menubar)

    def getEditMenu(self):
        return self.__Edit

    def getCheckValue(self):
        return self.__checkVariable.get()


class TextArea:
    def __init__(self, master=None):
        self.__isWrap = NONE
        self.__master = master
        self.__xScroll = Scrollbar(self.__master, orient=HORIZONTAL)
        self.__yScroll = Scrollbar(self.__master)
        self.__xScroll.pack(side=BOTTOM, fill='x')
        self.__yScroll.pack(side=RIGHT, fill='y')

        self.__textArea = Text(
            master,
            borderwidth=0,
            highlightthickness=0,  # for macOS
            wrap=self.__isWrap,
            font=('consolas', 11),
            xscrollcommand=self.__xScroll.set,
            yscrollcommand=self.__yScroll.set)
        self.__textArea.pack(expand=TRUE, fill=BOTH)

        self.__xScroll.config(command=self.__textArea.xview)
        self.__yScroll.config(command=self.__textArea.yview)
        self.__textArea.focus()

    def getTextObject(self):
        return self.__textArea

    def setWrap(self, changeWrap):
        if changeWrap:
            self.__isWrap = WORD
        else:
            self.__isWrap = NONE
        self.__textArea.configure(wrap=self.__isWrap)


class FontChooser:
    def __init__(self, master=None):
        self.__fontWindow = Toplevel(master)
        self.__fontWindow.title("Font")
        self.__fontWindow.geometry('500x500+300+150')


# Function to show CONTEXT MENU
def showContextMenu(event):
    popupMenu = Menu(master, tearoff=0)
    popupMenu.add_command(label="Undo")
    popupMenu.add_separator()
    popupMenu.add_command(label="Cut")
    popupMenu.add_command(label="Copy")
    popupMenu.add_command(label="Paste")
    popupMenu.add_command(label="Select All")

    popupMenu.post(event.x_root, event.y_root)


if __name__ == "__main__":
    master = Tk()
    master.title(DEFAULT_TITLE)
    master.geometry("500x300+200+100")

    textArea = TextArea(master)
    menuBar = MenuBar(master, textArea)

    # key-bindings / events
    master.bind("<Control-n>", lambda e: newFile())
    master.bind("<Control-N>", lambda e: newFile())
    master.bind("<Control-o>", lambda e: openFile())
    master.bind("<Control-O>", lambda e: openFile())
    master.bind("<Control-s>", lambda e: save())
    master.bind("<Control-S>", lambda e: save())
    master.bind("<Control-Shift-S>", lambda e: saveAs())
    master.bind("<Control-q>", lambda e: exitApplication())
    master.bind("<Control-Q>", lambda e: exitApplication())

    # If platform is macOS
    if master.tk.call('tk', 'windowingsystem') == 'aqua':
        master.bind("<Button-2>", showContextMenu)

    # If platform is Windows
    else:
        master.bind("<Button-3>", showContextMenu)

    master.protocol("WM_DELETE_WINDOW", exitApplication)

    mainloop()
