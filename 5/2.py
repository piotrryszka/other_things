from abc import ABC, abstractmethod

class Ptak(ABC):
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Jestem", self.gatunek, ". Startuje i będę leciał z prędkością: ", self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek, iloscP=50):
        super().__init__(gatunek, 0)
        self.iloscP = iloscP

    def wydajOdglos(self):
        print("kokokokokok")

    def lataj(self):
        print("Jestem", self.gatunek, ".Ja niestety nie latam.")


class Orzel(Ptak):
    def wydajOdglos(self):
        print("piiiii")

    def poluj(self):
        print("Rozpoczynam polowanie!")


k = Kura("kura",100)
k.wydajOdglos()
k.lataj()
print(k.iloscP)

o = Orzel("Orzeł", 10)
o.poluj()
