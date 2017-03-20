
import telegram
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import test1

address="http://www.readmanga.today/tales-of-demons-and-gods/"
name="talesofdemonegods"
num=1
URL, NUMBER, CONF= range(3)


mtoken="346510765:AAHMvPYEZ2JSKD0-mnHe1ngAJYFXROrd1TQ"
"""
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=name)
    num=test1.getChapterList(address)[0]
    filename=test1.create_page(address,name,num)
    print(filename+" created")
    bot.sendDocument(chat_id=update.message.chat_id,document=open(filename,'rb'))
    print("doc sent")
"""
def start(bot, update):
    update.message.reply_text("send me the url of the manga")
    return URL
def url(bot,update,user_data):
    text=update.message.text
    user_data['address']= text
    update.message.reply_text("send number of chapter")
    return NUMBER
def number(bot, update, user_data):
    num=update.message.text
    user_data['num'] = num
    update.message.reply_text("/send number of chapter")

    return CONF
def compute(bot, update, user_data):
    filename=test1.create_page(user_data['address'],"chapter",user_data['num'])
    print(filename+" created")
    bot.sendDocument(chat_id=update.message.chat_id,document=open(filename,'rb'))
    print("doc sent")
    user_data.clear()
    return ConversationHandler.END


def cancel(bot, update, user_data):
    update.message.reply_text("bye")
    user_data.clear()
    return ConversationHandler.END


bot = telegram.Bot(token=mtoken)
print(bot.getMe())

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

updater = Updater(token=mtoken)
dispatcher = updater.dispatcher


conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            URL: [MessageHandler(Filters.text, url,pass_user_data=True),
                    CommandHandler('skip', cancel,pass_user_data=True)],

            NUMBER: [MessageHandler(Filters.text, number,pass_user_data=True),
                    CommandHandler('skip', cancel,pass_user_data=True)],

            CONF: [CommandHandler('send', compute,pass_user_data=True),
                    CommandHandler('skip', cancel,pass_user_data=True)]
        },

        fallbacks=[CommandHandler('cancel', cancel,pass_user_data=True)]
    )

dispatcher.add_handler(conv_handler)



updater.start_polling()
updater.idle()
