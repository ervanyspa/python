from tkinter import *

mainform = Tk()
mainform.wm_title("Text")
mainform.geometry('500x200')

lbl=Label(mainform)
lbl['text']="text 1 :"
lbl.grid(row=0, column=0)

txt = Text(mainform)
txt['bg'] = "#aee1e1"
txt['bd']=5
txt['cursor']="man"
txt['font']="calibri 12"
txt['fg']="red"
txt['height']=5
txt['highlightbackground']="#00917c"
txt['highlightthickness']=5
txt['highlightcolor']="#025955"
txt['insertbackground']="#025955"
txt['insertofftime']=1000
txt['insertwidth']=2
txt['relief']="groove"
txt['selectbackground']="red"
txt['selectborderwidth']=10
txt['spacing1']=5
txt['spacing2']=5
txt['spacing3']=5
txt['tabs']=1
txt['width']=25

txt.insert(INSERT,"Hallo, ")
txt.grid(row=0, column=1)

mainform.mainloop()