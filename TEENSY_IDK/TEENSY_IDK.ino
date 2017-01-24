#include <FlexCAN.h>
#include <kinetis_flexcan.h>
#include <stdlib.h>
#include <Servo.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>


#define MAIN_CAN_ID 0x13
#define TIMEOUT_LIMIT 500 

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

int led = 13;
FlexCAN can(500000);

CAN_message_t message;
int16_t thrusters[8] = {0,0,0,0,0,0,0,0};
int16_t thrusters_before_range_map[6] = {296, 296, 296, 296, 296, 296, 296, 296};
int16_t pin_map[8] = {6, 1, 4, 3, 5, 12, 8, 9};

void setup() {
  
  pinMode(led, OUTPUT);  
  
  Serial.begin(115200);
  Serial.print("hi there");

  //start i2c
  Serial.println("STARTING\n");

  can.begin();
  pwm.begin();
  pwm.setPWMFreq(50);

  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
}

void loop() {
  delay(1);
  Serial.print("Main loop");

  Serial.printf("%d\t%d\t%d\t%d\t%d\t%d\n", thrusters[0],thrusters[1],thrusters[2],thrusters[3],thrusters[4],thrusters[5]);
  
  if (can.available()) {
    Serial.println("Can available");
    if(can.read(message)) {
      Serial.println("Got can message");
      digitalWrite(led, HIGH);
      
      //if message came from main micro
      if (message.id == MAIN_CAN_ID && message.len == 8) {
        switch (message.buf[0]) {
          case 'L': // longitudinal data
            memcpy(&thrusters_before_range_map[0], &(message.buf[1]), 2);
            memcpy(&thrusters_before_range_map[1], &(message.buf[3]), 2);
            memcpy(&thrusters_before_range_map[2], &(message.buf[5]), 2);
            break;
          case 'R': // rotational data
            memcpy(&thrusters_before_range_map[3], &(message.buf[1]), 2);
            memcpy(&thrusters_before_range_map[4], &(message.buf[3]), 2);
            memcpy(&thrusters_before_range_map[5], &(message.buf[5]), 2);
            break;
        }
      }
    }
  }

  for (int i = 0; i < 6; i++) {
    int t_value = thrusters_before_range_map[i];
    t_value = map(t_value, -32768, 32767, 241, 351);
    pwm.setPWM(pin_map[i], 0, t_value); 
    thrusters[i] = t_value;
  }
  
  //digitalWrite(led, LOW);
  Serial.println(" ");
}
