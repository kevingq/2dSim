from Simulation import Simulation
from Boundary import Boundary
import numpy as np
sim = Simulation(0)
# Set simulation parameters (overwrite default)
sim.setInitialPosition(np.array([0.0,0.0]))

sim.setInitialVelocity(np.array([2.0,2.0]))
sim.setInitialAcceleration(np.array([0.0,-9.81]))
sim.setStepTime(0.03)
sim.setWorldSize([[-2.0, 4.0],[-2.0,2.0]])

sim.setInitialVelocity(np.array([2.5,3.5]))
sim.setInitialAcceleration(np.array([0.0,-9.81]))
sim.setStepTime(0.01)
sim.setWorldSize([[-2.0, 2.0],[-2.0,2.0]])
sim.setStartTime(0.0)
sim.setStopTime(7.0)

# Define any walls in the world

b1=Boundary('b1','line',np.array([[1.0,3.0],[-1.0,0.0]]))
b2=Boundary('b2','line',np.array([[0.0,1.0],[-0.5,0.5]]))
b3=Boundary('b3','line',np.array([[-7.0,7.0],[-1.5,-1.5]]))
b4=Boundary('b4','stop',np.array([[-1.5,-0.5],[0.0,0.0]]))
b5=Boundary('b4','stop',np.array([[-1.5,-1.5],[0.0,0.2]]))
b6=Boundary('b4','stop',np.array([[-0.5,-0.5],[0.0,0.2]]))
b4.setColor('r-')
b5.setColor('r-')
b6.setColor('r-')

b2=Boundary('b1','line',np.array([[-1.0,1.0],[-1.0,-1.0]]))
b1=Boundary('b2','line',np.array([[1.0,1.0],[-1.0,1.0]]))
b3=Boundary('b3','line',np.array([[1.0,-1.0],[1.0,1.0]]))
b4=Boundary('b4','line',np.array([[-1.0,-1.0],[1.0,-1.0]]))
# Create array of boundaries and add them to the simulation
boundaries = np.array([b1,b2,b3,b4,b5,b6])
sim.setBoundaries(boundaries)

# Start the simulation
sim.start()
