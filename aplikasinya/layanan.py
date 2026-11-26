import inquirer
from data import sesi, daftar_user, daftar_buku, daftar_diskon
from template import TABEL_KERANJANG
from utils import clear_terminal, konfirmasi, jadikan_rupiah, tampilkan_tabel 

###untuk tes. hapus setelah selesai
username = 'usertofu1'
sesi['username'] = username
sesi['data'] = daftar_user[sesi['username']]
###

def tampilkan_keranjang(sesi):
    if not sesi['data']['keranjang']:
        print("Keranjang masih kosong!")
        return
    tampilkan_tabel({sesi['username']:sesi['data']}, TABEL_KERANJANG)

def tambah_keranjang(sesi, daftar):
    pertanyaan = [
        inquirer.List(
            name = 'pilih_buku',
            message = 'Pilih buku untuk ditambah ke keranjang',
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
    pertanyaan = [
        inquirer.List(
            name = 'pilih_buku',
            message = 'Pilih buku untuk dihapus',
            choices = [daftar_buku[idbuku]['identitas']['judul'] for idbuku in sesi['data']['keranjang'] ] + ['Kembali']
        )
    ]
    jawaban = inquirer.prompt(pertanyaan)
    if not jawaban or jawaban['pilih_buku'] == 'Kembali':
        return
    for idbuku in daftar_buku:
        if jawaban['pilih_buku'] == daftar_buku[idbuku]['identitas']['judul']:
            sesi['data']['keranjang'].remove(idbuku)
            print(f"\nBuku {jawaban['pilih_buku']} dihapus dari keranjang!")

def pembayaran(sesi):
    harga_kotor, jumlah_item = hitung_diskon(sesi, diskon_dipakai=False)

    print(f"""
Memproses {jumlah_item} item.
Total harga {jadikan_rupiah(harga_kotor)}!")
""")
    if sesi['data']['diskon_aktif']:
        print("Anda memiliki diskon di tas anda!")
        diskon_tersedia = [daftar_diskon[diskon]['nama_diskon'] for diskon in sesi['data']['diskon_aktif']]
        pilihan = [diskon_tersedia] + ['Tidak Pakai Diskon', 'Batalkan Pembayaran']
        pertanyaan = [
            inquirer.Checkbox(
                name = 'pilih_diskon',
                message = 'Pakai diskon',
                choices = pilihan
            )
        ]
        jawaban = inquirer.prompt(pertanyaan)
        if jawaban['pilih_diskon'] == 'Batalkan Pembayaran':
            return
        elif not jawaban or jawaban['pilih_diskon'] == 'Tidak Pakai Diskon':
            diskon_dipakai = False
        else:
            diskon_dipakai = jawaban['pilih_diskon']
    else:
        print("Tidak ada diskon di dalam tas.")
        diskon_dipakai = False
    
    harga_bersih, jumlah_item = hitung_diskon(sesi, diskon_dipakai)
    print(f"""
Memproses {jumlah_item} item.
Total harga {jadikan_rupiah(harga_bersih)}!")
""")

def hitung_diskon(sesi, diskon_dipakai):
    harga_total = 0
    jumlah_item = 0
    for idbuku in sesi['data']['keranjang']:
        if daftar_buku[idbuku]['tersedia']:
            harga_terdiskon = daftar_buku[idbuku]['harga']
            for diskon in daftar_buku[idbuku]['diskon_universal']:
                harga_terdiskon += harga_terdiskon - daftar_buku[idbuku]['harga']/daftar_diskon[diskon]['nilai']
            harga_total += harga_terdiskon
            jumlah_item += 1

    if diskon_dipakai:
        for diskon in diskon_dipakai:
            harga_total += harga_total - harga_total/daftar_diskon[diskon]['nilai']

    return harga_total, jumlah_item

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

