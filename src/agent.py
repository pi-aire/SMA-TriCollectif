import random

class Agent(object):
    """
    Classe des agents qui font le tri
    """

    def __init(self, position, loaded, kp, km, i, f, memory, littleGrid):
        """
        Position est un tableau ou position[0] = x et [1] = y
        Loaded est un char : 0 si vide, A si objet A et B si objet B
        kp : k+ 
        km : k-
        i : Le nombre de case de déplacement
        f : la proportion d'objet de même type A ou B dans l'env immédiat
        memory : file des objets déjà croisé 
        littleGrid : la grille autour de sois
        """
        self.position = position
        self.loaded = loaded
        self.kp = kp
        self.km = km
        self.i = i
        self.f = f
        self.memory = memory
        self.littleGrid = littleGrid

    def perception(self, env):
        """
        Perception de l'environnement
        """
        # Perçoit l'environnement proche
        self.littleGrid = env.getGrid(self.position)

    def action(self):
        """
        Gère la gestioin des actions dans l'environnement
        """
        nbObj = 0
        if self.loaded == 0:
            self.f = 0
        elif self.loaded == 'A':
            if  self.grid[self.position[0]-1][self.postion[1]] == 'A':
                nbObj += 1
            if  self.grid[self.position[0]+1][self.postion[1]] == 'A':
                nbObj += 1
            if  self.grid[self.position[0]][self.postion[1]-1] == 'A':
                nbObj += 1
            if  self.grid[self.position[0]][self.postion[1]+1] == 'A':
                nbObj += 1
            self.f = nbObj / 4
        elif self.loaded == 'B':
            if  self.grid[self.position[0]-1][self.postion[1]] == 'B':
                nbObj += 1
            if  self.grid[self.position[0]+1][self.postion[1]] == 'B':
                nbObj += 1
            if  self.grid[self.position[0]][self.postion[1]-1] == 'B':
                nbObj += 1
            if  self.grid[self.position[0]][self.postion[1]+1] == 'B':
                nbObj += 1
            self.f = nbObj / 4

    def move(self):
        """
        Gère les déplacements de l'agent
        """
        move = random.randint(1,4)
        if move == 1 and self.littleGrid[0][i-1] != "M":
            self.position[0] += self.i
        if move == 2:
            self.position[0] -= self.i
        if move == 3:
            self.position[1] += self.i
        if move ==4:
            self.position[1] -= self.i

    def take(self):
        """
        Gère la prise d'un objet
        """
        pPrise = (kp / (kp + f))*(kp / (kp + f))

    def drop(self):
        """
        Gère le dépot d'un objet
        """
        pDepot = (f / (km + f))* (f / (km + f))



