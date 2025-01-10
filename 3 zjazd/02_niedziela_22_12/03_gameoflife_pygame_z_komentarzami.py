import random  # Import modułu random do generowania losowych liczb (0 lub 1 dla komórek).
from time import sleep  # Import funkcji sleep do wstrzymywania programu no określony czas
import pygame  # Import biblioteki pygame do graficznej wizualizacji.

# Definicja klasy reprezentującej grę w życie Conwaya.
class GameOfLife:
    def __init__(self, width, height, cell_size=10):  # Konstruktor klasy z wymiarami planszy i rozmiarem komórki.
        self.width = width  # Szerokość planszy w liczbie komórek.
        self.height = height  # Wysokość planszy w liczbie komórek.
        self.cell_size = cell_size  # Rozmiar jednej komórki w pikselach.

        pygame.init()  # Inicjalizacja modułów pygame.
        # Ustawienie okna gry o wymiarach (szerokość*rozmiar komórki, wysokość*rozmiar komórki).
        self.screen = pygame.display.set_mode((self.width * self.cell_size, self.height * self.cell_size))
        pygame.display.set_caption('Gra w życie')  # Ustawienie tytułu okna gry.

        # Tworzenie siatki (grid) z losowymi wartościami 0 (martwa komórka) lub 1 (żywa komórka).
        self.grid = [[random.randint(0, 1) for _ in range(self.width)] for _ in range(self.height)]

    def count(self, x, y):  # Metoda licząca liczbę żywych sąsiadów dla komórki (x, y).
        count = 0  # Inicjalizacja licznika sąsiadów.
        for j in range(y - 1, y + 2):  # Iteracja po wierszach sąsiednich.
            if j == self.height:  # Obsługa zawijania planszy w pionie.
                j = 0 # służy do obsługi przypadku, gdy j (pozioma współrzędna sąsiada komórki) przekroczy granicę planszy na dole.
            for i in range(x - 1, x + 2):  # Iteracja po kolumnach sąsiednich.
                if i == self.width:  # Obsługa zawijania planszy w poziomie.
                    i = 0
                # Sprawdzenie, czy sąsiad jest żywy i nie jest to sama komórka (x, y).
                if self.grid[j][i] == 1 and (x != i or y != j):
                    count += 1  # Zwiększenie licznika żywych sąsiadów.
        return count  # Zwrócenie liczby żywych sąsiadów.

    def update(self):  # Metoda aktualizująca stan planszy zgodnie z regułami gry.
        # Tworzenie nowej, pustej planszy (wszystkie komórki martwe).
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):  # Iteracja po wierszach planszy.
            for x in range(self.width):  # Iteracja po kolumnach planszy.
                if self.grid[y][x] == 1:  # Jeśli komórka jest żywa:
                    # Pozostaje żywa, jeśli ma 2 lub 3 żywych sąsiadów.
                    if self.count(x, y) == 2 or self.count(x, y) == 3:
                        new_grid[y][x] = 1
                else:  # Jeśli komórka jest martwa:
                    # Ożywa, jeśli ma dokładnie 3 żywych sąsiadów.
                    if self.count(x, y) == 3:
                        new_grid[y][x] = 1
        self.grid = new_grid  # Nadpisanie starej planszy nową planszą.

    def print(self):  # Metoda drukująca planszę w terminalu.
        for y in self.grid:  # Iteracja po wierszach planszy.
            for x in y:  # Iteracja po komórkach w wierszu.
                if x == 1:  # Jeśli komórka jest żywa:
                    print('*', end='')  # Drukowanie gwiazdki bez przechodzenia do nowej linii.
                else:  # Jeśli komórka jest martwa:
                    print('.', end='')  # Drukowanie kropki bez przechodzenia do nowej linii.
            print()  # Przejście do nowej linii po każdym wierszu.

    def display(self):  # Metoda rysująca planszę w oknie pygame.
        self.screen.fill((0, 0, 0))  # Wypełnienie ekranu czarnym kolorem.
        for y in range(self.height):  # Iteracja po wierszach planszy.
            for x in range(self.width):  # Iteracja po komórkach w wierszu.
                if self.grid[y][x] == 1:  # Jeśli komórka jest żywa:
                    # Rysowanie białego prostokąta reprezentującego żywą komórkę.
                    pygame.draw.rect(
                        self.screen, 'white',
                        (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                    )

if __name__ == '__main__':  # Blok uruchamiany tylko przy bezpośrednim uruchomieniu skryptu.
    game = GameOfLife(30, 30)  # Tworzy grę z planszą 30x30 komórek.
    run = True  # Flaga sterująca pętlą gry.
    while run:  # Nieskończona pętla gry.
        for event in pygame.event.get():  # Iteracja po zdarzeniach pygame.
            if event.type == pygame.QUIT:  # Jeśli użytkownik zamknie okno gry:
                run = False  # Zakończ pętlę gry.
        pygame.display.flip()  # Aktualizuje ekran pygame.
        game.print()  # Wyświetla planszę w terminalu.
        game.display()  # Wyświetla planszę w oknie graficznym pygame.
        game.update()  # Aktualizuje stan planszy zgodnie z regułami gry.
        sleep(0.5)  # Wstrzymuje program na 0.5 sekundy przed kolejną iteracją.

