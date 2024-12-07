
numbers = []
while True:
    try:
        for i in range (3):
            number = float(input(f'Podaj liczbę nr {i+1}: '))
            numbers.append(number)
        break
    except:
        print('Proszę podać poprawne liczby')

print(f'Średnia Twoich liczb to : {((numbers[0] + numbers[1] + numbers[2])/3)}')

