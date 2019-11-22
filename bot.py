import telebot
import api_handler
import json
import config
import keys
import dbworker


# try:
#     bot = telebot.TeleBot(config.bot_api_key)
# except Exception:
#     print("Нужно включить VPN")
bot = telebot.TeleBot(keys.bot_api_key)

@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    bot.send_message(message.chat.id, 'Привет!\nВ каком городе хочешь узнать погоду?')
    dbworker.set_state(message.chat.id, config.States.S_CITY_SEARCH.value)
    #print(message.chat.id)

@bot.message_handler(commands=['weather'])
def start_message(message):
    print(dbworker.get_state(message.chat.id)) #
    bot.send_message(message.chat.id, api_handler.get_currentconditions(291102), parse_mode="Markdown")

@bot.message_handler(func=lambda message: dbworker.get_state(message.chat.id) == config.States.S_CITY_SEARCH.value)
def user_entering_name(message):
    print(message.text)
    bot.send_message(message.chat.id, api_handler.get_location(message.text))
    dbworker.set_state(message.chat.id, config.States.S_CITY_CHOSEN.value)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, '*Пока*', parse_mode="Markdown")

bot.polling()
