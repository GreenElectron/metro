
DT = 1./60.
GX = 0.
GY = -10. #9.81

class Hamilton():
    def __init__(self, free, int):
        self.free = free                # 
        self.int = int
        
    def propagate(self, particles):
        for prop in self.free:
            for part in particles:
                if prop.check(part):
                    prop.prop_free(part)
    

class Free():
    def __init__(self, tags, function):
        self.tags = tags
        self.function = function        # propagator
        
    def check(self, part):                #
        for t in part.tags:
            if (t in self.tags):
                return True
            return False
        
    def prop_free(self, particle):    # free propagation ()
        return self.function(particle)

class Particle():
    def __init__(self, tags):
        self.tags = tags
        
    

def g(particle):                # free fall
    particle.u += GX * DT
    particle.v += GY * DT
    particle.x += particle.u * DT
    particle.y += particle.v * DT
    return particle
    
freefall = Free(['freefall'], g)
    


        
    
        