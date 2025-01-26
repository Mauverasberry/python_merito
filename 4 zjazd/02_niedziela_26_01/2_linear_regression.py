import pandas as pd   #zamiast pandas bedziemy pisac pd
from matplotlib import pyplot as plt   #matematyczna podstwawowa
import seaborn as sns #do bardziej złożonych rzeczy
from sklearn.linear_model import LinearRegression  #zaimportuj regresje liniowa
from sklearn.model_selection import train_test_split #dzieli dane w danym srtosunku np 80 na 20

df = pd.read_csv('data\\otodom.csv')
print(df)
print(df.describe().T.to_string())  #poka jak sie zachowuje  T- zamienia wiersze xz kolumnami by ladniej sie czytalo

# print(df.loc[:,'cena'])
#sns.heatmap(df.iloc[:,1:].corr(), annot=True)  #wytnij kulumne z indexem 0 i na tym zrfob korelacje i zrob ztegpo mape ciepla annot dodaje adnotacje
#plt.show()
#print(df.corr())  #corr - korelacja miedzy danymi


# #plt.show()
# plt.scatter(df.powierzchnia, df.cena) #wykeres punktowy
# sns.histplot(df.cena)
# plt.show()

q1 = df.describe().loc['25%', 'cena']
print(q1)
q3 = df.describe().loc['75%', 'cena']
print(q3)

#df1 = df[(df.cena >= q1) & (df.cena <= q3)]
df1 = df[(df.cena <= q3)]

sns.histplot(df1.cena)
plt.show()

X = df1.iloc[: , 2:]  #wszytskie kolumny bez 2 pierwszych
y= df1.cena

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape, X_test.shape) #pokaz mi ksztalt tyuch danychy

model = LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test)) #policz na danych testowych na ikle model jest sprawny

print(model.coef_)
print(pd.DataFrame(model.coef_, X.columns))

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(X_train, y_train)
print(model.score(X_test,y_test))