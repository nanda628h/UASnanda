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