import telebot
import random
from datetime import datetime
from config import mezzage_day, mezzage_night

bot = telebot.TeleBot("5254236633:AAFXg6vQmckgHgysEkKES50Vohme-hWQFJQ")
am_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 22)
pm_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day+1, 8)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if am_time < datetime.now() < pm_time:
        bot.reply_to(message, "Тссссссс, ты хренли команды пишешь ночью??????\nладно.....\nГОЛОСОВЫЕ НЕЛЬЗЯ!!!!!")
    else:
        bot.reply_to(message, "короч, НЕЛЬЗЯ гс отправлять")


@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    if am_time < datetime.now() < pm_time:
        bot.reply_to(message, random.choice(mezzage_night))
    else:
        bot.reply_to(message, random.choice(mezzage_day))
    pass


@bot.message_handler(content_types=['video_note'])
def handle_pochti_audio(message):
    bot.reply_to(message, 'нихера ты пидор, но только на половину, тебя ебёт только 1 негр')
    pass


bot.infinity_polling()
