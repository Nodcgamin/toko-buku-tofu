sesi = {'username':None, 'role':None, 'data':None} #simpan dict dg. username sebagai key

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
        'password' : 'user123',
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
            'B001','B002'      #jika user1 membayar buku lebih dahulu, tersedia buku berubah False
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
        'diskon_universal' : None,
        'harga' : 20000,
        'tersedia' : True
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
        'diskon_universal' : ['D002'],
        'harga' : 20000,
        'tersedia' : True
    },
    'B003' : {
        'identitas' : {
            'judul' : 'Gintama, Volume 3',
            'pengarang' : 'Hideaki Sorachi',
            'tahun_terbit' : '2007',
            'penerbit' : 'Viz Media',
            'bahasa' : 'Inggris',
            'seri' : '3'
        },
        'konten' : {
            'genre' : 'fiksi fantasi',
            'target_usia' : 'remaja',
            'kata_kunci' : ['manga', 'samurai', 'alien']
        },
        'diskon_universal' : ['D002', 'D003'],
        'harga' : 20000,
        'tersedia' : True
    }
}

daftar_diskon = {
    'D001' : {
        'nama_diskon' : 'Diskon 50% Pengguna Baru',
        'nilai' : 0.50,
        'durasi' : '7 hari', #durasi setelah aktivasi
    },
    'D002' : {
        'nama_diskon' : "Diskon 75% Selector's Pick",
        'nilai' : 0.75,
        'durasi' : '7 hari', #durasi setelah aktivasi
    },
    'D003' : {
        'nama_diskon' : 'Diskon 26%, 26 November',
        'nilai' : 0.25,
        'durasi' : '7 hari', #durasi setelah aktivasi
    }
}