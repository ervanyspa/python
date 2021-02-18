#import modul tkinter
import tkinter
#import modul tkinter messagebox
import tkinter.messagebox
#import modul random
import random

def main() :
    #membuat form utama
    mainform = tkinter.Tk()
    # digunakan untuk membuat objek atau instance dari kelas Tk
    # yang akan dijadikan form utama

    #merandom angka dari 1 sampai 100 dan dimasukkan ke variable angka
    angka = random.randint(1,100)
    #fungsi respon dari button
    def buttonclick():
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

    #menambahkan title, warna, ukuran pada form
    mainform.wm_title("Tebak Angka (Ervany Septa Prawara.A - 193307053)")
    mainform['background'] = "#ffdea6"
    mainform.geometry('500x200')

    # menambah Label "Masukkan Nama Anda"
    lbl = tkinter.Label(mainform)
    lbl['text'] = "Masukkan Nama Anda"
    lbl.pack()

    # menambah Entry dan ukuran entry untuk memasukkan inputan dari user dan dimasukkan kedalam variable nama
    nama = tkinter.Entry(mainform)
    nama['width'] = 40
    nama.pack()

    # menambah Label "Tebak angka, masukkan angka 1 sampai 100"
    lbl2 = tkinter.Label(mainform)
    lbl2['text'] = "Tebak angka, masukkan angka 1 sampai 100"
    lbl2.pack()

    # menambah Entry dan ukuran entry untuk memasukkan inputan dari user untuk angka dan dimasukkan kedalam variabel tbkangka
    tbkangka = tkinter.Entry(mainform)
    tbkangka['width'] = 40
    tbkangka.pack()

    # menambah button dengan text "Lihat Hasil", jika diclick oleh user akan menjalankan method buttonclick
    btn = tkinter.Button(mainform, command=buttonclick)
    btn['text'] = "Lihat Hasil"
    btn.pack()

    # menampilkan form
    mainform.mainloop()

# digunakan untuk memastikan bahwa tidak ada program lain yang di eksekusi ketika
# modul ini di import program lain
if __name__ == "__main__" :
    main()