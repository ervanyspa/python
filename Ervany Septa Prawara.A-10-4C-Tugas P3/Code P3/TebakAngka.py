#import modul tkinter
import tkinter
#import modul tkinter messagebox
import tkinter.messagebox
#import modul random
import random

class Tebak(tkinter.Frame): #membuat class Tebak
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.buttonclick()
    def buttonclick(self):
        angka = random.randint(1,100)

        def buttonhasil():
        #konversi tipedata entry ke int
            a = int(tbkangka.get())
        
        # membuat kondisi yang harus dipenuhi dengan if elif else
        # kondisi tebakan user dengan angka sama, maka program akan menampilkan messagebox "Tebakan user Benar"
            if a == angka :
                tkinter.messagebox.showinfo(
                    "Hasil", "Tebakan %s, Benar!!!" % (nama.get()))
        # kondisi tebakan user lebih besar dengan angka, maka program akan menampilkan messagebox "Tebakan user, kurang kecil" 
            elif a > angka :
                tkinter.messagebox.showinfo(
                    "Hasil", "Tebakan %s, Terlalu Besar" % (nama.get()))
        # kondisi tebakan user lebih besar dengan angka, maka program akan menampilkan messagebox "Tebakan user, kurang besar" 
            else:
                tkinter.messagebox.showinfo(
                    "Hasil", "Tebakan %s, Terlalu Kecil" % (nama.get()))

    # menambah Label "Masukkan Nama Anda"
        lbl = tkinter.Label(self)
        lbl['text'] = "Masukkan Nama Anda"
        lbl.pack()

    # menambah Entry dan ukuran entry untuk memasukkan inputan dari user dan dimasukkan kedalam variable nama
        nama = tkinter.Entry(self)
        nama['width'] = 40
        nama.pack()

    # menambah Label "Tebak angka, masukkan angka 1 sampai 100"
        lbl2 = tkinter.Label(self)
        lbl2['text'] = "Tebak angka, masukkan angka 1 sampai 100"
        lbl2.pack()

    # menambah Entry dan ukuran entry untuk memasukkan inputan dari user untuk angka dan dimasukkan kedalam variabel tbkangka
        tbkangka = tkinter.Entry(self)
        tbkangka['width'] = 40
        tbkangka.pack()

    # menambah button dengan text "Lihat Hasil", jika diclick oleh user akan menjalankan method buttonclick
        btn = tkinter.Button(self, command=buttonhasil)
        btn['text'] = "Lihat Hasil"
        btn.pack()

def mulai():
    app2 = Tebak()
    app2.mainloop()