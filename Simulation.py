from Particle import Particle
import matplotlib.pyplot as plt
import numpy as np
import time
class Simulation:
    def __init__(self,runNum):
        self.runNum=runNum
        self.tStart=0.0 #sFIXME: move info to param file that gets called based on runNum
        self.tStop=1.0
        self.tStep=0.1
        self.pVec_init=[0.1,0.2]
        self.vVec_init=[0.3,0.4]
        self.aVec_init=[0.5,0.6]
        self.worldSize=[[-1.0,1.0], [-1.0,1.0]] # x1->x2,y1->y2

    def setWorldSize(self,worldSize):
        self.worldSize=worldSize

    def start(self):
        x = np.linspace(0, 10*np.pi, 100)
        y = np.sin(x)
        plt.ion()
        fig=plt.figure()
        p=Particle(0,self.pVec_init,self.vVec_init,self.aVec_init)
        for phase in np.linspace(0, 10*np.pi, 100):
            pVec=p.getPos()
            fig.clear()
            plt.scatter(pVec[0],pVec[1])
            plt.xlim(self.worldSize[0][0], self.worldSize[0][1])
            plt.ylim(self.worldSize[1][0], self.worldSize[1][1])
            plt.grid()
            plt.pause(0.1)
            p.takeStep(self.tStep)
