#include <Wire.h>

#define I2C_ID 0x13 //Device pin

char incomingByte;  // incoming data
int  LED = 13;      // LED pin
char n;
char c = 0;
int16_t packetdata[8] = {0};

void setup() {
  Serial.begin(9600); // initialization
  Wire.begin();   
}

void sendi2c(int* packetdata) {
   // transmit to device I2C_ID
  for(int i = 0;i<10;i++){
    Wire.beginTransmission(I2C_ID);
    Wire.write(packetdata[i]);    
    Wire.endTransmission();
    delay(10);
  }
      // stop transmitting  
 
}
 
void loop() {  
  Serial.flush();
  Serial.print(packetdata[0]);
  printf("%d %d %d %d",packetdata[4],packetdata[5],packetdata[6],packetdata[7]);
  sendi2c(packetdata);
}
