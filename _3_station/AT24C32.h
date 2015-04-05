
#ifndef AT24C32_h
#define AT24C32_h
#include <Arduino.h>
#include <Wire.h>
//eeaddress <= [0,4096)


class AT24C32 {
	public:

		AT24C32();
		  void i2c_write(unsigned int eeaddress, byte data  );
	  
		 byte i2c_read(unsigned int eeaddress );
	
	private:
		
		
};
#endif
