# zadanie często bywa na rozmowach rekrutacyjnych
# program przyjmuje dowolnie długą liczbę i zwraca sumę cyfr

while True:
    try:
        number = int(input('Podaj dowolną liczbę:  '))
        break
    except:
     print('Jeszcze raz')

str_number = str(number)
sum = 0
for digit in str_number:
   sum += int(digit)
print(f'Suma cyfr to {sum}')