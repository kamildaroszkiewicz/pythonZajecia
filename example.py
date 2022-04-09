from platform import platform
import requests
from pprint import pprint

response = requests.get("https://www.mmobomb.com/api1/games")

data = (response.json())
pprint(data)

print("Zobacz wedlug:")
print("1.Platformy")
print("2. Developera")
print("3.Genre")
print("4. Publishera")
print("5. Tytul")


option = input('Podaj swoj wybór: ')
if option == '1':
    platform = input("Podaj platforme: ")
    pprint([char for char in data if char.get('platform') == platform])
elif option == '2':
    developer = input("Podaj developera: ")
    pprint([char for char in data if char.get('developer') == developer])
elif option == '3':
    genre = input("Podaj genre: ")
    pprint([char for char in data if char.get('genre') == genre])
elif option == '4':
    publisher = input("Podaj publishera: ")
    pprint([char for char in data if char.get('publisher') == publisher])
elif option == '5':
    title = input("Podaj tytul: ")
    pprint([char for char in data if char.get('title') == title])