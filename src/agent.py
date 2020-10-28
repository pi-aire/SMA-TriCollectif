import random
import math
from environnement import *

class Agent(object):
    """
    Sorting agent class
    """

    def __init(self, env:Environnement, id, position, kp, km, i, memorySize):
        """
        Position position is a table position[0] = x et [1] = y
        Loaded is a char : 0 empty, A if object A et B if object B
        kp : k+ 
        km : k-
        i : The number of movement boxes
        f : The proportion of objects of the same type A or B in the immediate environment
        littleGrid : queue of already crossed objects 
        """
        self.env = env
        self.id = id
        self.position = position # temporaire
        self.loaded = ""
        self.kp = kp
        self.km = km
        self.i = i
        self.memory = []
        self.neighborhood
        self.memorySize = memorySize

    def perception(self):
        """
        Perception of the environment
        """
        # Perceives the surrounding environment
        self.neighborhood, self.self = self.env.getNeighborhood(self.id, self.i)

    def action(self):
        """
        Manages the management of actions in the environment
        """
        # Filling the memory queue. We look if it isn't a wall
        while True:
            lookAt = random.randint(0,3)
            if len(self.neighborhood[lookAt]) != 0:
                self.move(CP(lookAt))
                # it is on the new point
                
                if self.neighborhood[lookAt][self.i-1] == "0" and self.loaded != "":
                    self.drop()
                elif self.neighborhood[lookAt][self.i-1] != "0" and self.loaded == "":
                    self.take(self.neighborhood[lookAt][self.i-1])
                    
                # self.memory.append(self.neighborhood[lookAt][self.i-1])
                break
        # sliding window
        if len(self.memory) == self.memorySize:
            self.memory.pop(0)

    def move(self, oriantation:CP):
        """
        Manages the agent's movements. We must check if the "teleportation" box is not a wall.
        """
        self.env.newPosition(self.id,oriantation,self.i)

    def take(self,object:str):
        """
        Manages the taking of an object
        """ 
        f = self.proportionCalculation(object)
        pTake = math.pow(self.kp / (self.kp + f), 2)
        if self.doI(pTake):
            self.loaded = object
            
            #TODO 
            #Voir comment on prend un objet. As-ton besoin de la lettre ? 

    def drop(self):
        """
        Manages the drop of an object
        """
        f = self.proportionCalculation(self.loaded)
        pDrop = math.pow(f / (self.km + f), 2) 
        if self.doI(pDrop):
            self.loaded = ""
            # TODO
            # Prévenir l'environnement qu'on a plus l'objet

    def proportionCalculation(self,object):
        """
        Calculation of the proportion of objects 
        """
        nbObj = 0
        for i in range(4):
            if self.neighborhood[i][self.i-1] == object:
                nbObj += 1
        return nbObj / 4

    def doI(self, probability):
        """
        Determines if the object is taken/dropped or not.
        """
        random = random.randfloat(0,100)
        if random <= probability*100:
            return True
        return False