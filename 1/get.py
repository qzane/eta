#coding:utf-8
import serial
import serial.tools.list_ports as ports
#ports.main()
''' python
inWaiting()
Return the number of chars in the receive buffer.
flush()
Flush of file like objects. In this case, wait until all data is written.
flushInput()
Flush input buffer, discarding all it’s contents.
flushOutput()
Clear output buffer, aborting the current output and discarding all that is in the buffer.
'''
''' C
available()

Description

Get the number of bytes (characters) available for reading from the serial port. This is data that's already arrived and stored in the serial receive buffer (which holds 64 bytes). available() inherits from the Stream utility class. 

millis()

Description

Returns the number of milliseconds since the Arduino board began running the current program. This number will overflow (go back to zero), after approximately 50 days. 

micros()

Description

Returns the number of microseconds since the Arduino board began running the current program. This number will overflow (go back to zero), after approximately 70 minutes. On 16 MHz Arduino boards (e.g. Duemilanove and Nano), this function has a resolution of four microseconds (i.e. the value returned is always a multiple of four). On 8 MHz Arduino boards (e.g. the LilyPad), this function has a resolution of eight microseconds. 


Note: there are 1,000 microseconds in a millisecond and 1,000,000 microseconds in a second. 
Returns

Number of microseconds since the program started (unsigned long) 


'''
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