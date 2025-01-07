class Vehicle:
    def __init__(self, mark, model, year, color=None):
        self.mark = mark
        self.model = model
        self.year = year
        self.color = color

    def honk(self):
        print(f"Samochód {self.color} {self.mark} trąbi")

if __name__ == '__main__':
    vehicle = Vehicle('BMW', 'e30', 2000, 'niebieski')
    vehicle.honk()

