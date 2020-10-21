import environnement as e




def main():
    env = e.Environnement(50,50,200,200,20)
    env.dropObjects()
    env.dropAgents(["A"+str(i) for i in range(20) ])
    print(env)


if __name__ == '__main__':
    main()