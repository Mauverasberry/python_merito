def dodawanie(a, b):
    try:
        return round(float(a) + float(b), 5)  # round(..., 5): Ostateczny wynik jest zaokrąglony do 5 miejsc po przecinku.
    except ValueError:                        # Jeśli nie można przekonwertować wartości na float, łapiemy wyjątek
        return None

