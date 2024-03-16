import requests
import random
import telebot

bot = telebot.TeleBot("6942844571:AAGYspt3qcvTgpXd4pcH-BDoHEpZWA19LXk")

def get_combo():
    url = requests.get("https://combolist.org/generate").text
    hi = url.split("false>")[1].split("</textarea>")[0]
    lines = hi.split('\n')
    random_line = random.choice(lines)
    el = random_line.split(':')[0]
    pd = random_line.split(':')[1]
    return "https://www.pythonanywhere.com/registration/register/beginner/**email :    **" + "`" + el + "`" + f"\n**pass :    `{pd}`"

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "**" + get_combo() + "**", parse_mode="Markdown")

bot.polling()
