import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import cv2 as cv2
import numpy
from PIL import Image
from PIL import ImageTk
import os
from tkinter import filedialog
import tensorflow as tf
from tkinter.font import Font


class Program:
    def __init__(self, window):

        self.text_ = 'Welcome to our Brain Tumor Segmentation Tool. We are dedicated to transforming brain tumor ' \
                     'diagnosis. Our cutting-edge technology and deep learning algorithms provide accurate and rapid ' \
                     'segmentation of brain tumors from MRI scans. Join us in the quest for early detection and ' \
                     'effective treatment. SCAN YOUR MRI REPORTS NOW.'

        self.window = window
        self.window.geometry("800x500")
        self.window.title("BRAIN TUMOR SEGMENTATION")
        self.window.config(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.custom_font = Font(family="Helvetica", size=34, weight="bold")
        self.custom_font_2 = Font(family="Helvetica", size=22, weight="bold")
        self.custom_font3 = Font(family="Helvetica", size=8, weight="bold")

        # LABEL ---> THE BLACK LABEL -----------------------------------
        self.label = Label(self.window, bg='#141414', width=115, height=15)
        self.label.grid(row=0, column=0, columnspan=2)
        self.label_title = Label(self.label, text='Brain Tumor Segmentation Tool', fg='white', width=100,
                                 height=5, bg='#141414', anchor='w', font=self.custom_font, justify='left')
        self.label_title.place(x=10, y=10)

        # LABEL ---> CONTENT AND BUTTON LABEL -----------------------------------
        self.content_label = Label(self.window, bg='#FFFFFF', width=115, height=18, anchor='center', justify='center')
        self.content_label_1 = Label(self.content_label, text='BRAIN TUMOR',font=self.custom_font_2, fg='#141414',
                                    bg='#FFFFFF')
        self.content_label.grid(row=1,column=0)
        self.content_label_1.place(x=280, y=0)

        self.about_label = Label(self.content_label,  text=self.text_, wraplength=600, width=70,font=('Helvetica', 12),
                                 height=5, justify="left", anchor="center", bg='#FFFFFF')
        self.about_label.place(x=85, y=40)

        self.buttons_label = Label(self.content_label, width=75,height=3, bg='#FFFFFF')
        self.buttons_label.place(x=160, y=155)

        self.UPLOAD_BUTTON = Button(self.buttons_label, text="UPLOAD MRI/ X-RAYS", width=30, height=2, fg='white',
                                    bg='#4ca3d9', borderwidth=0,
                                    highlightbackground=self.buttons_label.cget('background'), font=self.custom_font3)
        self.SCAN_BUTTON = Button(self.buttons_label, text="SCAN MRI/ X-RAYS", width=30, height=2, fg='white',
                                  bg='#4ca3d9', borderwidth=0,
                                  highlightbackground=self.buttons_label.cget('background'), font=self.custom_font3)

        self.UPLOAD_BUTTON.grid(row=0, column=0,  padx=(0, 10))
        self.SCAN_BUTTON.grid(row=0, column=1,  padx=(10, 0))


def main():
    window = Tk()
    app = Program(window)
    window.mainloop()


if __name__ == "__main__":
    main()
