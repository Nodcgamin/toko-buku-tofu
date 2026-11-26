from data import daftar_buku
from utils import jadikan_rupiah

TABEL_BUKU = [
    ("Judul", lambda key, value: value['identitas']['judul']), #lambda key, value: mengembalikan
    ("Pengarang", lambda key, value: value['identitas']['pengarang']), #apapun setelah ":"
    ("Harga", lambda key, value: jadikan_rupiah(value['harga'])),
    ("Diskon", lambda key, value: ";".join(diskon for diskon in value['diskon_universal']))
    ("Tersedia?", lambda key, value: '✅' if value['tersedia'] else '❌')
]

TABEL_IDENTITAS_BUKU = TABEL_BUKU[:2] + [
    ("Tahun Terbit", lambda key, value: value['identitas']['tahun_terbit']),
    ("Penerbit", lambda key, value: value['identitas']['penerbit']),
    ("Bahasa", lambda key, value: value['identitas']['bahasa']),
    ("Seri", lambda key, value: value['identitas']['seri']),
]

TABEL_KONTEN_BUKU = [
    ("Genre", lambda key, value: value['konten']['genre']),
    ("Target Usia", lambda key, value: value['konten']['target_usia']),
    ("Kata Kunci", lambda key, value: ",".join(value['konten']['kata_kunci']))
]

TABEL_STATUS_BUKU = TABEL_BUKU[2:4]

TABEL_KERANJANG = [
    ("Nama Pengguna", lambda key, value: key),
    ("Keranjang", lambda key, value: "; ".join(daftar_buku[idbuku]['identitas']['judul'] for idbuku in value['keranjang'])) #isi keranjang adalah idbuku
]