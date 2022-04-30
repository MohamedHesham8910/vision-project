from tkinter import *
from milestone1 import *

####################################################################
#GUI

main = Tk()
main.geometry("500x500")

var = StringVar()
l = Label(main,textvariable=var)
var.set("Choose Type of Augmentation to Perform")
l.place(relx=0.5, rely=0.5, anchor=N)

resizing = Button(main, text="Resize", command= lambda: resize(image))
resizing.place(relx=0.1, rely=0.6, anchor=N)

trans = Button(main, text="Translate", command= lambda: translate(image))
trans.place(relx=0.3, rely=0.6, anchor=N)

rotation = Button(main, text="Rotation", command= lambda: rotate(image))
rotation.place(relx=0.5, rely=0.6, anchor=N)

flipping = Button(main, text="Flip", command= lambda: flip(image))
flipping.place(relx=0.7, rely=0.6, anchor=N)

zooming = Button(main, text="Zoom", command= lambda: zoom(image))
zooming.place(relx=0.9, rely=0.6, anchor=N)


main.mainloop()