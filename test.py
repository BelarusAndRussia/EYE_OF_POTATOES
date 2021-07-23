import telebot
import psycopg2


conn = psycopg2.connect(dbname='eye_of_potatoes', user='postgres', password='101010', host='localhost', port='1234')
conn.autocommit = True
cur = conn.cursor()

bot = telebot.TeleBot('1872273294:AAFE2PGjCEIo28bh6UowoELtmJ7Qal3VxG0')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот созданный Даниилом Турпаковым. Приятно познакомиться, {message.from_user.first_name}. Ведите номер телефона цели')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    cur.execute(f"SELECT * FROM eyeofgod WHERE phone = '{message.text}'")
    data = cur.fetchall()
    if data:
        colnames = [desc[0] for desc in cur.description]
        msg = ""
        for i in range(len(data[0])):
            msg = msg + colnames[i] + ": " + str(data[0][i]) + "\n"
        bot.send_message(message.from_user.id, msg)
    else:
        bot.send_message(message.from_user.id, "Ничего не найдено")

bot.polling(none_stop=True)