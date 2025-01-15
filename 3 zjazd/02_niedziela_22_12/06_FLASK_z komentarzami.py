<!DOCTYPE html>
#Deklaracja typu dokumentu, informująca przeglądarkę, że jest to dokument HTML5
<html lang="pl">
#Otwiera znacznik HTML z ustawieniem języka na polski (pl).
<head>
#Rozpoczęcie sekcji nagłówkowej dokumentu
    <meta charset="UTF-8">
    # Ustawienie kodowania znaków na UTF-8, co pozwala na poprawne wyświetlanie polskich znaków -->
    <title>Title</title>
    # Tytuł strony, wyświetlany na karcie przeglądarki -->
</head>
<body>
# Zawiera główną zawartość strony.
    <h1> {{ hello }} </h1>
    # Nagłówek H1, którego zawartość jest zmienną {{ hello }}, przekazywaną z backendu -->
</body>
</html>

<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <table border="1">
    # Rozpoczęcie tabeli z obramowaniem o grubości 1 piksela - tak NIE robic, to tylko w celu przyspieszenia zajec
        <tr>
        # Rozpoczęcie wiersza tabeli -->
            <th>Waluta</th>
            # Nagłówek kolumny z tytułem "Waluta" -->
            <th>Przelicznik</th>
            # Nagłówek kolumny z tytułem "Przelicznik" -->
        </tr>
        {% for key, value in kursy.items() %}
        # Pętla Jinja2, która iteruje przez elementy słownika kursy, gdzie key to nazwa waluty, a value to przelicznik
            <tr>
            # Rozpoczęcie nowego wiersza tabeli -->
                <td>{{ key }}</td>
                # Wyświetla nazwę waluty.
                <td>{{ value }}</td>
               # Wyświetla przelicznik dla danej waluty.
            </tr>
        {% endfor %}
        # Koniec pętli -->
    </table>
</body>
</html>

<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Przelicznik</title>
</head>
<body>
    <form action="/przelicznik" method="post">
    # Formularz, który wysyła dane do ścieżki "/przelicznik" z metodą POST -->
    # Metoda POST jest jednym z dwóch najczęściej używanych metod HTTP (druga to GET)
    # do przesyłania danych z klienta (np. przeglądarki internetowej) do serwera.
        <input name="pln" type="number">
        # Pole do wprowadzenia kwoty w PLN
        <select name="waluta">
        # Lista rozwijana do wyboru waluty -->
            {% for key, value in kursy.items() %}
           # Pętla, która iteruje przez kursy, aby dodać opcje do listy -->
                <option>{{ key }}</option>
                # Opcja z nazwą waluty (key) -->
            {% endfor %}
        </select>
        <button>Przelicz</button>
        # Przycisk do zatwierdzenia formularza -->
    </form>
    {% if text %}
    # Sprawdzenie, czy zmienna text nie jest pusta -->
    <p>{{ text }}</p>
    # Wyświetla wynik przeliczenia, jeśli text jest dostępny
    {% endif %}
</body>
</html>


from flask import Flask, render_template, jsonify, request
# Importowanie Flask: Do tworzenia aplikacj, render_template: Do generowania stron HTML.
#jsonify: Do zwracania danych w formacie JSON, request: Do obsługi żądań HTTP

import requests
# Do wysyłania żądań HTTP do zewnętrznych API.

url = 'https://api.frankfurter.dev/v1/latest?base=PLN'
# URL do API, które zwraca aktualne kursy walut w stosunku do PLN

response = requests.get(url)
# Pobieramy dane z API.

data = response.json()
# Przekształcenie odpowiedzi z API w format JSON (Parsujemy odpowiedź na słownik w Pythonie)

print(data)
# Wydrukowanie danych kursów walut w konsoli

citys = {'Jelenia Góra': 100000, 'Warszawa': 345345345, 'Poznań': 324324}
# Słownik z miastami i przykładowymi populacjami.

app = Flask(__name__)
# Utworzenie instancji aplikacji Flask

@app.route('/')
# Dekorator, który definiuje trasę dla głównej strony aplikacji
def hello():
    a = 'Witaj Flask!'
    # Zmienna a z powitaniem
    return render_template("hello.html", hello=a)
    # Renderowanie szablonu hello.html i przekazywanie zmiennej hello

@app.route('/trasa_z_bledem_500')
# Dekorator dla trasy, która symuluje błąd serwera 500
def error_500():
    return "Wystąpił błąd serwera", 500
    # Zwracanie komunikatu o błędzie oraz kodu statusu 500

@app.route('/kursy')
# Dekorator dla trasy, która wyświetla kursy walut
def kursy():
    return render_template("kursy.html", kursy=data['rates'])
    # Renderowanie szablonu kursy.html i przekazywanie danych o kursach

@app.route('/przelicznik', methods=['GET', 'POST'])
# Dekorator dla trasy, która obsługuje zarówno metody GET, jak i POST
def przelicznik():
    text = None
    # Inicjalizacja zmiennej text jako None
    if request.method == 'POST':
        # Sprawdzenie, czy metoda żądania to POST
        pln = float(request.form['pln'])
        # Pobranie wartości z formularza i konwersja na typ float
        waluta = request.form['waluta']
        # Pobranie wybranej waluty z formularza
        przelicznik = data['rates'][waluta]
        # Pobranie przelicznika dla wybranej waluty
        text = f"{pln}PLN = {pln*przelicznik}{waluta}"
        # Ustawienie tekstu do wyświetlenia z wynikiem przeliczenia
    return render_template("przelicznik.html", kursy=data['rates'], text=text)
    # Renderowanie szablonu przelicznik.html i przekazywanie kursów oraz tekstu

@app.route('/api/kursy')
# Dekorator dla trasy, która zwraca dane kursów w formacie JSON
def api_kursy():
    return jsonify(data), 200
    # Zwracanie danych w formacie JSON oraz kodu statusu 200

@app.route('/api/city')
# Dekorator dla trasy, która zwraca dane miast w formacie JSON
def city():
    return jsonify(citys), 200
    # Zwracanie słownika citys w formacie JSON oraz kodu statusu 200

if __name__ == '__main__':
# Sprawdzenie, czy skrypt jest uruchamiany jako główny program
    app.run(debug=True)
    # Uruchomienie aplikacji Flask w trybie debugowania, co umożliwia automatyczne przeładowanie po zmianach
