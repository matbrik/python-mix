"""
0 inizializzo telegram bot
1 leggo da file i dati dei manga
2 controllo se c'� un update
3 se si invio all'utente i pdf
4 aggiorno il file 
5 aspetto n minuti 
6 punto 1
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
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

def callback_updater(bot,job):
    print("called")
    job.enabled=False
    fn="mangas.txt"
    lista=json.loads(iointerface.readFile(fn))
    
    print(lista)
#2
    for m in lista:
        cl=scraping.getChapterList(m["url"])
        print(cl)
        if(int(m["last_chap"])<int(cl[0])):
            print("here")
            cl=cl[:cl.index(str(m["last_chap"]))]
            last=cl[0]
            for chap in sorted(cl):
#3      
                filename=scraping.create_page(m["url"],m["name"],chap)
                print(filename+" created")
                bot.sendDocument(chat_id=me,document=open(filename,'rb'))
                os.remove(filename)
                print(filename+" removed")
            m["last_chap"]=str(last)
    print(lista)
#4
    iointerface.writeFile(fn,json.dumps(lista))
    job.enabled=True

job_updater=Job(callback_updater,2*60.0)
j.put(job_updater,next_t=0.0)
u.start_polling()
u.idle()