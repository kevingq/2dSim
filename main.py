from Simulation import Simulation
from Boundary import Boundary
import numpy as np
sim = Simulation(0)
# Set simulation parameters (overwrite default)
sim.setInitialPosition(np.array([-0.4,-0.4]))
sim.setInitialVelocity(np.array([2.0,4.0]))
sim.setInitialAcceleration(np.array([0.0,-9.81]))
sim.setStepTime(0.05)
sim.setWorldSize([[-0.5, 1.5],[-0.5,1.5]])
sim.setStartTime(0.0)
sim.setStopTime(0.5)

# Define any walls in the world
b1=Boundary('b1','line',np.array([[0.0,1.0],[0.0,0.0]]))
b2=Boundary('b1','line',np.array([[1.0,1.0],[0.0,1.0]]))

# Create array of boundaries and add them to the simulation
boundaries = np.array([b1,b2])
sim.setBoundaries(boundaries)

# Start the simulation
sim.start()
