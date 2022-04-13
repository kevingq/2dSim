import numpy as np

# Class definition for object: Boundary
# Description: An object that can interact with Particle objects
class Boundary:
    def __init__(self,name,type,line):
        self.name=name
        self.type=type
        self.line=line

    def getBoundary(self):
        return self.line

    def getIntersection(self,line): # get intersection between this object and a given line
        return False
