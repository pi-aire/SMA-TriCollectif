import random

class Agent(object):
    """
    Sorting agent class
    """

    def __init(self, position, loaded, kp, km, i, f, memory, memorySize, littleGrid):
        """
        Position position is a table position[0] = x et [1] = y
        Loaded is a char : 0 empty, A if object A et B if object B
        kp : k+ 
        km : k-
        i : The number of movement boxes
        f : The proportion of objects of the same type A or B in the immediate environment
        memory : file des objets déjà croisé 
        littleGrid : queue of already crossed objects 
        """
        self.position = position
        self.loaded = loaded
        self.kp = kp
        self.km = km
        self.i = i
        self.f = f
        self.memory = memory
        self.littleGrid = littleGrid
        self.memorySize = memorySize

    def perception(self, env):
        """
        Perception of the environment
        """
        # Perceives the surrounding environment
        self.littleGrid = env.getGrid(self.position)

    def action(self):
        """
        Manages the management of actions in the environment
        """
        # Filling the memory queue. We look if it isn't a wall
        lookAt = random.randint(1,4)
        if lookAt == 1 and self.littleGrid[0][self.i+1] != "W":
            memory.append(self.littleGrid[0][self.i+1])
        if lookAt == 2 and self.littleGrid[0][self.i-1] != "W":
            memory.append(self.littleGrid[0][self.i-1])
        if lookAt == 3 and self.littleGrid[self.i+1][0] != "W":
            memory.append(self.littleGrid[self.i+1][0])
        if lookAt == 4 and self.littleGrid[self.i-1][0] != "W":
            memory.append(self.littleGrid[self.i-1][0])

        # Calculation of the memory size
        actualSize = len(memory)
        # Removal of excess items
        for i in range (actualSize - self.memorySize):
            memory.pop(0)

    def move(self, move):
        """
        Manages the agent's movements. We must check if the "teleportation" box is not a wall.
        """
        if move == 1 and self.littleGrid[0][self.i+1] != "W":
            self.position[0] += self.i
        if move == 2 and self.littleGrid[0][self.i-1] != "W":
            self.position[0] -= self.i
        if move == 3 and self.littleGrid[self.i+1][0] != "W":
            self.position[1] += self.i
        if move ==4 and self.littleGrid[self.i-1][0] != "W":
            self.position[1] -= self.i

    def take(self):
        """
        Manages the taking of an object
        """
        pPrise = (self.kp / (self.kp + self.f))*(self.kp / (self.kp + self.f))
        bool = takeOrDrop(pPrise)
        if bool:
            pass
            #TODO 
            #Voir comment on prend un objet. As-ton besoin de la lettre ? 

    def drop(self):
        """
        Manages the drop of an object
        """
        pDepot = (self.f / (self.km + self.f))* (self.f / (self.km + self.f))
        bool = takeOrDrop(pDepot)
        if bool:
            self.loaded = 0
            # TODO
            # Prévenir l'environnement qu'on a plus l'objet

    def proportionCalculation(self):
        """
        Calculation of the proportion of objects 
        """
        nbObj = 0
        if self.loaded == 0:
            self.f = 0
        elif self.loaded == 'A':
            if  self.littleGrid[self.position[0]-1][self.postion[1]] == 'A':
                nbObj += 1
            if  self.littleGrid[self.position[0]+1][self.postion[1]] == 'A':
                nbObj += 1
            if  self.littleGrid[self.position[0]][self.postion[1]-1] == 'A':
                nbObj += 1
            if  self.littleGrid[self.position[0]][self.postion[1]+1] == 'A':
                nbObj += 1
            self.f = nbObj / 4
        elif self.loaded == 'B':
            if  self.littleGrid[self.position[0]-1][self.postion[1]] == 'B':
                nbObj += 1
            if  self.littleGrid[self.position[0]+1][self.postion[1]] == 'B':
                nbObj += 1
            if  self.littleGrid[self.position[0]][self.postion[1]-1] == 'B':
                nbObj += 1
            if  self.littleGrid[self.position[0]][self.postion[1]+1] == 'B':
                nbObj += 1
            self.f = nbObj / 4

    def takeOrDrop(self, probability):
        """
        Determines if the object is taken/dropped or not.
        """
        random = random.randfloat(0,100)
        if random <= probability:
            return True
        return False