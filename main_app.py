import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def calculate_mse_psnr():
    file1 = file_entry1.get()
    file2 = file_entry2.get()

    if not file1 or not file2:
        messagebox.showerror("Error", "Mohon pilih dua file gambar terlebih dahulu.")
        return

    image1 = cv2.imread(file1)
    image2 = cv2.imread(file2)

    if image1.shape != image2.shape:
        messagebox.showerror("Error", "Ukuran gambar tidak sama.")
        return

    mse_label.config(text=f"MSE: {mse:.2f}")
    psnr_label.config(text=f"PSNR: {psnr:.2f} dB")

    result_text = f"MSE: {mse:.2f}\nPSNR: {psnr:.2f} dB"
    pyperclip.copy(result_text)
    messagebox.showinfo("Info", "Hasil perhitungan disalin ke clipboard.")

    preview_canvas1.create_image(0, 0, anchor=tk.NW, image=img1)
    preview_canvas2.create_image(0, 0, anchor=tk.NW, image=img2)


def browse_file1():
    file1 = filedialog.askopenfilename()
    file_entry1.delete(0, tk.END)
    file_entry1.insert(0, file1)

    image1 = Image.open(file1)
    image1 = image1.resize((100, 100), Image.LANCZOS)
    global img1
    img1 = ImageTk.PhotoImage(image1)
    preview_canvas1.create_image(0, 0, anchor=tk.NW, image=img1)


def browse_file2():
    file2 = filedialog.askopenfilename()
    file_entry2.delete(0, tk.END)
    file_entry2.insert(0, file2)

    image2 = Image.open(file2)
    image2 = image2.resize((100, 100), Image.LANCZOS)
    global img2
    img2 = ImageTk.PhotoImage(image2)
    preview_canvas2.create_image(0, 0, anchor=tk.NW, image=img2)


root = tk.Tk()

file_label1 = tk.Label(root, text="Gambar 1:")
file_label1.grid(row=0, column=0, padx=10, pady=10)
file_entry1 = tk.Entry(root)
file_entry1.grid(row=0, column=1, padx=10, pady=10)
browse_button1 = tk.Button(root, text="Cari Gambar", command=browse_file1)
browse_button1.grid(row=0, column=2, padx=10, pady=10)

file_label2 = tk.Label(root, text="Gambar 2:")
file_label2.grid(row=2, column=0, padx=10, pady=10)

file_entry2 = tk.Entry(root)
file_entry2.grid(row=2, column=1, padx=10, pady=10)
browse_button2 = tk.Button(root, text="Cari Gambar", command=browse_file2)
browse_button2.grid(row=2, column=2, padx=10, pady=10)

preview_canvas1 = tk.Canvas(root, width=100, height=100, bg="white")
preview_canvas1.grid(row=1, column=1, padx=10, pady=10)

preview_canvas2 = tk.Canvas(root, width=100, height=100, bg="white")
preview_canvas2.grid(row=3, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Hitung MSE dan PSNR", command=calculate_mse_psnr)
calculate_button.grid(row=5, column=1, padx=10, pady=10)

mse_label = tk.Label(root, text="")
mse_label.grid(row=6, column=0, columnspan=3)
psnr_label = tk.Label(root, text="")
psnr_label.grid(row=7, column=0, columnspan=3)


root.mainloop()
