from timeS import absTime
import numpy as np
class kalman(object):
    """The init values need to be found """
    def __init__(self,
            xNoise,
            yNoise,
            zNoise,
            tNoise,
            rNoise,
            sNoise,
            aXnoise,
            aYnoise,
            aZnoise,
            aTnoise,
            aRnoise,
            aSnoise):
        """we will need to initilize these with sensor data or known values"""
        self.stateX = np.array([(0),(0)])
        self.stateY = np.array([(0),(0)])
        self.stateZ = np.array([(0),(0)])
        self.stateT = np.array([(0),(0)])
        self.stateR = np.array([(0),(0)])
        self.stateS = np.array([(0),(0)])

        self.noiseX = xNoise
        self.noiseY = yNoise
        self.noiseZ = zNoise
        self.noiseT = tNoise
        self.noiseR = rNoise
        self.noiseS = sNoise

        self.aXnoise = aXnoise
        self.aYnoise = aYnoise
        self.aZnoise = aZnoise
        self.aTnoise = aTnoise
        self.aRnoise = aRnoise
        self.aSnoise = aSnoise

        self.stateTime = absTime()
        self.dT = 0

        self.xVar = pow(aXnoise,2)*np.array(
                [(pow(self.dT,4)/4,pow(self.dT,3)/2),
                    (pow(self.dT,3)/2,pow(self.dT,2))])
        self.yVar = pow(aYnoise,2)*np.array(
                [(pow(self.dT,4)/4,pow(self.dT,3)/2),
                    (pow(self.dT,3)/2,pow(self.dT,2))])
        self.zVar = pow(aZnoise,2)*np.array(
                [(pow(self.dT,4)/4,pow(self.dT,3)/2),
                    (pow(self.dT,3)/2,pow(self.dT,2))])
        self.tVar = pow(aTnoise,2)*np.array(
                [(pow(self.dT,4)/4,pow(self.dT,3)/2),
                    (pow(self.dT,3)/2,pow(self.dT,2))])
        self.rVar = pow(aRnoise,2)*np.array(
                [(pow(self.dT,4)/4,pow(self.dT,3)/2),
                    (pow(self.dT,3)/2,pow(self.dT,2))])
        self.sVar = pow(aSnoise,2)*np.array(
                [(pow(self.dT,4)/4,pow(self.dT,3)/2),
                    (pow(self.dT,3)/2,pow(self.dT,2))])

        self.A = np.array ([(1,self.dT),(0,1)])
        self.B = np.array ([(pow(self.dT,2)/2),( self.dT)])
        
    def est_vel(self):
        return [self.stateX[1],
                self.stateY[1],
                self.stateZ[1],
                self.stateT[1],
                self.stateR[1],
                self.stateS[1]]    

    def est_pos(self):
        return [self.stateX[0],
                self.stateY[0],
                self.stateZ[0],
                self.stateT[0],
                self.stateR[0],
                self.stateS[0]]    

    """accellerations from motors are to be input. if we can call them from classed I think we don't need to do this"""
    def update(self,accelX,accelY,accelZ,accelT,accelR,accelS):
        C = np.array([(1),(0)])
        """to be replace by sensor calls later"""
        measX = np.array([(1),(1)])
        measY = np.array([(1),(1)])
        measZ = np.array([(1),(1)])
        measT = np.array([(1),(1)])
        measR = np.array([(1),(1)])
        measS = np.array([(1),(1)])

        """timestep vars"""
        self.dT = absTime()-self.stateTime
        self.stateTime = absTime()
        self.A = np.array ([(1,self.dT),(0,1)])
        self.B = np.array ([(pow(self.dT,2)/2),( self.dT)])

        """kalman for X""" 
        self.stateX = self.A.dot(self.stateX)+self.B*accelX
        self.xVar = self.A.dot(self.xVar.dot(self.A.T))+pow(self.aXnoise,2)*np.array([(pow(self.dT,4)/4,pow(self.dT,3)/2),(pow(self.dT,3)/2,pow(self.dT,2))])
        Kx = self.xVar.dot(C.T)/(C.dot(self.xVar.dot(C.T))+pow(self.noiseX,2))
        self.stateX =self.stateX +Kx.dot(measX-C.dot(self.stateX))
        self.xVar=self.xVar.dot(np.identity(2)-Kx.dot(C))
            

        """kalman for Y""" 
        self.stateY = self.A.dot(self.stateY)+self.B*accelY
        self.yVar = self.A.dot(self.yVar.dot(self.A.T))+pow(self.aYnoise,2)*np.array([(pow(self.dT,4)/4,pow(self.dT,3)/2),(pow(self.dT,3)/2,pow(self.dT,2))])
        Ky = self.yVar.dot(C.T)/(C.dot(self.yVar.dot(C.T))+pow(self.noiseY,2))
        self.stateY =self.stateY +Ky.dot(measY-C.dot(self.stateY))
        self.yVar=self.yVar.dot(np.identity(2)-Ky.dot(C))
        
        
        """kalman for Z""" 
        self.stateZ = self.A.dot(self.stateZ)+self.B*accelZ
        self.zVar = self.A.dot(self.zVar.dot(self.A.T))+pow(self.aZnoise,2)*np.array([(pow(self.dT,4)/4,pow(self.dT,3)/2),(pow(self.dT,3)/2,pow(self.dT,2))])
        Kz = self.zVar.dot(C.T)/(C.dot(self.zVar.dot(C.T))+pow(self.noiseZ,2))
        self.stateZ =self.stateZ +Kz.dot(measZ-C.dot(self.stateZ))
        self.zVar=self.zVar.dot(np.identity(2)-Kz.dot(C))
        

        """kalman for t""" 
        self.stateT = self.A.dot(self.stateT)+self.B*accelT
        self.tVar = self.A.dot(self.tVar.dot(self.A.T))+pow(self.aTnoise,2)*np.array([(pow(self.dT,4)/4,pow(self.dT,3)/2),(pow(self.dT,3)/2,pow(self.dT,2))])
        Kt = self.tVar.dot(C.T)/(C.dot(self.tVar.dot(C.T))+pow(self.noiseT,2))
        self.stateT =self.stateT +Kt.dot(measT-C.dot(self.stateT))
        self.tVar=self.tVar.dot(np.identity(2)-Kt.dot(C))

        """kalman for r""" 
        self.stateR = self.A.dot(self.stateR)+self.B*accelR
        self.rVar = self.A.dot(self.rVar.dot(self.A.T))+pow(self.aRnoise,2)*np.array([(pow(self.dT,4)/4,pow(self.dT,3)/2),(pow(self.dT,3)/2,pow(self.dT,2))])
        Kr = self.rVar.dot(C.T)/(C.dot(self.rVar.dot(C.T))+pow(self.noiseR,2))
        self.stateR =self.stateR +Kr.dot(measR-C.dot(self.stateR))
        self.rVar=self.rVar.dot(np.identity(2)-Kr.dot(C))

        """kalman for s""" 
        self.stateS = self.A.dot(self.stateS)+self.B*accelS
        self.sVar = self.A.dot(self.sVar.dot(self.A.T))+pow(self.aSnoise,2)*np.array([(pow(self.dT,4)/4,pow(self.dT,3)/2),(pow(self.dT,3)/2,pow(self.dT,2))])
        Ks = self.sVar.dot(C.T)/(C.dot(self.sVar.dot(C.T))+pow(self.noiseS,2))
        self.stateS =self.stateS +Ks.dot(measS-C.dot(self.stateS))
        self.sVar=self.sVar.dot(np.identity(2)-Ks.dot(C))
