from tkinter import *

mainform = Tk()
mainform.wm_title("Scale")
mainform.geometry('500x200')
mainform['background']="#bbdfc8"

lbl = Label(mainform)
lbl['text'] = "Scale    :"
lbl['bg']="#bbdfc8"
lbl.grid(row=0 , column=0)

def hasil():
    getvlm = "Volume : " + str(vlm.get())
    lbl2.config(text=getvlm)

scl = Scale(mainform)
vlm = StringVar()
scl['activebackground']="#161d6f"
scl['bg']="#ffd56b"
scl['bd']=5
scl['cursor']="dot"
scl['digits']=4
scl['font']="calibri 12"
scl['fg']="#161d6f"
scl['from_']=10
scl['highlightbackground']="#161d6f"
scl['label']="Volume"
scl['length']=200
scl['orient']="horizontal"
scl['relief']="groove"
scl['resolution']=5
scl['showvalue']=1
scl['sliderlength']=20
scl['tickinterval']=30
scl['troughcolor']="#aee1e1"
scl['width']=20
scl['variable']=vlm
scl.grid(row=0, column=1)

btn = Button(mainform)
btn['text'] = "Hasil Volume"
btn['command']=hasil
btn.grid(row=0, column=2)

lbl2 = Label(mainform)
lbl2['bg']="#bbdfc8"
lbl2.grid(row=1, column=0)


mainform.mainloop()