import numpy as np
import matplotlib.pyplot as plt
from functions import standardForm
import math
#b1=np.empty([0])
b1=np.array([[0.0,5.0],[3.0,3.0]])
pVec=np.array([[0.0,5.0],[1.0,1.0]])
px1=pVec[0][0]
px2=pVec[0][1]
py1=pVec[1][0]
py2=pVec[1][1]
l1=standardForm(b1)
l2=standardForm(pVec)
A=np.array([[l1[0],l1[1]],[l2[0],l2[1]]])
b=np.array([[-l1[2]],[-l2[2]]])
try:
    x=np.linalg.solve(A,b)
    print("I=",x[0],",",x[1],")")
    print("I-p1=",np.array([x[0]-px1,x[1]-py1]))
    print("I-p2=",np.array([[x[0]-px2],[x[1]-py2]]))
    print("p1-p2=",np.array([[px1-px2],[py1-py2]]))
    distP1_to_I=np.linalg.norm(np.array([[x[0]-px1],[x[1]-py1]]))
    distP2_to_I=np.linalg.norm(np.array([[x[0]-px2],[x[1]-py2]]))
    distP1_to_P2=np.linalg.norm(np.array([[px1-px2],[py1-py2]]))
    print("|p1-I|= ",distP1_to_I)
    print("|p2-I|= ",distP2_to_I)
    print("|p1-p2|= ",distP1_to_P2)
    print("|p1-I|+|p2-I|=",distP1_to_I+distP2_to_I)

    minDistToBoundary=distP1_to_P2 - (distP1_to_I+distP2_to_I)
    print(minDistToBoundary)
    if np.linalg.norm((distP1_to_P2 - (distP1_to_I+distP2_to_I))) < 0.01:
        print("Particle will collide!")
    else:
        print("No collision predicted.")
except :
    print("Lines are parallel. Particle will not collide.")


lines=np.array([b1,pVec])
fig=plt.figure()
for i in lines:
    plt.plot(i[0],i[1],'k-',lw=2)
plt.xlim(-1.5, 6.0)
plt.ylim(-0.5,6.0)
plt.grid()
plt.show()
