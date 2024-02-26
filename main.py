import logging
import random
import telebot
import time
from datetime import datetime, timedelta
import pytz

# Token do seu bot aqui
TOKEN = "6891220585:AAFQ0oNT7F3gOEoSBeeh-VJEbugfGM3AZ5Q"
bot = telebot.telebot(TOKEN)




timezone = pytz.timezone('America/Sao_Paulo')

start_enabled = True

@bot.message_handler(commands=["✅Introduzar teu id"])
@bot.message_handler(commands=["Id encontrado✅"])
def send_welcome(message):
    global start_enabled
    if start_enabled:
        start_enabled = False
# Lista de imagens (coloque o caminho para suas imagens ou URLs)
imagens = [
     
    'https://www.canva.com/design/DAF9tjoqkEk/yqzB5XHL90Vzp28v1n-nDA/edit?utm_content=DAF9tjoqkEk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton',
    'https://www.canva.com/design/DAF9tjoqkEk/yqzB5XHL90Vzp28v1n-nDA/edit?utm_content=DAF9tjoqkEk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton',
    'https://www.canva.com/design/DAF9tjoqkEk/yqzB5XHL90Vzp28v1n-nDA/edit?utm_content=DAF9tjoqkEk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton',
    'https://www.canva.com/design/DAF9tjoqkEk/yqzB5XHL90Vzp28v1n-nDA/edit?utm_content=DAF9tjoqkEk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton',
    'https://www.canva.com/design/DAF9tjoqkEk/yqzB5XHL90Vzp28v1n-nDA/edit?utm_content=DAF9tjoqkEk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton',
]

# URL do site para o qual o botão irá direcionar
url_site = "https://oceano.bet/game/evoplay-penalty-shoot-out"

def start(update: Update, context: CallbackContext) -> None:
    # Seleciona uma imagem aleatória
    imagem_selecionada = random.choice(imagens)

    # Cria um botão que direciona para um site
    keyboard = [[InlineKeyboardButton("https://oceano.bet", url=url_site)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Envia a imagem com o botão
    update.message.reply_photo(photo=imagem_selecionada, reply_markup=reply_markup)

bot.polling()