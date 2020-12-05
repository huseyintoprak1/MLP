from tkinter import *
from PIL import ImageTk, Image
from guizero import *
import pandas as pd 

root = Tk()
root.iconbitmap('C:\\Users\\Hüseyin\\Desktop\\MLP\\ytulogo.ico')
root.title('MLP')
root.geometry("500x500")
root.resizable(0,0)



my_menu = Menu(root)
root.config(menu=my_menu)

def our_command():
    pass


#File menü
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label = "File", menu=file_menu)
file_menu.add_command(label="New", command = our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command = root.quit)

#edit menü
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label= "Edit", menu= edit_menu)
edit_menu.add_command(label="Cut", command = our_command)
edit_menu.add_command(label="Copy", command = our_command)



root.mainloop()