import telebot
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'core')))
import account_creator


bot = telebot.TeleBot("7604424348:AAHtkmD0YKApTg4B9-QeJNW5SXUmOmctK7E")

user_data = {}

@bot.message_handler(commands=['create_account'])
def ask_email(message):
    bot.reply_to(message, "✉️ Enter the email address for the Instagram account:")
    bot.register_next_step_handler(message, process_email)

def process_email(message):
    user_data[message.chat.id] = {"email": message.text}
    bot.reply_to(message, "📩 Enter the OTP received on email:")
    bot.register_next_step_handler(message, process_otp)

def process_otp(message):
    user_data[message.chat.id]["otp"] = message.text
    email = user_data[message.chat.id]["email"]
    otp = user_data[message.chat.id]["otp"]
    
    bot.reply_to(message, "⏳ Creating account... Please wait!")
    
    # Call account creator function
    result = account_creator.create_instagram_account(email, otp)
    
    if result:
        bot.reply_to(message, f"✅ Account Created Successfully!\nUsername: {result}")
    else:
        bot.reply_to(message, "❌ Account creation failed. Try again.")

bot.polling()
