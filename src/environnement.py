import random
import enum

class CP(enum.Enum):
    """ Cardinal Points """
    NORTH=0
    EAST=1
    SOUTH=2
    WEST=3

class Environnement(object):
    """
    Environment class
    """
    def __init__(self,N,M,na,nb,nAgent) -> None:
        self.grid = [[ "0" for j in range(M)] for i in range(N)]
        self.na  = na
        self.nb  = nb
        self.nAgent  = nAgent
        self.N = N 
        self.M = M
        self.agentsPosition = dict()

    def dropObjects(self) -> None:
        """
        Drops the A , the B
        """
        naDroped = 0
        while(naDroped != self.na):
            x = random.randint(0,self.N-1)
            y = random.randint(0,self.M-1)
            if self.grid[x][y] == "0":
                self.grid[x][y] = "A"
                naDroped +=1
        nbDropped = 0
        while(nbDropped != self.nb):
            x = random.randint(0,self.N-1)
            y = random.randint(0,self.M-1)
            if self.grid[x][y] == "0":
                self.grid[x][y] = "B"
                nbDropped +=1

    def dropAgents(self,ids:list) -> None:
        """
        Places agents in the environment only on the available 0 boxes
        """
        naDroped = 0
        while(naDroped != self.nAgent):
            x = random.randint(0,self.N-1)
            y = random.randint(0,self.M-1)
            if self.grid[x][y] == "0":
                self.grid[x][y] = "R"
                self.agentsPosition[ids[naDroped]] = {"x":x,"y":y}
                naDroped +=1
        # return agentPosition

    def getNeighborhood(self,id:str, range:int) -> list:
        """
        Return the neighborhood of the agent
        Args:
            id (str): agent id
            range (int): agent view distance
        """
        ap = self.agentsPosition[id] #Position de l'agent
        nbh = []
        for oriantation in [(0,-1),(1,0),(0,1),(-1,0)]:
            boundx = ap["x"] + (oriantation[0] * range)
            boundy = ap["y"] + (oriantation[1] * range)
            if (boundx < self.N and boundx >= 0 and 
                boundy < self.M and boundy >= 0 and
                self.grid[boundx][boundy] != "R"and 
                len(self.grid[boundx][boundy]) != 2):
                if boundx == ap["x"]:
                    if boundy < ap["y"]:
                        nbh.append(self.grid[ap["x"]][boundy:ap["y"]])
                    else:
                        nbh.append(self.grid[ap["x"]][ap["y"]+oriantation[1]:boundy+oriantation[1]])
                else:
                    if boundx < ap["x"]:
                        nbh.append(self.grid[boundx:ap["x"]][ap["y"]])
                    else:
                        nbh.append(self.grid[ap["x"]+oriantation[0]:boundx+oriantation[0]][ap["y"]])    
            else:
                nbh.append([])
        underAgent = "0"
        if len(self.grid[ap["x"]][ap["y"]]) == 2:
            underAgent = self.grid[ap["x"]][ap["y"]][0]
        return nbh, underAgent

    def newPosition(self, id:str, orentation:CP, range:int) -> None:
        """[summary]

        Args:
            id (str): [description]
            orentation (CP): [description]
            range (int): [description]
        """
        orientations = [(0,-1),(1,0),(0,1),(-1,0)]
        ap = self.agentsPosition[id] #Position de l'agent
        newx = ap["x"] + (orientations[orentation][0] * range)
        newy = ap["y"] + (orientations[orentation][1] * range)
        # clean the previous position
        if len(self.grid[ap["x"]][ap["y"]]) == 2:
            self.grid[ap["x"]][ap["y"]] = self.grid[ap["x"]][ap["y"]][0]
        else:
            self.grid[ap["x"]][ap["y"]] = "0"
            
        # Set the new position
        self.agentsPosition[id] = {"x":newx, "y":newy}
        if self.grid[newx][newy] != "0":
            self.grid[newx][newy] += "R"
        else:
            self.grid[newx][newy] = "R"
            
    def setBlock(self, id:str, block:str) -> None:
        ap = self.agentsPosition[id] #Position de l'agent
        if block == "0":
            # take block AR or BR
            self.grid[ap["x"]][ap["y"]] = "R"
        else:
            # drop block
            self.grid[ap["x"]][ap["y"]] = block+"R"
    
    def __str__(self) -> str:
        result = ""
        for line in self.grid:
            for value in line:
                if value == "0":
                    result += "⬜"
                elif value == "A":
                    result += "🅰 "
                elif value == "B":
                    result += "🅱 "
                elif len(value) == 2:
                    result += "🛂"
                else:
                    result += "🤖"
            result += "\n"
        return result