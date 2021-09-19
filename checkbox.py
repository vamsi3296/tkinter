from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Message')
root.iconbitmap('./Images/canvas.ico')
root.geometry("500x500")

def show():
	myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check the box", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

# myLabel = Label(root, text=var.get()).pack()

myButton = Button(root, text="Show Selection", command=show).pack()

mainloop()