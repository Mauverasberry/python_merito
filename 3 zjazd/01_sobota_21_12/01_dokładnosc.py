
# a = int(0.1*100)
# b = int(0.2*100)
# c = int(0.3*100)
# print(a + b == c)
# print(a/100)

# a = 0.1
# b = 0.2
# ab = a + b
# c = 0.3
# e = 1e-9  # epsilon, ktory ma 1 na 9 miejscu po przecinku 0.000000009 - 1 * 10 do potegi -9
# # tolerancja błędu
#
# print(abs(ab -c) < e) #abs - odcinamy minusy - wartosc bezwzględna
# # porównanie liczb z uwzględnieniem tolerancji

from decimal import Decimal, getcontext
getcontext().prec = 28  # Ustawienie precyzji obliczeń na 28 miejsc po przecinku

number1 = Decimal('0.1') + Decimal('0.2') # oblicza sumę 0.1 i 0.2 przy użyciu typu Decimal.
number2 = Decimal('0.3')

# Porównanie liczb
are_equal = number1 == number2

print("Liczba 1:", number1)
print("Liczba 2:", number2)
print("Czy liczby są równe:", are_equal)


