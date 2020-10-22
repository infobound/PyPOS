#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#    Jul 03, 2020 03:50:49 PM EDT  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Forms.formTopLevel_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = formTopLevel (root)
    formTopLevel_support.init(root, top)
    root.mainloop()

w = None
def create_formTopLevel(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_formTopLevel(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = formTopLevel (w)
    formTopLevel_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_formTopLevel():
    global w
    w.destroy()
    w = None

class formTopLevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1024x768+0+0")
        top.minsize(124, 1)
        top.maxsize(1908, 1045)
        top.resizable(1, 1)
        top.title("PyPOS")
        top.configure(background="#d9d9d9")
        
        self.frameSubForm = tk.Frame(top)
        self.frameSubForm.place(relx=0.01, rely=0.13, relheight=0.866, relwidth=0.981)
        #self.frameSubForm.configure(relief='sunken')
        self.frameSubForm.configure(borderwidth="2")
        #self.frameSubForm.configure(relief="sunken")
        self.frameSubForm.configure(background="#d9d9d9")

        self.btnRegister = tk.Button(top)
        self.btnRegister.place(relx=0.01, rely=0.013, height=84, width=80)
        self.btnRegister.configure(activebackground="#ececec")
        self.btnRegister.configure(activeforeground="#000000")
        self.btnRegister.configure(background="#d9d9d9")
        self.btnRegister.configure(command=Forms.formTopLevel_support.ShowSubForm(self.frameSubForm, "formRegister"))
        self.btnRegister.configure(disabledforeground="#a3a3a3")
        self.btnRegister.configure(foreground="#000000")
        self.btnRegister.configure(highlightbackground="#d9d9d9")
        self.btnRegister.configure(highlightcolor="black")
        photo_location = "Resources/Register.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.btnRegister.configure(image=_img0)
        self.btnRegister.configure(pady="0")

        self.btnEditItems = tk.Button(top)
        self.btnEditItems.place(relx=0.088, rely=0.013, height=84, width=80)
        self.btnEditItems.configure(activebackground="#ececec")
        self.btnEditItems.configure(activeforeground="#000000")
        self.btnEditItems.configure(background="#d9d9d9")
        self.btnEditItems.configure(disabledforeground="#a3a3a3")
        self.btnEditItems.configure(foreground="#000000")
        self.btnEditItems.configure(highlightbackground="#d9d9d9")
        self.btnEditItems.configure(highlightcolor="black")
        self.btnEditItems.configure(pady="0")
        self.btnEditItems.configure(text='''Edit Items''')

        self.btnReports = tk.Button(top)
        self.btnReports.place(relx=0.166, rely=0.013, height=84, width=80)
        self.btnReports.configure(activebackground="#ececec")
        self.btnReports.configure(activeforeground="#000000")
        self.btnReports.configure(background="#d9d9d9")
        self.btnReports.configure(disabledforeground="#a3a3a3")
        self.btnReports.configure(foreground="#000000")
        self.btnReports.configure(highlightbackground="#d9d9d9")
        self.btnReports.configure(highlightcolor="black")
        self.btnReports.configure(pady="0")
        self.btnReports.configure(text='''Reports''')

        self.btnSettings = tk.Button(top)
        self.btnSettings.place(relx=0.244, rely=0.013, height=84, width=80)
        self.btnSettings.configure(activebackground="#ececec")
        self.btnSettings.configure(activeforeground="#000000")
        self.btnSettings.configure(background="#d9d9d9")
        self.btnSettings.configure(disabledforeground="#a3a3a3")
        self.btnSettings.configure(foreground="#000000")
        self.btnSettings.configure(highlightbackground="#d9d9d9")
        self.btnSettings.configure(highlightcolor="black")
        self.btnSettings.configure(pady="0")
        self.btnSettings.configure(text='''Settings''')

        self.btrnAdmin = tk.Button(top)
        self.btrnAdmin.place(relx=0.322, rely=0.013, height=84, width=80)
        self.btrnAdmin.configure(activebackground="#ececec")
        self.btrnAdmin.configure(activeforeground="#000000")
        self.btrnAdmin.configure(background="#d9d9d9")
        self.btrnAdmin.configure(disabledforeground="#a3a3a3")
        self.btrnAdmin.configure(foreground="#000000")
        self.btrnAdmin.configure(highlightbackground="#d9d9d9")
        self.btrnAdmin.configure(highlightcolor="black")
        self.btrnAdmin.configure(pady="0")
        self.btrnAdmin.configure(text='''Admin''')
        self.btrnAdmin.configure(command=lambda: top.destroy())
        

if __name__ == '__main__':
    vp_start_gui()





