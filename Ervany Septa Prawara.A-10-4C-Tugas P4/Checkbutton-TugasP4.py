# import tkinter
from tkinter import *
# from tkinter import IntVar


def main():
    mainform = Tk()

    mainform.wm_title("Checkbutton")
    mainform.geometry('500x200')

    lbl1 = Label(mainform)
    lbl1['text'] = "Checkbutton    :"
    lbl1.grid(row=0, column=0)

    chk1 = Checkbutton(mainform)
    chk1['activebackground']="green"
    chk1['activeforeground']="red"
    chk1['bg']="yellow"
    chk1['bitmap']='warning'
    chk1['bd']=9
    chk1['command']=lbl1.destroy
    chk1['cursor']='plus'
    chk1['height']=30
    chk1['relief']='sunken'
    chk1['state']='active'
    chk1['width']=40
    chk1.grid(row=0, column=1)

    lbl2 = Label(mainform)
    lbl2['text'] = "Checkbutton 2   :"
    lbl2.grid(row=1, column=0)

    def tampil() :
        lblchk = Label(mainform)
        lblchk['text']=chk.get()
        lblchk.grid(row=1, column=2)

    chk2 = Checkbutton(mainform)
    chk=StringVar()
    chk2['text']="Check Button"
    chk2['variable']=chk
    chk2['command'] = tampil
    chk2['font']="calibri"
    chk2['justify'] = "left"
    chk2['offvalue']="Off"
    chk2['onvalue']="On"
    chk2['padx']=30
    chk2['pady']=30
    chk2['selectcolor']="yellow"
    chk2['underline']=1
    chk2['wraplength']=80
    chk2.grid(row=1, column=1)

    lbl3 = Label(mainform)
    lbl3['text'] = "Checkbutton 3   :"
    lbl3.grid(row=2, column=0)

    
    mainform.mainloop()


if __name__ == "__main__":
    main()