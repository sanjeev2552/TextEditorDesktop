from tkinter import *
from tkinter.ttk import *

from constants import *

FONT = 'Consolas'
SIZE = '11'
STYLE = 'Regular'


class LabeledCombobox(Frame):
    def __init__(self, master=None, **kw):
        Frame.__init__(self, master)
        self.__label = Label(self, text=kw['text'])
        self.__combo = Combobox(self,
                                values=kw['values'],
                                textvariable=kw['textvariable'],
                                state='readonly',
                                width=kw['width'],
                                height=6)

        self.__combo.current(kw['index'])
        self.__label.grid(row=kw['row'], column=kw['column'], sticky=W)
        self.__combo.grid(row=kw['row'] + 1, column=kw['column'])

        self.grid(row=kw['row'], column=kw['column'])

        self.__combo.bind("<<ComboboxSelected>>", lambda e: kw['callback_func']
                          ())
        self.configure(padding=(12, 12, 0, 0))


class FontChooser:
    def __init__(self, master=None, **kw):
        self.__fontWindow = Toplevel(master)
        self.__fontWindow.title("Font")
        self.__fontWindow.geometry('425x430+300+150')
        self.__fontWindow.resizable(0, 0)

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

        self.__lc1 = LabeledCombobox(master=self.__fontWindow,
                                     text='Font:',
                                     values=self.__fontFamilies,
                                     textvariable=self.__fontVar,
                                     width=26,
                                     index=self.__fontFamilies.index(FONT),
                                     row=0,
                                     column=0,
                                     callback_func=self.changeSampleTextStyle)

        self.__lc2 = LabeledCombobox(master=self.__fontWindow,
                                     text='Font Style:',
                                     values=FONT_STYLES,
                                     textvariable=self.__styleVar,
                                     width=18,
                                     index=FONT_STYLES.index(STYLE),
                                     row=0,
                                     column=1,
                                     callback_func=self.changeSampleTextStyle)

        self.__lc3 = LabeledCombobox(master=self.__fontWindow,
                                     text='Size:',
                                     values=FONT_SIZES,
                                     textvariable=self.__sizeVar,
                                     width=7,
                                     index=FONT_SIZES.index(SIZE),
                                     row=0,
                                     column=2,
                                     callback_func=self.changeSampleTextStyle)

        self.__sample = LabelFrame(self.__fontWindow,
                                   text='Sample',
                                   height=80,
                                   width=220,
                                   borderwidth=2)
        self.__sample.grid(row=2,
                           column=1,
                           columnspan=200,
                           sticky='w',
                           pady=120,
                           ipadx=2,
                           ipady=2)

        self.__label = Label(self.__sample, text="AaBbYyZz")
        self.__label.place(relx=.5, rely=.5, anchor=CENTER)

        self.__btnok = Button(self.__fontWindow,
                              text='OK',
                              command=lambda: kw['callback_func']
                              (self.applyStyles()))
        self.__btnok.grid(row=3, column=1, sticky=E, padx=10)

        self.__btncancel = Button(self.__fontWindow,
                                  text='Cancel',
                                  command=self.__fontWindow.destroy)
        self.__btncancel.grid(row=3, column=2, sticky=E)

    def changeSampleTextStyle(self):
        styleVar = self.__styleVar.get()

        if self.__styleVar.get() == 'Regular':
            styleVar = ''

        self.__label.config(font=(self.__fontVar.get(), self.__sizeVar.get(),
                                  styleVar.lower()))

    def applyStyles(self):
        DEFAULT_FONT = self.__fontVar.get()
        DEFAULT_STYLE = self.__styleVar.get()
        DEFAULT_SIZE = self.__sizeVar.get()

        self.__fontWindow.destroy()
        return (self.__fontVar.get(), self.__sizeVar.get(),
                self.__styleVar.get())
