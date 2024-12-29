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

samochody = []

ile = int(input('Ile samochodów dodać do świata?  '))
for i in range(ile):
    marka = input(f'Marka {i} samochodu:  ')
    model = input(f'Model {i} samochodu:  ')
    samochody.append(Samochod(marka, model))

while True:
    ktory = int(input(f'ktory samochod (0-{ile-1}):   '))
    co = int(input('Co ma zrobic (1-przyspiesz, 2-hamuj):  '))

    if co == 1:
        samochody[ktory].przyspiesz()
    elif co == 2:
        samochody[ktory].hamuj()
