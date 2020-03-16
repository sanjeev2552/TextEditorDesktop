from tkinter import *
from tkinter.ttk import *

from constants import *


class LabeledCombobox(Frame):
    def __init__(self,
                 master=None,
                 text=None,
                 values=None,
                 textvariable=None,
                 width=None,
                 row=None,
                 column=None,
                 index=None,
                 callback_func=None):
        Frame.__init__(self, master)
        self.__label = Label(self, text=text)
        self.__combo = Combobox(self,
                                values=values,
                                textvariable=textvariable,
                                state='readonly',
                                width=width)
        print(index)
        self.__combo.current(index)
        self.__label.grid(row=row, column=column, sticky=W)
        self.__combo.grid(row=row + 1, column=column)

        self.grid(row=row, column=column)

        self.__combo.bind("<<ComboboxSelected>>",
                          lambda e: print(textvariable.get()))
        self.configure(padding=(12, 12, 0, 0))


class FontChooser:
    def __init__(self, master=None, **kw):
        self.__fontWindow = Toplevel(master)
        self.__fontWindow.title("Font")
        self.__fontWindow.geometry('425x440+300+150')

        self.__fontFamilies = font.families(self.__fontWindow)

        # only for windows
        if self.__fontWindow._windowingsystem == WINDOWS_WINDOWING_SYSTEM:
            self.__filteredFontFamilies = [
                i for i in filter(lambda x: x[0] != '@', self.__fontFamilies)
            ]

        self.__fontFamilies = self.__filteredFontFamilies
        self.__fontFamilies.sort()
        self.__fontVar = StringVar()
        self.__styleVar = StringVar()
        self.__sizeVar = StringVar()

        self.__lc1 = LabeledCombobox(self.__fontWindow, 'Font:',
                                     self.__fontFamilies, self.__fontVar,
                                     26, 0, 0,
                                     self.__fontFamilies.index('Consolas'))

        self.__lc2 = LabeledCombobox(self.__fontWindow, 'Font Style:',
                                     FONT_STYLES, self.__styleVar, 18, 0, 1,
                                     FONT_STYLES.index('Regular'))

        self.__lc3 = LabeledCombobox(self.__fontWindow, 'Size:', FONT_SIZES,
                                     self.__sizeVar, 7, 0, 2,
                                     FONT_SIZES.index('11'))
