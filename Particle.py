import numpy as np
from functions import standardForm

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

    def standardForm(line):
        x1=line[0][0]
        x2=line[0][1]
        y1=line[1][0]
        y2=line[1][1]
        a=-(y2-y1)
        b=(x2-x1)
        c=-(b*y1+a*x1)
        return np.array([a,b,c])

    def willCollide(self,pVec_pred,boundary):
        px1=self.pVec[0]
        py1=self.pVec[1]
        px2=pVec_pred[0]
        py2=pVec_pred[1]
        pChange=np.array([[px1,px2],[py1,py2]])
        l1=standardForm(boundary)
        l2=standardForm(pChange)
        print(l1[0],",",l1[1])
        print(l2[0],",",l2[1])
        A=np.array([[l1[0],l1[1]],[l2[0],l2[1]]])
        b=np.array([[-l1[2]],[-l2[2]]])
        try:
            x=np.linalg.solve(A,b)
            distP1_to_I=np.linalg.norm(np.array([[x[0]-px1],[x[1]-py1]]))
            distP2_to_I=np.linalg.norm(np.array([[x[0]-px2],[x[1]-py2]]))
            distP1_to_P2=np.linalg.norm(np.array([[px1-px2],[py1-py2]]))
            minDistToBoundary=np.linalg.norm((distP1_to_P2 - (distP1_to_I+distP2_to_I)))
            if minDistToBoundary < 0.01:
                return True
            else:
                return False
        except :
            return False



    def takeStep(self,tStep,boundaries):
        # Fixme: Test if vector [pVec_pred - pVec] crosses any boundaries
        vVec_pred=np.add(self.vVec,self.aVec*tStep)
        pVec_pred=np.add(self.pVec,self.vVec*tStep)
        if self.willCollide(pVec_pred,boundaries[0].getBoundary()):
            self.vVec=-vVec_pred
            self.pVec=np.add(self.pVec,self.vVec*tStep)
        else:
            self.vVec=vVec_pred
            self.pVec=pVec_pred
