class Rekening:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("Saldo tidak boleh negatif")

r = Rekening("Rahma", 10000)
print(r.pemilik)
print(r.get_saldo())
r.set_saldo(-500)
r.set_saldo(25000)
print(r.get_saldo())
try:
    print(r.__saldo)
except AttributeError:
    print("Atribut private tidak bisa diakses langsung")
