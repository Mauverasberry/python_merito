class Samochod:
    def __init__(self, marka, model, kolor, rocznik):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.rocznik = rocznik
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

samochod1 = Samochod("Fiat", "126p", 'czerwony', 1980)
samochod2 = Samochod('BMW', 'E30', "niebieski", 2000)

while True:
    samochod = int(input('ktory samochod (1-2):   '))
    co = int(input('Co ma zrobic (1-przyspiesz, 2-hamuj):  '))
    if samochod == 1:
        if co == 1:
            samochod1.przyspiesz()
        elif co == 2:
            samochod1.hamuj()
    elif samochod == 2:
        if co == 1:
            samochod2.przyspiesz()
        elif co == 2:
            samochod2.hamuj()
