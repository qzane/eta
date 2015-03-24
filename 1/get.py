import serial
import re
import urllib2
import time

global ser
ser = None
def init():
    global ser
    for i in xrange(0,20):
        try:
            print 'try to open COM%d '%i,
            ser = serial.Serial(i)
            ser.baudrate = 9600
            print 'Done!'
            break
        except:
            print "Fail!"
def getTem():
    global ser
    if not ser:
        init()
    ser.flush()
    ser.flush()
    while(True):
        reply = ser.readline()
        begin = reply.find('Temperature')
        if begin != -1:
            end = reply.find('deg')
            Tem = float(reply[begin+12:end])
            break
    return Tem
            
            
if __name__ == '__main__':
    init()
'''        
def get_tmp():
    tmp = ''
    ser.flushInput()
    tmp = ser.read(15)
    tmp = re.search("[0-9][0-9]\.[0-9][0-9]",tmp).group(0)
    return tmp
    
while 1:
    try:
        temp = get_tmp()
        if temp > '80.00':
            0/0
        print temp
        res = urllib2.urlopen("http://qzanenet.sinaapp.com/put_temp?temp=%s"%temp)
        res = res.read()
        print res
        time.sleep(1)
    except:
        print "something wrong"
'''