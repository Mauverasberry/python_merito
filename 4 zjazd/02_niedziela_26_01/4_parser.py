import argparse

def calculate (operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Nie można dzielić przez zero!")
        return num1 / num2
    else:
        raise ValueError("Nieznana operacja! Dostępne: add, subtract, multiply, divide")

parser = argparse.ArgumentParser(description='Prosty kalkulator')
parser.add_argument('operation', type=str, help = 'dwozwolone oparacje add,, sub')
parser.add_argument('num1', type=float, help = 'Pierwsza liczba')
parser.add_argument('num2', type=float, help = 'Druga liczba')
args = parser.parse_args()


result = calculate(args.operation, args.num1, args.num2)
print(f'Wynik: {result}')
