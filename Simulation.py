from Particle import Particle
import matplotlib.pyplot as plt
import numpy as np

class Simulation:
    def __init__(self,runNum):
        self.runNum=runNum
        self.tStart=0.0 #sFIXME: move info to param file that gets called based on runNum
        self.tStop=5.0
        self.tStep=0.1
        self.tCurr=self.tStart
        self.pVec_init=[0.1,0.2]
        self.vVec_init=[0.3,0.4]
        self.aVec_init=[0.5,0.6]
        self.xMin=-1.0 # x1->x2,y1->y2
        self.xMax=1.0
        self.yMin=-1.0
        self.yMax=1.0

    def setRunNumber(self,runNum):
        self.runNum=runNum

    def setStartTime(self,tStart):
        if tStart >= self.tStop:
            print("Start time cannot be after stop time. Using default start time instead...")
        else:
            self.tStart = tStart
            self.tCurr = tStart

    def setStopTime(self,tStop):
        if tStop <= self.tStart:
            print("Stop time cannot be before start time. Using default stop time instead...")
        else:
            self.tStop = tStop

    def setStepTime(self,tStep):
        self.tStep = tStep

    def setWorldSize(self,worldSize):
        if worldSize[0][0] >= worldSize[0][1] or worldSize[1][0] >= worldSize[1][1]:
            print("World size impossible. Using default world size instead...")
        else:
            self.xMin=worldSize[0][0]
            self.xMax=worldSize[0][1]
            self.yMin=worldSize[1][0]
            self.yMax=worldSize[1][1]

    def setInitialPosition(self,pVec_init):
        xPos=pVec_init[0]
        yPos=pVec_init[1]
        if xPos<=self.xMin or xPos>=self.xMax or yPos<=self.yMin or yPos>=self.yMax:
            print("Initial position cannot be outside world. Using default initial position instead...")
        else:
            self.pVec_init = pVec_init

    def setInitialVelocity(self,vVec_init):
        self.vVec_init = vVec_init

    def setInitialAcceleration(self,aVec_init):
        self.aVec_init = aVec_init

    def start(self):
        print("Starting simulation",self.runNum)
        plt.ion()
        fig=plt.figure()
        p=Particle(0,self.pVec_init,self.vVec_init,self.aVec_init)
        while self.tCurr < self.tStop:
            pVec=p.getPos()
            fig.clear()
            plt.scatter(pVec[0],pVec[1])
            plt.xlim(self.xMin,self.xMax)
            plt.ylim(self.yMin, self.yMax)
            plt.grid()
            plt.pause(0.1)
            p.takeStep(self.tStep)
            self.tCurr=self.tCurr+self.tStep
        print("Simulation finished after",self.tCurr-self.tStart,"seconds")
