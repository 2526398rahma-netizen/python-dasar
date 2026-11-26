class Siswa:
    def __init__(self, nama, sekolah):
        self.nama = nama
        self.sekolah = sekolah

    def perkenalan(self):
        print("Nama saya", self.nama, "dari", self.sekolah)

siswa1 = Siswa("Rahma", "SMKN 2 Subang")
siswa1.perkenalan()
print(siswa1.nama)
