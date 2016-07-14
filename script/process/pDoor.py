#from theBrain import *
import logging

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

# f = open('store.pckl', 'rb')
# object = pickle.load(f)
# f.close()


if os.path.isfile(TELEGRAM_BRIDGE_REL):

    f_rel=open(TELEGRAM_BRIDGE_REL,'rb')
    msg = pickle.load(f_rel)
    f_rel.close()

    buff.close()
    RM_FILE_COMMAND = "sudo rm " + TELEGRAM_BRIDGE_REL
    os.system(RM_FILE_COMMAND)

    print msg
