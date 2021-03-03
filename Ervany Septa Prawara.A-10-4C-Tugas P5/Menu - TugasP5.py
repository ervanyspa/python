from tkinter import *
   
mainform = Tk()
mainform.geometry('500x200')
mainform['background']="#bbdfc8"
mainform.wm_title("Menu")

menubar = Menu(mainform)
filemenu = Menu(menubar, tearoff=0)
filemenu['activebackground']="#75cfb8"
filemenu['activeborderwidth']=2
filemenu['activeforeground']="blue"
filemenu['bg']="#f7f7e8"
filemenu['bd']=10
filemenu['font']="calibri 10"
filemenu['fg']="#ec4646"
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=mainform.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Select All")
menubar.add_cascade(label="Edit", menu=editmenu)

mainform.config(menu=menubar)
mainform.mainloop()