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
            time.sleep(3)
            #ser.close()
            print 'Done!'
            break
        except:
            print "Fail!",
            
def setTime(Time=None):
    global ser
    if not ser:
        init()
    if not Time:
        #ser.open()
        #time.sleep(3)
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
        #ser.close()
        
def checkTime():
    global ser
    if not ser:
        init()
    #ser.open()
    #time.sleep(3)
    ser.flushInput()
    ti1 = time.time()
    ser.write('103\n')
    ser.flush()
    time.sleep(0.3)
    a = ser.read(ser.inWaiting())
    ti = time.time()
    #ser.close()
    a = a.split('\n')
    w = [int(i) for i in a[:6]]+[0,0,0]
    tt = time.mktime(w)
    ttt = int(a[6])
    print tt-ti,tt,ttt,ti,ti-ti1
    return tt-ti
    
def getData():
    global ser
    if not ser:
        init()
    #ser.open()
    #time.sleep(3)
    ser.flushInput();
    ser.write('107\n')
    q = []
    tmp = ''
    now = 0
    while 1:
        time.sleep(0.3)
        if now == ser.inWaiting():
            break
        now = ser.inWaiting();
        
    tmp = ser.read(ser.inWaiting())
    for i in tmp.split(' '):
        try:
            q.append(int(i))
        except:
            pass
    q = q + q[:9]
    data = []
    w = []
    check = 0xa5
    for i in q:
        if len(w)<9:
            w.append(i)
            check ^= i
        elif check != 0 and check == i:
            ti = 0
            for j in range(3,-1,-1):
                ti <<= 8
                ti |= w[j]
            temp = (w[4]+(w[5]<<8))/100.0
            pre = (w[6]+(w[7]<<8))*10
            hum = w[8]
            data.append((ti,temp,pre,hum))
            check = 0xa5
            w = []
        else:
            check ^= i
            check ^= w[0]
            del(w[0])
            w.append(i)
    
    return (data,q)
    
    
    
    
if __name__ == '__main__':
    init()
    setTime()
        