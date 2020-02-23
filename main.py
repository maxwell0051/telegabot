import telebot
from telebot import types
import random
import ctt

strings = ['да', 'нет']


bot = telebot.TeleBot('909996276:AAED9HryFPnjNxWQu7ixYwDyBGJY7uB_9_4')

@bot.message_handler(commands=['start'])
def start(message):
 bot.send_message(message.chat.id, "Привет!🍪")

 markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
 cmd = types.KeyboardButton("📜Цитаты")
 gms = types.KeyboardButton("🎮Игры")



 markup.add(cmd,gms)
 bot.send_message(message.chat.id, "Я Бот <b>РАНДОМ</b> ", reply_markup=markup, parse_mode='HTML')

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Цитаты':

        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("🐺Волчьи")
        item2 = types.KeyboardButton("🏆Цитаты Великих Людей")
        item3 = types.KeyboardButton("🔙Назад")

        markup3.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Выбери тип цитаты", reply_markup=markup3)
    elif message.text == 'Игры':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("🎲Данетка")
        item2 = types.KeyboardButton("🎲Случайно число")
        item3 = types.KeyboardButton("🔙Назад")

        markup2.add(item1, item2, item3)

        bot.send_message(message.chat.id, '<b>Выбери игру</b>', parse_mode='HTML', reply_markup=markup2)
    elif message.text == 'Цитаты':
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("🐺Волчьи")
        item2 = types.KeyboardButton("🏆Цитаты Великих Людей")
        item3 = types.KeyboardButton("🔙Назад")

        markup3.add(item1, item2, item3)

        bot.send_message(message.chat.id, "Выбери тип цитаты", reply_markup=markup3)

    elif message.text == '🐺Волчьи':
            bot.send_message(message.chat.id, random.choice(ctt.wolfs))
    elif message.text == '🏆Цитаты Великих Людей':
            bot.send_message(message.chat.id, random.choice(ctt.norm))
    elif message.text == '🔙Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cmd = types.KeyboardButton("📜Цитаты")
            gms = types.KeyboardButton("🎮Игры")

            markup.add(cmd, gms)
            bot.send_message(message.chat.id, "<i>Возвращаемся</i>", parse_mode='HTML', reply_markup=markup)

    else:
        if message.text == '🎲Данетка':
            bot.send_message(message.chat.id, 'Задай вопрос, а я отвечу <b>Да</b> или <b>Нет</b>', parse_mode='HTML')
        elif message.text == '🎲Случайно число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == '🔙Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            cmd = types.KeyboardButton("📜 Цитаты")
            gms = types.KeyboardButton("🎮Игры")

            markup.add(cmd, gms)
            bot.send_message(message.chat.id, "<i>Возвращаемся</i>", parse_mode='HTML',reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Я думаю что " + random.choice(strings))


@bot.message_handler(content_types=['text'])
def text1(message):
 if message.text == '🎲Данетка':
    bot.send_message(message.chat.id, 'Задай вопрос, а я отвечу <b>Да</b> или <b>Нет</b>', parse_mode='HTML')
 elif message.text == '🎲Случайно число':
    bot.send_message(message.chat.id, str(random.randint(0,100)))
 elif message.text == 'Цитаты':
     markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
     item1 = types.KeyboardButton("🐺Волчьи")
     item2 = types.KeyboardButton("🏆Цитаты Великих Людей")
     item3 = types.KeyboardButton("🔙Назад")

     markup3.add(item1, item2, item3)
     bot.send_message(message.chat.id, "Выбери тип цитаты", reply_markup=markup3)

     if message.text == '🐺Волчьи':
       bot.send_message(message.chat.id, random.choice(ctt.wolfs))
     elif message.text == '🏆Цитаты Великих Людей':
       bot.send_message(message.chat.id, random.choice(ctt.norm))
     elif message.text == '🔙Назад':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         cmd = types.KeyboardButton("Цитаты")
         gms = types.KeyboardButton("Игры")

         markup.add(cmd, gms)
         bot.send_message(message.chat.id, "<i>Возвращаемся</i>", parse_mode='HTML', reply_markup=markup)

 else:
     bot.send_message(message.chat.id, "Я думаю что " + random.choice(strings))










bot.polling()
