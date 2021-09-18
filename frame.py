from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Frame')
root.iconbitmap('./Images/canvas.ico')

frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't Click Here!")
b1 = Button(frame, text="B2")
b.grid(row=0, column=1)
b1.grid(row=1, column=0)


root.mainloop()