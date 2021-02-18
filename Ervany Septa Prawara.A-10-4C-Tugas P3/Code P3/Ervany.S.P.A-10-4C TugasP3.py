from tkinter import * #import modul tkinter
import tkinter.messagebox #import modul tkinter messagebox
from TebakAngka import Tebak, mulai # import lybrary pada modul atau file TebakAngka

class Login (tkinter.Frame): #membuat class Login dan memanggil Frame pada modul tkinter
    def __init__(self, master=None): 
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.Kontrol()

    def Kontrol(self): #membuat fungsi untuk form login
        def new_window(self):
            self.newWindow = Toplevel(self.master)
            self.app = Tebak(self.newWindow)
        def akun():
            # konversi inputan user pada entry username dan password menjadi string
            user = (str(self.username.get()))
            pas = (str(self.password.get()))
    
            #kondisi login jika benar 
            if (user == "admin" and pas == "admin"):
                self.newWindow = Toplevel(self.master)
                self.app = Tebak(self.newWindow)
            #kondisi login jika salah
            else:
                tkinter.messagebox.showinfo("Login Gagal","Username atau Password Salah")
        
        # membuat label username
        self.lbl1 = tkinter.Label(self)
        self.lbl1['text'] = "Username"
        self.lbl1.grid(row=0, column=0, sticky=tkinter.E)  # memberikan fungsi rata kanan dengan atribut sticky=tkinter.E

         # membuat label password
        self.lbl2 = tkinter.Label(self)
        self.lbl2['text'] = "Password"
        self.lbl2.grid(row=1, column=0, sticky=tkinter.E)

        # membuat entry username
        self.username = tkinter.Entry(self)
        self.username['width'] = 40
        self.username.grid(row=0, column=1, columnspan=2)

        # membuat entry password
        self.password = tkinter.Entry(self)
        self.password = tkinter.Entry(self, show="*")
        self.password['width'] = 40
        self.password.grid(row=1, column=1, columnspan=2)

        # membuat button login
        self.btn1 = tkinter.Button(self, command= akun)
        self.btn1['text'] = "Login"
        self.btn1.grid(row=2, column=2, sticky=tkinter.N + tkinter.E + tkinter.W)

def main():
    app = Login()
    app.master.title("Tebak Angka (Ervany Septa Prawara.A - 193307053)")
    app.mainloop()


if __name__ == "__main__":
    main()