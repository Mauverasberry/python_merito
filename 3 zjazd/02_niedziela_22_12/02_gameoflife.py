import random
from time import sleep


class GameOfLife:
    def __init__(self,width, height):   #   tworzenie planszy
        self.width = width
        self.height = height

        self.grid = [[random.randint(0,1) for _ in range(self.width)]for _ in range(self.height)]
        # to samo mozna zapisac jak niżej
        # self.grid = []  #lista siatka - plansza w kt bedziemy przetrzymywac
        # for y in range(self.height):
        #     row = []
        #     for x in range(self.width):
        #         row.append(random.randint(0,1))
        #     self.grid.append(row)
    def count(self, x,y):
        count = 0
        for j in range(y-1, y+2):
            if j  == self.height:
                j=0
            for i in range(x-1, x+2):
                if i == self.width:
                    i=0
                if self.grid[j][i] == 1 and (x != i or y != j):   # 1=True x != i - sama siebie komorka do zycia nie moze liczyc
                    count += 1
        return count

    def update(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
               if self.grid[y][x] == 1:
                   if self.count(x,y) == 2 or self.count(x,y) == 3:
                       new_grid[y][x] =1
               else:
                   if self.count(x,y) == 3:
                       new_grid[y][x] = 1
        self.grid = new_grid
        #pusta plansza, ktora uzupelnimy 1 na podstawie istnienia zycia lub nie i potem podmiana na grid

    def print(self):
        for y in self.grid:
            for x in y:
                if x ==1:
                    print('*', end='')
                else:
                    print('.', end='')
            print()



if __name__ == '__main__':
    game = GameOfLife(30,30)
    while True:
        game.print()
        game.update() #updat'uje i zlicza sąsiadów i podmienia stan komórek
        sleep(0.5)