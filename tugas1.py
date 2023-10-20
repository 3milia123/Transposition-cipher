import tkinter as tk
from tkinter import Label, Entry, Button

# Fungsi untuk enkripsi teks plainteks
def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "")  
    plaintext_length = len(plaintext)
    num_rows = (plaintext_length + key - 1) // key  
    matrix = [[' ' for _ in range(key)] for _ in range(num_rows)]  

    row, col = 0, 0
    for char in plaintext:
        matrix[row][col] = char
        col += 1
        if col == key:
            col = 0
            row += 1

    ciphertext = ''
    for col in range(key):
        for row in range(num_rows):
            ciphertext += matrix[row][col]

    return ciphertext

# Fungsi untuk dekripsi teks cipherteks
def decrypt(ciphertext, key):
    ciphertext_length = len(ciphertext)
    num_rows = (ciphertext_length + key - 1) // key 
    matrix = [[' ' for _ in range(key)] for _ in range(num_rows)] 

    col, row = 0, 0
    for char in ciphertext:
        matrix[row][col] = char
        row += 1
        if row == num_rows:
            row = 0
            col += 1

    plaintext = ''
    for row in range(num_rows):
        for col in range(key):
            plaintext += matrix[row][col]

    return plaintext

# Fungsi untuk menangani klik tombol "Enkripsi"
def encrypt_button_click():
    plaintext = plaintext_entry.get()  
    key = int(key_entry.get())  
    ciphertext = encrypt(plaintext, key)  
    ciphertext_label.config(text="Cipherteks: " + ciphertext)  
# Fungsi untuk menangani klik tombol "Dekripsi"
def decrypt_button_click():
    ciphertext = ciphertext_entry.get()  
    key = int(key_entry.get()) 
    plaintext = decrypt(ciphertext, key)  
    plaintext_label.config(text="Plainteks: " + plaintext)  
app = tk.Tk()  
app.title("Transposition Cipher App")  

# Label dan Entri untuk plainteks
plaintext_label = Label(app, text="Masukkan Plainteks:")
plaintext_label.pack()
plaintext_entry = Entry(app)
plaintext_entry.pack()

# Label dan Entri untuk kunci
key_label = Label(app, text="Masukkan Kunci:")
key_label.pack()
key_entry = Entry(app)
key_entry.pack()

# Tombol "Enkripsi" yang memanggil fungsi encrypt_button_click saat ditekan
encrypt_button = Button(app, text="Enkripsi", command=encrypt_button_click)
encrypt_button.pack()

# Label untuk menampilkan hasil enkripsi
ciphertext_label = Label(app, text="Cipherteks: ")
ciphertext_label.pack()

# Label dan Entri untuk cipherteks
ciphertext_label = Label(app, text="Masukkan Cipherteks:")
ciphertext_label.pack()
ciphertext_entry = Entry(app)
ciphertext_entry.pack()

# Tombol "Dekripsi" yang memanggil fungsi decrypt_button_click saat ditekan
decrypt_button = Button(app, text="Dekripsi", command=decrypt_button_click)
decrypt_button.pack()

# Label untuk menampilkan hasil dekripsi
plaintext_label = Label(app, text="Plainteks: ")
plaintext_label.pack()

app.mainloop()  
