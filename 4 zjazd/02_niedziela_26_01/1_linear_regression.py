import pandas as pd   #zamiast pandas bedziemy pisac pd
from matplotlib import pyplot as plt   #matematyczna podstwawowa
import seaborn as sns #do bardziej złożonych rzeczy
from sklearn.linear_model import LinearRegression  #zaimportuj regresje liniowa

#r 101 - r langhuahe filimk na ypoutube z super wyklresami


df = pd.read_csv('data//weight-height.csv')   #wczytujemy plik
print(df) # df to data frame
print(df.head(10))   #df.head to domyslnie 5 pierwszych wynikow tu ustalamy 10

df.Height *= 2.54  #cala kolumna jest * by zamienic cale na cm
df.Weight /= 2.2

print(df.describe()) #9:12 nie wiem cpo to robi

# plt.hist(df.Weight, bins=30) #histogram, dzieli na 30 słupków
# plt.show()   #wyświetl
# plt.hist(df.query('Gender=="Male"').Weight, bins=30)  #query - zapytanie, tylko o panow
# #plt.show() - gdy to damy da K I M w histogramach osobno, gdy usumieny wcvzesniejszed show pokazed wsio w 1 wykresie
# plt.hist(df.query('Gender=="Female"').Weight, bins=30)
# plt.show()
#
# sns.histplot(df.Weight)
# plt.show()  #do uruchamiania zawsze
# sns.histplot(df.query('Gender=="Male"').Weight)
# sns.histplot(df.query('Gender=="Female"').Weight)
# plt.show()

#d. wejsciowe m, dane niezalezne -> gender, height
#d. wyjsciowe , dane zalezne -> weight

print('get_dummies - zamieniam dane nienumeryczne na numeryczne')
df = pd.get_dummies(df)  #zmien nazwy na identyfikatory 0 1
print(df)
print('usuwam kolumnę Gender_Male')
del(df['Gender_Male']) #usun kolumne
print(df)
print("zmieniam nazwę kolumny")
df.rename(columns={'Gender_Female':'Gender'}, inplace=True) #zamień nazwę , inplace to nadpisz
print(df)
print("dane gotowe")
# gender 0 - facet, 1 - kobieta

model = LinearRegression() #wykonaj model regresji liniowej
model.fit(df[['Height', 'Gender']], df['Weight']) #dopasuj - model ma sie uczyc na podstawie danych wejsciowych i wyjsciowych
print(f'Wspolczynnik kierunkowy: {model.coef_}\nwyraz wolny: {model.intercept_}')

height = 192
gender = 1
weight = 1.06 * height  -8.8 * gender -102.5   #10:57
print(weight)

print(model.predict([[192,0], [167,1], [10,1]]))  #predict=przewidz facet o wzroscie 192