import requests  #biblioteka, która pozwala pobieranie z sieci

url = 'https://api.frankfurter.dev/v1/latest?base=USD'

response = requests.get(url)
data = response.json()

# print(response.text) #odp w formie tekstowek
# print(response.headers) #naglówki

if response.status_code ==200:
    print(data)
else:
    print('cos jest nie tak')