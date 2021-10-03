import telebot
from settings import token
from telebot import types
from detection import draw_detecions

bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item=types.KeyboardButton("/send")
    markup.add(item)							
    bot.send_message(message.chat.id, 'Привет, добавь изображение чтобы обнаружить на нём объекты', reply_markup=markup)

@bot.message_handler(commands=['send'])
def send_message(message):
    bot.send_message(message.chat.id, 'Пришли фото файлом')

@bot.message_handler(content_types=['photo'])
def send_detect(message):
    fileID = message.photo[-1].file_id
    file = bot.get_file(fileID)
    downloaded_file = bot.download_file(file.file_path)
    with open("input.png", "wb") as f:
        f.write(downloaded_file)
    draw_detecions("input.png", "output.png")
    bot.send_chat_action(message.chat.id, 'upload_photo')
    bot.send_photo(message.chat.id, open("output.png", 'rb'))

bot.infinity_polling()
