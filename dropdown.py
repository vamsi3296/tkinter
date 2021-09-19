from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Message')
root.iconbitmap('./Images/canvas.ico')
root.geometry("500x500")

# Drop down boxes

def show():
	myLabel = Label(root, text=clicked.get()).pack()


options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

clicked = StringVar()
clicked.set(option[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()