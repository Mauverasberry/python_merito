import random
from time import sleep

class Samochod:
    def __init__(self):
        self.modyfikator = 1 #by jechał tez do tylu
        self.predkosc = 1
        self.x = 0 #pozycja

    def losuj_predkosc(self):
        self.predkosc = random.randint(1,3)

    def aktualizuj_pozycje(self):
        self.x += self.modyfikator * self.predkosc
        if self.x > 30:
            self.modyfikator = -1 #by jechal do tylu
            self.x = 29 # by nie wychodzil poza planszę
        if self.x < 0:
            self.modyfikator = 1 #by jechał do przodu znow
            self.x = 0 #by nie wychodzil poza planszę

class Swiat:
    def __init__(self):
        self.samochod = Samochod()
        self.zycie()

    def print(self):
        for x in range(30): # tworzenie planszy na 30x
            if x == self.samochod.x:
                print("*", end='') # postaw gwiazdkę i nie przchodz do nowej linii - end jest puste
            else:
                print('.', end='')
        print() #przejście do nowej linii

    def zycie(self):
        while True:
            self.print() #drukowanie planszy
            self.samochod.losuj_predkosc()
            self.samochod.aktualizuj_pozycje()
            #print(self.samochod.x)
            sleep(.3)

if __name__ == '__main__':
    Swiat()


