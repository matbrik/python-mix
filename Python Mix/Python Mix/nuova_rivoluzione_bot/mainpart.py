import os
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
#0
import telegram
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler,Job)
import unidecode

import telegramdata
mtoken=telegramdata.mtoken
me=telegramdata.me

bot = telegram.Bot(token=mtoken)
u=Updater(token=mtoken)
j = u.job_queue

import requests

#1
import iointerface
import json
import scraping
import time
def wrapper(bot,job):

    print("called")
    job.enabled=False
    fn="riv.txt"
    lista=json.loads(iointerface.readFile(fn))


    cl=scraping.getChapterList("http://sgi-italia.org/riviste/nr/wordpress/")

    print(cl)
    max=int(lista)
    for article in cl:

        print(article)
        if int(article[0])>int(lista):
            if max<int(article[0]):
                max=int(article[0])
                print(str(max))
            response = requests.get(article[1]+"?print=pdf")
            name=str(article[0])
            with open(name+'.pdf', 'wb') as f:
                
                f.write(response.content)
                f.close()
                print("scritto")
                bot.sendDocument(chat_id=telegramdata.dele,document=open(name+".pdf",'rb'))
                os.remove(name+".pdf")
            #pappa
    iointerface.writeFile(fn,str(max))
    job.enabled=True


job_updater=Job(wrapper,2*60.0)
j.put(job_updater,next_t=0.0)
u.start_polling()
u.idle()
