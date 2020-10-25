import random

class Agent(object):
    """
    Classe des agents qui font le tri
    """

    def __init(self, position, loaded, kp, km, i, f, memory, memorySize, littleGrid):
        """
        Position est un tableau ou position[0] = x et [1] = y
        Loaded est un char : 0 si vide, A si objet A et B si objet B
        kp : k+ 
        km : k-
        i : Le nombre de case de déplacement
        f : la proportion d'objets de même type A ou B dans l'environnement immédiat
        memory : file des objets déjà croisé 
        littleGrid : la grille autour de soi
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
        Perception de l'environnement
        """
        # Perçoit l'environnement proche
        self.littleGrid = env.getGrid(self.position)

    def action(self):
        """
        Gère la gestion des actions dans l'environnement
        """
        # Remplissage de la file de mémoire
        if littleGrid[0][1] == "A":
            memory.append("A")
        if littleGrid[0][1] == "B":
            memory.append("B")
        if littleGrid[0][1] == "0":
            memory.append("0")
        if littleGrid[0][-1] == "A":
            memory.append("A")
        if littleGrid[0][-1] == "B":
            memory.append("B")
        if littleGrid[0][-1] == "0":
            memory.append("0")
        if littleGrid[1][0] == "A":
            memory.append("A")
        if littleGrid[1][0] == "B":
            memory.append("B")
        if littleGrid[1][0] == "0":
            memory.append("0")
        if littleGrid[-1][0] == "A":
            memory.append("A")
        if littleGrid[-1][0] == "B":
            memory.append("B")
        if littleGrid[-1][0] == "0":
            memory.append("0")
        # Calcul de la taille de la memoire
        actualSize = len(memory)
        # Suppression des éléments en trop
        for i in range (actualSize - self.memorySize):
            memory.pop(0)

    def move(self):
        """
        Gère les déplacements de l'agent. On doit vérifier si la case de "téléportation" n'est pas un mur.
        """
        move = random.randint(1,4)
        if move == 1 and self.littleGrid[0][self.i+1] != "M":
            self.position[0] += self.i
        if move == 2 and self.littleGrid[0][self.i-1] != "M":
            self.position[0] -= self.i
        if move == 3 and self.littleGrid[self.i+1][0] != "M":
            self.position[1] += self.i
        if move ==4 and self.littleGrid[self.i-1][0] != "M":
            self.position[1] -= self.i

    def take(self):
        """
        Gère la prise d'un objet
        """
        pPrise = (self.kp / (self.kp + self.f))*(self.kp / (self.kp + self.f))
        bool = takeOrDrop(pPrise)
        if bool:
            pass
            #TODO 
            #Voir comment on prend un objet. As-ton besoin de la lettre ? 

    def drop(self):
        """
        Gère le dépot d'un objet
        """
        pDepot = (self.f / (self.km + self.f))* (self.f / (self.km + self.f))
        bool = takeOrDrop(pDepot)
        if bool:
            self.loaded = 0
            # TODO
            # Prévenir l'environnement qu'on a plus l'objet

    def proportionCalculation(self):
        #Calcul de la proportion d'objets 
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

    def takeOrDrop(self, proba):
        """
        Détermine si l'objet est pris/laché ou non
        """
        random = random.randfloat(0,100)
        if random <= proba:
            return True
        return False