from tkinter import *

def main():
    mainform = Tk()

    mainform.wm_title("List Box")
    mainform.geometry('500x200')

    lbl1 = Label(mainform)
    lbl1['text'] = "List Box    :"
    lbl1.grid(row=0, column=0)

    list1=Listbox(mainform)
    list1.insert(1,"Los Angeles Lakers")
    list1.insert(2,"Celtics")
    list1.insert(3,"Rockets")
    list1.insert(4,"Warriors")
    list1.insert(5,"Bucks")
    list1.insert(6,"Nets")
    list1.insert(7,"Bulls")
    list1.insert(8,"Thunder")
    
    list1['bg']="pink"
    list1['bd']=5
    list1['cursor']="dot"
    list1['font']="calibri 10"
    list1['fg']="green"
    list1['height']=5
    list1['highlightcolor']='green'
    list1['highlightthickness']=3
    list1['relief']='groove'
    list1['selectbackground']='red'
    list1['selectmode']='multiple'
    list1['width']=10
    list1['xscrollcommand']=1
    list1['yscrollcommand']=1
    list1.grid(row=0, column=1)

    mainform.mainloop()


if __name__ == "__main__":
    main()