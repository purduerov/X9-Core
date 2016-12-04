import platform
import numpy as np

if platform.system() == "Darwin":
    from timeS_OSX import absTime
else:
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
        self.increase = 0
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

        self.xVar = 1/np.arctan(pow(aXnoise,2))*np.array(
                [(pow(self.dT,4)/4,pow(self.dT,3)/2),
                    (pow(self.dT,3)/2,pow(self.dT,2))])
        self.yVar = 1/np.arctan(pow(aYnoise,2))*np.array(
                [(pow(self.dT,4)/4,pow(self.dT,3)/2),
                    (pow(self.dT,3)/2,pow(self.dT,2))])
        self.zVar = pow(aZnoise,2)*np.array(
                [(pow(self.dT,4)/4,pow(self.dT,3)/2),
                    (pow(self.dT,3)/2,pow(self.dT,2))])

       #self.xVar = pow(aXnoise,0.5)*np.array(
        #        [(pow(self.dT,4)/4,pow(self.dT,3)/2),
        #            (pow(self.dT,3)/2,pow(self.dT,2))])
        #self.yVar = pow(aYnoise,0.5)*np.array(
        #       [(pow(self.dT,4)/4,pow(self.dT,3)/2),
        #           (pow(self.dT,3)/2,pow(self.dT,2))])
        #self.zVar = pow(aZnoise,0.5)*np.array(
        #        [(pow(self.dT,4)/4,pow(self.dT,3)/2),
        #            (pow(self.dT,3)/2,pow(self.dT,2))]) '''

        self.xCov = self.xVar
        self.yCov = self.yVar
        self.zCov = self.zVar

        self.tVar = np.array([(pow(self.noiseT,2),0),(0,pow(self.bTnoise,2))])*self.dT
        self.rVar = np.array([(pow(self.noiseR,2),0),(0,pow(self.bRnoise,2))])*self.dT
        self.sVar = np.array([(pow(self.noiseS,2),0),(0,pow(self.bSnoise,2))])*self.dT

       #lA.dot(self.yVar.dot(lA.T))+pow(self.aYnoise,2)*np.array([(pow(self.dT,4)/4,pow(self.dT,3)/2),(pow(self.dT,3)/2,pow(self.dT,2))])"""
        
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


    def update(self):

        def calcState(A,prevState,B,u):
            return A.dot(prevState)+B*u

        def calcVar(A,prevVar,covM):
            return A.dot(prevVar.dot(A.T))+covM
        """ lA.dot(self.yVar.dot(lA.T))+pow(self.aYnoise,2)*np.array([(pow(self.dT,4)/4,pow(self.dT,3)/2),(pow(self.dT,3)/2,pow(self.dT,2))])"""
        def calcEst(meas,observation,state):
            return meas - observation.dot(state)

        def calcTrust(observation,errvar,measvar):
            return observation.dot(errvar*(observation.T))+pow(measvar,2)

        def calcK(variance,observation,trust):
            return variance.dot(observation.T)/trust

        def newState(state,kGain,est):
            return state + kGain*est

        def calcNVar( kGain,observation, var):
            return var.dot(np.identity(2)-kGain.dot(observation))
        C = np.array([(1),(0)])
        """to be replace by sensor calls once the stateClass is wrutten"""
        measX =self.increase+self.noiseX*pow(np.random.random(),5)
        measY =self.increase+self.noiseY*pow(np.random.random(),5)
        measZ = self.increase+self.noiseZ*np.random.random()
        measT = self.increase+self.noiseT*pow(np.random.random(),5)

        self.increase = self.increase+self.dT

        measX2 =0
        measY2 = 0
        measZ2 =0
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
        self.xCov = pow(self.aXnoise,2)*np.array([(pow(self.dT,4)/4,pow(self.dT,3)/2),(pow(self.dT,3)/2,pow(self.dT,2))]);
        self.xVar = calcVar(lA,self.xVar,self.xCov) 
        xEst = calcEst(measX,C,self.stateX)
        xTrust = calcTrust(C,self.noiseX,self.aXnoise)
        Kx = calcK(self.xVar,C,xTrust)
        self.stateX = newState(self.stateX,Kx,xEst)
        self.xVar=calcNVar(Kx,C,self.xVar)            

        """kalman for Y""" 
        self.stateY = calcState(lA,self.stateY,lB,measY2)
        self.yCov = pow(self.aYnoise,2)*np.array([(pow(self.dT,4)/4,pow(self.dT,3)/2),(pow(self.dT,3)/2,pow(self.dT,2))]);
        self.yVar = calcVar(lA,self.yVar,self.yCov)
        yEst = calcEst(measY,C,self.stateY)
        yTrust = calcTrust(C,self.noiseY,self.aYnoise)
        Ky = calcK(self.yVar,C,yTrust)
        self.stateY = newState(self.stateY,Ky,yEst)
        self.yVar = calcNVar(Ky,C,self.yVar)



        """kalman for Z""" 
        self.stateZ = calcState(lA,self.stateZ,lB,measZ2)
        self.zCov = pow(self.aZnoise,2)*np.array([(pow(self.dT,4)/4,pow(self.dT,3)/2),(pow(self.dT,3)/2,pow(self.dT,2))]);
        self.zVar = calcVar(lA,self.zVar,self.zCov)
        zEst = calcEst(measZ,C,self.stateZ)
        zTrust = calcTrust(C,self.noiseZ,self.aZnoise)
        Kz = calcK(self.zVar,C,zTrust)
        self.stateZ = newState(self.stateZ,Kz,zEst)
        self.zVar = calcNVar(Kz,C,self.zVar)

        """kalman for T""" 
        self.stateT = calcState(aA,self.stateT,aB,measT1)
        self.tCov = self.dT*np.array([(pow(self.noiseT,2),0),(0,pow(self.bTnoise,2))]);
        self.tVar = calcVar(aA,self.tVar,self.tCov)
        tEst = calcEst(measT,C,self.stateT)
        tTrust = calcTrust(C,self.noiseT,self.bTnoise)
        Kt = calcK(self.tVar,C,tTrust)
        self.stateT = newState(self.stateT,Kt,tEst)
        """self.stateY +Ky.dot(measY-C.dot(self.stateY))"""
        self.tVar = calcNVar(Kt,C,self.tVar)
