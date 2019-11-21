import telebot
import telegram
import api_handler
import json
import config
import keys

# try:
#     bot = telebot.TeleBot(config.bot_api_key)
# except Exception:
#     print("Нужно включить VPN")
bot = telebot.TeleBot(keys.bot_api_key)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Чё каво')
    print(message.chat.id)

@bot.message_handler(commands=['weather'])
def start_message(message):
    bot.send_message(message.chat.id, api_handler.get_currentconditions(291102), parse_mode=telegram.ParseMode.HTML)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'А')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, '<b>Э</b>', parse_mode=telegram.ParseMode.HTML)

bot.polling()
print('kek')