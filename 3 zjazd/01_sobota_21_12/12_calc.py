class Calc:

    # def __init__(self):  #konstruktor nie jest tu potrzebny
    #     pass

    @staticmethod #dekorator - metoda statyczna - nie musimy dzieki temu tworzyc obiektu z tej klasy tylko uzywać to jako funkcji
    def add(a,b):  #self jest zbędne
        return float(a)+ float(b)
    @staticmethod
    def mul(a,b):
        return float(a)*float(b)


# print(Calc().add(0.1, 0.2)) standardowe wywoływanie obiektu
print(Calc.add(0.1,0.2)) # wywolywanie przy metodzie statycznej  - bez ()
print(Calc.mul(4,2))