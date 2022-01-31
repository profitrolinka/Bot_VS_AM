import telebot
bot = telebot.TeleBot("5254236633:AAFXg6vQmckgHgysEkKES50Vohme-hWQFJQ")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "короч, НЕЛЬЗЯ гс отправлять")


@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    bot.reply_to(message, "сука, я же блина говорил, ГОЛОСОВЫЕ НЕЛЬЗЯ, пидор")
    pass


@bot.message_handler(content_types=['video_note'])
def handle_pochti_audio(message):
    bot.reply_to(message, 'нихера ты пидор, но только на половину, тебя ебёт только 1 негр')
    pass


bot.infinity_polling()