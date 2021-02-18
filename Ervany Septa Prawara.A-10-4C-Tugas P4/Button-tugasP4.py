# import modul
import tkinter


def main():
    mainform = tkinter.Tk()

    mainform.wm_title("Button")
    mainform.geometry('500x200')

    lbl1 = tkinter.Label(mainform)
    lbl1['text'] = "Button   :"
    lbl1.grid(row=0, column=0)

    #lbl2 = tkinter.Label(mainform)
    #lbl2['text'] = "Password"
    #lbl2.grid(row=1, column=0)


    btn1 = tkinter.Button(mainform)
    btn1['text']="Hilangkan Text"
    btn1['activebackground']="pink"
    btn1['activeforeground']="red"
    btn1['bd']=5
    btn1['bg']="yellow"
    btn1['command']=lbl1.destroy
    btn1['fg']="green"
    btn1['font']="calibri"
    btn1['height']=2
    # btn1['highlightcolor']="white"
    # btn1['image']='button.png'
    btn1['justify']='center'
    btn1['padx']=10
    btn1['pady']=10
    btn1['relief']='ridge'
    btn1['state']='active'
    btn1['underline']=5
    btn1['width'] = 40
    btn1['wraplength']=100
    btn1.grid(row=0, column=1)

    #txt2 = tkinter.Entry(mainform)
    #txt2['width'] = 40
    # sd
    #txt2.grid(row=1, column=1, columnspan=2)

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