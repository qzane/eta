#coding utf-8
import time
import serial
global ser

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
    if not Time:
        ser.open()
        time.sleep(3)
        Time = time.time()
        ser.write('%d %d\n'%(101,Time));
        time.sleep(0.3)
        print ser.read(ser.inWaiting())
        ser.close()
        
if __name__ == '__main__':
    init()
    setTime()
        