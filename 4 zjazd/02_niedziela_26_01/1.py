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

plt.hist(df.Weight, bins=30)                  # rysuje histogram wagi z 30 przedziałami bins=30 – dzieli dane na 30 grup (słupków w histogramie).
plt.show()                                    # wyświetl wykres
plt.hist(df.query('Gender=="Male"').Weight, bins=30)  #query - zapytanie, tylko o mezczyzn
#plt.show() - gdy to damy da kobiet i mezczyzn w histogramach osobno, gdy usumieny wcvzesniejszed show pokazed wsio w 1 wykresie
plt.hist(df.query('Gender=="Female"').Weight, bins=30)    # Histogram dla kobiet
plt.show()

sns.histplot(df.Weight)
plt.show()  #do uruchamiania zawsze
sns.histplot(df.query('Gender=="Male"').Weight)
sns.histplot(df.query('Gender=="Female"').Weight)
plt.show()
#
# d. wejsciowe m, dane niezalezne -> gender, height
# d. wyjsciowe , dane zalezne -> weight