
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z']

sentence = input('Wprowadź zdanie do kodowania:   ')
kod = 2
wynik = ''
for litera in sentence:
    byla_duza = False
    if litera.isupper():
        byla_duza = True
        litera = litera.lower()
    if litera in alphabet:
        alphabet_index = alphabet.index(litera)
        kodowany_index = (alphabet_index + kod) % len(alphabet)
        if byla_duza:
            wynik += alphabet[kodowany_index].upper()
        else:
            wynik += alphabet[kodowany_index]
    else:
        wynik += litera
print (wynik)