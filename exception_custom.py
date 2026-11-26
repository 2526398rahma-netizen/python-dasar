class SaldoKurangError(Exception):
    pass

def tarik(saldo, jumlah):
    if jumlah > saldo:
        raise SaldoKurangError("Saldo tidak cukup")
    return saldo - jumlah

try:
    tarik(10000, 25000)
except SaldoKurangError as e:
    print("Error:", e)

print(tarik(10000, 3000))
