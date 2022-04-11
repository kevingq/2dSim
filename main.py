from Simulation import Simulation
import numpy as np
sim = Simulation(0)
sim.setInitialPosition(np.array([-0.4,-0.4]))
sim.setInitialVelocity(np.array([2.0,4.0]))
sim.setInitialAcceleration(np.array([0.0,-9.81]))
sim.setStepTime(0.01)
sim.addBoundary(np.array([0.5,0.5]))
sim.start()
