from timeS import absTime
import numpy as np
class kalman(object):
    """The init noise values need to be found """
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
            bTnoise,
            bRnoise,
            bSnoise):

        """X X'"""
        self.stateX = np.array([(0),(0)])
        self.stateY = np.array([(0),(0)])
        self.stateZ = np.array([(0),(0)])

        """T Tb"""
        self.stateT = np.array([(0),(0)])
        self.stateR = np.array([(0),(0)])
        self.stateS = np.array([(0),(0)])

        """scalar noise values"""
        self.noiseX = xNoise
        self.noiseY = yNoise
        self.noiseZ = zNoise
        self.noiseT = tNoise
        self.noiseR = rNoise
        self.noiseS = sNoise

        self.aXnoise = aXnoise
        self.aYnoise = aYnoise
        self.aZnoise = aZnoise
        self.bTnoise = bTnoise
        self.bRnoise = bRnoise
        self.bSnoise = bSnoise

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

        self.tVar = np.array([(pow(self.noiseT,2),0),(0,pow(self.bTnoise,2))])*self.dT
        self.rVar = np.array([(pow(self.noiseR,2),0),(0,pow(self.bRnoise,2))])*self.dT
        self.sVar = np.array([(pow(self.noiseS,2),0),(0,pow(self.bSnoise,2))])*self.dT

        
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
    def update(self):

        def calcState(A,prevState,B,u):
            return A.dot(prevState)+B*u

        def calcVar(A,prevVar,noise1,noise2):
            return A.dot(prevVar.dot(A.T))+np.array([(pow(noise1,2),noise1*noise2),(noise2*noise1,pow(noise2,2))])*self.dT

        def calcEst(meas,observation,state):
            return meas - observation.dot(state)

        def calcTrust(observation,errvar,measvar):
            return observation.dot(errvar*(observation.T))+measvar

        def calcK(variance,observation,trust):
            return variance.dot(observation.T)/trust

        def newState(state,kGain,est):
            return state + kGain*est

        def calcNVar( kGain,observation, var):
            return var.dot(np.identity(2)-kGain.dot(observation))
        C = np.array([(1),(0)])
        """to be replace by sensor calls once the stateClass is wrutten"""
        measX =1
        measX2 =1
        measY =1
        measY2 = 1
        measZ = 1
        measZ2 =1
        measT = 1
        measT1 = 1
        measR = 1
        measR1 = 1
        measS =1
        measS1 =1 

        """timestep vars"""
        self.dT = absTime()-self.stateTime
        self.stateTime = absTime()

        lA = np.array ([(1,self.dT),(0,1)])
        lB = np.array ([(pow(self.dT,2)/2),( self.dT)])
        aA = np.array ([(1,-self.dT),(0,1)])
        aB = np.array ([(self.dT),(0)])
        """kalman for X""" 
        self.stateX = calcState(lA,self.stateX,lB,measX2) 
        self.xVar = calcVar(lA,self.xVar,self.noiseX,self.aXnoise) 
        xEst = calcEst(measX,C,self.stateX)
        xTrust = calcTrust(C,self.noiseX,self.aXnoise)
        Kx = calcK(self.xVar,C,xTrust)
        self.stateX = newState(self.stateX,Kx,xEst)
        self.xVar=calcNVar(Kx,C,self.xVar)            

        """kalman for Y""" 
        """
        self.stateY = self.A.dot(self.stateY)+self.B*accelY

        self.yVar = self.A.dot(self.yVar.dot(self.A.T))+pow(self.aYnoise,2)*np.array([(pow(self.dT,4)/4,pow(self.dT,3)/2),(pow(self.dT,3)/2,pow(self.dT,2))])
        Ky = self.yVar.dot(C.T)/(C.dot(self.yVar.dot(C.T))+pow(self.noiseY,2))
        self.stateY =self.stateY +Ky.dot(measY-C.dot(self.stateY))
        self.yVar=self.yVar.dot(np.identity(2)-Ky.dot(C))
       """ 
