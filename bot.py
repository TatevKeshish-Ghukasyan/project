import telebot
from automation_bot.config import TOKEN
from automation_bot.parser import get_weather

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Напиши город или /weather")


@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.chat.id, "Собираю погоду...")

    result = get_weather("Yerevan")
    bot.send_message(message.chat.id, result)


@bot.message_handler(func=lambda m: True)
def echo(message):
    city = message.text
    bot.send_message(message.chat.id, f"Ищу погоду в {city}...")

    result = get_weather(city)
    bot.send_message(message.chat.id, result)


bot.infinity_polling()