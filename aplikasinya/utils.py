from tabulate import tabulate
import inquirer
import time
import os

def clear_terminal(waktu=1, msg="Membersihkan terminal..."):
    if msg != None:
        print(msg)
    time.sleep(waktu)
    os.system('cls' if os.name == 'nt' else 'clear')

def minta_angka(minim=None, maxim=None, msg='Masukkan angka.'):
    try:
        angka = input(f"{msg}\n> ")
        if not angka:
            raise ValueError("Masukan tidak boleh kosong!")
        elif not angka.isdigit():
            raise ValueError("Masukan harus berupa angka!")

        angka = int(angka)
        if minim and angka <= minim:
            raise ValueError(f"Nilai angka minimal {minim}!")
        elif maxim and angka >= maxim:
            raise ValueError(f"Nilai angka maksimal {maxim}!")
        
    except ValueError as e:
        print(e)
        return None

    else:
        return angka

def validasi_input(msg='Masukkan input.'):
    nilai = input(f"{msg}\n> ")
    if not nilai:
        print("Nilai tidak boleh kosong!")
        return

def jadikan_rupiah(angka):
    return "Rp" + f"{angka:,}".replace(",", ".")

def buat_tabel(data, baris):
    judul = [judul for judul, x in baris]
    kolom = []
    for key, value in data.items():
        isi_kolom = []
        for y, f_lambda in baris:
            isi_kolom.append(f_lambda(key, value))
        kolom.append(isi_kolom)
    return judul, kolom

def tampilkan_tabel(data, baris, kapasitas_halaman=10, berhalaman=True):
    judul, data_kolom = buat_tabel(data, baris)
    if not data_kolom:
        print("Data masih kosong!")
        return

    if not berhalaman:
        print(tabulate(data_kolom, judul, "grid"))
        return

    total_halaman = (len(data_kolom) + kapasitas_halaman - 1) // kapasitas_halaman #hitung halaman dg. // pembulatan ke atas
    halaman_ke = 0
    while True:
        nomor_mulai = halaman_ke * kapasitas_halaman
        nomor_akhir = nomor_mulai + kapasitas_halaman
        kolom_halaman = data_kolom[nomor_mulai:nomor_akhir]

        print(f"Halaman ke-{halaman_ke}/{total_halaman}")
        print(tabulate(kolom_halaman, judul, "grid"))

        aksi = ["Halaman Sebelum", "Halaman Setelah", "Tutup"]
        pertanyaan = [
            inquirer.List(
                name = 'pilih_aksi',
                message = 'Pilih aksi untuk melanjutkan.',
                choices = aksi
            )
        ]
        jawaban = inquirer.prompt(pertanyaan)
        aksi = jawaban['pilih_aksi']

        if not jawaban or aksi == "Tutup":
            return
        elif aksi == "Halaman Sebelum" and halaman_ke > 0:
            halaman_ke -= 1
        elif aksi == "Halaman Lanjut" and halaman_ke < total_halaman - 1:
            halaman_ke += 1
        else:
            print("Berada di ujung halaman!")