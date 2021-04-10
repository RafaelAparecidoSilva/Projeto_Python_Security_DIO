from bs4 import BeautifulSoup
import requests

# Objeto site contém o conteúdo da requisição Http do site (é do tipo byte)
site = requests.get('https://www.climatempo.com.br/').content

# Objeto soup transforma o conteúdo do objeto site em html
soup = BeautifulSoup(site, 'html.parser')

# Transforma o conteúdo do objeto soup em string e imprime na tela
print(soup.prettify())

temperatura = soup.find('p', class_="-gray _flex _align-center")

# print(temperatura)
print(soup.title.string)
print(soup.a is iter)
