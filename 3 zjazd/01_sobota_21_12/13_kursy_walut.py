import requests  #biblioteka, która pozwala pobieranie z sieci

url = 'https://api.frankfurter.dev/v1/latest?base=USD'

response = requests.get(url)
#opdytujemy i cos nam zwraca
# request - zapytanie
# response - odpowiedź

data = response.json() #zawraca dane jsonem
date = data['date'] #wyciagniecie daty z zew api
rates = data['rates']#kursy walut
#print(rates) #dluga lista
# w formie tabelarycznej

for key,value in rates.items():
    print(f'{key} {value}')

pln = float(input('Ile masz PLN?   '))
euro = rates['EUR'] * pln
print (f'Mając {pln}PLN możesz wymienić na {euro:.2f} Euro')  #dwa 0 po przecinku