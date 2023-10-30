import telebot
from bs4 import BeautifulSoup
import random
import requests

url_cats = 'https://www.anekdot.ru/tags/кошки'
html1 = requests.get(url_cats)
soup1 = BeautifulSoup(html1.text, features="lxml")
rofls1 = soup1.findAll('div', class_='text')
print(rofls1)

listrofl1 = []
num1 = 0
for rofl1 in rofls1:
    listrofl1.append(rofl1.text)
    num1 +=1
print(listrofl1[0])
