with open("data.txt", "r") as f:
    baris_pertama = f.readline()
print("Baris pertama:", baris_pertama.strip())
print("File tertutup:", f.closed)
