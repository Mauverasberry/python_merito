import pandas as pd   #  zamiast pandas bedziemy pisac pd - biblioteka do pracy z danymi w formacie tabeli (DataFrame)
from matplotlib import pyplot as plt   # Matplotlib - biblioteka do tworzenia wykresów
import seaborn as sns # rozszerzenie Matplotliba, pozwala na bardziej zaawansowane wizualizacje
from sklearn.linear_model import LinearRegression  # Importowanie modelu regresji liniowej ze Scikit-learn

#r 101 - r langhuahe filimk na ypoutube z super wyklresami


df = pd.read_csv('data//weight-height.csv')     # wczytujemy plik  CSV z danymi (o wzroście i wadze.)




print(df)                                       # df to data frame - Wyświetlamy całą tabelę (jeśli mało danych)
print(df.head(10))                              # df.head to domyslnie 5 pierwszych i ost. wynikow tu ustalamy 10

df.Height *= 2.54                               # Przekształcamy wysokość z cali na centymetry (1 cal = 2.54 cm)
df.Weight /= 2.2                                # Przekształcamy wagę z funtów na kilogramy (1 kg = 2.2 funta)

print(df.describe())                            # Opis statystyczny danych (średnia, min, max, kwartyle itd.)

# plt.hist(df.Weight, bins=30)                  # rysuje histogram wagi z 30 przedziałami bins=30 – dzieli dane na 30 grup (słupków w histogramie).
# plt.show()                                    # wyświetl wykres
# plt.hist(df.query('Gender=="Male"').Weight, bins=30)  #query - zapytanie, tylko o mezczyzn
# #plt.show() - gdy to damy da kobiet i mezczyzn w histogramach osobno, gdy usumieny wcvzesniejszed show pokazed wsio w 1 wykresie
# plt.hist(df.query('Gender=="Female"').Weight, bins=30)    # Histogram dla kobiet
# plt.show()

# sns.histplot(df.Weight)
# plt.show()  #do uruchamiania zawsze
# sns.histplot(df.query('Gender=="Male"').Weight)
# sns.histplot(df.query('Gender=="Female"').Weight)
# plt.show()

#d. wejsciowe m, dane niezalezne -> gender, height
#d. wyjsciowe , dane zalezne -> weight

print('get_dummies - zamieniam dane nienumeryczne na numeryczne')
df = pd.get_dummies(df)                     #zmien nazwy na identyfikatory 0 1 -Zamienia kolumnę "Gender" na kolumny "Gender_Male" i "Gender_Female"
print(df)
print('usuwam kolumnę Gender_Male')
del(df['Gender_Male'])                      #usun kolumnę Gender_Male - wystarczy jedna kolumna Gender, gdzie 1 oznacza kobietę, a 0 mężczyznę.
print(df)
print("zmieniam nazwę kolumny")
df.rename(columns={'Gender_Female':'Gender'}, inplace=True) #zamień nazwę kolumny, inplace to nadpisz
print(df)
print("dane gotowe")
# gender 0 - facet, 1 - kobieta

# Tworzenie modelu regresji liniowej - model matematyczny, który przewiduje wagę na podstawie wzrostu i płci.
model = LinearRegression()                  #wykonaj model regresji liniowej
model.fit(df[['Height', 'Gender']], df['Weight']) #dopasuj - model ma sie uczyc na podstawie danych wejsciowych i wyjsciowych (wzrostu i płci)
# fit(X, y) – uczy model na podstawie:
# X – cechy niezależne ([['Height', 'Gender']]).
# y – wartość do przewidzenia ('Weight')


#  Współczynniki modelu:
print(f'Wspolczynnik kierunkowy: {model.coef_}\nwyraz wolny: {model.intercept_}')
# coef_ – współczynniki (ile jednostek zmienia się waga przy zmianie wzrostu lub płci).
# intercept_ – wartość stała, od której zaczyna się funkcja.

# Przewidywanie wagi - Przewidujemy wagę osoby o wzroście 192 cm i płci żeńskiej (1).
height = 192
gender = 1                                              # Kobieta
weight = 1.06 * height  -8.8 * gender -102.5            # Przybliżony wzór
print(weight)

print(model.predict([[192,0], [167,1], [10,1], ]))  #predict=przewidz facet o wzroscie 192
# predict([[192,0], [167,1], [10,1]]) – przewidujemy wagę dla:
# Mężczyzny (0) o wzroście 192 cm.
# Kobiety (1) o wzroście 167 cm.
# Dziecka (1) o wzroście 10 cm (przykładowe wartości).