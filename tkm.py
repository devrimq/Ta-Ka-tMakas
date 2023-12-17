import random
from tkinter import *

oyuncu_skoru = 0

def oyunu_baslat(secim):
    global oyuncu_skoru
    bilgisayar_secimi = random.choice(["Taş", "Kağıt", "Makas"])
    sonuc = kontrol_et(secim, bilgisayar_secimi)

    if sonuc == "Oyuncu kazandı":
        oyuncu_skoru += 1
    elif sonuc == "Bilgisayar kazandı":
        oyuncu_skoru -= 1

    player_score_label.config(text=f"Oyuncu: {oyuncu_skoru}")
    sonuc_etiketi.config(text=f"Bilgisayar: {bilgisayar_secimi}\nSonuç: {sonuc}")

def kontrol_et(oyuncu_secimi, bilgisayar_secimi):
    if oyuncu_secimi == bilgisayar_secimi:
        return "Berabere"
    elif (
        (oyuncu_secimi == "Taş" and bilgisayar_secimi == "Makas")
        or (oyuncu_secimi == "Kağıt" and bilgisayar_secimi == "Taş")
        or (oyuncu_secimi == "Makas" and bilgisayar_secimi == "Kağıt")
    ):
        return "Oyuncu kazandı"
    else:
        return "Bilgisayar kazandı"

master = Tk()
master.title("TKM")

Label(master, text="Taş, Kağıt, Makas", font=("Calibri", 14)).grid(row=0, sticky=W, padx=200)
Label(master, text="Lütfen birini seçiniz", font=("Calibri", 12)).grid(row=1, sticky=N)

player_score_label = Label(master, text="Oyuncu : 0", font=("Calibri", 12))
player_score_label.grid(row=2, sticky=W)

sonuc_etiketi = Label(master, text="", font=("Calibri", 12))
sonuc_etiketi.grid(row=3, sticky=W, pady=10)

Button(master, text="Taş", command=lambda: oyunu_baslat("Taş")).grid(row=4, sticky=W)
Button(master, text="Kağıt", command=lambda: oyunu_baslat("Kağıt")).grid(row=4, sticky=N)
Button(master, text="Makas", command=lambda: oyunu_baslat("Makas")).grid(row=4, sticky=E)

master.mainloop()
