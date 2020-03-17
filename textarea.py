from tkinter import *
from tkinter.ttk import *

DEFAULT_FONT = ('COnsolas', 11, '')


class TextArea:
    def __init__(self, master=None, **kw):
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
            font=DEFAULT_FONT,
            xscrollcommand=self.__xScroll.set,
            yscrollcommand=self.__yScroll.set,
            maxundo=2000,
            undo=TRUE)
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

    def setNewFont(self, newFont):
        newSize = newFont[1]
        newStyle = newFont[2].lower()
        newFont = newFont[0]

        if newStyle == 'regular':
            newStyle = ''
        self.__textArea.config(font=(newFont, int(newSize), newStyle))
