# Imports
from tkinter import *
from tkinter.ttk import *
from tkinter import font
from tkinter.messagebox import *
from tkinter.filedialog import *
from datetime import date, datetime

from constants import *
from textarea import TextArea
from menubar import MenuBar
from font_chooser import FontChooser


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
    textObject = textArea.getTextObject()
    textObject.tag_add('all', '1.0', 'end-1c')
    textObject.tag_config('all', background='dodgerblue3', foreground='white')

    # textObject.delete('1.0', END)


def pushDateAndTime():
    today = date.today().strftime('%d-%m-%Y')
    time = datetime.now().strftime("%H:%M %p")
    print(time, today)


def setWrap(menuBar, textArea):
    value = menuBar.getCheckValue()
    textArea.setWrap(value)


def fontChooser(master):
    fontChooser = FontChooser(master)


if __name__ == "__main__":
    master = Tk()
    master.title(DEFAULT_TITLE)
    master.geometry("500x300+200+100")

    textArea = TextArea(master)
    menuBar = MenuBar(master,
                      textArea=textArea,
                      newFile=newFile,
                      openFile=openFile,
                      save=save,
                      saveAs=saveAs,
                      exitApplication=exitApplication,
                      selectAll=selectAll,
                      pushDateAndTime=pushDateAndTime,
                      setWrap=setWrap,
                      fontChooser=fontChooser)

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
    master.bind("<Control-a>", lambda e: selectAll())
    master.bind("<Control-A>", lambda e: selectAll())

    if master._windowingsystem == MAC_WINDOWING_SYSTEM:  # for macOS
        master.bind("<Button-2>", menuBar.showContextMenu)
    else:  # for windows and unix
        master.bind("<Button-3>", menuBar.showContextMenu)

    master.protocol("WM_DELETE_WINDOW", exitApplication)

    mainloop()
