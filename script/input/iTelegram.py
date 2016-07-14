import sys
import time
import telepot
import datetime
import pickle
import logging


# f = open('store.pckl', 'wb')
# pickle.dump(object, f)
# f.close()
#


SYSTEM_PATH = '/home/pi/Documents/'
PATH_KEYS = SYSTEM_PATH + 'keys.txt'
fkey=open(PATH_KEYS,'r')
fkeylines=fkey.readlines()
TELEGRAM_BRIDGE = SYSTEM_PATH + fkeylines[5].split('\n')[0]
TELEGRAM_KEY = fkeylines[11].split('\n')[0]
fkey.close()

TELEGRAM_BRIDGE_REL = TELEGRAM_BRIDGE + ".buffer"

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(message)s')
logger = logging.getLogger()

def handle(msg):
    f_abs = open(TELEGRAM_BRIDGE, 'a+')
    f_rel = open(TELEGRAM_BRIDGE_REL, 'a+')
    pickle.dump(msg, f_abs)
    pickle.dump(msg, f_rel)
    f_abs.close()
    f_rel.close()

    chat_id = msg['chat']['id']
    command = msg['text']

    try:
        nome = msg['from']['first_name']
    except:
            nome = "utente che non hai inserito il suo nome in Telegram"

    logger.debug(chat_id)

    #if command == '/door' and chat_id == -123571607:
    if command == '/door':
        notizia = "ai tuoi ordini " + nome
        bot.sendMessage(chat_id, notizia)


bot = telepot.Bot(TELEGRAM_KEY)
bot.message_loop(handle)

while True:

    time.sleep(10)
