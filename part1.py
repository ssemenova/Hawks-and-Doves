import numpy as np
import random

w = 26 # constant
G = np.matrix([[-25, 50], [0, 15]]) # payoff matrix

# I have this for loop run just 10 times because otherwise the output gets lengthy, but feel free to increase the number of iterations
for i in range(0,10):
    randomPop = random.uniform(0,1)
    # generate random populations of hawks and doves
    # p = proportions with which the strategies of G are used in the population, sums to 1
    p = np.matrix( [[randomPop], [1 - randomPop]] )
    print "Trial " + str(i) + " = for initial p \n" + str(p)

    # evolve for 200 generations (these are the 3 formulas in the paper)
    for i in range(0,200):
        f = np.dot(G,p) + w
        normalization = p[0]*f[0] + p[1]*f[1] # note = the numpy inner method was doing something weird and returning a matrix instead of a scalar. I'm not too knowledgeable about matrixes so I don't understand why it would have that behavior. I just did the inner product myself since it's pretty straightforward for matrixes of size 2x1
        p = np.multiply(p,f)/normalization

    print "convergence to\n" + str(p) + "\n"
