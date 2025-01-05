# Tugas UAS
Buatlah program sederhana dengan ketentuan:
• Program harus dibuat dengan konsep modular dan OOP (pisahkan
class data, class view, dan class process)
• Program harus meminta input dari pengguna
• Tambahkan validasi input (dapat menggunakan konsep eksepsi)
• Program menapilkan hasil (dapat berupa table view)

## Kode Program 
1. Data.py
``` python
class DataMahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai
```
2. View.py
``` python
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
```
3. process.py
``` python
from data import DataMahasiswa
from view import ViewMahasiswa

class ProcessMahasiswa:
    def __init__(self):
        self.view = ViewMahasiswa()
        self.data_mahasiswa = []

    def tambah_data(self):
        try:
            nim, nama, nilai = self.view.input_data()
            nilai = float(nilai)
            if nilai < 0 or nilai > 100:
                self.view.error_message("Nilai harus antara 0-100")
            else:
                self.data_mahasiswa.append(DataMahasiswa(nim, nama, nilai))
        except ValueError:
            self.view.error_message("Nilai harus berupa angka")

    def tampil_data(self):
        data = [(d.nim, d.nama, d.nilai) for d in self.data_mahasiswa]
        self.view.tampil_data(data)
```
4. main.py
``` python
from process import ProcessMahasiswa

def main():
    proses = ProcessMahasiswa()
    while True:
        print("\n1. Tambah Data")
        print("2. Tampil Data")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            proses.tambah_data()
        elif pilihan == "2":
            proses.tampil_data()
        elif pilihan == "3":
            break
        else:
            print("Menu tidak tersedia")

if __name__ == "__main__":
    main()
```
## penjelasan program

1. data.py
Kode ini mendefinisikan kelas DataMahasiswa, yang digunakan untuk merepresentasikan data seorang mahasiswa.
Tujuan: Kelas ini bertindak sebagai blueprint untuk objek mahasiswa dengan atribut:
nim (Nomor Induk Mahasiswa),
nama (Nama Mahasiswa),
nilai (Nilai Mahasiswa).
Fungsi __init__: Konstruktor yang akan diinisialisasi setiap kali objek DataMahasiswa dibuat.


Berikut penjelasan masing-masing kode:

1. data.py
Kode ini mendefinisikan kelas DataMahasiswa, yang digunakan untuk merepresentasikan data seorang mahasiswa.

python
Copy code
class DataMahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai
Tujuan: Kelas ini bertindak sebagai blueprint untuk objek mahasiswa dengan atribut:
nim (Nomor Induk Mahasiswa),
nama (Nama Mahasiswa),
nilai (Nilai Mahasiswa).
Fungsi __init__: Konstruktor yang akan diinisialisasi setiap kali objek DataMahasiswa dibuat.

2. view.py
Kode ini menyediakan antarmuka untuk menampilkan dan mengambil input dari pengguna.

tampil_data(self, data):
Menampilkan data mahasiswa dalam bentuk tabel dengan library tabulate.
Argumen data adalah daftar tuple yang merepresentasikan mahasiswa.

input_data(self):
Mengambil input nim, nama, dan nilai dari pengguna.
Mengembalikan tuple (nim, nama, nilai).

error_message(self, pesan):
Menampilkan pesan kesalahan.

3. process.py
Kode ini mengelola proses pengolahan data mahasiswa dengan memanfaatkan DataMahasiswa dan ViewMahasiswa.

__init__:
Menginisialisasi objek ViewMahasiswa untuk interaksi dengan pengguna.
Menyediakan list kosong data_mahasiswa untuk menyimpan data mahasiswa.

tambah_data(self):
Mengambil input dari pengguna menggunakan input_data dari ViewMahasiswa.
Memvalidasi nilai agar berupa angka antara 0-100.
Jika valid, menambahkan data mahasiswa ke dalam data_mahasiswa.

tampil_data(self):
Mengonversi data di data_mahasiswa menjadi format daftar tuple.
Memanggil tampil_data dari ViewMahasiswa untuk menampilkan data.

__init__:

Menginisialisasi objek ViewMahasiswa untuk interaksi dengan pengguna.
Menyediakan list kosong data_mahasiswa untuk menyimpan data mahasiswa.
tambah_data(self):

Mengambil input dari pengguna menggunakan input_data dari ViewMahasiswa.
Memvalidasi nilai agar berupa angka antara 0-100.
Jika valid, menambahkan data mahasiswa ke dalam data_mahasiswa.

tampil_data(self):
Mengonversi data di data_mahasiswa menjadi format daftar tuple.
Memanggil tampil_data dari ViewMahasiswa untuk menampilkan data.

4. main.py
Kode ini adalah titik masuk utama untuk menjalankan aplikasi.

Fungsi main():

Membuat objek ProcessMahasiswa.
Menampilkan menu pilihan untuk pengguna.
Menjalankan proses berdasarkan input pengguna:
"1": Menambahkan data mahasiswa.
"2": Menampilkan data mahasiswa.
"3": Keluar dari aplikasi.
Selain itu, memberikan pesan jika menu tidak tersedia.
if __name__ == "__main__"::

Menjamin bahwa kode hanya dijalankan jika file ini dieksekusi langsung, bukan diimpor sebagai modul.


