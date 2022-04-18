import numpy as np
import math
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

    def dotProd(self,v1,v2):
        return v1[0]*v2[0]+v1[1]*v2[1]

    def normal(self,v):
        dir_y=(v[1][1]-v[1][0])
        dir_x=(v[0][1]-v[0][0])
        perp_dir=np.array([-dir_y,dir_x]) # direction vector of normal
        perp_dir=(1/np.linalg.norm(perp_dir))*perp_dir # set magnitude to 1
        return perp_dir

    def standardForm(self,line):
        x1=line[0][0]
        x2=line[0][1]
        y1=line[1][0]
        y2=line[1][1]
        a=-(y2-y1)
        b=(x2-x1)
        c=-(b*y1+a*x1)
        return np.array([a,b,c])

    def willCollide(self,pVec_pred,boundary):
        bx1=boundary[0][0]
        bx2=boundary[0][1]
        by1=boundary[1][0]
        by2=boundary[1][1]

        tan_bound="Normal vector to collision: Not yet implemented"
        px1=self.pVec[0]
        py1=self.pVec[1]
        px2=pVec_pred[0]
        py2=pVec_pred[1]
        pChange=np.array([[px1,px2],[py1,py2]])
        l1=self.standardForm(boundary)
        l2=self.standardForm(pChange)
        A=np.array([[l1[0],l1[1]],[l2[0],l2[1]]])
        b=np.array([[-l1[2]],[-l2[2]]])
        x=np.empty([0,0])
        #try:
        if True:
            x=np.linalg.solve(A,b)
            distP1_to_I=np.linalg.norm(np.array([[x[0]-bx1],[x[1]-by1]]))
            distP2_to_I=np.linalg.norm(np.array([[x[0]-bx2],[x[1]-by2]]))
            distP1_to_P2=np.linalg.norm(np.array([[bx1-bx2],[by1-by2]]))
            minDistIntersectToBoundary=np.linalg.norm((distP1_to_P2 - (distP1_to_I+distP2_to_I)))
            minDistParticleToBoundary=abs(l1[0]*px2+l1[1]*py2+l1[2])/math.sqrt(math.pow(l1[0],2)+math.pow(l1[1],2))
            print("minDistParticleToBoundary:",minDistParticleToBoundary, "minDistIntersectToBoundary:",minDistIntersectToBoundary)

            if minDistIntersectToBoundary < 0.01 and minDistParticleToBoundary<0.1:
                print("Collision!!")
                return [True,x]
            else:
                return [False,x]
        except :
            return [False,x]
            if minDistToBoundary < 0.08:
                return [True,tan_bound]
            else:
                return [False,tan_bound]
        except :
            return [False,tan_bound]

    def takeStep(self,tStep,boundaries):
        # Fixme: Test if vector [pVec_pred - pVec] crosses any boundaries
        vVec_pred=np.add(self.vVec,self.aVec*tStep)
        pVec_pred=np.add(self.pVec,self.vVec*tStep)
        for b_obj in boundaries:
            b=b_obj.getBoundary()
            collision=self.willCollide(pVec_pred,b)
            collisionFound=collision[0]
            if collisionFound:
                xI=collision[1][0]
                yI=collision[1][1]
                n=self.normal(b)
                if(self.dotProd(n,vVec_pred) > 0):
                    n=self.normal(-b)
                self.vVec=n*np.linalg.norm(vVec_pred)
                print(collision[1])
                self.vVec=-vVec_pred
                self.pVec=np.add(self.pVec,self.vVec*tStep)
                return True
        self.vVec=vVec_pred
        self.pVec=pVec_pred
