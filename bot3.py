import telebot
from bs4 import BeautifulSoup
import random
import requests
url_best_joke_off_week = 'https://www.anekdot.ru/release/anekdot/week/'
url_cats = 'https://www.anekdot.ru/tags/кошки'
bot = telebot.TeleBot('6644013089:AAEskf4UYa1ks4Hh8Kd3sSgaIEZJNaqsngg')
pic = 'https://i.pinimg.com/564x/0d/c1/60/0dc16089460b8714ff31997b5acfa63b.jpg'
@bot.message_handler(commands=['start'])
def start(message):
    mess = 'Привет!!!\nЯ бот-анекдот, я всего-навсего скидываю анекдоты ;(, не судите строго(((\nТы можешь написать мне "/help" и я скину тебе темы анекдотво)))\n За анекдоты мой создатель не отвечает!!! Они парсятся с сайта!!!'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_photo(message.chat.id, pic)

@bot.message_handler(commands=['help'])
def send_info(message):
    info = 'Ты можешь выбрать различные типы анекдотов: \n 1- Анекдоты про котиков(напишит \n 2- Лучшине анекдоты за неделю'
    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=['send_bjokew'])
def send_joke(message):
    html = requests.get(url_best_joke_off_week)
    soup = BeautifulSoup(html.text, features="lxml")
    rofls = soup.findAll('div', class_='text')

    listrofl = []
    for rofl in rofls:
        listrofl.append(rofl.text)

    if len(listrofl) > 0:
        rand_rofl = random.choice(listrofl)  # Получение случайного анекдота
        bot.send_message(message.chat.id, rand_rofl)
    else:
        bot.send_message(message.chat.id, "Извините, не удалось получить анекдот.")

bot.polling(none_stop=True)
