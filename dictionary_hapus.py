siswa = {"nama": "Rahma", "sekolah": "SMKN 2 Subang", "buah_favorit": "jeruk", "jumlah_jeruk": 8}
del siswa["jumlah_jeruk"]
print(siswa)
dihapus = siswa.pop("buah_favorit")
print("Dihapus:", dihapus)
print(siswa)
