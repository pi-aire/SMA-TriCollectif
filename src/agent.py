import math
from environnement import *

class Agent(object):
    """
    Sorting agent class
    """

    def __init__(self, env:Environnement, id:str, kp:float, km:float, i:int, memorySize:int) -> None:
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
        self.loaded = ""
        self.kp = kp
        self.km = km
        self.i = i
        self.memory = []
        self.memorySize = memorySize

    def perception(self) -> None:
        """
        Perception of the environment
        """
        # Perceives the surrounding environment
        self.neighborhood, self.underMe = self.env.getNeighborhood(self.id, self.i)

    def action(self) -> None:
        """
        Manages the management of actions in the environment
        """
        # Take or drop an object at is position 
        if self.underMe != "0" and self.loaded == "":
            # It can take object
            self.take(self.self[0])
        elif self.underMe == "0" and self.loaded != "":
            # It can drop object
            self.drop()
        
        # Filling the memory queue. We look if it isn't a wall
        while True:
            lookAt = random.randint(0,3)
            if len(self.neighborhood[lookAt]) != 0:
                self.move(CP(lookAt))                   
                # self.memory.append(self.neighborhood[lookAt][self.i-1])
                break
        # sliding window
        if len(self.memory) == self.memorySize:
            self.memory.pop(0)

    def move(self, oriantation:CP) -> None:
        """
        Manages the agent's movements. We must check if the "teleportation" box is not a wall.
        """
        self.env.newPosition(self.id,oriantation,self.i)

    def take(self,object:str) -> None:
        """
        Manages the taking of an object
        """ 
        f = self.proportionCalculation(object)
        pTake = math.pow(self.kp / (self.kp + f), 2)
        if self.doI(pTake):
            self.loaded = object
            self.env.setBlock(self.id,"0")

    def drop(self) -> None:
        """
        Manages the drop of an object
        """
        f = self.proportionCalculation(self.loaded)
        pDrop = math.pow(f / (self.km + f), 2) 
        if self.doI(pDrop):
            self.env.setBlock(self.id,self.loaded)
            self.loaded = ""

    def proportionCalculation(self, object:str) -> float:
        """
        Calculation of the proportion of objects 
        """
        nbObj = 0.0
        for i in range(4):
            if self.neighborhood[i][self.i-1] == object:
                nbObj += 1.0
        return nbObj / 4.0

    def doI(self, probability:float) -> bool:
        """
        Determines if the object is taken/dropped or not.
        """
        randomValue = random.randfloat(0,100)
        if randomValue <= probability*100:
            return True
        return False