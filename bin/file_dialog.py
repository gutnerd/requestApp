#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd


class FileDialogClass:
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()

        self.open_file_manager = tk.Button(text='Click to Open File', command=self.callback)
        self.open_file_manager.pack()



    def callback(self):
        self.name = fd.askopenfilename()
        print(self.name)

        errmsg = 'Error!'
        # tk.Button(text='Click to Open File',
        #           command=callback).pack()


class AnotherFile:
    def __init__(self, master):
        self.greet_button = Button(master, text='Click to Open File', command=self.callback)
        self.greet_button.grid(row=0, column=1, pady=15, padx=140)


    def greet(self):
        print("Greetings!")

    def callback(self):
        self.name = fd.askopenfilename()
        print(self.name)