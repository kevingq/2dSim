from Simulation import Simulation

init_pos = [0.3,0.4]
init_vel = [0.3,0.3]
worldSizeX = [-1.0,1.0]
worldSizeY = [-1.0,1.0]

sim = Simulation(0)
sim.setWorldSize([worldSizeX,worldSizeY])
sim.start()
