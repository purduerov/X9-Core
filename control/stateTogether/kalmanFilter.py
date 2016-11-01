class kalman:
    stateX = [0 ,0]
    stateY = [0 ,0]
    stateZ = [0 ,0]
    stateT = [0 ,0]
    stateR = [0 ,0]
    stateS = [0 ,0]
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
