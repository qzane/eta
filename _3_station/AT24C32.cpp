#include "AT24C32.h"

const int AT24C32_ADDR = 0x57;

AT24C32::AT24C32() {
	// nothing to do for this constructor.
}


void AT24C32::i2c_write(unsigned int eeaddress, byte data  ) {
    //int rdata = data;
    Wire.beginTransmission(AT24C32_ADDR);
    Wire.write((int)(eeaddress >> 8)); // MSB
    Wire.write((int)(eeaddress & 0xFF)); // LSB
    Wire.write(data);
    Wire.endTransmission();
    delay(2);
  }


byte AT24C32::i2c_read(unsigned int eeaddress ) {
    byte rdata = 0xFF;
    Wire.beginTransmission(AT24C32_ADDR);
    Wire.write((int)(eeaddress >> 8)); // MSB
    Wire.write((int)(eeaddress & 0xFF)); // LSB
    Wire.endTransmission();
    Wire.requestFrom(AT24C32_ADDR,1);
    if (Wire.available()) rdata = Wire.read();
    return rdata;
  }

