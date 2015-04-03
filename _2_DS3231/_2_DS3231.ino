#include <Wire.h>
#include "DS3231.h"
#include "BMP180.h"
#include "dht11.h"
dht11 DHT11;
DS3231 RTC; //Create the DS3231 object
BMP180 bmp;
char weekDay[][4] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };

//year, month, date, hour, min, sec and week-day(starts from 0 and goes to 6)
//writing any non-existent time-data may interfere with normal operation of the RTC.
//Take care of week-day also.
DateTime date(0);
unsigned long serialTime;

void setup () 
{
    Serial.begin(9600);
    Wire.begin();
    RTC.begin();
    bmp.begin();
    serialTime = 0;
    RTC.convertTemperature();             //convert current temperature into registers
    Serial.println("Ready!");
    Serial.print(RTC.getTemperature()); //read registers and display the temperature
    Serial.println("deg C");
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
      
      RTC.convertTemperature();             //convert current temperature into registers
      Serial.print(RTC.getTemperature()); //read registers and display the temperature
      Serial.println("deg C");
      float t,p;
      bmp.read(t,p);
      Serial.println(t);
      Serial.println(p);
      readHumidity();
}
void readHumidity(){
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
void loop () 
{
  if ((micros()- serialTime) > 1000000 && Serial.available() > 0){
    //listening to Serial Port;
    int mood = Serial.parseInt();
    if (mood == 101){
      // set time signal
      setTime();
    }//end mood 101
    if (mood == 103){
       putTime(); 
    }
    
    serialTime = micros();
  }//end listening to Serial Port;
  
  
}

