"""
0 inizializzo telegram bot
1 leggo da file i dati dei manga
2 controllo se c un update
3 se si invio all'utente i pdf
4 aggiorno il file 
5 aspetto n minuti 
6 punto 1

aggingo ln from wuxiaworld appoggiandmi su un altro progetto già realizzato

"""
import os
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
#0
import telegram
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler,Job)


import telegramdata
mtoken=telegramdata.mtoken
me=telegramdata.me

bot = telegram.Bot(token=mtoken)
u=Updater(token=mtoken)
j = u.job_queue



#1
import iointerface
import json
import scraping
import time
def wrapper(bot,job):


    print("called")
    job.enabled=False
    fn="wuxia.txt"
    lista=json.loads(iointerface.readFile(fn))
    
    print(lista)
#2
    for m in lista:
        cl=scraping.getChapterList(m["url"],int(m["last_chap"]))
        print(cl)
        if(int(m["last_chap"])<int(cl)):
            print("here")

            filename=scraping.create_page(m["url"],m["name"],int(m["last_chap"]),cl+1)
            print(str(filename))
            print(filename+" created")
            bot.sendDocument(chat_id=me,document=open(filename,'rb'))
            os.remove(filename)
            print(filename+" removed")
            m["last_chap"]=str(cl)
    print(lista)
#4
    iointerface.writeFile(fn,json.dumps(lista))
    job.enabled=True

job_updater=Job(wrapper,2*60.0)
j.put(job_updater,next_t=0.0)
u.start_polling()
u.idle()
