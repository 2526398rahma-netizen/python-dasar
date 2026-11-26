def jumlahkan(*angka):
    return sum(angka)

def tampilkan(**data):
    for kunci, nilai in data.items():
        print(kunci, "=", nilai)

print(jumlahkan(1, 2, 3, 4))
tampilkan(nama="Rahma", buah="jeruk", jumlah=8)
