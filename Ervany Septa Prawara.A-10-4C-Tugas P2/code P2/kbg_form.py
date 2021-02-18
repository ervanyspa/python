import tkinter
import tkinter.messagebox
import random
import utils

def main() :
    mainform = tkinter.Tk()
    mainform2 = tkinter.Tk()
    def buttonclick() :
        a = tngpemain.get()
        b = int(a)
        c = txt.get()
        d = str(c)
        if utils.validate(b) :
           tngcomp = random.randint(0,2)

           utils.print_hand(b,d)
           utils.print_hand(tngcomp, 'Komputer')
           result=utils.judge(b, tngcomp)
           tkinter.messagebox.showinfo(
            "Hasil", result )
           txt.delete(0, 'end')
           tngpemain.delete(0, 'end')
        else:
            tkinter.messagebox.showinfo(
                "Salah Input", "Mohon Masukkan angka yang benar")

    mainform.wm_title("Kertas Batu Gunting (Ervany Septa Prawara.A - 193307053)")
    mainform['background'] = "#ffdea6"
    mainform.geometry('500x200')

    lbl = tkinter.Label(mainform)
    lbl['text'] = "Masukkan Nama Anda"
    lbl.pack()

    txt = tkinter.Entry(mainform)
    txt['width'] = 40
    txt.pack()
    
    lbl2 = tkinter.Label(mainform)
    lbl2['text'] = "Pilih Tangan: (0: Batu, 1: Kertas, 2: Gunting)"
    lbl2.pack()

    tngpemain = tkinter.Entry(mainform)
    tngpemain['width'] = 40
    tngpemain.pack()
    
    btn = tkinter.Button(mainform, command=buttonclick)
    btn['text'] = "Lihat Hasil"
    btn.pack()


    mainform.mainloop()

if __name__ == "__main__" :
    main()
