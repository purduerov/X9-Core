import logging
import sys
import time
import smbus
from CameraServo import Servo

#ASSUME that you are using a Servo Class created by Power and Movement that sets the servo to a raw angle.
#ASSUME that servo has a function called setAngle which sets the servo angle appropriately.

class CameraServoWrapper(object):
      def __init__(self):
            self.servo = Servo
            #The angle is the raw angle from servo.
            self.angle = 0
            #The reference angle is the angle we SET zero
            self.HomeAngle = 0
    
      def setRawAngle(self, angle):
            #sets the raw angle of the servo appropriately
            self.servo.setAngle(angle)
            self.angle = angle
  
      def upAngle(self, angle):
            #sets the angle up a certain number of degrees above the current angle
            self.angle = self.angle + angle
            if self.angle > 180:
                  self.angle = 180
            self.setRawAngle(set.angle)

      def downAngle(self, angle):
            #sets the angle DOWN a certain number of degrees above the current angle
            self.angle = self.angle - angle
            if self.angle < 0:
                  self.angle = 0
            self.setRawAngle(set.angle)

      def positionAtZero(self):
            #sets the angle of the camera servo at zero
            self.setRawAngle(self, 0)

      def setHomeToCurrentAngle(self):
            #sets the Home angle to the current angle
            self.HomeAngle = self.angle

      def setHomeToAngle(self, angle):
            #sets the Home angle to a given angle
            tempAngle = angle
            if (angle < 0):
                  tempAngle = 0
            if (angle > 180):
                  tempAngle = 180
            self.HomeAngle = tempAngle                  
        
      def setHomeAndMoveToAngle(self, angle):
            self.setHomeToAngle(angle)
            self.setRawAngle(self.HomeAngle)

      def positionAtHome(self):
            self.setRawAngle(self.HomeAngle)

      def returnCurrentAngle(self):
            return self.angle

      def returnHomeAngle(self):
            return self.HomeAngle