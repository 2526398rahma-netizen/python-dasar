with open("contoh.txt", "w") as f:
    f.write("Halo dari Rahma\n")
    f.write("Jumlah jeruk: 8\n")

with open("contoh.txt", "r") as f:
    for baris in f:
        print(baris.strip())
