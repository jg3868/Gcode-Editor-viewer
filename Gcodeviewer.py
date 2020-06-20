import tkinter, tkinter.filedialog, tkinter.messagebox
import os

filetype = [("", "*.gcode")]
dirpath = os.path.abspath(os.path.dirname(__file__))
filepath = tkinter.filedialog.askopenfilename(filetypes = filetype, initialdir = dirpath)
g_line = []

with open(filepath) as f:
    for temp_line in f:
        print(temp_line)
        g_line.append(temp_line.strip())
# print(g_line)

for l in g_line:
    print("No:",l,"/ code:",g_line[l])