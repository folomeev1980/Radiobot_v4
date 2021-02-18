import os
import config
import logging
import  time
from pytube3.__main__ import YouTube as YouTube3
import re
import time
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

TOKEN = os.environ.get("TOKEN", '574990729:AAHvFVDSNg-LQ5RUSaPdbiQ2pOdDA7XI5Xc')
PORT = int(os.environ.get('PORT', '5000'))
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def link(update, context):
    try:
        if len(re.findall(r'(https?://[^\s]+)', update.message.text)) > 0:

            config.remove_files()
            mp3_link = config.youtube_link(update.message.text)

            yt = YouTube3(mp3_link)
            print(yt)
            filename = "input.webm"
            titl = str(yt.title)[0:35]
            audio = yt.streams.filter(only_audio=True, file_extension="webm")[0]
            #update.message.reply_text("\n....Начало скачивания....")
            audio.download(filename='input')

            update.message.reply_text("Начало конвертации: " + config.file_size(filename))
            config.convert_low32(filename)
            update.message.reply_text("Конец конвертации: " + config.file_size('output.mp3'))
            context.bot.send_chat_action(update.message.chat.id, 'upload_audio')
            audio = open("output.mp3", 'rb')
            context.bot.send_audio(update.message.chat.id, audio, title=titl)





        else:
            update.message.reply_text(config.help)

    except Exception as ex:
        update.message.reply_text("Error <<<{}>>>>".format(str(ex)))


def update(update, context):
    update.message.reply_text(str(update.message))
    
def cicle(update, context):
    while True:
        print("response", os.system('ping -c 1 ' + "https://radiobot3.herokuapp.com/"))
        time.sleep(20 * 60)



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)



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
    
    cicle_handler = MessageHandler(Filters.text, cicle)
    dispatcher.add_handler(cicle_handler)

  

    ##----------------Webhook-----------------------------

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.setWebhook("https://radiobot3.herokuapp.com/" + TOKEN)
    updater.idle()

    # while True:
    #     print( "response",os.system('ping -c 1 ' + "https://radiobot3.herokuapp.com/"))
    #     time.sleep(20*60)

        ##---------------------Webhook_end---------------------


if __name__ == '__main__':
    main()
