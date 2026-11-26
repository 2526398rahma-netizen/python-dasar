class Hewan:
    def __init__(self, nama):
        self.nama = nama

class Kucing(Hewan):
    def __init__(self, nama, warna):
        super().__init__(nama)
        self.warna = warna

    def info(self):
        print(self.nama, "berwarna", self.warna)

k = Kucing("Mimi", "putih")
k.info()
