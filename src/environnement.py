import random

class Environnement(object):
    """
    docstring
    """
    def __init__(self,N,M,na,nb,nAgent):
        self.grid = [[ 0 for j in range(M)] for i in range(N)]
        self.na  = na
        self.nb  = nb
        self.nAgent  = nAgent
        self.N = N 
        self.M = M
        self.agentPosition = dict()

    def dropObjects(self):
        """
        Drops the A , the B
        """
        naDroped = 0
        while(naDroped != self.na):
            x = random.randint(0,self.N-1)
            y = random.randint(0,self.M-1)
            if self.grid[x][y] == 0:
                self.grid[x][y] = "A"
                naDroped +=1
        nbDropped = 0
        while(nbDropped != self.nb):
            x = random.randint(0,self.N-1)
            y = random.randint(0,self.M-1)
            if self.grid[x][y] == 0:
                self.grid[x][y] = "B"
                nbDropped +=1

    def dropAgents(self,ids):
        """
        Places agents in the environment only on the available 0 boxes
        """
        agentPosition = []
        naDroped = 0
        while(naDroped != self.nAgent):
            x = random.randint(0,self.N-1)
            y = random.randint(0,self.M-1)
            if self.grid[x][y] == 0:
                self.grid[x][y] = ids[naDroped]
                self.agentPosition
                naDroped +=1
        # return agentPosition

    def getSensoredData(self,id,distance):
        """
        Provides environmental sensor data
        Args:
            id (str): id of the agent you wish to perceive
            distance (int): distance of vision of the agent
        Returns:
            [list<list>]: list of list of each direction of distance of vision
        """
        # toric perception impossible
        

        
    
    def __str__(self):
        result = ""
        for line in self.grid:
            for value in line:
                if value == 0:
                    result += "⬜"
                elif value == "A":
                    result += "🅰 "
                elif value == "B":
                    result += "🅱 "
                else:
                    result += "🤖"
            result += "\n"
        return result