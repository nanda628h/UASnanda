from tabulate import tabulate

class ViewMahasiswa:
    def __init__(self):
        pass

    def tampil_data(self, data):
        header = ["NIM", "Nama", "Nilai"]
        print(tabulate(data, header, tablefmt="grid"))

    def input_data(self):
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        nilai = input("Masukkan Nilai: ")
        return nim, nama, nilai

    def error_message(self, pesan):
        print(f"Error: {pesan}")
