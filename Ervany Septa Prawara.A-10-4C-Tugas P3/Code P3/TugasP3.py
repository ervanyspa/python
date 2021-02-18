import tkinter #mengimport tkinter
import tkinter.messagebox #mengimport messagebox 

class Motor(tkinter.Frame):
    def __init__(self, master=None):
        # memanggil konstruktor kelas induk (tkinter.Frame)
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.buttonclick()
    def buttonclick(self):
        def hitung():
            try:
                nama = str(txtNama.get())
                P = float(num1.get())
                S = float(num2.get())
                ccA = 0.785*(P**2)*S
                ccB = ccA/1000
                asking = tkinter.messagebox.askquestion("Motor", "Type Montor : %s ?"%(nama))
                if asking == 'yes':    
                    tkinter.messagebox.showinfo("Hasil", "Hasilnya %.2f" %(ccB))
                elif asking == 'no':
                    pass
            except:
                tkinter.messagebox.showerror("error", "Tolong Masukan angka")
                
        lbl = tkinter.Label(self) #membuat label
        lbl['text'] = "Merek Motor" #memangil item pertama di list 
        lbl.grid(row=1, column=0, sticky = tkinter.W) #mengatur baris dan kolom
            #entry
        txtNama =tkinter.Entry(self)#menmbuat entry lalu menyimpanya di variabel txtNama
        txtNama['width']=20 #mengatur ukuran entry
        txtNama.grid(row=1, column=1)

        lblP = tkinter.Label(self)
        lblP['text'] = "Diameter Piston"
        lblP.grid(row=2, column=0, sticky = tkinter.W)

        num1 = tkinter.Entry(self)
        num1['width'] = 20
        num1.grid(row=2, column=1)

        lblS = tkinter.Label(self)
        lblS['text'] = "Diameter Stroke"
        lblS.grid(row=3, column=0, sticky = tkinter.W)

        num2 = tkinter.Entry(self)
        num2['width'] = 20
        num2.grid(row=3, column=1)

        btn = tkinter.Button(self, command=hitung)
        btn['text'] = "hitung"#memanggil fungsi buttonclick pada button
        btn.grid(row=4, column=1, sticky = tkinter.E + tkinter.W)

def start():
    app = Motor()
    app.master.title("Demo Frame")
    app.mainloop()

if __name__ == "__main__":
    start()
   