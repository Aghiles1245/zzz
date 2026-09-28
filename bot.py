import telebot
bot = telebot.TeleBot("8902779511:AAH9L4_tX3Do2ozuEFcW7klX9mCkVIl9v-8")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك! أنا بوت التسويق الخاص بك 🚀")
bot.infinity_polling()