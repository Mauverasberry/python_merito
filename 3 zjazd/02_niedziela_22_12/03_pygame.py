import random  # Importuje moduł random do generowania losowych liczb (tu: 0 lub 1).
from time import sleep  # Importuje funkcję sleep do wstrzymywania programu na określony czas.

class GameOfLife:  # Definicja klasy gry w życie Conwaya.
    def __init__(self, width, height):  # Konstruktor klasy, inicjalizuje grę.
        self.width = width  # Szerokość planszy.
        self.height = height  # Wysokość planszy.

        # Tworzy dwuwymiarową listę (grid) o wymiarach width x height, wypełnioną losowymi wartościami 0 (martwa komórka) i 1 (żywa komórka).
        self.grid = [[random.randint(0, 1) for _ in range(self.width)] for _ in range(self.height)]

    def count(self, x, y):  # Liczy liczbę żywych sąsiadów komórki na pozycji (x, y).
        count = 0  # Inicjalizuje licznik sąsiadów.
        for j in range(y-1, y+2):  # Iteruje po rzędach sąsiednich (góra, środek, dół).
            if j == self.height:  # Obsługuje zawijanie planszy w pionie (dolna krawędź zawija na górę).
                j = 0
            for i in range(x-1, x+2):  # Iteruje po kolumnach sąsiednich (lewo, środek, prawo).
                if i == self.width:  # Obsługuje zawijanie planszy w poziomie (prawa krawędź zawija na lewo).
                    i = 0
                # Sprawdza, czy sąsiadująca komórka jest żywa (1) i nie jest to sama komórka (x, y).
                if self.grid[j][i] == 1 and (x != i or y != j):
                    count += 1  # Zwiększa licznik żywych sąsiadów.
        return count  # Zwraca liczbę żywych sąsiadów.

    def update(self):  # Aktualizuje stan planszy na podstawie reguł gry.
        # Tworzy nową, pustą planszę (new_grid) wypełnioną martwymi komórkami (0).
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):  # Iteruje po każdym wierszu planszy.
            for x in range(self.width):  # Iteruje po każdej kolumnie planszy.
                if self.grid[y][x] == 1:  # Jeśli komórka jest żywa:
                    if self.count(x, y) in [2, 3]:  # Pozostaje żywa, jeśli ma 2 lub 3 żywych sąsiadów.
                        new_grid[y][x] = 1
                else:  # Jeśli komórka jest martwa:
                    if self.count(x, y) == 3:  # Ożywa, jeśli ma dokładnie 3 żywych sąsiadów.
                        new_grid[y][x] = 1
        self.grid = new_grid  # Nadpisuje starą planszę nową zaktualizowaną planszą.

    def print(self):  # Wyświetla aktualny stan planszy.
        for y in self.grid:  # Iteruje po każdym wierszu planszy.
            for x in y:  # Iteruje po każdej komórce w wierszu.
                if x == 1:  # Jeśli komórka jest żywa:
                    print("*", end="")  # Wyświetla "*" bez przechodzenia do nowej linii.
                else:  # Jeśli komórka jest martwa:
                    print(".", end="")  # Wyświetla "." bez przechodzenia do nowej linii.
            print()  # Przechodzi do nowej linii po zakończeniu wiersza.

if __name__ == '__main__':  # Blok kodu uruchamianego tylko przy bezpośrednim uruchomieniu skryptu.
    game = GameOfLife(30, 30)  # Tworzy grę z planszą o wymiarach 30x30.
    while True:  # Nieskończona pętla.
        game.print()  # Wyświetla aktualny stan planszy.
        game.update()  # Aktualizuje stan planszy zgodnie z regułami gry.
        sleep(0.5)  # Wstrzymuje program na 0.5 sekundy przed kolejną iteracją.
