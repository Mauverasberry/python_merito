
try:
    num1 = float(input('Podaj pierwszą liczbę:  '))
    num2 = float(input('Podaj drugą liczbę:  '))
except:
    print('Wpisana wartość nie jest liczbą')

if num2 == 0:
    print('Nie można dzielić przez 0, przyjmuję, że wybrana liczba to 1')
    num2 = 1
print(f'Suma podanych cyfr to {num1+num2}, różnica: {num1-num2}, iloczyn: {num1*num2}, iloraz {num1/num2}')