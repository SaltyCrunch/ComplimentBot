import random

import telebot
from telebot import types
import time
from random import randint
import os

bot = telebot.TeleBot('BOT_TOKEN')

cnt = 0

users = [USERS_ID]

complimentsList = ['LIST_OF_COMPLIMENTS']


@bot.message_handler(func=lambda message: message.chat.id not in users)
def some(message):
    bot.send_message(message.chat.id, "Прости, мой создатель запретил мне с тобой разговаривать 😢")


# @bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda message: message.text == "/start")
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    compliment = types.KeyboardButton("💌 Комплимент")
    ourPhoto = types.KeyboardButton("📸 Фото, напоминающее о тебе")
    secrets = types.KeyboardButton("🤭 Секретики")
    question = types.KeyboardButton("❓ Задать вопрос")

    markup.add(compliment, ourPhoto, secrets, question)

    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b> 😊'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def base(message):
    if message.text == "💌 Комплимент":

        randomIndexCompliment = random.randrange(len(complimentsList))

        bot.send_message(message.chat.id, complimentsList[randomIndexCompliment])

        bot.send_message(chat_id=591703681, text=message.from_user.username + ":\n" + message.text)

    elif message.text == "📸 Фото, напоминающее о тебе":

        bot.send_message(message.chat.id, "Подожди немножко, я выбираю.. 🤔")

        countPhoto = len(os.listdir("assets")) - 1

        temp = randint(1, countPhoto)
        random_number_photo = str(temp)

        ph = 'assets/' + random_number_photo + '.png'
        photo = open(ph, 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()

        bot.send_message(chat_id=591703681, text=message.from_user.username + ":\n" + message.text)

    elif message.text == "🤭 Секретики":

        bot.send_message(message.chat.id, "Ну рассказывай что тебя гложет, подруга 😉")
        time.sleep(2)
        bot.send_message(message.chat.id, "Ты можешь рассказать мне всё, что хочешь")
        time.sleep(2)
        bot.send_message(message.chat.id, "Можешь рассказать, что тебе нравится или не нравится")
        time.sleep(2)
        bot.send_message(message.chat.id, "Это останется между нами 🤐")
        time.sleep(2)
        bot.send_message(message.chat.id, "И я конечно же не передам ничего моему создателю 😏")
        time.sleep(2)
        bot.send_message(message.chat.id, "Единственное правило: одно сообщение - один секретик")
        time.sleep(2)
        msg = bot.send_message(message.chat.id, "Могу предложить несколько тем..")
        time.sleep(2)

        markup_inline1 = types.InlineKeyboardMarkup()
        item_yes1 = types.InlineKeyboardButton("✅ Да", callback_data='yes1')
        item_no1 = types.InlineKeyboardButton("❌ Нет", callback_data='no1')
        markup_inline1.add(item_yes1, item_no1)
        bot.send_message(message.chat.id, "Хочешь?)", reply_markup=markup_inline1)

        bot.register_next_step_handler(msg, secretWow)

    elif message.text == "❓ Задать вопрос":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        que1 = types.KeyboardButton("🤡 Как тебя зовут?")
        que2 = types.KeyboardButton("💪🏻 Что ты можешь?")
        callback = types.KeyboardButton("🤔 Любит ли меня твой создатель?")
        back = types.KeyboardButton("⬅️ Вернуться в главное меню")

        markup.add(que1, que2, callback, back)

        bot.send_message(message.chat.id, "Задай мне вопрос ⏳", reply_markup=markup)

    elif message.text == "🤡 Как тебя зовут?":

        bot.send_message(message.chat.id, "Называй меня как хочешь 🤡")

        bot.send_message(chat_id=591703681, text=message.from_user.username + ":\n" + message.text)

    elif message.text == "💪🏻 Что ты можешь?":

        bot.send_message(message.chat.id, "Поднимать тебе настроение)")
        time.sleep(2)
        bot.send_message(message.chat.id, "Скажу тебе по секрету.. 🤫")
        time.sleep(2)
        bot.send_message(message.chat.id, "Он устал делать это самостоятельно, поэтому и создал меня 😎")
        time.sleep(3)
        bot.send_message(message.chat.id, "Только ему не передавай, а то он меня отключит, а мне очень нравится твоя компания) 🤗")
        time.sleep(4)
        markup_inline2 = types.InlineKeyboardMarkup()
        item_yes2 = types.InlineKeyboardButton("✅ Да", callback_data='yes2')
        item_no2 = types.InlineKeyboardButton("❌ Нет", callback_data='no2')
        markup_inline2.add(item_yes2, item_no2)
        bot.send_message(message.chat.id, "Договорились?) 🤝", reply_markup=markup_inline2)

        bot.send_message(chat_id=591703681, text=message.from_user.username + ":\n" + message.text)

    elif message.text == "🤔 Любит ли меня твой создатель?":

        markup = types.InlineKeyboardMarkup()
        love = types.InlineKeyboardButton('Любит? 🤔', callback_data='love')
        markup.add(love)
        bot.send_message(message.chat.id, "Нажми на кнопку и узнаешь) 🙈", reply_markup=markup)

        bot.send_message(chat_id=591703681, text=message.from_user.username + ":\n" + message.text)

    elif message.text == "⬅️ Вернуться в главное меню":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        compliment = types.KeyboardButton("💌 Комплимент")
        ourPhoto = types.KeyboardButton("📸 Фото, напоминающее о тебе")
        secrets = types.KeyboardButton("🤭 Секретики")
        question = types.KeyboardButton("❓ Задать вопрос")

        markup.add(compliment, ourPhoto, secrets, question)
        bot.send_message(message.chat.id, "Ты вернулась в главное меню ⬅️", reply_markup=markup)

    elif message.text == "id":

        bot.send_message(message.chat.id, f"Твой id: {message.from_user.id}")
        # bot.send_message(message.chat.id, message)

    else:

        bot.send_message(message.chat.id, "Даже не знаю, что сказать..")
        time.sleep(1)
        bot.send_message(message.chat.id, "Ты лучшая! 🤩")

        bot.send_message(chat_id=591703681, text=message.from_user.username + ":\n" +  message.text)

def secretWow(message):

    bot.send_message(message.chat.id, "Да ты что.. Серьёзно? 😱")
    time.sleep(2)
    bot.send_message(message.chat.id, "Мой создатель непременно должен это узнать")
    time.sleep(2)
    bot.send_message(message.chat.id, "Я уже отправил ему сообщение 🐁")

    bot.send_message(chat_id=591703681, text="Секретик " + message.from_user.username + ":\n" + message.text)

@bot.callback_query_handler(func=lambda call: True)
def callback_love(call):
    if call.data == 'love':

        global cnt
        cnt += 1
        bot.answer_callback_query(call.id)
        print(cnt)
        if cnt % 4 == 0:

            bot.send_message(call.message.chat.id, "Да любит он тебя, ***! 🤬")

            bot.send_message(chat_id=591703681, text=call.from_user.username + ":\n" + "Да любит он тебя, ***! 🤬")

        elif cnt % 3 == 0:

            bot.send_message(call.message.chat.id, "Из головы у него не вылезаешь! ❤️‍")

            bot.send_message(chat_id=591703681, text=call.from_user.username + ":\n" + "Из головы у него не вылезаешь! ❤")

        elif cnt % 2 == 0:

            bot.send_message(call.message.chat.id, "Души в тебе не чает! 💞")

            bot.send_message(chat_id=591703681, text=call.from_user.username + ":\n" + "Души в тебе не чает! 💞")

        else:

            bot.send_message(call.message.chat.id, "Любит безумно! 🫶🏻")

            bot.send_message(chat_id=591703681, text=call.from_user.username + ":\n" + "Любит безумно! 🫶🏻")


    elif call.data == 'yes1':

        bot.send_message(call.message.chat.id, "<b>Твои любимы блюда и вкусняшки</b>", parse_mode='html')
        time.sleep(2)
        bot.send_message(call.message.chat.id, "<b>Что бы ты хотела совершить вместе с моим создателем</b>", parse_mode='html')
        time.sleep(2)
        bot.send_message(call.message.chat.id, "<b>За что ты любишь моего создателя</b>", parse_mode='html')
        time.sleep(2)
        bot.send_message(call.message.chat.id, "Давай рассказывай 😉")

    elif call.data == 'no1':

        bot.send_message(call.message.chat.id, "Как пожелаешь)")
        time.sleep(2)
        bot.send_message(call.message.chat.id, "Давай рассказывай тогда 😉")

    elif call.data == 'yes2':

        bot.send_message(call.message.chat.id, "Вот и славненько, я знал, что на тебя можно положиться! ✊🏻")

    elif call.data == 'no2':

        bot.send_message(call.message.chat.id, "Создатель говорил, что тебе можно доверять, видимо он ошибался... 😢")


@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.chat.id, "Ваааау, я с ума схожу от твоей красоты! 😍 Повезло же этому кожаному ублюдку...")

    print ('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print ('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print ('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    photo = open("image.jpg", 'rb')
    bot.send_photo(chat_id=591703681, photo=photo, caption=message.from_user.username)

    photo.close()
    os.remove('image.jpg')


@bot.message_handler(content_types=['video'])
def get_user_video(message):
    bot.send_message(message.chat.id, "Я не настолько умён, чтобы смотреть видео, но уверен, что на нём что-то красивое) Мой создатель обязательно проверит это!")

    print('message.video =', message.video)
    fileID = message.video.file_id
    print('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("video.MP4", 'wb') as new_file:
        new_file.write(downloaded_file)

    video = open("video.MP4", 'rb')
    bot.send_video(chat_id=591703681, video=video, caption=message.from_user.username)

    video.close()
    os.remove('video.MP4')

@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    bot.send_sticker(message.chat.id, sticker="CAACAgIAAxkBAAEINihkGJnQaBAzMRJ2GwZcscSOAn8PdAACaRUAAuLiyUsN3Y_gFzxdai8E")

@bot.message_handler(content_types=['document', 'location', 'contact'])
def get_user_any(message):
    bot.send_message(message.chat.id, "Прости, но меня не научили распознавать такой тип файла 😢")


bot.polling(none_stop=True)
