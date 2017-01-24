#include <Wire.h>

#define I2C_ID 0x13

char incomingByte;  // incoming data
int  LED = 13;      // LED pin
char n;
char c = 0;
int16_t packetdata[8] = {0};

void setup() {
  Serial.begin(9600); // initialization
  Wire.begin();   
   while (!Serial.available()){
    incomingByte = Serial.read();
    if(incomingByte == '5'){
        c = 0;
        Serial.println("Receieved 5");
       }
  }
}

void sendi2c(int* packetdata) {
   // transmit to device #9
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
  sendi2c(packetdata);
}
