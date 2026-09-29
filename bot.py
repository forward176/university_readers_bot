import os
from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = TeleBot(BOT_TOKEN)

if __name__ == "__main__":
    print("bot started")
    bot.infinity_polling()