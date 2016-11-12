import logging
import sys
import time
import smbus
from ServoClass import Servo

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
    self.servo.selfAngle(angle)
    self.angle = angle
  
  def upAngle(self, angle):
    #sets the angle up a certain number of degrees above the current angle
    self.angle = self.angle + angle
    if self.angle > 180:
      self.angle = 180
    setRawAngle(self, set.angle)

  def downAngle(self, angle):
    #sets the angle DOWN a certain number of degrees above the current angle
    self.angle = self.angle - angle
    if self.angle < 0:
      self.angle = 0
    setRawAngle(self, set.angle)

  def setToZero(self):
    setRawAngle(self, 0)

  def setHomeToCurrentAngle(self):
