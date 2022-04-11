import numpy as np
import matplotlib.pyplot as plt
boundary=np.empty([0])
b1=np.array([[0.0,1.0],[0.0,0.0]])
b2=np.array([[1.0,1.0],[0.0,1.0]])
b3=np.array([[0.0,1.0],[1.0,1.0]])
b4=np.array([[0.0,0.0],[0.0,1.0]])
boundary = np.array([b1, b2, b3, b4])
fig=plt.figure()
plt.scatter(0.5,0.5)
for i in boundary:
    plt.plot(i[0],i[1],'k-',lw=2)
plt.xlim(-0.5, 1.5)
plt.show()
