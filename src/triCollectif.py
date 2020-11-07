import environnement as e
from agent import Agent

def main():
    nbAgent = 20
    env = e.Environnement(50,50,200,200,nbAgent)
    env.dropObjects()
    agentIds = ["A"+str(i) for i in range(nbAgent) ]
    env.dropAgents(agentIds)
    agents = [Agent(env,agentIds[a],0.1,0.3,1,10) for a in range(nbAgent)]
    step = 500000
    while step:
        for agent in agents:
            agent.perception()
            agent.action()
        if step % 100000 == 0:
            display(env)
        step -= 1

# Display the grid and refresh
# stdscr = curses.initscr()

def display(str:str) -> None:
    # stdscr.erase()
    # stdscr.addstr(str)
    # stdscr.refresh()
    print()
    print()
    print(str)
    

if __name__ == '__main__':
    main()