# Importujemy bibliotekę `random`, która pozwala generować losowe liczby i wybierać losowe elementy z list
import random

# ANSI kolory
GREEN = '\033[32m'
RED = '\033[31m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BROWN = '\033[33m'  # Brązowy pień (ten sam kod co żółty)
RESET = '\033[0m'   # Resetowanie koloru, aby wrócić do domyślnego wyglądu tekstu

height = 10
baubles = ['o', '@', '$', '*']  # Ozdoby
colors = [RED, YELLOW, BLUE, MAGENTA, CYAN]  # Dostępne kolory bombek
probability = 0.25  # Szansa na bombkę (25%)

# Rysowanie korony choinki
# Wewnątrz pętli for, jeśli losowa liczba jest mniejsza od probability,
# na danym miejscu pojawi się losowa ozdoba, w przeciwnym wypadku rysowana jest zwykła gwiazdka *.
for i in range(height):
    row = ''  # Tworzymy pusty ciąg znaków, który będzie reprezentował jedną linię choinki
    for j in range(2 * i + 1): # Iterujemy przez liczbę znaków w danej linii (rośnie z każdym poziomem)
        if random.random() < probability:   # Sprawdzamy, czy losowa liczba (0-1) jest mniejsza niż 0.25 (25% szans)
            color = random.choice(colors)  # Losowy kolor dla bombki
            row += f"{color}{random.choice(baubles)}{RESET}" # Dodajemy bombkę z losowym kolorem i symbolem
        else:
            row += f"{GREEN}*{RESET}"  # Jeśli nie ma bombki, dodajemy zielony symbol gałęzi
    print(' ' * (height - i - 1) + row)  # # Drukujemy linię choinki, przesuwając ją w prawo o odpowiednią liczbę spacji


# Rysowanie pnia
trunk_height = 2
trunk_width = 3
for i in range(trunk_height):
    print(' ' * (height - trunk_width // 2 - 1) + f"{BROWN}{'*' * trunk_width}{RESET}")
    # Drukujemy linię pnia, przesuwając ją w prawo o odpowiednią liczbę spacji, tak aby była wyrównana do środka

