from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Konversi Bilangan")

        # Mengatur ukuran window dan posisi tengah layar
        self.master.geometry("600x400")

        # Frame utama
        self.main_frame = Frame(self.master)
        self.main_frame.pack(expand=True, fill=BOTH)

        # Frame untuk widget input
        self.input_frame = Frame(self.main_frame)
        self.input_frame.pack(pady=15)

        # Label untuk memasukkan angka
        self.label1 = Label(self.input_frame, text="Masukkan Angka:", font=("Arial", 12))
        self.label1.pack(side=LEFT, padx=10)

        # Entry untuk memasukkan angka
        self.entry1 = Entry(self.input_frame, width=25, font=("Arial", 12))
        self.entry1.pack(side=LEFT, padx=10)
        self.entry1.bind("<Return>", lambda event: self.convert())  # Menambahkan keyboard binding pada tombol enter

        # Frame untuk memilih jenis bilangan
        self.option_frame = Frame(self.main_frame)
        self.option_frame.pack(pady=15)

        # Label untuk memilih jenis bilangan
        self.label2 = Label(self.option_frame, text="Pilih Jenis Bilangan:", font=("Arial", 12))
        self.label2.pack(side=LEFT, padx=10)

        # Option Menu untuk memilih jenis bilangan
        self.options = ["Desimal", "Biner", "Oktal", "Heksadesimal", "ASCII"]
        self.variable = StringVar(self.master)
        self.variable.set(self.options[0])
        self.option_menu = OptionMenu(self.option_frame, self.variable, *self.options)
        self.option_menu.config(width=10, font=("Arial", 12))
        self.option_menu.pack(side=LEFT, padx=10)

        # Frame untuk tombol konversi
        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(pady=15)

        # Button untuk konversi
        self.button = Button(self.button_frame, text="Konversi", command=self.convert, width=10, font=("Arial", 12))
        self.button.pack(side=LEFT, padx=10)

        # Frame untuk menampilkan hasil konversi
        self.result_frame = Frame(self.master)
        self.result_frame.pack(pady=10)

        # Label untuk menampilkan hasil konversi
        self.label3 = Label(self.result_frame, text="", font=("Arial", 14), width=45, height=10, anchor=NW, justify=CENTER)
        self.label3.pack(side=LEFT, padx=5)

    
    def convert(self):
        try: 
            # Mengambil angka dan jenis bilangan dari input
            num = self.entry1.get()
            base = self.variable.get()
        
            # Konversi bilangan
            if base == "Desimal":
                bin_num = bin(int(num))[2:]
                oct_num = oct(int(num))[2:]
                hex_num = hex(int(num))[2:].upper()
                ASCII_num = chr(int(num))
            elif base == "Biner":
                dec_num = int(num, 2)
                oct_num = oct(dec_num)[2:]
                hex_num = hex(dec_num)[2:].upper()
                ASCII_num = chr(dec_num)
            elif base == "Oktal":
                dec_num = int(num, 8)
                bin_num = bin(dec_num)[2:]
                hex_num = hex(dec_num)[2:].upper()
                ASCII_num = chr(dec_num)
            elif base == "Heksadesimal":
                dec_num = int(num, 16)
                bin_num = bin(dec_num)[2:]
                oct_num = oct(dec_num)[2:]
                ASCII_num = chr(dec_num)
            elif base == "ASCII":
                dec_num = ord(num)
                bin_num = bin(dec_num)[2:]
                oct_num = oct(dec_num)[2:]
                hex_num = hex(dec_num)[2:].upper()
        
            # Menampilkan hasil konversi
            if base == "Desimal":
                self.label3.config(text = "Biner: " + bin_num + "\nOktal: " + oct_num + "\nHeksadesimal: " + hex_num + "\nASCII: " + ASCII_num)
            elif base == "Biner":
                self.label3.config(text="Desimal: " + str(dec_num) + "\nOktal: " + oct_num + "\nHeksadesimal: " + hex_num + "\nASCII: " + ASCII_num)
            elif base == "Oktal":
                self.label3.config(text="Desimal: " + str(dec_num) + "\nBiner: " + bin_num + "\nHeksadesimal: " + hex_num + "\nASCII: " + ASCII_num)
            elif base == "Heksadesimal":
                self.label3.config(text="Desimal: " + str(dec_num) + "\nBiner: " + bin_num + "\nOktal: " + oct_num + "\nASCII: " + ASCII_num)
            elif base == "ASCII":
                self.label3.config(text="Desimal: " + str(dec_num) + ", Biner: " + bin_num + ", Oktal: " + oct_num + ", Heksadesimal: " + hex_num)

        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")
    

root = Tk()
app = App(root)
root.mainloop()