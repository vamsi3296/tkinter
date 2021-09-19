from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Message')
root.iconbitmap('./Images/canvas.ico')
root.geometry("400x200")

def graph():
	house_prices = np.random.normal(200000, 25000, 5000)

	
root.mainloop()