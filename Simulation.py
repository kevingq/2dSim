from Particle import Particle
import matplotlib.pyplot as plt
import numpy as np
class Simulation:
    def __init__(self,runNum):
        self.runNum=runNum
        self.tStart=0.0 #sFIXME: move info to param file that gets called based on runNum
        self.tStop=2.0
        self.tStep=0.1
        self.pVec_init=[0.1,0.2]
        self.vVec_init=[0.3,0.4]
        self.aVec_init=[0.5,0.6]


    def start(self):
        print("Starting simulation")
        fig=plt.figure()
        p=Particle(0,self.pVec_init,self.vVec_init,self.aVec_init)
        for step in range(10):
            p.takeStep(self.tStep)
            pVec=p.getPos()
            fig.clear()
            plt.scatter(pVec[0],pVec[1])
            plt.show()
            print(p.getPos())
