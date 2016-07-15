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

inputTelegram_filename = SYSTEM_PATH + "iFiles/" + "iTelegram.plk.buffer"
outputSerial_filename = SYSTEM_PATH + "oFiles/" + "oSerial.plk"
outputSerial_filename_rel = outputSerial_filename + ".buffer"

while True:
    if os.path.isfile(inputTelegram_filename):

        msgIn = []

        f = open(inputTelegram_filename,'r')

        while 1:
            try:
                o = pickle.load(f)
            except EOFError:
                break
            msgIn.append(o)

        f.close()

        RM_FILE_COMMAND = "sudo rm " + inputTelegram_filename
        os.system(RM_FILE_COMMAND)


        for item in msgIn:
            if item['text'] == '/door':
                logger.DEBUG("trovata un testo door")
                msgOut = answerTelegram()
                f_abs = open(outputSerial_filename, 'a+')
                f_rel = open(outputSerial_filename_rel, 'a+')

                pickle.dump(msgOut, f_abs)
                pickle.dump(msgOut, f_rel)

                f_abs.close()
                f_rel.close()
                logger.DEBUG("fatto")
