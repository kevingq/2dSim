import numpy as np

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

    def takeStep(self,tStep):
        self.vVec=np.add(self.vVec,self.aVec*tStep)
        self.pVec=np.add(self.pVec,self.vVec*tStep)
