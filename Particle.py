import numpy as np

# Class definition for object: Particle
# Description: Have a defined position, velocity, acceleration, a method 
# for updating them with changes in time, and an ability to detect if
# will encounter any physical objects

class Particle:
    def __init__(self,pNum,pVec,vVec,aVec):
        self.pNum = pNum
        self.pVec = pVec
        self.vVec = vVec
        self.aVec = aVec

    def getPos(self):
        return self.pVec

    def getVel(self):
        return self.vVec

    def getAcc(self):
        return self.aVec

    def takeStep(self,tStep,boundaries):
        # Fixme: Test if vector [pVec_new - pVec] crosses any boundaries
        boundaries[1].getBoundary()
        vVec_new=np.add(self.vVec,self.aVec*tStep)
        pVec_new=np.add(self.pVec,self.vVec*tStep)
        self.vVec=vVec_new
        self.pVec=pVec_new
