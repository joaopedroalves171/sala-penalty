from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import logging
import random

# Habilita o logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(_name_)

# Token do seu bot aqui
TOKEN = '6891220585:AAH0mT-cmkSorNVh8qYgL4VaSm3xfArG_NY'

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

def main() -> None:
    """Inicia o bot."""
    updater = Updater(TOKEN)

    # Obtém o despachante para registrar manipuladores
    dp = updater.dispatcher

    # Diferentes manipuladores
    dp.add_handler(CommandHandler("start", start))

    # Inicia o Bot
    updater.start_polling()

    # Bloqueia até que você pressione Ctrl+C
    updater.idle()

if _name_ == '_main_':
    main()