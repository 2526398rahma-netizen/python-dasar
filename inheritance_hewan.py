class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print(self.nama, "bersuara")

class Kucing(Hewan):
    pass

k = Kucing("Mimi")
k.bersuara()
