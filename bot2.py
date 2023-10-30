import telebot
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
    num += 1

rand_rofl = (listrofl[random.randint(0, num)])

bot = telebot.TeleBot('6644013089:AAEskf4UYa1ks4Hh8Kd3sSgaIEZJNaqsngg')

@bot.message_handler(commands=['start'])
def start(message):
    mess = 'Привет!!!\nЯ бот-анекдот, я всего-навсего скидываю анекдоты ;(, не судите строго(((\nТы можешь написать мне "Скинь анекдот" и я его скину)))'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['send_joke'])
def send_joke(message):
    bot.send_message(message.chat.id, rand_rofl)

bot.polling(none_stop=True)
