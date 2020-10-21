import random

class Environnement(object):
    """
    docstring
    """
    def __init__(self,N,M,na,nb,nagent):
        self.grid = [[ 0 for j in range(M)] for i in range(N)]
        self.na  = na
        self.nb  = nb
        self.nagent  = nagent
        self.N = N 
        self.M = M
        self.agentPosition = dict()

    def dropObjects(self):
        """
        Dépose les A , les B
        """
        naDroped = 0
        while(naDroped != self.na):
            x = random.randint(0,self.N-1)
            y = random.randint(0,self.M-1)
            if self.grid[x][y] == 0:
                self.grid[x][y] = "A"
                naDroped +=1
        nbDroped = 0
        while(nbDroped != self.nb):
            x = random.randint(0,self.N-1)
            y = random.randint(0,self.M-1)
            if self.grid[x][y] == 0:
                self.grid[x][y] = "B"
                nbDroped +=1

    def dropAgents(self,ids):
        """Place les agents dans l'environnement
        seulement sur les cases 0 disponible
        """
        agentPosition = []
        naDroped = 0
        while(naDroped != self.nagent):
            x = random.randint(0,self.N-1)
            y = random.randint(0,self.M-1)
            if self.grid[x][y] == 0:
                self.grid[x][y] = ids[naDroped]
                self.agentPosition
                naDroped +=1
        # return agentPosition

    def getSensoredData(self,id,distance):
        """
        Fournis les données du capteurs de l'environement 
        Args:
            id (str): id de l'agent que l'on souhaite percevoir
            distance (int): distance de vision de l'agent
        Returns:
            [list<list>]: liste de liste de chaque direction de distance de la vision
        """
        # perception torique ou impossible
        

        
    
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