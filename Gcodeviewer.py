import tkinter, tkinter.filedialog, tkinter.messagebox
import os

filetype = [("", "*.gcode")]
dirpath = os.path.abspath(os.path.dirname(__file__))
filepath = tkinter.filedialog.askopenfilename(filetypes = filetype, initialdir = dirpath)

f = open(filepath,'r', encoding="utf-8")
print(type(f))
print(f)

f.close