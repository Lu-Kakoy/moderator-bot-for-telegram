import telebot
from telebot.types import *
                                                                                                       # @moderat0r1_bot
token1 = '7650991154:AAFfreZ8QhgKr1xm1KtVzX3KRnffFZ5vz6U'
bot1 = telebot.TeleBot(token1)
import s_taper
from s_taper.consts import *

data1 = {'id': INT, 'name': TEXT, 'message': TEXT, 'message_id': INT}
data2 = s_taper.Taper('users', 'data1.db').create_table(data1)
end2 = 0
end1 = 0

@bot1.message_handler(['clean123'])
def clean1(message1: Message):
    chat_id1 = []
    message_id1 = []
    date3 = data2.read_all()
    for i in date3:
        if i[0] == message1.chat.id:
            chat_id1.append(i[0])
            message_id1.append(i[3])
            data2.delete_row('id', i[0])
    try:
        bot1.delete_messages(chat_id1[0], message_id1)
        bot1.delete_message(chat_id1[0], message1.message_id)
    except:
        print('error1')
        print(message1.text)

file1 = open('ploxie_slova.txt', 'r', encoding='utf-8')
list_of_bad_words = []
for i in file1:
    list_of_bad_words.append(i.strip())
file1.close()

@bot1.message_handler(content_types=['text'])
def save_message1(message1):
    global end2
    global end1
    data2.write([message1.chat.id, message1.from_user.username, message1.text, message1.message_id])
    for i in list_of_bad_words:
        print(i)
        for k in message1.text.split(' '):
            args_for_strip = [',', '!', '?', '.', ':', ';', '(', ')']
            for rep1 in range(0, 6):
                for n in args_for_strip:
                    k = k.strip(n)
            k = k.lower()
            print(k)
            if i == k:
                print(1)
                bot1.delete_message(message1.chat.id, message1.message_id)
                data2.delete_row('message', message1.text)
            else:
                break
    if message1.text == 'режим 1':
        end2 = 1
    if message1.text == 'режим 2':
        end2 = 0
    if end2 == 1:
        if end1 == 0:
            bot1.send_message(message1.chat.id, f'все говорят «{message1.text}», а ты купи слона')
        else:
            bot1.send_message(message1.chat.id, f'пук пук пук')


bot1.infinity_polling()