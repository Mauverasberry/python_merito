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