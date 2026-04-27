import telebot
import os
from dotenv import load_dotenv

import weatherHandler

load_dotenv()

# sync version of bot
def main():
    API_TOKEN = os.getenv("BOT_API_TOKEN")
    if(API_TOKEN == None): return

    WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")

    bot = telebot.TeleBot(API_TOKEN)
    print("Bot started!")

    @bot.message_handler(commands=['help', 'start'])
    def send_welcome(message):
        bot.reply_to(message, """\
    Hi there, I am EchoBot.
    I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
    """)

    @bot.message_handler(commands=['weather'])
    def show_weather(message):
        bot.reply_to(message, weatherHandler.get_weather(str.split(message.text, ' ')[1], WEATHER_TOKEN))

    # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
    @bot.message_handler(func=lambda message: True)
    def echo_message(message):
        bot.reply_to(message, message.text)

    bot.infinity_polling()

main()