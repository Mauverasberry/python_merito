class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.predkosc = 0

    def print(self):
        print(f"Samochod {self.marka} {self.model}, predkość {self.predkosc} km/h")

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

    def get_predkosc(self):
        return self.predkosc

    def set_predkosc(self, nowa_predkosc):
        if nowa_predkosc >= 0 and nowa_predkosc <= 200:
            self.predkosc = nowa_predkosc


if __name__ == '__main__':
    print('test')
    samochod = Samochod('BMW', 'e30')
    samochod.print()
    # samochod.predkosc = -100 # tak sie nie powinno robic
    samochod.set_predkosc(-100) # tylko tak
    samochod.print()

