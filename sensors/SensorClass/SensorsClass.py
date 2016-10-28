import logging
import sys
import time

from Adafrui_BNO055 import BNO055

bno = BNO055.BNO055(rst=18)

class SensorsClass(object)
{
    #initialize function
    def __init__(self)
    {
        bno.begin()
        #start all other sensors here as well
    }

    #EULER FUNCTIONS
    def get_Heading(self)
    { 
        return bno.read_euler()[0]
    }

    def get_Roll(self)
    {
        return bno.read_euler()[1]
    }

    def get_Pitch(self)
    {
        return bno.read_euler()[2]
    }

    def get_HeadingRollPitch(self)
    {
        x,y,z = bno.read_euler()
        return (x,y,z)
    }

    #LINEAR ACCELERATION FUNCTIONS, acceleration from movement, not gravity
    def get_X_LinearAcceleration(self)
    {
        return bno.read_linear_acceleration()[0]
    }

    def get_Y_LinearAcceleration(self)
    {
        return bno.read_linear_acceleration()[1]
    }

    def get_Z_LinearAcceleration(self)
    {
        return bno.read_linear_acceleration()[2]
    }

    def get_Linear_Acceleration(self)
    {
        x,y,z = bno.read_linear_acceleration()
        return (x,y,z)
    }

    #ACCELERATION FUNCTIONS
    def get_X_Acceleration(self)
    {
        return bno.read_accelerometer()[0]
    }

    def get_Y_Acceleration(self)
    {
        return bno.read_accelerometer()[1]
    }

    def get_Z_Acceleration(self)
    {
        return bno.read_accelerometer()[2]
    }

    def get_Acceleration(self)
    {
        x,y,z = bno.read_accelerometer()
        return (x,y,z)
    }

    #GRAVITY ACCELERATION FUNCTIONS
    def get_X_Gravity(self)
    {
        return bno.read_gravity()[0]
    }
    
    def get_Y_Gravity(self)
    {
        return bno.read_gravity()[1]
    }

    def get_Z_Gracity(self)
    {
        return bno.read_gravity()[2]
    }

    def get_Gravity(self)
    {
        x,y,z - bno.read_gravity()
        return (x,y,z)
    }

    #TEMPERATURE FUNCTION
    def get_temp(self)
    {
        return bno.read_temp()
    }

    #ANGULAR VELOCITY FUNCTIONS
    def get_X_AngularVelocity(self)
    {
        return bno.read_gyroscope()[0]
    }

    def get_Y_AngularVelocity(self)
    {
        return bno.read_gyroscope()[1]
    }

    def get_Z_AngularVelocity(self)
    {
        return bno.read_gyroscope()[2]
    }

    def get_AngularVelocity(self)
    {
        x,y,z = bno.read_gyroscope()
        return (x,y,z)
    }

    #MAGNETOMETER FUNCTIONS
    def get_X_MagField(self)
    {
        return bno.read_magnetometer()[0]
    }

    def get_Y_MagField(self)
    {
        return bno.read_magnetometer()[1]
    }

    def get_Z_MagField(self)
    {
        return bno.read_magnetometer()[2]
    }

    def get_MagField(self)
    {
        x,y,z = bno.read_magnetometer()
        return (x,y,z)
    }

    #TO DO
    #Add functions to get quaternion stuff
    #Add reset and set functions
    #Add calibration functions
    #
    #
    #
    #
}