from Particle import Particle
import matplotlib.pyplot as plt
import numpy as np

# Class definition for object: Simulation
# Description: Defined as empty 2D space with set dimensions
class Simulation:
    def __init__(self,runNum):
        self.runNum=runNum
        self.tStart=0.0 #sFIXME: move info to param file that gets called based on runNum
        self.tStop=5.0
        self.tStep=0.1
        self.tCurr=self.tStart
        self.pVec_init=np.array([1.0,1.0])
        self.vVec_init=np.array([1.0,1.0])
        self.aVec_init=np.array([1.0,1.0])
        self.xMin=-1.0 # world size boundaries
        self.xMax=1.0
        self.yMin=-1.0
        self.yMax=1.0
        self.boundaries=np.empty([0]) # fixme: Figure out how to declare it as empty
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
    def setBoundaries(self,boundaries):
        self.boundaries=boundaries

    def start(self):
        # Run the simulation based on set parameters
        print("Starting simulation",self.runNum)
        plt.ion()
        fig, ax = plt.subplots()

        # Create a particle with position, velocity, and acceleration
        p=Particle(0,self.pVec_init,self.vVec_init,self.aVec_init)

        # Increment time on each loop until stop time reached
        while self.tCurr < self.tStop:
            pVec=p.getPos()
            fig.clear()
            plt.scatter(pVec[0],pVec[1])

            acc=np.linalg.norm(p.getAcc())
            vel=np.linalg.norm(p.getVel())
            pos=np.linalg.norm(p.getPos())
            textStr = '$time:%.2f\:s$\n$acc:%.2f\:m/s^2$\n$vel:%.2f\:m/s$\n$pos:%.2f\:m$' %(self.tCurr,acc,vel,pos)
            plt.text(self.xMin+abs(self.xMin)*0.10, self.yMax-abs(self.yMax)*0.55, textStr)
            for b_obj in self.boundaries:
                b=b_obj.getBoundary()
                plt.plot(b[0],b[1],'k-',lw=2)
            plt.xlim(self.xMin,self.xMax)
            plt.ylim(self.yMin, self.yMax)
            plt.grid()
            plt.pause(0.01)
            # Update kinematics of particle
            p.takeStep(self.tStep,self.boundaries)
            self.tCurr=self.tCurr+self.tStep

        print("Simulation finished after",self.tCurr-self.tStart,"seconds")
