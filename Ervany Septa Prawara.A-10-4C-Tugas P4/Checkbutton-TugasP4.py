import tkinter


def main():
    mainform = tkinter.Tk()

    mainform.wm_title("Checkbutton")
    mainform.geometry('500x200')

    lbl1 = tkinter.Label(mainform)
    lbl1['text'] = "Checkbutton    :"
    lbl1.grid(row=0, column=0)

    chk1 = tkinter.Checkbutton(mainform)
    # chk1['text']="sdadsa"
    chk1['activebackground']="green"
    chk1['activeforeground']="red"
    chk1['bg']="yellow"
    chk1['bitmap']='warning'
    chk1['bd']=9
    chk1['command']=lbl1.destroy
    chk1['cursor']='plus'
    # chk1['disabledforeground']="white"
    # chk1['font']="calibri"
    # chk1['fg']="yellow"
    chk1['height']=30
    chk1['highlightcolor']="white"
    chk1.grid(row=0, column=1)
    
    mainform.mainloop()


if __name__ == "__main__":
    main()