from bs4 import BeautifulSoup
import random
import requests
url = 'https://www.anekdot.ru/release/anekdot/day/'
html = requests.get(url)
soup = BeautifulSoup(html.text, features="lxml")

listrofl = []
rofls = soup.findAll('div', class_='text')
num = 0

for rofl in rofls:
    listrofl.append(rofl.text)
    num +=1

rand_rofl = (listrofl[random.randint(0, num)])
print(rand_rofl)


