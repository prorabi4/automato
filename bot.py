import telebot
from bs4 import BeautifulSoup
import random
import requests
from telebot import types

url = 'https://www.anekdot.ru/'
bot = telebot.TeleBot('6644013089:AAEskf4UYa1ks4Hh8Kd3sSgaIEZJNaqsngg')
pic = 'https://i.pinimg.com/564x/0d/c1/60/0dc16089460b8714ff31997b5acfa63b.jpg'

@bot.message_handler(commands=['start'])
def start(message):
    html = requests.get(url + 'release/anekdot/week/')
    soup = BeautifulSoup(html.text, features="lxml")
    global rofls
    rofls = soup.findAll('div', class_='text')


    global listrofl
    listrofl = []
    global num
    num = 0
    for rofl in rofls:
        listrofl.append(rofl.text)
        num +=1

    html1 = requests.get(url + 'tags/кошки')
    soup1 = BeautifulSoup(html1.text, features="lxml")
    global rofls1
    rofls1 = soup1.findAll('div', class_='text')

    global listrofl1
    listrofl1 = []
    global num1
    num1 = 0
    for rofl1 in rofls1:
        listrofl1.append(rofl1.text)
        num1 +=1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Анекдоты недели')
    button1 = types.KeyboardButton('Истории про котиков')
    button2 = types.KeyboardButton('Помощь')
    markup.add(button, button1, button2)
    mess = 'Привет!!!\nЯ бот-анекдот, я всего-навсего скидываю анекдоты ;(, не судите строго((( \nТы можешь попросить скинуть анекдот или историю про котиков!!!\nЗа анекдоты и истории мой создатель не отвечает!!! Они парсятся с сайта!!!'
    bot.send_photo(message.chat.id, pic, caption=mess, reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == 'Помощь')
def send_info(message):
    info = 'Ты можешь выбрать различные типы анекдотов: \n 1- Истории про котиков \n 2- Лучшине анекдоты за неделю'
    bot.send_message(message.chat.id, info)

@bot.message_handler(func=lambda msg: msg.text == 'Истории про котиков')
def send_joke(message):
    bot.send_message(message.chat.id, listrofl1[random.randint(0, num1)])

@bot.message_handler(func=lambda msg: msg.text == 'Анекдоты недели')
def send_jokeweek(message):
    bot.send_message(message.chat.id, listrofl[random.randint(0, num)])

bot.polling(none_stop=True)
