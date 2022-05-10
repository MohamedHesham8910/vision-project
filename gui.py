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
    image = filedialog.askopenfile(mode='r', filetypes=[('Image Files', ['.jpeg', '.jpg', '.png', '.gif', '.tiff', '.tif', '.bmp', 'svg'])])
    imgdir = os.path.dirname(image.name)
    dir = image.name

img = Label(main,text="Choose an Image", font="Times 15 bold")

img.place(relx=0.5,rely=0.1,anchor=N)

browse = Button(main, text="Browse",font="Times 12",bd= 3,command=open_file)

browse.place(relx=0.5,rely=0.25,anchor=N)

l = Label(main,text="Choose Type of Augmentation to Perform",font="Times 15 bold")
l.place(relx=0.5, rely=0.45, anchor=N)

resizing = Button(main, text="Resize",font="Times 12",bd= 3, command= lambda: resize(dir,imgdir))
resizing.place(relx=0.3, rely=0.6, anchor=N)

trans = Button(main, text="Translate",font="Times 12",bd= 3, command= lambda: translate(dir,imgdir))
trans.place(relx=0.5, rely=0.6, anchor=N)

rotation = Button(main, text="Rotation",font="Times 12",bd= 3, command= lambda: rotate(dir,imgdir))
rotation.place(relx=0.1, rely=0.6, anchor=N)

flipping = Button(main, text="Flip",font="Times 12",bd= 3, command= lambda: flip(dir,imgdir))
flipping.place(relx=0.7, rely=0.6, anchor=N)

zooming = Button(main, text="Zoom",font="Times 12",bd= 3, command= lambda: zoom(dir,imgdir))
zooming.place(relx=0.9, rely=0.6, anchor=N)


main.mainloop()