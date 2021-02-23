from tkinter import *

def main():
    mainform = Tk()

    mainform.wm_title("Radiobutton")
    mainform.geometry('500x200')

    lbl1 = Label(mainform)
    lbl1['text'] = "Radiobutton     :"
    lbl1.grid(row=0, column=0)