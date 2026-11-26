jumlah_jeruk = 8
print(jumlah_jeruk)
del jumlah_jeruk
print("Variabel sudah dihapus")
try:
    print(jumlah_jeruk)
except NameError:
    print("jumlah_jeruk tidak ditemukan")
