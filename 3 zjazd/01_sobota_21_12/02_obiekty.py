
class Samochod:
    def __init__(self, marka, model, kolor, rocznik):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.rocznik = rocznik

    def przedstaw_sie(self):
        print(f'Samochod {self.marka} {self.model}')

    def przyspiesz(self):
        print(f"Samochod {self.marka}{self.model} przyspiesza!")

samochod1 = Samochod("Fiat", "126p", 'czerwony', 1980)
samochod2 = Samochod('BMW', 'E30', "niebieski", 2000)


while True:
    samochod = int(input('ktory samochod (1-2):   '))
    if samochod == 1:
        samochod1.przedstaw_sie()
    elif samochod == 2:
        samochod2.przedstaw_sie()


