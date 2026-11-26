import inquirer
from data import sesi, daftar_user, daftar_buku
from template import TABEL_KERANJANG
from utils import clear_terminal, konfirmasi, tampilkan_tabel 

username = 'usertofu1'
sesi['username'] = username
sesi['data'] = daftar_user[sesi['username']]

def tampilkan_keranjang(sesi):
    if not sesi['data']['keranjang']:
        print("Keranjang masih kosong!")
        return
    tampilkan_tabel({sesi['username']:sesi['data']}, TABEL_KERANJANG)

def tambah_keranjang(sesi, daftar):
    pertanyaan = [
        inquirer.List(
            name = 'pilih_buku',
            message = 'Pilih buku untuk ditambah ke keranjang.',
            choices = [isi['identitas']['judul'] for idbuku, isi in daftar.items() if idbuku not in sesi['data']['keranjang']] + ['Kembali']
        )
    ]
    jawaban = inquirer.prompt(pertanyaan)
    for idbuku in daftar_buku:
        if jawaban['pilih_buku'] == daftar_buku[idbuku]['identitas']['judul']:
            buku = idbuku
    if not jawaban or jawaban['pilih_buku'] == 'Kembali':
        return
    sesi['data']['keranjang'].append(buku)
    print(f"\nBuku {jawaban['pilih_buku']} telah masuk ke keranjang!")

def hapus_keranjang(sesi):
    isi_keranjang =[]
    for buku in sesi['data']['keranjang']:
        isi_keranjang.append(daftar_buku[buku]['identitas']['judul'])
    
    pertanyaan = [
        inquirer.List(
            name = 'pilih_buku',
            message = 'Pilih buku untuk dihapus.',
            choices = isi_keranjang + ['Kembali']
        )
    ]
    jawaban = inquirer.prompt(pertanyaan)
    buku = jawaban['pilih_buku']
    if not jawaban or buku == 'Kembali':
        return
    sesi['data']['keranjang'].pop(buku)
    print(f"\nBuku {buku} dihapus dari keranjang!")

clear_terminal()
tampilkan_keranjang(sesi)
tambah_keranjang(sesi, daftar_buku)
tampilkan_keranjang(sesi)
hapus_keranjang(sesi)
tampilkan_keranjang(sesi)

def pembayaran():
    pass

def hitung_diskon():
    pass

def tambah_saldo():
    pass

def gabung_membership():
    pass

def tampilkan_buku():
    pass

def tambah_buku():
    pass

def edit_buku():
    pass

def hapus_buku():
    pass

def tampilkan_diskon():
    pass

def tambah_diskon():
    pass

def edit_diskon():
    pass

def hapus_diskon():
    pass

