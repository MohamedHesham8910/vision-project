from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from milestone1 import *

####################################################################
#GUI

main = Tk()
main.geometry("500x300")

def open_file():
    global dir
    image = filedialog.askopenfile(mode='r', filetypes=[('Image Files', ['.jpeg', '.jpg', '.png', '.gif', '.tiff', '.tif', '.bmp'])])
    dir = image.name

img = Label(main,text="Please Choose an Image")

img.place(relx=0.5,rely=0.1,anchor=N)

browse = Button(main, text="Browse", command=open_file)

browse.place(relx=0.5,rely=0.2,anchor=N)

var = StringVar()
l = Label(main,textvariable=var)
var.set("Choose Type of Augmentation to Perform")
l.place(relx=0.5, rely=0.4, anchor=N)

resizing = Button(main, text="Resize", command= lambda: resize(dir))
resizing.place(relx=0.1, rely=0.55, anchor=N)

trans = Button(main, text="Translate", command= lambda: translate(dir))
trans.place(relx=0.3, rely=0.55, anchor=N)

rotation = Button(main, text="Rotation", command= lambda: rotate(dir))
rotation.place(relx=0.5, rely=0.55, anchor=N)

flipping = Button(main, text="Flip", command= lambda: flip(dir))
flipping.place(relx=0.7, rely=0.55, anchor=N)

zooming = Button(main, text="Zoom", command= lambda: zoom(dir))
zooming.place(relx=0.9, rely=0.55, anchor=N)


main.mainloop()