class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.predkosc = 0

    def przedstaw_sie(self):
        print(f'Samochod {self.marka} {self.model}')

    def hamuj(self):
        if self.predkosc > 0:
            self.predkosc -= 10
            print(f"Samochod {self.marka}{self.model} hamuje do predkosci {self.predkosc} km/h")
        else:
            print(f'Samochod {self.marka} już stoi.')

    def przyspiesz(self):
        self.predkosc += 10
        print(f"Samochod {self.marka}{self.model} przyspiesza do predkosci {self.predkosc} km/h")

class Swiat:
    def __init__(self):
        self.samochody = []
        self.ile = int(input('Ile samochodów dodać do świata?  '))
        for i in range(self.ile):
            marka = input(f'Marka {i} samochodu:  ')
            model = input(f'Model {i} samochodu:  ')
            self.samochody.append(Samochod(marka, model))
        self.zycie() #inicjalizacja programu sposob 2 Swiat() na koncu

    def zycie(self):
        while True:
            ktory = int(input(f'ktory samochod (0-{self.ile-1}):   '))
            co = int(input('Co ma zrobic (1-przyspiesz, 2-hamuj):  '))
            if co == 1:
                self.samochody[ktory].przyspiesz()
            elif co == 2:
                self.samochody[ktory].hamuj()

# Swiat().zycie() #inicjalizacja programu 1 sposob
# Swiat() # a na koncu initu self.zycie - 2 sposób inicjalizacji programu

if __name__ == '__main__':     # 3sposob a na koncu initu self.zycie - 2 sposób inicjalizacji programu
    Swiat()


