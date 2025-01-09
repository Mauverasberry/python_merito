from vehicle import Vehicle

class Electric(Vehicle): #definicja klasy Electric, kt dziedziczy po klasie Vehicle
    def __init__(self, mark, model,year,battery):
        super().__init__(mark, model, year) #super - klasa nadrzędna tu Vehicle, uruchommmy jej konstruktor
        self.battery = battery

    def honk(self):
        print(f'{self.mark} inaczej trąbi') #napisauje starego honka

    def get_battery_info(self):
        print(f'Pojemność baterii {self.mark} wynosi {self.battery} Ah')

if __name__ == '__main__':
    electric = Electric('Tesla', 126, 1979, 100)
    electric.honk()
    electric.get_battery_info()


