
"""
Simple Bot to reply to Telegram messages taken from the python-telegram-bot examples.
Source: https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py
"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '574990729:AAHvFVDSNg-LQ5RUSaPdbiQ2pOdDA7XI5Xc'


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

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    if not "radiobotv4":  # pooling mode
        print("Can't detect 'HEROKU_APP_NAME' env. Running bot in pooling mode.")
        print("Note: this is not a great way to deploy the bot in Heroku.")

        updater.start_polling()
        updater.idle()

    else:  # webhook mode
        print(
            f"Running bot in webhook mode. Make sure that this url is correct: https://radiobotv4.herokuapp.com/")
        updater.start_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
            webhook_url="https://{}.herokuapp.com/{}".format("radiobotv4",TOKEN)
        )

        #    updater.bot.set_webhook(f"https://{HEROKU_APP_NAME}.herokuapp.com/{TELEGRAM_TOKEN}")
        updater.idle()

if __name__ == '__main__':
    main()
#view rawpythontelegrambot.py hosted with ❤ by GitHub