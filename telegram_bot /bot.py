import telebot
import account_creator
import auto_liker
import auto_commenter

from config import TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.reply_to(message, "👋 Welcome! Use /help to see available commands.")

@bot.message_handler(commands=['create_account'])
def create_account(message):
    result = account_creator.create_instagram_account()
    bot.reply_to(message, result)

@bot.message_handler(commands=['auto_like'])
def auto_like(message):
    result = auto_liker.auto_like("https://www.instagram.com/p/example_post", None)
    bot.reply_to(message, result)

@bot.message_handler(commands=['auto_comment'])
def auto_comment(message):
    result = auto_commenter.auto_comment("https://www.instagram.com/p/example_post", None)
    bot.reply_to(message, result)

bot.polling()
