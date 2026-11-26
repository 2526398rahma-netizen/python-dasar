class Hewan:
    def suara(self):
        print("Hewan bersuara")

class Kucing(Hewan):
    def suara(self):
        print("Meong")

class Anjing(Hewan):
    def suara(self):
        print("Guk")

for h in [Hewan(), Kucing(), Anjing()]:
    h.suara()
