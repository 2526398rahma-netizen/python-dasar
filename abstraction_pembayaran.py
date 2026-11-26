from abc import ABC, abstractmethod

class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass

class Tunai(Pembayaran):
    def bayar(self, jumlah):
        print("Bayar tunai sebesar", jumlah)

class Transfer(Pembayaran):
    def bayar(self, jumlah):
        print("Bayar transfer sebesar", jumlah)

for metode in [Tunai(), Transfer()]:
    metode.bayar(28000)
