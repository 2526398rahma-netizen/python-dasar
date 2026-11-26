try:
    angka = int("8")
except ValueError:
    print("Gagal konversi")
else:
    print("Berhasil:", angka)
finally:
    print("Selesai diproses")
