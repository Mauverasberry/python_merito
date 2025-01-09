class Vehicle:
    def __init__(self, mark, model, year, color):
        self.mark = mark
        self.model = model
        self.__year = int(year) # pole "prywatne", nie mozna z zewnatrz podmienić chyba, że... car._Vehicle__year = 1000
        self._color = color #pole "chronione", nie powinniesmy z zewnatrz ingerowac ale funkcjonalnie można podmienić
        #uzywamy getterow i setterow

    def change_color(self, new_color):  #setter
        self._color = new_color

    def get_color(self):   #getter
        return self._color

    def get_year(self):
        return self.__year

if __name__ == '__main__':
    car = Vehicle('BMW', 'e30', 2000, 'niebieski')
    #print(car._color)
    print(car.get_color())   # używamy getera do pobierania danych z pola
    car.change_color('czerwony') # uzywamy settera do ustawienia danych
    print(car.get_color())
    car._color = 'czarny' #NIE używamy bezpośredniego odwołania do chronionych pól, bo mogą być obwarowania (warunki), kt ominiemy
    # w javie by nie przeszlo
    print(car._color)
    print(car.get_year())
    car.__year = 9999  # NIE dostaniemy się w sposób podobny do pól prywatnych
    car._Vehicle__year = 1000 #złamanie hermetyzacji pola prywatnego
    print(car.get_year()) # jest to niezalecane, ale możliwe