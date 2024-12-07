# sprawdz, czy wprowadzone słowo jest anagramem
# sprawdz to dla listy wprowadzonych słów - np. z 10 słów 6 jest anagramem a 4 nie

word = input('Wprowadź słowo:  ')
# word = word.replace(' ' , '').lower() #zamienia spacje na brak znaku i wsio na male - zrobione w prostszym sposobie

no_of_interations = len(word)  //2  # część całkowita z dzielenia

# for i in range(no_of_interations):
#     if word[i] != word[-1-i]:
#         print('nok')
#         break
#     else:
#         print('ok')

# prostszy sposób
if word.replace(' ', '').lower() == word [::-1].replace(' ', '').lower():  # [::-1] - slowo od poczatku do  końca co -1 #zamien spacje na prosty znak + male litery
    print('ok')
else:
    print('nok')
