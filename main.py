import telebot
import const
import os
import random

bot = telebot.TeleBot(const.token)

# bot.send_message(495176837, "test")


upd = bot.get_updates()
print(upd)

# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)
print(bot.get_me())


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('Photo', 'Audio', 'Documents')
    user_markup.row('Sticker', 'Video', 'Voice', 'Location')
    bot.send_message(message.from_user.id, 'Welcome', reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'BB keyboard', reply_markup=hide_markup)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Я помогу")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Photo':
        directory = '/Users/dianakraukle/Documents/IMAGES/botik/pics'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        print(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == 'Audio':
        directory = '/Users/dianakraukle/Documents/IMAGES/botik/music/Cycad - Always.mp3'
        audio = open(directory, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
    elif message.text == 'Documents':
        directory = '/Users/dianakraukle/Documents/IMAGES/botik/docs'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, doc)
            doc.close()
    elif message.text == 'Sticker':
        bot.send_sticker(message.from_user.id, const.template_sticker_id)
    elif message.text == 'Voice':
        directory = '/Users/dianakraukle/Documents/IMAGES/botik/voice/2018-08-16 19.52.18.ogg'
        voice = open(directory, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_voice(message.from_user.id, voice)
        voice.close()
    elif message.text == 'Video':
        directory = '/Users/dianakraukle/Documents/IMAGES/botik/video/Shooting Stars meme gordinho(Original Shooting Stars).mp4'
        video = open(directory, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_video')
        bot.send_voice(message.from_user.id, video)
        video.close()
    elif message.text == 'Location':
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, 56.9523121, 24.0996367)

    elif message.text == "a":
        answer = "B"
        bot.send_message(message.from_user.id, answer)
        log(message, answer)
    elif message.text == "b":
        answer = "C"
        bot.send_message(message.from_user.id, answer)
        log(message, answer)
    elif message.text == "3" or message.text == "4":
        answer = "3 or 4"
        bot.send_message(message.from_user.id, answer)
        log(message, answer)
    else:
        answer = "Ты лох"
        bot.send_message(message.from_user.id, answer)
        log(message, answer)


def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}, (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)


bot.polling(none_stop=True, interval=0)
