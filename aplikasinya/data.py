sesi = {}

daftar_user = {
    'admintofu' : {
        'role' : 'admin',
        'password' : 'admin123',
        'saldo' : 0,
        'membership' : {
            'aktif' : True,
            'total_hari' : 500,
            'total_belanja' : None
        },
        'diskon_aktif' : None,
        'keranjang' : None
    },
    'usertofu1' : {
        'role' : 'pengguna',
        'pasword' : 'user123',
        'saldo' : 1000000,
        'membership' : {
            'aktif' : True,
            'total_hari' : 100,
            'total_belanja' : 1 #tetap dihitung meski blm join membership
        },
        'diskon_aktif' : [
            'D001'
        ],
        'keranjang' : [ #buku yg sama bisa masuk keranjang berbeda dalam satu waktu,
            'B001'      #jika user1 membayar buku lebih dahulu, ketersediaan buku berubah False
        ]               #user 2 tidak bisa bayar bukunya/di-skip di kasir,
    },                  #walau buku tsb. masih ada di keranjang (kayak shopee)
    'usertofu2' : {
        'role' : 'pengguna',
        'password' : 'user234',
        'saldo' : 50000,
        'membership' : {
            'aktif' : False,
            'total_hari' : 100,
            'total_belanja' : 11
        },
        'diskon_aktif' : None,
        'keranjang' : [
            'B001'
        ]
    }
}

daftar_buku = {
    'B001' : {
        'identitas' : {
            'judul' : 'Gintama, Volume 1',
            'pengarang' : 'Hideaki Sorachi',
            'tahun_terbit' : '2007',
            'penerbit' : 'Viz Media',
            'bahasa' : 'Inggris',
            'seri' : '1'
        },
        'konten' : {
            'genre' : 'fiksi fantasi',
            'target_usia' : 'remaja',
            'kata_kunci' : ['manga', 'samurai', 'alien']
        },
        'harga' : 20000,
        'ketersediaan' : True
    },
    'B002' : {
        'identitas' : {
            'judul' : 'Gintama, Volume 2',
            'pengarang' : 'Hideaki Sorachi',
            'tahun_terbit' : '2007',
            'penerbit' : 'Viz Media',
            'bahasa' : 'Inggris',
            'seri' : '2'
        },
        'konten' : {
            'genre' : 'fiksi fantasi',
            'target_usia' : 'remaja',
            'kata_kunci' : ['manga', 'samurai', 'alien']
        },
        'harga' : 20000,
        'ketersediaan' : True
    }
}

diskon = {
    'D001' : {
        'nama_diskon' : 'Diskon 50% Pengguna Baru',
        'nilai' : 0.50,
        'durasi' : '7 hari', #durasi setelah aktivasi
    }
}