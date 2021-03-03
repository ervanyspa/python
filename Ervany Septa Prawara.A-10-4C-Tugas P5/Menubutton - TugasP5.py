from tkinter import *

mainform = Tk()
mainform.geometry('500x200')
mainform.wm_title("Menubutton")
mainform['background']="#bbdfc8"

lbl = Label(mainform)
lbl['text']="Pilih Bahasa Pemrograman"
lbl.pack()

mbt = Menubutton(mainform)
mbt['text']="Bahasa Pemrograman"
mbt['activebackground']="#75cfb8"
mbt['activeforeground']="red"
mbt['bg'] = "#fde8cd"
mbt['bd']=2
mbt['cursor']="star"
mbt['direction']="right"
mbt['fg']="navy"
mbt['height']=2
mbt.pack()

mbt.menu = Menu(mbt, tearoff=0)
mbt['menu'] = mbt.menu
mbt.menu.add_checkbutton(label="Python")
mbt.menu.add_checkbutton(label="Java")
mbt.menu.add_checkbutton(label="C++")


mainform.mainloop()