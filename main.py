from Simulation import Simulation
import numpy as np
sim = Simulation(0)
sim.setInitialPosition(np.array([-0.4,-0.4]))
sim.setInitialVelocity(np.array([2.0,4.0]))
sim.setInitialAcceleration(np.array([0.0,-9.81]))
sim.setStepTime(0.01)
sim.setWorldSize([[-0.5, 1.5],[-0.5,1.5]])

b1=np.array([[0.0,1.0],[0.0,0.0]])
b2=np.array([[1.0,1.0],[0.0,1.0]])
b3=np.array([[0.0,1.0],[1.0,1.0]])
b4=np.array([[0.0,0.0],[0.0,1.0]])
boundary = np.array([b1, b2, b3, b4])
sim.setBoundary(boundary)
sim.start()
