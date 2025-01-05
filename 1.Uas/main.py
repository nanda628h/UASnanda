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
