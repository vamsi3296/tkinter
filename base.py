from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message')
root.iconbitmap('./Images/canvas.ico')

def open():
	global my_img
	top = Toplevel()
	top.title("Picture")
	top.iconbitmap('./Images/canvas.ico')

	my_img = ImageTk.PhotoImage(Image.open("./Images/my_img1.jpg").resize((600, 340), Image.ANTIALIAS))
	my_label = Label(top, image=my_img).pack()

	btn2 = Button(top, text="Close", command=top.destroy).pack()


btn = Button(root, text="Open Picture", command=open).pack()

# lbl = Label(top, text="Hello World").pack()

mainloop()