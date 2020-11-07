import math
from environnement import *

class Agent(object):
    """
    Sorting agent class
    """

    def __init__(self, env:Environnement, id:str, kp:float, km:float, i:int, memorySize:int, error:float = .0) -> None:
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
        self.neighborhood:list = []
        self.error = error

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
            self.take(self.underMe)
        elif self.underMe == "0" and self.loaded != "":
            # It can drop object
            self.drop()
        
        # Filling the memory queue. We look if it isn't a wall
        possible = [0,1,2,3]
        while len(possible) != 0:
            lookAt = random.randint(0,len(possible)-1)
            if len(self.neighborhood[possible[lookAt]]) != 0:
                self.move(CP(possible[lookAt]))                   
                # self.memory.append(self.neighborhood[lookAt][self.i-1])
                break
            else:
                possible.pop(lookAt)
        
        # sliding window
        self.memory.append(self.underMe)
        if len(self.memory) > self.memorySize:
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
        """Calculation of the proportion of objects 
        Args:
            object (str): the type of object
        Returns:
            float: f
        """
        if self.memorySize != 0 and self.error != 0.0:
            return self.proportionCalculationError(object)
        elif self.memorySize != 0:
            return self.propotionCalculationMemory(object)
        else:
            return self.proportionCalculationNeighborhood(object)

    def proportionCalculationNeighborhood(self, object:str) -> float:
        """
        Calculation of the proportion of objects around the agent
        """
        nbObj = 0.0
        total = 0.0
        for i in range(4):
            if len(self.neighborhood[i]) != 0 :
                total += 1.0
                if self.neighborhood[i][self.i-1] == object:
                    nbObj += 1.0
        return nbObj / total

    def propotionCalculationMemory(self, object:str) -> float:
        """ 
        Calculation of the proportion of objects in the memory
        """
        nbObj = 0.0
        for m in self.memory:
            if m == object:
                nbObj += 1.0
        return nbObj / len(self.memory)

    def proportionCalculationError(self, object:str) -> float:
        """ 
        Calculation of the proportion of objects in the memory with a possible error
        """
        nbObj = 0.0
        nbObjOther = 0.0
        for m in self.memory:
            if m == object:
                nbObj += 1.0
            elif m != '0':
                nbObjOther += 1.0
        return (nbObj+( nbObjOther * self.error)) / len(self.memory)
        
    def doI(self, probability:float) -> bool:
        """
        Determines if the object is taken/dropped or not.
        """
        randomValue = random.uniform(0.0, 1.0)
        if randomValue <= probability:
            return True
        return False