import numpy as np
import random
import matplotlib.pyplot as plt

def main():
    file = open('results.txt', 'w')
    w = 26 # constant
    G = np.matrix([[-25, 50], [0, 15]]) # payoff matrix

    file.write("***Prove convergence to 5/12 and 7/12 for random starting conditions\n")
    infinite(file, w, G)

    file.write("***Roulette wheel selection\n")
    roulette(60, file, w, G)
    roulette(120, file, w, G)
    roulette(300, file, w, G)
    roulette(600, file, w, G)
    roulette(900, file, w, G)
    plt.savefig('roulette.png')

    file.write("***Stochastic sampling\n")
    stochastic(60, file, w, G)
    stochastic(120, file, w, G)
    stochastic(300, file, w, G)
    stochastic(600, file, w, G)
    stochastic(900, file, w, G)
    plt.savefig('stochastic.png')

    file.close()

def infinite(file, w, G):
    # I have this for loop run just 10 times because otherwise the output gets lengthy, but feel free to increase the number of iterations
    for i in range(0,10):
        file.write("TRIAL " + str(i) + "\n")

        randomPop = random.uniform(0,1)
        # generate random populations of hawks and doves
        # p = proportions with which the strategies of G are used in the population, sums to 1
        p = np.matrix( [[randomPop], [1 - randomPop]] )

        file.write("Initial p = \n" + str(p) + "\n")

        # evolve for 200 generations (these are the 3 formulas in the paper)
        for i in range(0,200):
            f = np.dot(G,p) + w
            normalp = p[0]*f[0] + p[1]*f[1] # note = the numpy inner method was doing something weird and returning a matrix instead of a scalar. I'm not too knowledgeable about matrixes so I don't understand why it would have that behavior. I just did the inner product myself since it's pretty straightforward for matrixes of size 2x1
            p = np.multiply(p,f)/normalp
        file.write("convergence to = \n" + str(p) + "\n\n")

def roulette(totalPop, file, w, G):
    # 20 trials
    for i in range(0,20):
        numDoves = (5.0/12.0)*totalPop
        numHawks = (7.0/12.0)*totalPop

        file.write("Population size = " + str(totalPop) + "\n")

        # evolve for 200 generations
        for i in range(0,200):
            p = np.matrix([[numHawks],[numDoves]])/(numHawks + numDoves)
            # hawk fitness = -25 * # Hawks + 50 * # Doves +26
            # dove fitness = 0 * # Hawks + 15 * # Doves + 26
            f = np.matrix([[-25*p.item(0,0) + 50*p.item(1,0) + w],[15*p.item(1,0) + w]])

            # generate new population
            newHawks = 0.0
            newDoves = 0.0
            totalFitness = (numHawks*f[0]) + (numDoves*f[1])
            # randomly select a fitness
            # if fitness if bigger than number of hawks * hawk fitness, then it is a dove
            # otherwise, it is a hawk
            for i in range(0, totalPop):
                randomNew = random.uniform(0, totalFitness)
                if (randomNew > (numHawks*f[0])):
                    newDoves += 1
                else:
                    newHawks += 1

            numHawks = newHawks
            numDoves = newDoves

        file.write("convergence to = \n" + str(p) + "\n\n")
        plt.scatter(totalPop, float(p[0]))

def stochastic(totalPop, file, w, G):
    # 5 trials
    for i in range(0,5):
        # start with ESS
        numDoves = (5.0/12.0)*totalPop
        numHawks = (7.0/12.0)*totalPop

        file.write("Population size = " + str(totalPop) + "\n")

        # evolve for 200 generations
        for i in range(0,200):
            # population and fitness functions same as in roulette
            p = np.matrix([[numHawks],[numDoves]])/(numHawks + numDoves)
            f = np.matrix([[-25*p.item(0,0) + 50*p.item(1,0) + w],[15*p.item(1,0) + w]])

            # generate new population, start with 0 hawks and 0 doves
            newHawks = 0.0
            newDoves = 0.0
            totalFitness = (numHawks*f[0]) + (numDoves*f[1])
            randomNew = random.uniform(0, totalFitness) # random new bird
            step = totalFitness/totalPop
            # for the amount that we have in the population, check if the current new member is bigger than the hawk fitness * number of hawks, and add new dove or hawk accordingly
            # also then add step to randomNew, if we get larger than the total fitness, mod by total fitness so we go around the circle instead of fall off
            for i in range(0, totalPop):
                if (randomNew > (numHawks*f[0])):
                    newDoves += 1
                else:
                    newHawks += 1
                randomNew = (randomNew + step) % totalFitness

            numHawks = newHawks
            numDoves = newDoves

        file.write("convergence to = \n" + str(p) + "\n\n")
        plt.scatter(totalPop, float(p[0]))

main()
