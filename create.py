import requests
import random
import telebot

bot = telebot.TeleBot("6993056231:AAFtrEyEfbWBo6ABAYLab6l9Ta7Mdw6Sioc")

def get_combo():
    url = requests.get("https://combolist.org/generate").text
    hi = url.split("false>")[1].split("</textarea>")[0]
    lines = hi.split('\n')
    random_line = random.choice(lines)
    el = random_line.split(':')[0]
    pd = random_line.split(':')[1]
    return "https://www.pythonanywhere.com/registration/register/beginner/\n\n**email :    **" + "`" + el + "`" + f"\n**pass :    `{pd}`"

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "**" + get_combo() + "**", parse_mode="Markdown")

bot.polling()
