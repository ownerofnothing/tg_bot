import random
import telebot
import info
token = '6788020728:AAGZwqEp6r2NffMuWF6-JW2E9n8YSX2KxW0'
bot = telebot.TeleBot(token)


def hello_checker(message):
    return "привет" in message.text.lower()


@bot.message_handler(content_types=['text'], func=hello_checker)
def get_message(message):
    bot.send_message(message.chat.id, random.choice(info.greetings), reply_to_message_id=message.id)


def call_checker(message):
    return message.text.lower() == "брут"


@bot.message_handler(content_types=['text'], func=call_checker)
def get_message(message):
    bot.send_message(message.chat.id, random.choice(info.called), reply_to_message_id=message.id)


def bye_checker(message):
    return "пока" in message.text.lower()


@bot.message_handler(content_types=['text'], func=bye_checker)
def get_message(message):
    bot.send_message(chat_id=message.chat.id, text=random.choice(info.goodbyes), reply_to_message_id=message.id)


def start_checker(message):
    return "/start" in message.text


@bot.message_handler(content_types=['text'], func=start_checker)
def start(message):
    bot.send_message(chat_id=message.chat.id, text=info.start_soo, reply_to_message_id=message.id)


def good_friend(message):
    return message.text.lower() == "ты хороший друг, брут"


@bot.message_handler(content_types=['text'], func=good_friend)
def blin(message):
    bot.send_message(chat_id=message.chat.id, text="Я сделаю вид, что Вы этого не говорили, и мы сменим тему, ладно?", reply_to_message_id=message.id)


def help_checker(message):
    return message.text == "/help"


@bot.message_handler(content_types=['text'], func=help_checker)
def helps(message):
    bot.send_message(chat_id=message.chat.id, text=info.help_soo, reply_to_message_id=message.id)


def about_checker(message):
    return message.text == "/about"


@bot.message_handler(content_types=['text'], func=about_checker)
def about(message):
    bot.send_message(chat_id=message.chat.id, text=info.about_soo, reply_to_message_id=message.id)


def hobbie_checker(message):
    return message.text == "/hobbies"


@bot.message_handler(content_types=['text'], func=hobbie_checker)
def hobbies(message):
    bot.send_message(chat_id=message.chat.id, text=info.hobbies_soo, reply_to_message_id=message.id)


bot.polling()
