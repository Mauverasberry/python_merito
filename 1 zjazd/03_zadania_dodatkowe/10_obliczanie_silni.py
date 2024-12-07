# Napisz program, który obliczy silnię dla podanej liczby całkowitej.

# 2! = 1 *2
# 3! = 1 *2 *3
# 4! = 1 *2 *3 *4

num = int(input('Wprowadź liczbę:  '))

# Inicjalizujemy zmienną do przechowywania silni
silnia = 1

if num < 0:
    print('Silnia nie może być liczbą ujemną')
elif num == 0 or num== 1:
    print(f'Silnia z {num} równa się 1')
else:
    for i in range(1, num +1):
        silnia *= i

    print(f'Silnia z {num} równa się {silnia}')