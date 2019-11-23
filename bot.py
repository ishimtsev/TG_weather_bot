import telebot
import api_handler

import config
import keys
import dbworker as db


bot = telebot.TeleBot(keys.bot_api_key)


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


@bot.message_handler(commands=['start'])
def func(message):
    if db.is_user_exist(message.chat.id):
        bot.send_message(message.chat.id, "В каком городе хотите узнать погоду?")
        db.set_user_state(message.chat.id, config.States.S_CITY_SEARCH.value)
    else:
        bot.send_message(message.chat.id, "Привет!\nВ каком городе хотите узнать погоду?")
        db.add_user(message.chat.id)


@bot.message_handler(commands=['weather'])
def func(message):
    if db.get_user_state(message.chat.id) != config.States.S_CITY_OK.value: # Проверка, есть ли у пользователя сохранённый город
        bot.send_message(message.chat.id, "Сначала нужно выбрать город. Сделайте это с помощью комманды */start*", parse_mode="Markdown")
    else:
        city_info = db.get_city(message.chat.id)
        s = "*" + str(city_info[0]) + "*\n\n" + str(api_handler.get_currentconditions(city_info[1]))
        bot.send_message(message.chat.id, s, parse_mode="Markdown")


@bot.message_handler(func=lambda message: db.get_user_state(message.chat.id) == config.States.S_CITY_SEARCH.value)
def func(message):
    db.delete_temp_results(message.chat.id) # Удаление результатов предыдущего поиска
    results = api_handler.get_location(message.text) # Получение новых результатов
    if results is None:
        bot.send_message(message.chat.id, "Ничего не найдено.\nНапишите название города ещё раз:")
    else:
        db.add_temp_results(message.chat.id, results) # Сохраняем результаты в БД
        s="Результаты:\n\n"
        for row in results:
            s += "*" + str(row.number) + "*. " + row.full_str + "\n"
        s += "\nНапишите номер города, чтобы узнать погоду."
        bot.send_message(message.chat.id, s, parse_mode="Markdown")
        db.set_user_state(message.chat.id, config.States.S_CITY_FOUND.value)


@bot.message_handler(func=lambda message: db.get_user_state(message.chat.id) == config.States.S_CITY_FOUND.value)
def func(message):
    results = db.get_temp_results(message.chat.id)
    if represents_int(message.text):
        if 1 <= int(message.text) <= len(results):
            for result in results:  # ['city_number', 'city_name', 'city_key']
                if str(result["city_number"]) == str(message.text):
                    db.set_city(message.chat.id, str(result["city_name"]), str(result["city_key"]))
                    s = "Отлично! Теперь с помощью команды */weather* вы можете узнать погоду в городе *" + str(result["city_name"]) + "*."
                    bot.send_message(message.chat.id, s, parse_mode="Markdown")
                    db.set_user_state(message.chat.id, config.States.S_CITY_OK.value)
                    db.delete_temp_results(message.chat.id)  # Удаление временных результатов поиска
                    break
        else:
            bot.send_message(message.chat.id, "Неверный номер города.\nНапишите номер города, чтобы узнать погоду или /start для поиска другого города.",
                             parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "Неверный номер города.\nНапишите номер города, чтобы узнать погоду или /start для поиска другого города.",
                         parse_mode="Markdown")


bot.polling()
