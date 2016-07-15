#from theBrain import *
import os
import sys
import logging
import pickle
from theBrain import *

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(message)s')
logger = logging.getLogger()

if sys.platform == 'darwin':
    SYSTEM_PATH = '/Users/paolo/Documents/'
else:
    SYSTEM_PATH = '/home/pi/Documents/'

PATH_KEYS = SYSTEM_PATH + 'keys.txt'
fkey=open(PATH_KEYS,'r')
fkeylines=fkey.readlines()
GDRIVE_API_KEY = SYSTEM_PATH + fkeylines[1].split('\n')[0]
MONGODB_CLIENT_MLAB = fkeylines[3].split('\n')[0]
TELEGRAM_BRIDGE_REL = SYSTEM_PATH + fkeylines[5].split('\n')[0] + ".buffer"
ENERGYLOG = SYSTEM_PATH + fkeylines[7].split('\n')[0]
LOGCONFIG = SYSTEM_PATH + fkeylines[9].split('\n')[0]
SYNC_TRIG = SYSTEM_PATH + fkeylines[13].split('\n')[0]
PANEL_HTML = SYSTEM_PATH + fkeylines[15].split('\n')[0]
fkey.close()


while True:
    if os.path.isfile(TELEGRAM_BRIDGE_REL):

        msg = []

        f_rel=open(TELEGRAM_BRIDGE_REL,'rb')

        while 1:
            try:
                o = pickle.load(f_rel)
            except EOFError:
                break
            msg.append(o)

        f_rel.close()

        RM_FILE_COMMAND = "sudo rm " + TELEGRAM_BRIDGE_REL
        os.system(RM_FILE_COMMAND)

        for item in msg:
            if item['text'] == '/door':
                msgOut = answerTelegram()
