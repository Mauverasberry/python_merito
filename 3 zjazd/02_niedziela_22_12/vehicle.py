class Vehicle:
    def __init__(self, mark, model, year, color=None):
        self.mark = mark
        self.model = model
        self.year = year
        self.color = color

    def __str__(self): #metoda magiczna str pozwala na podmiane tekstu wyswietlanego podczas drukowania obiektu
        return f'Jestem obiekt z klasy Vehicle  - marka {self.mark}'

    def honk(self):
        print(f"Samochód {self.color} {self.mark} trąbi")


    vehicle = Vehicle('BMW', 'e30', 2000, 'niebieski')
    vehicle.honk()
    print(vehicle)


