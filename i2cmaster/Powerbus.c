// Code used from Peter Fleury <pfleury@gmx.ch> - Ajay
// Not tested with power brick, temporary code 


#include <avr/io.h>
#include "i2cmaster.h"
#define Dev24C02  0xA2      // device address of EEPROM 24C02, see datasheet
#define Bus1 0x33 //Power Bus 1

int main(void){}
{
    unsigned char ret;
    

    DDRB  = 0xff;                              // use all pins on port B for output 
    PORTB = 0xff;                              // (active low LED's )

    i2c_init();                                // init I2C interface

    /* write 0x75 to eeprom address 0x05 (Byte Write) */
    //  ret = i2c_start(Dev24C02+I2C_WRITE);       // set device address and write mode
 // if ( ret ) {
        /* failed to issue start condition, possibly no device found */
   //     i2c_stop();
   //     PORTB=0x00;                            // activate all 8 LED to show error */
  //}else {
        /* issuing start condition ok, device accessible */
    //    i2c_write(0x05);                       // write address = 5
      //  i2c_write(0x75);                       // ret=0 -> Ok, ret=1 -> no ACK 
        //i2c_stop();                            // set stop conditon = release bus

        /* write ok, read value back from eeprom address 0x05, wait until 
           the device is no longer busy from the previous write operation */
       // i2c_start_wait(Dev24C02+I2C_WRITE);     // set device address and write mode
        //i2c_write(0x05);                        // write address = 5
    /*    i2c_rep_start(Dev24C02+I2C_READ);       // set device address and read mode
        ret = i2c_readNak();                    // read one byte
        i2c_stop();
        
        PORTB = ~ret;                           // output byte on the LED's*/

        /* write 0x70,0x71,072,073 to eeprom address 0x00..0x03 (Page Write),
           wait until the device is no longer busy from the previous write operation */
        /*i2c_start_wait(Dev24C02+I2C_WRITE);     // set device address and write mode
        i2c_write(0x00);                        // write start address = 0
        i2c_write(0x70);                        // write data to address 0
        i2c_write(0x71);                        //    "    "   "    "    1
        i2c_write(0x72);                        //    "    "   "    "    2
        i2c_write(0x74);                        //    "    "   "    "    3
        i2c_stop();                             // set stop conditon = release bus*/
    
        /* write ok, read value back from eeprom address 0..3 (Sequencial Read),
           wait until the device is no longer busy from the previous write operation */
       /* i2c_start_wait(Dev24C02+I2C_WRITE);      // set device address and write mode
        i2c_write(0x00);                         // write address = 0
        i2c_rep_start(Dev24C02+I2C_READ);        // set device address and read mode
        ret = i2c_readAck();                       // read one byte form address 0
        ret = i2c_readAck();                       //  "    "    "    "     "    1
        ret = i2c_readAck();                       //  "    "    "    "     "    2
        ret = i2c_readNak();                       //  "    "    "    "     "    3
        i2c_stop();                              // set stop condition = release bus
    
        PORTB = ~ret;                            // output byte on the LED's        
    }*/
    
   
	
	ret = i2c_start(Bus1+I2C_WRITE);  
	if ( ret ) {
        /* failed to issue start condition, possibly no device found */
        i2c_stop();
        PORTB=0x00;                            // activate all 8 LED to show error */
    }
	else {
		i2c_write(Bus1);                       // write address = Bus1
        i2c_write(0x75);                       // write at address 42, value 75
       
	    i2c_start_wait(Dev24C02+I2C_WRITE);     // set device address and write mode
        i2c_write(Bus1);                   // write address = 5
		i2c_rep_start(Bus1+I2C_READ);       // set device address and read mode
        ret = i2c_readNak();                    // read one byte
        i2c_stop();
	}
}