import pylab

def readData():
    with open('data.csv') as f:
        q = f.readlines()
    w =[i.split(',') for i in q]
    ti = []
    temp = []
    pre = []
    hi = []
    for i in w:
        #q.append((int(i[0]),float(i[1]),float(i[2]),int(i[3])))
        ti.append(int(i[0]))
        temp.append(float(i[1]))
        pre.append(float(i[2])/1000.0)
        hi.append(int(i[3]))        
    return (ti,temp,pre,hi)
    
def main():
    q = readData()
    pylab.plot(q[0],q[1],'.',label = 'temperature $(^{\circ}\mathrm{C})$')
    pylab.plot(q[0],q[2],'.',label = 'pressure $(KPa)$')
    pylab.plot(q[0],q[3],'.',label = r'humidity $(\%)$')
    pylab.legend()
    pylab.show()
    
if __name__ == '__main__':
    main()