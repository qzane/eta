#coding utf-8
import time
import serial
global ser
ser = None
def init():
    global ser
    for i in xrange(0,20):
        try:
            print 'try to open COM%d '%i,
            ser = serial.Serial(i)
            ser.baudrate = 9600
            ser.close()
            print 'Done!'
            break
        except:
            print "Fail!"
            
def setTime(Time=None):
    global ser
    if not ser:
        init()
    if not Time:
        ser.open()
        time.sleep(3)
        ser.flushInput()
        ser.write('101\n')
        ser.flush()
        print 'connecting...'
        while(True):
            if(ser.inWaiting()!=0 and ser.read(1)=='2'):
                break
        Time = time.time()
        ser.write('%d\n'%(Time+1))
        ser.flush()
        time.sleep(0.3)
        print ser.read(ser.inWaiting())
        ser.close()
        
def checkTime():
    global ser
    if not ser:
        init()
    ser.open()
    time.sleep(3)
    ser.flushInput()
    ti1 = time.time()
    ser.write('103\n')
    ser.flush()
    ti = time.time()
    time.sleep(0.3)
    a = ser.read(ser.inWaiting())
    ser.close()
    a = a.split('\n')
    w = [int(i) for i in a[:6]]+[0,0,0]
    tt = time.mktime(w)
    print tt-ti,tt,ti,ti-ti1
    return tt-ti
    
if __name__ == '__main__':
    init()
    setTime()
        