"""main.py - Titik masuk program Toko Buku."""

import auth
import data
import menu_admin
import menu_user


def jalankan_menu(username):
    """Membuka menu sesuai akses akun yang sedang login."""
    if data.daftar_user[username]["akses"] == "admin":
        menu_admin.menu_admin()
    else:
        menu_user.menu_user()

def main():
    print("Selamat datang di Toko Buku!")
    # Selama user berhasil login, tampilkan menunya.
    # Setelah logout, kembali ke menu awal agar akun lain bisa masuk.
    while auth.register():
        jalankan_menu(data.sesi["username"])
        data.sesi["username"] = None  # logout
    print("Terima kasih, sampai jumpa!")


if __name__ == "__main__":
    main()