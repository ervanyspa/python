# import modul
from tkinter import *
# from tkinter import *

def main():
    mainform = Tk()

    mainform.wm_title("Button")
    mainform.geometry('500x200')

    lbl1 = Label(mainform)
    lbl1['text'] = "Button   :"
    lbl1.grid(row=0, column=0)

    btn1 = Button(mainform)
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
    btn1['justify']='center'
    btn1['padx']=10
    btn1['pady']=10
    btn1['relief']='ridge'
    btn1['state']='active'
    btn1['underline']=5
    btn1['width'] = 40
    btn1['wraplength']=100
    btn1.grid(row=0, column=1)

    lbl2 = Label(mainform)
    lbl2['text'] = "Button 2    :"
    lbl2.grid(row=1, column=0)

    btn2 = Button(mainform)
    photo = PhotoImage(file =r"D:\Kuliah\Semester 4\Pemrograman Berbasis Desktop (Muhammad Syaeful Fajar, S.Pd., M.Kom.)\Tugas\Ervany Septa Prawara.A-10-4C-Tugas P4\owl.png")
    btn2['text']="Button"
    photoimage = photo.subsample(10, 10) 
    btn2['image']=photoimage
    # btn1['highlightcolor']="white"
    btn2.grid(row=1, column=1)
    
    mainform.mainloop()


if __name__ == "__main__":
    main()