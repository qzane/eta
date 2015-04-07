#include <Wire.h> 
//SDA <----> A4
//SCL <----> A5
#include "DS3231.h"
#include "BMP180.h"
#include "dht11.h"
#include "AT24C32.h"
dht11 DHT11;
DS3231 RTC; //Create the DS3231 object
BMP180 bmp;
AT24C32 ROM;
char weekDay[][4] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };

//year, month, date, hour, min, sec and week-day(starts from 0 and goes to 6)
//writing any non-existent time-data may interfere with normal operation of the RTC.
//Take care of week-day also.
DateTime date(0);
unsigned long serialTime;
unsigned long recordTime;
void setup () 
{
    Serial.begin(9600);
    Wire.begin();
    RTC.begin();
    //bmp.begin();
    serialTime = 0;
    RTC.convertTemperature();             //convert current temperature into registers
    Serial.println("Ready!");
    Serial.print(RTC.getTemperature()); //read registers and display the temperature
    Serial.println("deg C");
    //record();
    recordTime = micros();
    
}

void setTime(){
      Serial.println(102);
      long time  = Serial.parseInt();
      time -= 946656000;//the seconds to 2000-1-1 00:00:00
      date = DateTime(time);
      RTC.adjust(date);
      Serial.println(2);   
      date = RTC.now();
      Serial.println(date.year());
      Serial.println(date.month());
      Serial.println(date.date());
      Serial.println(date.hour());
      Serial.println(date.minute());
      Serial.println(date.second());   
      Serial.println(date.get()+946656000);
      RTC.convertTemperature();             //convert current temperature into registers
      Serial.print(RTC.getTemperature()); //read registers and display the temperature
      Serial.println("deg C");
}
void putTime(){
      date = RTC.now();
      Serial.println(date.year());
      Serial.println(date.month());
      Serial.println(date.date());
      Serial.println(date.hour());
      Serial.println(date.minute());
      Serial.println(date.second());   
      Serial.println(date.get()+946656000);
      RTC.convertTemperature();             //convert current temperature into registers
      Serial.print(RTC.getTemperature()); //read registers and display the temperature
      Serial.println("deg C");
      float t,p;
      //bmp.read(t,p);
      Serial.println(t);
      Serial.println(p);
      readHumidity();
}
void readHumidity(){
  return ;
 int chk = DHT11.read(2);

  Serial.print("Read sensor: ");
  switch (chk)
  {
    case DHTLIB_OK: 
                Serial.println("OK"); 
                break;
    case DHTLIB_ERROR_CHECKSUM: 
                Serial.println("Checksum error"); 
                break;
    case DHTLIB_ERROR_TIMEOUT: 
                Serial.println("Time out error"); 
                break;
    default: 
                Serial.println("Unknown error"); 
                break;
  }

  Serial.print("Humidity (%): ");
  Serial.println((float)DHT11.humidity, 2);

  Serial.print("Temperature (oC): ");
  Serial.println((float)DHT11.temperature, 2);

/*
  Serial.print("Dew Point (oC): ");
  Serial.println(dewPoint(DHT11.temperature, DHT11.humidity));

  Serial.print("Dew PointFast (oC): ");
  Serial.println(dewPointFast(DHT11.temperature, DHT11.humidity)); */
}
void clearROM(){
 for(int i=0;i<4096;++i)
    ROM.i2c_write(i,0); 
 Serial.println("Clear Done");
}

void record(){
  const unsigned short maxaddr = 4090;//4091~4095 used to record addr
  unsigned char buff[10];
  unsigned short addr;
  unsigned char i;
  for(i=0;i<2;++i)
    buff[i]=ROM.i2c_read(maxaddr+i);
  addr = *((unsigned short*)buff);
  
  Serial.print("addr: ");
  Serial.println(addr);
  date = RTC.now();
  RTC.convertTemperature();
  *(long*)buff = (long)(date.get()+946656000);
  *((short*)buff+2) =  (short)(RTC.getTemperature()*100);
  float t,p;
  //bmp.read(t,p);
  *((short*)buff+3) = (short)(p/10);
  DHT11.read(2);
  *((char*)buff+8) = (char)(DHT11.humidity);
  buff[9]=0xa5;
  for(i=0;i<9;++i)
    buff[9] ^= buff[i];
  Serial.println("Data:");
  for(i=0;i<10;++i){
    Serial.print(buff[i],DEC);
    Serial.print(' ');
  }  
  for(i=0;i<10;++i){
    ROM.i2c_write(addr,buff[i]);
    addr=(addr+1)%maxaddr;
  }
  *((unsigned short*)buff)=addr;
  for(i=0;i<2;++i){
    ROM.i2c_write(maxaddr+i,buff[i]);
  }
  Serial.println("Record Done");
}
void putRecord(){
  const int maxaddr = 4090;//4091~4095 used to record addr
  unsigned char buff[4];
  int addr,i;
  for(i=0;i<4;++i)
    buff[i]=ROM.i2c_read(maxaddr+i);
  addr = *((int*)buff);
  addr = (addr+1)%maxaddr;
  i=addr;
  do{
    Serial.print(ROM.i2c_read(i),DEC);
    Serial.print(' ');
    i=(i+1)%maxaddr;    
  }while(i!=addr);
  Serial.println("");
  Serial.flush();
  Serial.println("Record over!");
}
void loop () 
{
  if ((micros()- serialTime) > 50000 && Serial.available() > 0){
    //listening to Serial Port;
    int mood = Serial.parseInt();
    if (mood == 101){
      // set time signal
      setTime();
    }//end mood 101
    if (mood == 103){
       putTime(); 
    }
    if (mood == 5){
        clearROM();
    }
    if (mood == 107){
       putRecord(); 
    }
    if (mood == 105){
        record();
    }
    
    serialTime = micros();
  }//end listening to Serial Port;
  if((micros() - recordTime)>1500000000){ //25min
     record();
     recordTime = micros();
  }
  
}

