set time:
    * comp->101
    * ardu->102
    * comp->yy mm dd hh min ss d
    * ardu->002
	
EEPROM:
	* 时间 4 byte (unsigned long)
	* 温度 2 byte (short = short(temp*100))
	* 气压 2 byte (short(pre/10))
	* 湿度 1 byte (0~100)

