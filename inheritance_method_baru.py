class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(self.nama, "sedang makan")

class Kucing(Hewan):
    def mengeong(self):
        print(self.nama, "mengeong")

k = Kucing("Mimi")
k.makan()
k.mengeong()
