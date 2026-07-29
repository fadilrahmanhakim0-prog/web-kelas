import tkinter as tk
from tkinter import ttk

jadwal = {
    "Senin": [
        "1. PKN",
        "2. B. Jawa",
        "3. B. Arab"
    ],
    "Selasa": [
        "1. Seni Budaya",
        "2. MTK",
        "3. SKI",
        "4. B. Indonesia"
    ],
    "Rabu": [
        "1. B. Indonesia",
        "2. Bimbingan Konseling (BK)",
        "3. MTK",
        "4. Al-Qur'an Hadist"
    ],
    "Kamis": [
        "1. Fiqih",
        "2. IPA",
        "3. B. Inggris"
    ],
    "Jum'at": [
        "1. IPA",
        "2. IPS"
    ],
    "Sabtu": [
        "1. Akidah Akhlak",
        "2. Informatika",
        "3. PJOK"
    ]
}

def tampilkan():
    hari = combo.get()
    hasil.delete("1.0", tk.END)

    if hari in jadwal:
        hasil.insert(tk.END, f"Jadwal {hari}\n\n")
        for pelajaran in jadwal[hari]:
            hasil.insert(tk.END, pelajaran + "\n")

root = tk.Tk()
root.title("Jadwal Pelajaran Kelas 7H")
root.geometry("500x450")

judul = tk.Label(
    root,
    text="📚 Jadwal Pelajaran Kelas 7H",
    font=("Arial", 18, "bold")
)
judul.pack(pady=10)

combo = ttk.Combobox(
    root,
    values=list(jadwal.keys()),
    state="readonly",
    font=("Arial", 12)
)
combo.current(0)
combo.pack(pady=10)

btn = tk.Button(
    root,
    text="Tampilkan Jadwal",
    command=tampilkan
)
btn.pack()

hasil = tk.Text(root, width=45, height=15, font=("Arial", 12))
hasil.pack(pady=10)

tampilkan()

root.mainloop()
from flask import Flask

app = Flask(__name__)

@app.route("/ai")
def ai():
    return "Halo! Saya AI Kelas 7H."

app.run(host="0.0.0.0", port=5000)
