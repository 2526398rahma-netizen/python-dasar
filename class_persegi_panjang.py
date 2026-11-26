class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

kotak = PersegiPanjang(8, 5)
print("Luas:", kotak.luas())
print("Keliling:", kotak.keliling())
