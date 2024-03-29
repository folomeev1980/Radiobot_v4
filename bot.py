"""
Simple Bot to reply to Telegram messages taken from the python-telegram-bot examples.
Source:
"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import re
from pytube import YouTube as YouTube3
import os
import subprocess

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
# TOKEN = '574990729:AAHvFVDSNg-LQ5RUSaPdbiQ2pOdDA7XI5Xc'
# TOKEN = os.environ["TOKEN"]
TOKEN = None

# with open("tk.txt") as f:
#     TOKEN = f.read().strip()
#
#

# import os

TOKEN = os.environ["TOKEN"]
app_name = "radiobotv4"

import os

PORT = int(os.environ.get('PORT', 443))


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def link(update, context):
    try:
        if len(re.findall(r'(https?://[^\s]+)', update.message.text)) > 0:

            config.remove_files()
            mp3_link = config.youtube_link(update.message.text)

            #yt = YouTube3(mp3_link)

            filename = "input.webm"


            #titl = str(yt.title)[0:35]

            titl=config.get_title(mp3_link)[0:35]


            # audio = yt.streams.filter(only_audio=True, file_extension="webm")[0]
            # update.message.reply_text("\n....Начало скачивания....")
            # audio.download(filename='input')

            #
            bashCommand = "youtube-dl -f worstaudio -o input.webm " + mp3_link

            process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            print(output)

            update.message.reply_text("Начало конвертации: " + config.file_size(filename))

            # --------------------------------------------------------------------------------
            #config.convert_low32(filename)
            config.converter_api2()
            # update.message.reply_text("Конец конвертации: " + config.file_size('output.mp3'))
            context.bot.send_chat_action(update.message.chat.id, 'upload_audio')
            audio = open("output.mp3", 'rb')
            context.bot.send_audio(update.message.chat.id, audio, title=titl)
            # --------------------------------------------------------------------------------

            # config.convert_low32(filename)
            # update.message.reply_text("Конец конвертации: " + config.file_size('output.mp3'))
            # # context.bot.send_chat_action(update.message.chat.id, 'upload_audio')
            # audio = open("input.webm", 'rb')
            # context.bot.send_audio(update.message.chat.id, audio, title=titl)




        else:
            print(update.message.chat.id)
            update.message.reply_text(config.help)

    except Exception as ex:
        update.message.reply_text("Error <<<{}>>>>".format(str(ex)))


def update(update, context):
    update.message.reply_text(str(update.message))


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_error_handler(error)

    #    Commands

    update_handler = CommandHandler('update', update)
    dispatcher.add_handler(update_handler)

    #    Messages

    link_handler = MessageHandler(Filters.text, link)
    dispatcher.add_handler(link_handler)

    # Start the Bot
    if not app_name:  # pooling mode
        print("Can't detect 'HEROKU_APP_NAME' env. Running bot in pooling mode.")
        print("Note: this is not a great way to deploy the bot in Heroku.")

        updater.start_polling()
        updater.idle()

    else:  # webhook mode
        print("Running bot in webhook mode. Make sure that this url is correct: https://{}.herokuapp.com/".format(
            app_name))
        updater.start_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
            webhook_url="https://{}.herokuapp.com/{}".format(app_name, TOKEN)
        )

        #    updater.bot.set_webhook(f"https://{HEROKU_APP_NAME}.herokuapp.com/{TELEGRAM_TOKEN}")
        updater.idle()


if __name__ == '__main__':
    main()
