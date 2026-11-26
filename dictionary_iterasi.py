siswa = {"nama": "Rahma", "sekolah": "SMKN 2 Subang", "buah_favorit": "jeruk"}
for kunci in siswa:
    print("Kunci:", kunci)
for nilai in siswa.values():
    print("Nilai:", nilai)
for kunci, nilai in siswa.items():
    print(kunci, "->", nilai)
