from environnement import * 
from agent import Agent
import matplotlib.pyplot as plt
import sys
"""
    TP2 SMA Tri collectif multi agents
    authors: BRUNEAU - VASLIN
"""

def main(exo):
    """
    Main function
    """
    stepDefault = 5000000  #number max of steps
    stepGrap = 5000 # number of steps between each compute of mean and median
    stepDisplay = 10000 # number of steps between each displaying of the grid
    
    # Creation of the agents and the environment
    nbAgent = 20
    env = Environnement(50,50,200,200,nbAgent)
    env.dropObjects()
    agentIds = ["A"+str(i) for i in range(nbAgent) ]
    env.dropAgents(agentIds)
    if exo == 1:
        agents = [Agent(env,agentIds[a],0.1,0.3,1,10,0.0) for a in range(nbAgent)]
    else:
        agents = [Agent(env,agentIds[a],0.1,0.3,1,10,0.1) for a in range(nbAgent)]
        
    display(env)
    if exo == 1:
        print("Lancement du tri avec le paramètrage de l'exercice 1.\n La valeur du seuil est fixée à 5/8 afin d'optenir des résultats plus rapide.")
    else :
        print("Lancement du tri avec le paramètrage de l'exercice 2 \net un taux d'erreur à 0.1.\nLa valeur du seuil est fixée à 5/8 afin d'optenir des résultats plus rapide.")
    
    # Set the observing variables
    q1ByStep = []
    meanByStep = []
    window = WindowCheck(10,0.75)
    threshold = 5/8
    
    # Start the simulation
    step = int(stepDefault)
    while step and not window.valid(threshold):
        for agent in agents:
            agent.perception()
            agent.action()
        if step % stepDisplay == 0:
            display(env)
            print("En cours de traitement, veuillez patienter afin de visionner le résultat de la simulation et les graphiques.")
        if step % stepGrap == 0:
            mediane, mean = env.evaluateEnv()
            window.append(mediane)
            q1ByStep.append(mediane)
            meanByStep.append(mean)
        step -= 1
    display(env)
    display(env)
    if (step == 0):
        print("Le nombre d'étape maximale a été atteint.")
    else:
        print("Le seuil a été atteint.")
    
    # Display the results with matplotlib
    fig, (ax0, ax1) = plt.subplots(ncols=2)
    fig.suptitle('Taux de voisin de même type par objet \nen fonction du nombre d\'étapes', fontsize=14, fontweight='bold')
    ax0.plot([(i+1) for i in range(len(meanByStep))],meanByStep, label="Moyenne")
    ax0.plot([(i+1) for i in range(len(meanByStep))], [threshold for i in range(len(meanByStep))], label="Seuil")
    ax1.plot([(i+1) for i in range(len(q1ByStep))],q1ByStep, label="Q1")
    ax1.plot([(i+1) for i in range(len(q1ByStep))], [threshold for i in range(len(q1ByStep))], label="Seuil")
    ax0.set_xlabel(f'Nombre d\'étapes (x{stepGrap})')
    ax1.set_xlabel(f'Nombre d\'étapes (x{stepGrap})')
    ax0.set_ylabel('Moyenne du taux de voisins du même type par objet')
    ax1.set_ylabel('Q1 du taux de voisins du même type par objet')
    plt.show()

class WindowCheck(object):
    """
        Is a sliding windows
    """
    def __init__(self, size:int, percentage:float) -> None:
        self.window = []
        self.size = size
        self.p = percentage

    def append(self,value:float) -> None:
        """
            Add a elemetn to the windos
        """
        self.window.append(value)
        if len(self.window) > self.size:
            self.window.pop(0)

    def valid(self,threshold:float) -> bool:
        """
            Compute if the percentage p of value is higher or equals to the thresold
        """
        if len(self.window) != self.size:
            return False
        count = 0
        for v in self.window:
            if v >= threshold:
                count += 1
        return count/len(self.window) >= self.p

def display(env:Environnement) -> None:
    """
    Print the environment in the terminal
    """
    print()
    print()
    print(env)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "exo1":
            main(1)
        if sys.argv[2] == "exo2":
            main(2)
        else:
            print("Argument incorrect, choisir entre:\n-l'exercice 1 (exo1)\n-l'exercice 2 (exo2)")
    else:
        print("Argument manquant, choisir entre:\n-l'exercice 1 (exo1)\n-l'exercice 2 (exo2)")