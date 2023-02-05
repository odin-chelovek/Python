import telebot
from telebot import types
from time import sleep
from random import randrange
from my_modul import get_news
from Token import TOKEN

#Токен для связи с ботом

Token = TOKEN
bot = telebot.TeleBot(Token)

#Команда старт и последующий ответ бота после нее

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет , <b>{message.from_user.first_name}. </b> '
    m = 'Список команд : /start ,/game , /photo ,/author, /news'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, m, parse_mode='html')

#Команда новости и последующий парсинг и отправка новостей

@bot.message_handler(commands=['news'])
def news(message):
    count = 0
    bot.send_message(message.chat.id, 'please waiting...', parse_mode='html')
    for n in get_news():
        sleep(2)
        bot.send_message(message.chat.id, n, parse_mode='html')
        count += 1
        if count == 20 :
            break


#Команда game и реализация игры подбрасывания монетки

@bot.message_handler(commands=['game'])
def game(message):
    bot.send_message(message.chat.id, 'Игра орел или решка', parse_mode='html')
    monetka = ['Орел','Решка']
    n = randrange(0,2)
    sleep(3)
    bot.send_message(message.chat.id, monetka[n], parse_mode='html')


#Команда автор предоставляет ссылку на автора бота

@bot.message_handler(commands=['author'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Мой Создатель', url='https://t.me/Brown_mishka'))
    bot.send_message(message.chat.id, 'Перейди в чат с создателем)', reply_markup=markup)


#Команда фото просто отправляет смешную картинку

@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo = open('iicon.png.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, 'Это Данила. Он за вами наблюдает)))', parse_mode='html')



#Это реализация приветствия бота

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    hello_txt = ['Hello', 'hello','hi','Hi','Привет','привет','Здарова','Здраствуй','прив','Прив','здраствуй','здарова']
    if message.text in hello_txt :
        bot.send_message(message.chat.id, 'Здраствуй, пользователь)', parse_mode='html')

#При отправки фото бот может отреагировать

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау крутое фото')

#Чтобы бот работал постоянно

bot.polling(none_stop=True)
