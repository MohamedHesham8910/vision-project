from importlib.resources import path
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from milestone1 import *

####################################################################
#GUI

main = Tk()
main.title('Milestone 1')
main.geometry("500x300")

def open_file():
    global dir
    global imgdir
    image = filedialog.askopenfile(mode='r', filetypes=[('Image Files', ['.jpeg', '.jpg', '.png', '.gif', '.tiff', '.tif', '.bmp'])])
    imgdir = os.path.dirname(image.name)
    dir = image.name

img = Label(main,text="Please Choose an Image")

img.place(relx=0.5,rely=0.1,anchor=N)

browse = Button(main, text="Browse", command=open_file)

browse.place(relx=0.5,rely=0.2,anchor=N)

var = StringVar()
l = Label(main,textvariable=var)
var.set("Choose Type of Augmentation to Perform")
l.place(relx=0.5, rely=0.4, anchor=N)

resizing = Button(main, text="Resize", command= lambda: resize(dir,imgdir))
resizing.place(relx=0.1, rely=0.55, anchor=N)

trans = Button(main, text="Translate", command= lambda: translate(dir,imgdir))
trans.place(relx=0.3, rely=0.55, anchor=N)

rotation = Button(main, text="Rotation", command= lambda: rotate(dir,imgdir))
rotation.place(relx=0.5, rely=0.55, anchor=N)

flipping = Button(main, text="Flip", command= lambda: flip(dir,imgdir))
flipping.place(relx=0.7, rely=0.55, anchor=N)

zooming = Button(main, text="Zoom", command= lambda: zoom(dir,imgdir))
zooming.place(relx=0.9, rely=0.55, anchor=N)


main.mainloop()