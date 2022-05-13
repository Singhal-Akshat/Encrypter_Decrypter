
from tkinter import filedialog
from tkinter import *

class filewindow:
    path=""
    def folder(self):
        foldername= filedialog.askdirectory()
        self.flag = 1
        self.close()
        self.path+=foldername
        

    def filename(self):
        filename = filedialog.askopenfilename(title="Filename",filetypes = (("image files","*.png, *.jpg"),("all files","*.*")))
        self.flag = 1
        self.close()
        self.path+=filename
        
        

    def getname(self):
        global root
        root  = Tk()
        root.title("Folder")
        button = Button(text="Browse Folder",command = self.folder)
        button.pack()
        button2 = Button(text="Browse file",command =  self.filename)
        button2.pack()
        root.mainloop()
        return self.path


    def close(self):
        root.destroy()