# Importy
import pandas as pd                    # pandas jako pd: Służy do pracy z danymi w formie tabelarycznej (DataFrame)
from matplotlib import pyplot as plt   # matplotlib.pyplot jako plt: Do tworzenia wykresów i wizualizacji danych.
import seaborn as sns                  # Rozszerzenie Matplotlib, ułatwiające tworzenie estetycznych wykresów statystycznych.
from sklearn.linear_model import LinearRegression    # Do tworzenia modelu regresji liniowej
from sklearn.model_selection import train_test_split # Do podziału danych na zestawy treningowe i testowe (w stosunku np. 80 na 20)

# Wczytanie danych i podstawowa analiza
df = pd.read_csv('data\\otodom.csv')    # Wczytujemy dane z pliku CSV o nazwie otodom.csv do obiektu DataFrame o nazwie df.
# plik znajduje się w podfolderze data w tym samym katalogu co skrypt.
print(df)                               # Wyświetlamy pierwsze i ostatnie wiersze wczytanego DataFrame, dając ogólny pogląd na strukturę danych.
print(df.describe().T.to_string())      # describe() Generuje statystyki opisowe dla każdej kolumny numerycznej w DataFrame (np. średnia, min, max, kwartyle)
# .T to transpozycja — zamienia wiersze z kolumnami, żeby lepiej się czytało.
# .to_string() zapewnia, że cała tabela zostanie wyświetlona bez obcinania.


# Sekcje zakomentowane (#) to przykłady kodu, które można by wykorzystać do wstępnej analizy danych. Pokazują one możliwości:
# print(df.loc[:,'cena'])                       # Wyświetlania konkretnej kolumny
#sns.heatmap(df.iloc[:,1:].corr(), annot=True)  # wytnij kulumne z indexem 0 i na tym zrob korelacje i zrob z tego mape ciepla annot dodaje adnotacje
#plt.show()
#print(df.corr())  #corr - korelacja miedzy danymi


# #plt.show()
# plt.scatter(df.powierzchnia, df.cena)         # Wyświetlania wykresu punktowego dla powierzchnia vs cena
# sns.histplot(df.cena)                         # Wyświetlania wykresu histogramu dla kolumny cena
# plt.show()

# Obliczanie kwartylów (czyli podziału cen na grupy) - skupiamy się na filtrowaniu danych, aby usunąć potencjalne wartości odstające (outliery), które mogłyby zakłócić modelowanie:
q1 = df.describe().loc['25%', 'cena']           # Obliczamy pierwszy kwartyl (Q1) dla kolumny cena. Oznacza to, że 25% ofert ma cenę niższą lub równą tej wartości.
print(q1)
q3 = df.describe().loc['75%', 'cena']           # Obliczamy trzeci kwartyl (Q3) dla kolumny cena. Oznacza to, że 75% ofert ma cenę niższą lub równą tej wartości (lub 25% ma cenę wyższą).
print(q3)

# Filtrowanie danych
#df1 = df[(df.cena >= q1) & (df.cena <= q3)]    # jak można by dodatkowo odfiltrować dane, aby zawierały tylko ceny między Q1 a Q3, czyli środkowe 50% danych.
df1 = df[(df.cena <= q3)]                       # Tworzymy nowy DataFrame df1, który zawiera tylko te wiersze z df, gdzie cena jest mniejsza lub równa trzeciemu kwartylowi (Q3).

# Wizualizacja danych po filtrze
sns.histplot(df1.cena)
plt.show()                                      # Wyświetlamy histogram cen dla przefiltrowanych danych (df1.cena), aby zobaczyć rozkład cen po usunięciu górnych wartości odstających.

# Przygotowanie danych do trenowania modelu uczenia maszynowego:
X = df1.iloc[: , 2:]                            # Tworzymy macierz cech (X). iloc służy do indeksowania po pozycji. [: , 2:] oznacza, że bierzemy wszystkie wiersze (:) i wszystkie kolumny
# od indeksu 2 wzwyż (czyli trzecią kolumnę i kolejne). Zakładamy, że pierwsze dwie kolumny to identyfikatory lub inne dane, które nie są cechami predykcyjnymi (np. ID ogłoszenia, nazwa).
y= df1.cena                                     # Tworzymy wektor zmiennej zależnej (y), którą chcemy przewidywać – w tym przypadku jest to kolumna cena z przefiltrowanego DataFrame df1

# Podział na dane treningowe i testowe
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape, X_test.shape)              # pokaz mi ksztalt tyuch danych - Wyświetlamy wymiary (liczbę wierszy i kolumn) zestawów treningowych i testowych, aby potwierdzić poprawny podział.
# Dzielimy nasze dane na zestawy treningowe i testowe.
# X_train, y_train: Dane używane do trenowania modelu.
# X_test, y_test: Dane używane do oceny wydajności modelu (model ich "nie widział" podczas trenowania).
# test_size=0.2: Oznacza, że 20% danych zostanie przeznaczone na zestaw testowy, a pozostałe 80% na zestaw treningowy.

# Model regresji liniowej
model = LinearRegression()                      # Inicjalizujemy model regresji liniowej.
model.fit(X_train, y_train)                     # Trenujemy model, dopasowując go do danych treningowych
print(model.score(X_test, y_test))              # policz na danych testowych na ile model jest sprawny - Sprawdzamy skuteczność modelu – ile zmienności cen tłumaczy model (R²).
# Oceniamy model na danych testowych. Metoda .score() dla regresji liniowej zwraca współczynnik determinacji R-kwadrat (R²). R².  Im bliżej 1, tym lepiej.

print(model.coef_)                              #  Wyświetlamy współczynniki regresji (coefficients) - mówią, jak dana cecha (np. powierzchnia) wpływa na cenę.
# Dodatni = zwiększa cenę, ujemny = zmniejsza.
print(pd.DataFrame(model.coef_, X.columns))     # Tworzymy i wyświetlamy DataFrame, który ładnie pokazuje nazwy kolumn (cech) i odpowiadające im współczynniki. Ułatwia to interpretację, która cecha
# ma największy wpływ na cenę.

# Model drzewa decyzyjnego (porównanie)
from sklearn.tree import DecisionTreeRegressor  # Importujemy klasę DecisionTreeRegressor.
model = DecisionTreeRegressor()                 # Inicjalizujemy model drzewa decyzyjnego.
model.fit(X_train, y_train)                     # Trenujemy model drzewa decyzyjnego na tych samych danych treningowych.
print(model.score(X_test,y_test))               # Oceniamy model drzewa decyzyjnego na danych testowych, ponownie używając metryki R². Porównanie R² dla obu modeli (regresji liniowej i drzewa
# decyzyjnego) pozwala ocenić, który z nich lepiej radzi sobie z przewidywaniem cen nieruchomości na podstawie dostępnych cech.