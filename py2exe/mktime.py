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
    
def readData():
    global ser
    if not ser:
        init()
    ser.flushInput()
    ser.write('103\n')
    ser.flush()
    time.sleep(0.3)
    a = ser.read(ser.inWaiting())
    print a

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
    
    return (data)#,q)
    
def saveData():
    q = set(getData())
    
    try:
        with open('data.csv','w') as f:
            while(1):
                tmp = f.readline()
                if tmp == '':
                    break
                tmp = tmp.split(',')
                tmp = (int(tmp[0]),float(tmp[1]),float(tmp[2]),int(tmp[3]))
                q.add(tmp)
    except:
        pass
        
    q = list(q)
    q.sort(key=lambda x:x[0])
    
    with open('data.csv','w') as f:
        for i in q:
            f.write('%d,%f,%f,%d\n'%i)
        f.flush()
    
    
if __name__ == '__main__':
    while(1):
        try:
            print "1.给传感器对时\n2.读取传感器实时数据\n3.读取所有数据\n4.退出\n请选择: ".decode('utf-8'),
            mood = raw_input()
            mood = int(mood)
            if mood == 1:
                setTime()
            elif mood == 2:
                readData()
            elif mood == 3:
                print '大概需要20秒钟，请稍后...'.decode('utf-8')
                saveData()
                print "读取成功！数据保存在data.csv文件里，可以用excel打开，每行的数据分别是 时间,温度,气压,湿度".decode('utf-8')
                setTime()
            elif mood == 4:
                break
            else:
                pass
        except:
            print '输入错误'.decode('utf-8')