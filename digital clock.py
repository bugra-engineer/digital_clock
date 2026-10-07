import tkinter as tk
import time

pencere = tk.Tk()
pencere.title("Dijital Saat")
pencere.configure(bg="black")
pencere.resizable(False, False)

saat_label = tk.Label(pencere, font=("Courier", 60, "bold"),
                      fg="#00ff88", bg="black", padx=30, pady=10)
saat_label.pack()

tarih_label = tk.Label(pencere, font=("Courier", 20),
                       fg="white", bg="black", pady=10)
tarih_label.pack()

def guncelle():
    saat_label.config(text=time.strftime("%H:%M:%S"))
    tarih_label.config(text=time.strftime("%d/%m/%Y"))
    pencere.after(1000, guncelle)

guncelle()
pencere.mainloop()