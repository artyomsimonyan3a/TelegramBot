import telebot
import config


from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welecome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("👍Лайки")
    item2 = types.KeyboardButton("🧍Подписчики")
    item3 = types.KeyboardButton('👀Просмотры')
 
    markup.add(item1, item2, item3)
    
    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\nЗдесь вы можете накрутить подписчиков, лайков, просмотров  в Instagram.\n\nЦены:\n500 подписчиков - 125 рублей\n1000 подписчиков - 250 рублей\n\n100 лайков - 110 рублей\n200 лайков - 210 рублей\n\n500 просмотров - 100 рублей\n1000 просмотров - 200 рублей'.format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
     if message.chat.type == 'private':
        if message.text == "👍Лайки":
            bot.send_message(message.chat.id, 'Цены:\n100 лайков - 110 рублей\n200 лайков - 210 рублей\n\nНомер карты: 5336 6903 7504 6242\n\nЧек скинуть сюда @lonerichman. Чеки будут провиряться вручную.')
        elif message.text == "🧍Подписчики":
           bot.send_message(message.chat.id, "Цены:\n500 подписчиков - 125 рублей\n1000 подписчиков - 250 рублей\n\nНомер карты: 5336 6903 7504 6242\n\nЧек скинуть сюда @lonerichman. Чеки будут провиряться вручную.")
        elif message.text == "👀Просмотры":
            bot.send_message(message.chat.id, 'Цены:\n500 просмотров - 100 рублей\n1000 просмотров - 200 рублей\n\nНомер карты: 5336 6903 7504 6242\n\nЧек скинуть сюда @lonerichman. Чеки будут провиряться вручную.')

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

bot.polling(none_stop=True)