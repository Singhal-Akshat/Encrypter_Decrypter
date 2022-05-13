from encrypt import main_encrypt
from decrypt import main_decrypt
from tkinter import *
from Gui_folder import filewindow


def en():
    root.destroy()
    path  = f.getname()
    
    main_encrypt(path)


def de():
    root.destroy()
    path = f.getname()
    main_decrypt(path)


root = Tk()
root.title("Choose Encypt or decrypt")
f = filewindow()
button1 = Button(text="Encrypt",command = en)
button1.pack()
button2 = Button(text = "Decrypt",command = de)
button2.pack()
root.mainloop()