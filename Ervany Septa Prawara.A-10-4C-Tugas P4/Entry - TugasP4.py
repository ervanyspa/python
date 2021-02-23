from tkinter import *


def main():
    mainform = Tk()

    mainform.wm_title("Entry")
    mainform.geometry('500x200')

    lbl1 = Label(mainform)
    lbl1['text'] = "Entry 1     :"
    lbl1.grid(row=0, column=0)
    
    entry1 = Entry(mainform)
    entry1['bg']="red"
    entry1['bd']=5
    entry1['cursor']="pencil"
    # entry1['exportselection']=1
    entry1['fg'] = "pink"
    entry1['font']="calibri 12"
    entry1['highlightbackground']="green"
    entry1['highlightcolor']="yellow"
    entry1['highlightthickness']=10
    entry1['insertbackground']='cyan'
    # entry1['insertborderwidth']=100
    entry1['insertofftime']=50
    # entry1['insertontime']=50
    entry1['insertwidth']=10
    entry1['justify']="center"
    entry1['relief']="groove"
    entry1['selectbackground']="green"
    entry1['selectborderwidth']=50
    entry1['selectforeground']="yellow"
    # entry1['show']="*"
    # entry1['textvariable']=StringVar()
    entry1['width']=30
    # entry1['xscrollcommand']=
    entry1.grid(row=0, column=1)



    # txt1 = Label(mainform)
    # txt1['text']=entry1.get()
    # txt1['width'] = 40
    # txt1.grid(row=0, column=2)

    #chk = tkinter.Checkbutton(mainform)
    #chk['text'] = "Remember Me"
    #chk.grid(row=2, column=0)

    #btn1 = tkinter.Button(mainform)
    #btn1['text'] = "Login"
    #btn1.grid(row=2, column=1)

    #btn2 = tkinter.Button(mainform)
    #btn2['text'] = "Exit"
    #btn2.grid(row=2, column=2)

    mainform.mainloop()


if __name__ == "__main__":
    main()