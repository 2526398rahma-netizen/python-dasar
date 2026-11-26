class BankAccount:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        self.saldo += jumlah

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup")
        else:
            self.saldo -= jumlah

rekening = BankAccount("Rahma", 10000)
rekening.setor(5000)
print("Saldo:", rekening.saldo)
rekening.tarik(20000)
rekening.tarik(3000)
print("Saldo akhir:", rekening.saldo)
