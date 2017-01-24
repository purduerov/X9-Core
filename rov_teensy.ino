#include <FlexCAN.h>
#include <kinetis_flexcan.h>
#include <stdlib.h>
#include <Servo.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>


#define MAIN_CAN_ID 0x13
#define TIMEOUT_LIMIT 1000
#define LED 13

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
FlexCAN can(500000);

CAN_message_t message;
int16_t thrusters[8] = {0,0,0,0,0,0,0,0};
int8_t thrusters_before_range_map[8] = {0,0,0,0,0,0,0,0};
int8_t pin_map[8] = {6, 1, 4, 3, 5, 12, 8, 9};

int timeout = 0;

void setup() {
  pinMode(LED, OUTPUT);  
  Serial.begin(115200);

  //start i2c
  Serial.println("Starting initilizations...\n");

  can.begin();
  pwm.begin();
  pwm.setPWMFreq(50);

  digitalWrite(LED, LOW);
}

void loop() {
  delay(1);

  Serial.printf("%d %d %d %d ", thrusters[0],thrusters[1],thrusters[2],thrusters[3]);
  Serial.printf("%d %d %d %d\n", thrusters[4],thrusters[5],thrusters[6],thrusters[7]);
  
  if (can.available()) {
    if(can.read(message)) {
      digitalWrite(LED, HIGH);
      
      //if message came from main micro
      if (message.id == MAIN_CAN_ID && message.len == 8) {
        switch (message.buf[0]) {
          case 'L': // first set (1-4)
            memcpy(&thrusters_before_range_map[0], &(message.buf[1]), 4);
            break;
          case 'R': // second set (4-8)
            memcpy(&thrusters_before_range_map[4], &(message.buf[1]), 4);
            break;
        }

        timeout = 0;
      }
    }
  } else {
    digitalWrite(LED, LOW);
  }
  
  timeout++;

  if (timeout > TIMEOUT_LIMIT) {
    thrusters_before_range_map[0] = 0;
    thrusters_before_range_map[1] = 0;
    thrusters_before_range_map[2] = 0;
    thrusters_before_range_map[3] = 0;

    thrusters_before_range_map[4] = 0;
    thrusters_before_range_map[5] = 0;
    thrusters_before_range_map[6] = 0;
    thrusters_before_range_map[7] = 0;
  }

  for (int i = 0; i < 8; i++) {
    int t_value = thrusters_before_range_map[i];
    t_value = map(t_value, -128, 127, 241, 351);
    pwm.setPWM(pin_map[i], 0, t_value); 
    thrusters[i] = t_value;
  }
  
  Serial.println(" ");
}
