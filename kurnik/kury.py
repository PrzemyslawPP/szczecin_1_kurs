from abc import ABC, abstractmethod


class Ptak(ABC):

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print(f"Tutaj {self.gatunek}, startuje i rozpoczynam łowy.")

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Orzel(Ptak):
    def wydaj_odglos(self):
        print("piiiiii!")


class Kura(Ptak):

    def __init__(self, gatunek, jaja):
        super().__init__(gatunek, jaja)
        self.__ilosc_jaj = jaja

    def lataj(self):
        print(f"Tutaj {self.gatunek}, ja nie latam i nie poluje (jeszcze)...")

    def produkcja_jaja(self, ilosc):
        for _ in range(ilosc):
            self.__ilosc_jaj += 1
        print(f"Tu {self.gatunek}, zniosłam {self.__ilosc_jaj} jaj")

    def wydaj_odglos(self):
        print('KOKOKOK!')
