# lista_zakupow = ['marchew' ,3, 'ryz',5, 'woda',3] - z cenami mozna zapisać tak
# lista_zakupow2 = [['marchew' ,3], ['ryz',5], ['woda',3]] - lepiej tak ale najlepiej słownikiem
#print(lista_zakupow2 [1][1])
# slowniki lepsze bo produkty w nich sie nie powtarzają
# lista.zakupow2.append(['marchew',4]) - marchew sie doda kolejna


slownik_zakupow = {'marchew':3, 'ryz':5, 'woda': 3}  #słownik ma pary - klucz i wartosc
print(slownik_zakupow)
# w slowniku nie ma indeksow typu slownik_zakupow[2] - nie zapisuje slownik kolejnosci

print(slownik_zakupow['marchew']) #wchodzi w klucz i zwraca w warość

# klucze nie moga sie powtarzac

slownik_zakupow['serek'] = 4 # dodaje element jesli go nie ma a jesli jest zostanie nadpisany
slownik_zakupow['marchew'] = 1 #nadpisuje wartosc istniejaca

print(slownik_zakupow)

slownik_zakupow['marchew'] += 1

print(slownik_zakupow)

# for produkt in lista_zakupow: #dla listy
#     print(produkt)

for produkt in slownik_zakupow: #puste - bedzie szedl po kluczach i je wypisze
    print(f' chcesz kupic {produkt} w ilosci {slownik_zakupow[produkt]}')  #dojście do wartosci klucza

for produkt in slownik_zakupow.keys():   #to samo co u gory
    print(f' chcesz kupic {produkt} w ilosci {slownik_zakupow[produkt]}')

for cena in slownik_zakupow.values(): #wartosci
    print(cena)

for produkt,cena  in slownik_zakupow.items(): #wszytsko
    print(f'kupujesz {produkt} w liczbie {cena}')