def proses(nilai):
    try:
        angka = int(nilai)
        return 100 / angka
    except ValueError:
        print("Bukan angka:", nilai)
    except ZeroDivisionError:
        print("Tidak bisa dibagi nol")

print(proses("4"))
proses("jeruk")
proses("0")
