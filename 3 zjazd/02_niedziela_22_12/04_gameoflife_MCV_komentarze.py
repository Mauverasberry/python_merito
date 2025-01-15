import random  # Importowanie modułu random do generowania losowych liczb
from time import sleep  # Importowanie funkcji sleep do wstrzymywania wykonania programu
import pygame  # Importowanie biblioteki Pygame do tworzenia gier

# model - zajmuje sie tylko biznesem
class GameModel:
    def __init__(self, width, height):
        self.width = width  # Ustawienie szerokości planszy
        self.height = height  # Ustawienie wysokości planszy
        # Inicjalizacja planszy jako dwuwymiarowej listy z losowymi wartościami 0 lub 1
        self.grid = [[random.randint(0, 1) for _ in range(self.width)] for _ in range(self.height)]

    def count(self, x, y):
        count = 0  # Inicjalizacja licznika sąsiadów
        # Iterowanie przez wszystkie sąsiednie komórki (w tym samą komórkę)
        for j in range(y - 1, y + 2):
            if j == self.height:  # W przypadku przekroczenia wysokości, resetowanie do 0
                j = 0
            for i in range(x - 1, x + 2):
                if i == self.width:  # W przypadku przekroczenia szerokości, resetowanie do 0
                    i = 0
                # Zliczanie sąsiadów, ignorując samą komórkę
                if self.grid[j][i] == 1 and (x != i or y != j):
                    count += 1  # Zwiększanie licznika
        return count  # Zwracanie liczby żywych sąsiadów

    def update(self):
        # Tworzenie nowej planszy z martwymi komórkami
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        # Iteracja przez wszystkie komórki planszy
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:  # Sprawdzanie, czy komórka jest żywa
                    # Utrzymanie komórki przy życiu jeśli ma 2 lub 3 żywych sąsiadów
                    if self.count(x, y) in [2, 3]:
                        new_grid[y][x] = 1  # Komórka pozostaje żywa
                else:
                    # Ożywienie komórki jeśli ma dokładnie 3 żywych sąsiadów
                    if self.count(x, y) == 3:
                        new_grid[y][x] = 1  # Komórka staje się żywa
        self.grid = new_grid  # Aktualizacja planszy do nowego stanu

    def get_grid(self):
        return self.grid  # Zwracanie aktualnego stanu planszy

# view - odpowiada za drukowanie
class GameView:
    def __init__(self, width, height, cell_size=10):
        self.width = width  # Ustawienie szerokości widoku
        self.height = height  # Ustawienie wysokości widoku
        self.cell_size = cell_size  # Ustawienie rozmiaru komórki
        pygame.init()  # Inicjalizacja Pygame
        # Ustawienie rozmiaru okna na podstawie szerokości i wysokości planszy
        self.screen = pygame.display.set_mode((self.width*self.cell_size, self.height*self.cell_size))
        pygame.display.set_caption('Gra w życie')  # Ustawienie tytułu okna

    def display(self, grid):
        self.screen.fill((0, 0, 0))  # Wyczyszczenie planszy na czarno
        # Iteracja przez wszystkie komórki planszy
        for y in range(self.height):
            for x in range(self.width):
                if grid[y][x] == 1:  # Sprawdzanie, czy komórka jest żywa
                    # Rysowanie zielonego prostokąta dla żywej komórki
                    pygame.draw.rect(self.screen, 'green', (x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size))
        pygame.display.flip()  # Odświeżenie ekranu, aby pokazać zmiany

# controller - spina widok i biznes
class GameController:
    def __init__(self, width=50, height=50, cell_size=10):
        self.model = GameModel(width, height)  # Utworzenie modelu gry
        self.view = GameView(width, height, cell_size)  # Utworzenie widoku gry
        self.run()  # Rozpoczęcie głównej pętli gry

    def run(self):
        run = True  # Flaga do kontrolowania pętli gry
        while run:  # Główna pętla gry
            for event in pygame.event.get():  # Sprawdzanie zdarzeń Pygame
                if event.type == pygame.QUIT:  # Sprawdzenie, czy użytkownik zamknął okno
                    run = False  # Zatrzymanie pętli gry
            self.view.display(self.model.get_grid())  # Wyświetlenie aktualnego stanu planszy w widoku
            self.model.update()  # Aktualizacja stanu modelu gry
            sleep(0.5)  # Wstrzymanie działania na 0.5 sekundy

# Sprawdzenie, czy skrypt jest uruchamiany jako główny program
if __name__ == '__main__':
    controller = GameController()  # Utworzenie instancji kontrolera, co uruchamia grę
