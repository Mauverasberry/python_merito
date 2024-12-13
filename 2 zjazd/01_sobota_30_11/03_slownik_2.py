# dany jest słownik, produktów dostępnych w domu i produktów potrzenych do upieczenia ciasta
#program liczy ile ciast można upiec z dostępnych skladników i pokaże krytyczny składnik

dostepne = {'mleko': 5, 'jajko': 12, 'maka': 4, 'maslo': 2, 'woda': 10}
ciasto = {'jajko' : 4, 'maka': 0.5, 'maslo': 0.6, 'mleko': 1.9}

liczba_ciast = float('inf')  # Użyj nieskończoności jako początkowej wartości
krytyczny_skladnik = None  # Zmienna do przechowywania krytycznego składnika

for skladnik in ciasto: # Program iteruje przez składniki potrzebne do upieczenia ciasta
    if skladnik in dostepne: # Dla każdego składnika sprawdza, czy jest dostępny.
        ilosc_ciast = dostepne[skladnik] // ciasto[skladnik] # Oblicza, ile ciast można upiec z danego składnika,
        if ilosc_ciast < liczba_ciast: # Jeśli obliczona liczba ciast jest mniejsza niż dotychczasowa minimalna liczba ciast
            liczba_ciast = ilosc_ciast #aktualizuje zmienną liczba_ciast
            krytyczny_skladnik = skladnik  # aktualizuje krytyczny składnik

print(f'Można upiec {liczba_ciast} ciast.')
if krytyczny_skladnik:
    print(f'Krytyczny składnik: {krytyczny_skladnik}')

