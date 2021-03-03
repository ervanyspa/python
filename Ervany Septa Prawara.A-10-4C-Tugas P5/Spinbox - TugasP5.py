from tkinter import *

mainform = Tk()
mainform.wm_title("SpinBox")
mainform.geometry('500x200')
mainform['background']="#bbdfc8"

lbl = Label(mainform)
lbl['text'] = "SpinBox 1    :"
lbl['bg']="#bbdfc8"
lbl.grid(row=0, column=0)

spb = Spinbox(mainform)
spb['bg']="#aee1e1"
spb['bd']=5
spb['cursor']="star"
spb['fg']="red"
spb['font']="calibri 12 bold"
spb['format']="%02.0f"
spb['from']=0
spb['justify']="center"
spb['relief']="ridge"
spb['state']="readonly"
spb['to']=10
spb['width']=10
spb.grid(row=0, column=1)

mainform.mainloop()