from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title('Drug Prescription System')
root.geometry('1500x800+50+10')
root.configure(bg='#000626')
root.resizable(False, False)

img = PhotoImage(file='medbg.png')
Label(root, image=img, bg='blue').place(x=0, y=0)

root.mainloop()