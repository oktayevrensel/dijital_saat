import tkinter as tk
from datetime import datetime

# tkinter penceresi oluştur
root = tk.Tk()

# saat etiketi oluştur
time_label = tk.Label(root, font=('arial', 20, 'bold'))
time_label.pack()

# saat güncelleme fonksiyonu
def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.configure(text=current_time)
    root.after(1000, update_time)

# saat güncelleme fonksiyonunu çalıştır
update_time()

# pencereyi göster
root.mainloop()
