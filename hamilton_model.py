class Particle():
    def __init__(self, tags):
        self.tags = tags

class Free(): # as in the free (analytically solveable) Hamiltonian 
    def __init__(self, tags, function):
        self.tags = tags
        self.function = function        # propagator
        
    def check(self, part): # return True if a particle is tagged to this prop.
        for t in part.tags:
            if (t in self.tags):
                return True
        return False
        
    def prop_free(self, particle): # run a propogator on a particle
        return self.function(particle)

        
class Interaction():
    def __init__(self, tags_left, tags_right, condition, interactor):
        self.tag_left   = tag_left
        self.tag_right  = tag_right
        self.condition  = condition
        self.interactor = interactor
    
    def check_left(self, part_left):
        for t in part_left.tags:
            if (t in self.tags_left):
                return True
        return False

    def check_right(self, part_right):
        for t in part_right.tags:
            if (t in self.tags_right):
                return True
        return False
    
    def check(self, part_left, part_right):
        if self.check_left(part_left) and self.check_right(part_right):
            return self.condition(part_left, part_right)
        return False

    def interact(self, part_left, part_right):
        return self.interactor(part_left, part_right)

class Collect():
    def __init__(self, tags, collector):
        self.tags = tags
        self.collector = collector
    
    def check(self, part): # return True if a particle is tagged to this prop. 
        for t in part.tags:
            if (t in self.tags):
                return True
        return False
    
    def prop_collect(self, particle):
        return self.collector(particle)

def printandreturn(stuff):
    print stuff
    return stuff

class Hamilton():
    def __init__(self, free, int, coll):
        self.free = free
        self.int  = int
        self.coll = coll
    
    def get_free(self): 
        return self.free
    
    def get_coll(self, n):
        return self.coll[n]
    
    # Takes a list of particles, parts, and one (free) propogator prop, applies
    # prop to the relevant parts returns updated list of parts.
    def run1_free(self, parts, prop):
        return (parts and
                (prop.check(parts[0]) and [prop.prop_free(parts[0])] or parts[0:1])
                 + self.run1_free(parts[1:], prop))
    
    # Takes a list of particles, parts, and a list of (free) propogators, props,
    # by default the free propogators already assigned to this Hamiltonian and
    # runs each propogator on parts then returns the updated list of parts.
    def run_free(self, parts, props = None):
        if props == None:
            props = self.free
        return (props and self.run_free(self.run1_free(parts, props[0]),props[1:])
                or parts)
    
    # Takes a list of particles, parts, and a single (collect) propogator, col0,
    # by default the first collect propogator alreadz assigned to this Hamilton-
    # ian and returns a list of the outputs of col0.
    def run1_coll(self, parts, col0 = None):
        if col0 == None:
            col0 = self.get_coll(0)
        return (parts and
                (col0.check(parts[0]) and [col0.prop_collect(parts[0])])
                 + self.run1_coll(parts[1:], col0))

def id(particle):
    return particle

def trivial(left, right):
    return True