from theBrain import *
import logging
import serial

# readFromSerial(RFmsg):

ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=.5)

def readFromSerial():
    if ser.is_open:
        pl = ser.readline().rstrip()
        if len(pl) > 2 and pl[0] == '<' and pl[1] == ',':
                RFmsg = pl
                return (True, RFmsg)
        else:
            return (False, "")
    else:
        ser.open()
        readFromSerial(RFmsg)


# goReal(msgOut)

def goReal(msgOut):

    ser.write('i'+str(msgOut.idr)+'\0')
    ser.flush()
    time.sleep(1)

    ser.write('j'+str(msgOut.payload_out)+'\0')
    ser.flush()

file_name = SYSTEM_PATH + "oFiles/" + sys.argv[0].split('/')[7].split('.')[0] + ".plk.buffer"


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(message)s')
logger = logging.getLogger()


if os.path.isfile(file_name):

    msgIn = []

    f = open(file_name,'r')

    while 1:
        try:
            o = pickle.load(f)
        except EOFError:
            break
        msgIn.append(o)

    f.close()

    RM_FILE_COMMAND = "sudo rm " + inputTelegram_filename
    os.system(inputTelegram_filename)

    print msgIn   
