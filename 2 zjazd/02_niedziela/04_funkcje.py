

# parametry z domyslna wartoscia musza byc na koncu ()
def net_salary(age, gross_salary=3000, year=2024):  # =2024 domyslna wartosc
    if age < 26:
        return f' w toku {year} wyplata wynosi {gross_salary}'
    return f' w toku {year} wyplata wynosi {gross_salary*.8}'
    #.8= 0.8

print(net_salary(5000, 40)) #rok domyslny ale mozna wpisac inny
print(net_salary(5000, year=2021)) # gdy chcemy w pisac inna niekolejną wartosc
print(net_salary(year=2021, age=5000)) #gdy sami wpisujemy mozna zamieniac kolenosc


