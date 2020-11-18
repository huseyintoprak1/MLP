from tkinter import *

root = Tk()

def MyClick():
    MyLabel = Label(root, text="i clicked a button!", fg= "red")
    MyLabel.pack()        

myButton = Button(root, text = "buton", command = MyClick, fg = "blue", bg = "yellow")

myButton.pack()

root.mainloop()