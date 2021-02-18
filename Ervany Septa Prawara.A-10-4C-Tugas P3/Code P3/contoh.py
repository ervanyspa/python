# nama file : tkinter_gridmanager v2.py

# import modul
from tkinter import *
import tkinter.messagebox

class Layar1 (tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.BuatKontrol()

 
    def BuatKontrol(self):
        def new_window(self):
            self.newWindow = Toplevel(self.master)
            self.app = Layar2(self.newWindow)
        def Login():
            u = (self.username.get())
            p = (self.password.get())
    
            if (u == str("admin") and p == str("admin")):
                self.newWindow = Toplevel(self.master)
                self.app = Layar2(self.newWindow)
            else:
                tkinter.messagebox.askyesno("Login System","Invalid Login Detail")
        
        self.lbl1 = tkinter.Label(self)
        self.lbl1['text'] = "Username"
        # memberikan fungsi rata kanan dengan atribut sticky=tkinter.E
        self.lbl1.grid(row=0, column=0, sticky=tkinter.E)
        self.lbl2 = tkinter.Label(self)
        self.lbl2['text'] = "Password"
            # memberikan fungsi rata kanan dengan atribut sticky=tkinter.E
        self.lbl2.grid(row=1, column=0, sticky=tkinter.E)

        self.username = tkinter.Entry(self)
        self.username['width'] = 40
        self.username.grid(row=0, column=1, columnspan=2)

        self.password = tkinter.Entry(self)
        self.password['width'] = 40
        self.password.grid(row=1, column=1, columnspan=2)

        self.chk = tkinter.Checkbutton(self)
        self.chk['text'] = "Remember Me"
        self.chk.grid(row=2, column=0)

        self.btn1 = tkinter.Button(self, command= Login)
        self.btn1['text'] = "Login"
            # memberikan fungsi penempatan penuh pada button dengan atribut sticky=tkinter.N + tkinter.E + tkinter.W
        self.btn1.grid(row=2, column=1, sticky=tkinter.N + tkinter.E + tkinter.W)

        self.btn2 = tkinter.Button(self)
        self.btn2['text'] = "Exit"
        # memberikan fungsi penempatan penuh pada button dengan atribut sticky=tkinter.N + tkinter.E + tkinter.W
        self.btn2.grid(row=2, column=2, sticky=tkinter.N + tkinter.E + tkinter.W)
class Layar2(tkinter.Frame):
    # membuat konstruktor DemoFrame
    def __init__(self, master=None):
        # memanggil kontruktor kelas induk (tkinter.Frame)
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.buttonclick()
    def buttonclick(self):
        def main():
            try:
                T = float(Ltanah.get())
                X = 50 * T/1000
                tkinter.messagebox.showinfo("Hitung", "Jumlah Pupuk : %.2f Kg "% X)
            except:
                tkinter.messagebox.showerror("error","Masukan Luas tanah")

        lbl = tkinter.Label(self)
        lbl['text'] = "Masukkan Luas Tanah anda (m^2)" #label inputan
        lbl['background'] = "#73C2FB" #background label
        lbl.grid(row=1, column=1, sticky = tkinter.E + tkinter.W)

        Ltanah = tkinter.Entry(self)
        Ltanah['width'] = 35 #lebar inputan
        Ltanah.grid(row=2, column=1, stick= tkinter.E + tkinter.W)

        btn = tkinter.Button(self, command=main)
        btn['text'] = "Pilih" #nama tombol
        btn['background'] = "#d3d3d3" #background tombol
        btn.grid(row=3, column=1, sticky= tkinter.E + tkinter.W)

           
def main():
    # membuat kelas demo frame
    app = Layar1()
    app.master.title("Demo Frame")
    app.mainloop()


if __name__ == "__main__":
    main()