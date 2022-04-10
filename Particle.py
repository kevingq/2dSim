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
        self.pVec[0]=self.pVec[0] + self.vVec[0]*tStep
        self.pVec[1]=self.pVec[1] + self.vVec[1]*tStep
