from tkinter import Tk, Label, Button, PhotoImage, Canvas
import random

# Oyuncu ve bilgisayar skorları için başlangıç değerleri
oyuncu_skor = 0
bilgisayar_skor = 0
bilgisayar_secimi = None  # Bilgisayarın seçimini global olarak tanımla

# Oyuncu skorunu güncelle
def oyuncu_skor_guncelle(puan):
    global oyuncu_skor
    oyuncu_skor += puan
    oyuncu_skor_label.config(text=f"Oyuncu: {oyuncu_skor}")


# Bilgisayar skorunu güncelle
def bilgisayar_skor_guncelle(puan):
    global bilgisayar_skor
    bilgisayar_skor += puan
    bilgisayar_skor_label.config(text=f"Bilgisayar: {bilgisayar_skor}")

# Örnek bir durum_handler fonksiyonu
def durum_handler(secim):
    global oyuncu_skor, bilgisayar_skor, bilgisayar_secimi
    
    # Bilgisayarın seçimini random olarak belirle
    bilgisayar_secimi = random.choice(["Taş", "Kağıt", "Makas"])

    print(f"Oyuncunun seçimi: {secim}")
    print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

    if secim == bilgisayar_secimi:
        durum_label.config(text="Berabere!")
    elif (secim == "Taş" and bilgisayar_secimi == "Makas") or \
         (secim == "Makas" and bilgisayar_secimi == "Kağıt") or \
         (secim == "Kağıt" and bilgisayar_secimi == "Taş"):
        durum_label.config(text="Oyuncu kazandı!")
        oyuncu_skor_guncelle(1)
    else:
        durum_label.config(text="Bilgisayar kazandı!")
        bilgisayar_skor_guncelle(1)

    eksilen_kalp = canvas.find_withtag("kalp")
    if eksilen_kalp:
        canvas.delete(eksilen_kalp[-1])

# Kalp çizme fonksiyonu
def draw_kalp(canvas, x, y, renk):
    canvas.create_polygon(
        x, y - 15, x + 5, y, x + 10, y - 15,  # Üçgen üst kısmı
        x + 10, y + 15, x, y + 30, x - 10, y + 15,  # Üçgen alt kısmı
        fill=renk, outline="white", tags="kalp"
    )

def resmi_ayarla():
    global bilgisayar_secimi, oyuncu_skor_label, bilgisayar_skor_label, durum_label, canvas
    
    root = Tk()
    root.title("TaşKağıtMakas Oyunu")

    # PNG dosyasını yükleyin ve boyutlarını alın
    arka_plan = PhotoImage(file="arka_plan.png")
    genislik = arka_plan.width()
    yukseklik = arka_plan.height()

    # Pencere boyutunu ve konumunu ayarlayın
    pencere_genislik = genislik + 20  # Ekstra boşluklar için
    pencere_yukseklik = yukseklik + 40  # Ekstra boşluklar için
    ekran_genislik = root.winfo_screenwidth()
    ekran_yukseklik = root.winfo_screenheight()
    pencere_x = (ekran_genislik - pencere_genislik) // 2
    pencere_y = (ekran_yukseklik - pencere_yukseklik) // 2

    root.geometry("{}x{}+{}+{}".format(pencere_genislik, pencere_yukseklik, pencere_x, pencere_y))


   # Etiket oluşturun ve PNG dosyasını arka plana ayarlayın
    arka_plan_label = Label(root, image=arka_plan)
    arka_plan_label.place(x=10, y=20, width=genislik, height=yukseklik)

    # Başlık Etiketi
    baslik_label = Label(root, text="Taş Kağıt Makas", font=("Calibri", 14, "bold"), fg="dark green")
    baslik_label.place(relx=0.5, rely=0.05, anchor="center")

    # Taş butonu ve resmi
    tas_resmi = PhotoImage(file="tas.png")
    tas_buton = Button(root, text="Taş", image=tas_resmi, compound="top", command=lambda: durum_handler("Taş"))
    tas_buton.place(relx=0.25, rely=0.5, anchor="center")

    # Kağıt butonu ve resmi
    kagit_resmi = PhotoImage(file="kagit.png")
    kagit_buton = Button(root, text="Kağıt", image=kagit_resmi, compound="top", command=lambda: durum_handler("Kağıt"))
    kagit_buton.place(relx=0.5, rely=0.5, anchor="center")

    # Makas butonu ve resmi
    makas_resmi = PhotoImage(file="makas.png")
    makas_buton = Button(root, text="Makas", image=makas_resmi, compound="top", command=lambda: durum_handler("Makas"))
    makas_buton.place(relx=0.75, rely=0.5, anchor="center")
    
 # Oyuncu ve bilgisayar skorları için başlangıç değerleri
    oyuncu_skor_label = Label(root, text=f"Oyuncu: {oyuncu_skor}", font=("Calibri", 12))
    oyuncu_skor_label.place(relx=0.05, rely=0.9, anchor="sw")
    
    # Durum etiketi
    durum_label = Label(root, text="", font=("Calibri", 12))
    durum_label.place(relx=0.5, rely=0.8, anchor="center")

    bilgisayar_skor_label = Label(root, text=f"Bilgisayar: {bilgisayar_skor}", font=("Calibri", 12))
    bilgisayar_skor_label.place(relx=0.95, rely=0.9, anchor="se")


    # Oyuncu ve bilgisayar ikonları
    oyuncu_icon = PhotoImage(file="gamer.png")
    oyuncu_icon_label = Label(root, image=oyuncu_icon)
    oyuncu_icon_label.place(relx=0.20, rely=0.90, anchor="sw")

    bilgisayar_icon = PhotoImage(file="pc.png")
    bilgisayar_icon_label = Label(root, image=bilgisayar_icon)
    bilgisayar_icon_label.place(relx=0.80, rely=0.90, anchor="se")

    # Canvas boyutları
    canvas_genislik = 400
    canvas_yukseklik = 200

    # Canvas oluştur
    canvas = Canvas(root, bg="white", width=canvas_genislik, height=canvas_yukseklik)
    canvas.pack(pady=60)

    # Kalpleri çiz
    kalp_sayisi = 5
    kalp_genislik = 80
    kalp_aralik = 10

    for i in range(kalp_sayisi):
        x = kalp_aralik + i * (kalp_genislik + kalp_aralik)
        y = canvas_yukseklik // 2

        # Kalp çiz
        draw_kalp(canvas, x, y, "red")

    root.mainloop()

# Arayüzü oluşturun
resmi_ayarla()
