from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Message')
root.iconbitmap('./Images/canvas.ico')




def open():
	global my_image
	root.filename = filedialog.askopenfilename(
	initialdir="./Images", 
	title="Select a file", 
	filetypes=(("jpg files", "*.jpg"), ("All files", "*"))
	)
	my_label = Label(root, text=root.filename).pack()
	my_image = ImageTk.PhotoImage(Image.open(root.filename).resize((600,320), Image.ANTIALIAS))
	my_img_label = Label(root, image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()