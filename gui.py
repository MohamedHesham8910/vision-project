from importlib.resources import path
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from milestone1 import *

####################################################################
#GUI

main = Tk()
main.title('Milestone 1')
main.geometry("500x400")

def open_file():
    global imgpath
    global imgdir
    image = filedialog.askopenfile(mode='r', filetypes=[('Image Files', ['.jpeg', '.jpg', '.png', '.gif', '.tiff', '.tif', '.bmp', 'svg'])])
    imgdir = os.path.dirname(image.name)
    imgpath = image.name

def enterNo():
    global num
    num = e.get()

img = Label(main,text="Choose an Image", font="Times 15 bold")

img.place(relx=0.5,rely=0.1,anchor=N)

browse = Button(main, text="Browse",font="Times 12",bd= 3,command=open_file)

browse.place(relx=0.5,rely=0.25,anchor=N)

e = Entry(main)
e.place(relx=0.3, rely=0.55, anchor=N)

no = Label(main,text="Enter Number of Modified Data to Generate",font="Times 15 bold")
no.place(relx=0.5, rely=0.4, anchor=N)

enter = Button(main, text="Enter",font="Times 10",bd= 3,command=enterNo)
enter.place(relx=0.5,rely=0.54,anchor=N)

l = Label(main,text="Choose Type of Augmentation to Perform",font="Times 15 bold")
l.place(relx=0.5, rely=0.65, anchor=N)

rotation = Button(main, text="Rotation",font="Times 12",bd= 3, command= lambda: rotate(imgpath,imgdir,num))
rotation.place(relx=0.1, rely=0.8, anchor=N)

resizing = Button(main, text="Resize",font="Times 12",bd= 3, command= lambda: resize(imgpath,imgdir,num))
resizing.place(relx=0.3, rely=0.8, anchor=N)

trans = Button(main, text="Translate",font="Times 12",bd= 3, command= lambda: translate(imgpath,imgdir,num))
trans.place(relx=0.5, rely=0.8, anchor=N)

flipping = Button(main, text="Flip",font="Times 12",bd= 3, command= lambda: flip(imgpath,imgdir,num))
flipping.place(relx=0.7, rely=0.8, anchor=N)

zooming = Button(main, text="Zoom",font="Times 12",bd= 3, command= lambda: zoom(imgpath,imgdir,num))
zooming.place(relx=0.9, rely=0.8, anchor=N)


main.mainloop()