from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        return "Meong"

class Anjing(Hewan):
    def suara(self):
        return "Guk"

for h in [Kucing(), Anjing()]:
    print(h.suara())

try:
    h = Hewan()
except TypeError:
    print("Class abstrak tidak bisa dibuat objeknya")
