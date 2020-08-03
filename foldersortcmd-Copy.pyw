import os
import tkinter
from tkinter import filedialog, messagebox

# Command rundown
#foldsorte =

#path = os.getcwd()
#1  Detect every letter or number

#os.mkdir(path)
#2 make a directory for each counted on document by initial index element
# Sample directory styles
# ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',)

app = tkinter.Tk()
02
app.geometry('500x450')

app.title("FoldSorte")

label = tkinter.Label(app, text = "Hello. Choose a folder to organize")
label.pack(side="top", padx = 5, pady = 5)

#command=
btn = tkinter.Button(app,
	text="Sort")
btn.pack()

app.mainloop()

#3 move each file into each folder

# Folder_open = 
# Folder_sort =

# Error section
# raise exception if any folder is already present
# raise exception if there is no file in directory
# raise exception if directory selected is in root drive, C/ drive or anything similar