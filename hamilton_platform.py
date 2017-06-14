import numpy as np
from hamilton_model import *

DT = 1./60.
GX = np.array([0.,-10.])

# getter functions
def x(vect): return vect[0]
def y(vect): return vect[1]
def z(vect): return vect[2]
def w(vect): return vect[3]

# manipulator functions
def vlen(vector): return (np.sqrt(np.dot(np.array(vector),np.array(vector))))
def vscm(scalar, vector): return (scalar*np.array(vector))
def vadd(vect1,  vect2):  return (np.array(vect1)+np.array(vect2))
def vsub(vect1,  vect2):  return (np.array(vect1)-np.array(vect2))
def vdot(vect1,  vect2):  return (np.dot(np.array(vect1),np.array(vect2)))

# axis alligned vector and rectangle cast floor (unit vector pointing down)
def vrcfl(vect, pos1, rect, pos2):
    return ((x(pos2) <= x(pos1) <= (x(pos2) + x(rect))) and
            (y(pos1) <= y(pos2)) and (y(pos1) - (y(pos2) + y(rect))))
# axis alligned vector and rectangle cast ceiling (unit vector pointing up)
def vrccl(vect, pos1, rect, pos2):
    return ((x(pos2) <= x(pos1) <= (x(pos2) + x(rect))) and
            (y(pos1) <= (y(pos2) + y(rect))) and (y(pos2) - y(pos1))) 
# axis alligned vector and rectangle cast left wall (unit vector pointing right)
def vrclw(vect, pos1, rect, pos2):
    return ((y(pos2) <= y(pos1) <= (y(pos2) + y(rect))) and
            (x(pos1) <= x(pos2)) and (x(pos1) - (x(pos2) + x(rect))))
# axis alligned vector and rectangle cast right wall (unit vector pointing left)
def vrccl(vect, pos1, rect, pos2):
    return ((y(pos2) <= y(pos1) <= (y(pos2) + y(rect))) and
            (x(pos1) <= (x(pos2) + x(rect))) and (x(pos2) - x(pos1)))
    
# axis alligned rectangle rectangle collision
def rrcol(rect1, pos1, rect2, pos2): #returns true if rect1,2 overlap
    return (((x(pos2) - x(rect1)) <= x(pos1) <= (x(pos2) + x(rect2))) and
            ((y(pos2) - y(rect1)) <= y(pos1) <= (y(pos2) + y(rect2))))
    



def enforcefloor(particle, casting_constant, normal_vector = [0, -1]):
    if casting_constant >= 0:
        particle.x = vsub(particle.x,vscm(casting_constant,normal_vector))
        particle.dx = vsub(particle.dx,[0,y(particle.dx)])
        if not 'grounded' in particle.__dict__:
            particle.grounded = None
        if type(particle.grounded) in [float, int]:
            particle.grounded += DT
        else:
            particle.grounded = 0
    return particle

def testfloor1(particle, floor = -50):
    return enforcefloor(particle, floor - y(particle.x))

def testfloor2(particle, floor = -40):
    return testfloor1(particle,floor)

def freemotion1(particle):
    particle.x = vadd(particle.x,vscm(DT,particle.dx))
    return particle  

def freefall1(particle): # move a particle (also accelerate it under g)
    particle.dx = vadd(particle.dx,vscm(DT,GX))
    return freemotion1(particle)

def drawlist(particle):
    particle.pl = [particle.x, particle.pb]
    return particle.pl

freemotion = Free(   ['freemotion'], freemotion1)
freefall   = Free(   ['freefall'],   freefall1)
testfloor  = Free(   ['testfloor'],  testfloor1)
otherfloor = Free(   ['otherfloor'], testfloor2)
drawlist   = Collect(['drawable'],   drawlist)