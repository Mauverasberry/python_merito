#importujemy potrzebne biblioteki:
from flask import Flask, request, jsonify  # Importujemy Flask (framework do tworzenia aplikacji webowych),
# request (do obsługi danych wejściowych) i jsonify (do zwracania odpowiedzi w formacie JSON)
from flask_sqlalchemy import SQLAlchemy  # Importujemy SQLAlchemy - narzędzie ORM (Object-Relational Mapping)
# do obsługi baz danych
from flask_cors import CORS  # Importujemy CORS, aby umożliwić dostęp z innych domen
import os  # Biblioteka os pozwala na interakcję z systemem operacyjnym

# Tworzymy instancję aplikacji Flask
app = Flask(__name__)
CORS(app)  # Włączamy CORS, aby umożliwić dostęp do API z innych domen

# Ustalamy bazowy katalog, w którym znajduje się nasza aplikacja
basedir = os.path.abspath(os.path.dirname(__file__))  # Pobieramy ścieżkę katalogu, w którym znajduje się plik
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tictactoe.db')  # Tworzymy URI do pliku bazy danych
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Wyłączamy śledzenie zmian aby zaoszczedzic zasoby

# Inicjalizujemy bazę danych
db = SQLAlchemy(app)

# Definiujemy model bazy danych dla gry
class Game(db.Model):  # Klasa reprezentuje tabelę w bazie danych
    id = db.Column(db.Integer, primary_key=True)  # Kolumna `id` (unikalne ID gry) jako klucz główny
    moves = db.Column(db.String, default="")  # Kolumna `moves` przechowuje ruchy wykonane w grze, z domyślną wartością pustego ciągu

# Tworzymy wszystkie tabele w bazie danych, jeśli jeszcze nie istnieją
with app.app_context():  # Wymaga kontekstu aplikacji
    db.create_all()

# Tworzymy endpoint do rozpoczęcia nowej gry
@app.route('/game', methods=['POST'])  # Obsługuje żądania POST pod adresem /game
def create_game():
    new_game = Game()  # Tworzymy nową grę (instancję klasy Game)
    db.session.add(new_game)  # Dodajemy nową grę do sesji bazy danych
    db.session.commit()  # Zapisujemy zmiany w bazie danych
    return jsonify({'message': 'New game created', 'game_id': new_game.id}), 201  # Zwracamy odpowiedź z informacją o utworzeniu nowej gry i jej ID

# Tworzymy endpoint do wykonania ruchu w grze na planszy
@app.route('/game/<int:game_id>/move', methods=['POST'])  # Obsługuje żądania POST z parametrem game_id
def make_move(game_id):
    game = Game.query.get(game_id)  # Pobieramy grę o podanym ID z bazy danych
    if game is None:  # Jeśli gra nie istnieje, zwracamy błąd 404
        return jsonify({'error': 'Game not found'}), 404
    move_data = request.json  # Pobieramy dane przesłane w formacie JSON
    if 'cellIndex' in move_data:  # Sprawdzamy, czy w danych ruchu jest index komórki
        cell_index = str(move_data['cellIndex'])  # Odczytujemy index komórki jako ciąg znaków

        # Sprawdzamy, czy pole jest już zajęte
        occupied_cells = [move[0] for move in game.moves]  # Pobieramy listę zajętych pól
        if cell_index in occupied_cells:  # Jeśli pole jest zajęte, zwracamy błąd
            return jsonify({'message': 'Cell is already occupied'}), 400

        # Ustalamy, który gracz wykonuje ruch (X lub O)
        player = 'O' if game.moves.count('X') > game.moves.count('O') else 'X'  # X i O wykonują ruchy naprzemiennie
        move = f"{cell_index}{player}"  # Tworzymy ciąg oznaczający ruch (np. "1X")
        game.moves += move  # Dodajemy ruch do listy ruchów
        db.session.commit()  # Zapisujemy zmiany w bazie danych
        return jsonify({'message': 'Move made', 'game_id': game.id, 'moves': game.moves}), 200  # Zwracamy odpowiedź JSON
    else:
        return jsonify({'message': 'Move data is required'}), 400  # Zwracamy błąd, jeśli brakuje danych

# Tworzymy endpoint do pobrania szczegółów gry
@app.route('/game/<int:game_id>', methods=['GET'])  # Obsługuje żądania GET z parametrem game_id
def get_game(game_id):
    game = Game.query.get(game_id)  # Pobieramy grę o podanym ID z bazy danych
    if game is None:  # Jeśli gra nie istnieje, zwracamy błąd 404
        return jsonify({'error': 'Game not found'}), 404
    return jsonify({'game_id': game.id, 'moves': game.moves}), 200  # Zwracamy szczegóły gry w formacie JSON

# Uruchamiamy aplikację w trybie debugowania
if __name__ == '__main__':
    app.run(debug=True)  # Serwer Flask działa lokalnie na porcie 5000


