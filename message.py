from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message')
root.iconbitmap('./Images/canvas.ico')

#	Showinfo, showwarning, showerror, askquestion, asktocancel, askyesno

def popup():
	response = messagebox.askyesno("Warning!!!", "Ignore me")
	# Label(root, text=response).pack()
	if response == 1:
		Label(root, text="You clicked Yes").pack()
	else:
		Label(root, text="You clicked No!!").pack()

Button(root, text="Popup", command=popup).pack()

mainloop()