# Hawks and Doves 

Inside the file, I have three methods: infinite, roulette, and stochastic.
Infinite is the first part - implementing the three formulas in the paper and showing that the population of hawks and doves will converge to 5/12 and 7/12 for an "infinite" population. I run this for ten trials, for 200 generations each. The output can be seen in the file "results.txt", and shows, for each trial, the random starting conditions and the eventual convergence.
Roulette is the second part - replicating the infinite example, but with roulette wheel selection instead. Instead of starting with random initial conditions, I start with the correct ratio (5/12 and 7/12) and show that the ratio cannot be sustained. I have 20 trials for this, and evolve each population for 200 generations. I run the method 5 times - once for a population of 60, 120, 300, 600, and 900.
Stochastic is the third part - replacing the roulette wheel selection with SUS. Starting with the ratios of 5/12 and 7/12, I show that the ratio is maintained. I have 5 trials for this part, evolve each population for 200 generations, and run the method 5 times for different populations like I do for roulette.

There are two graphs that are generated - roulette.png and stochastic.png, which show population size on the x axis, and proportion of hawks on the y axis. For roulette, it's obvious that the proportion of hawks eventually converges to 7/12 with enough members of the population. For stochastic, the population always converges to 7/12, regardless of how many members there are.

I also have another file called results.txt, which shows:
    for #1 (the infinite example), for several random initial conditions, that the population eventually converges to 5/12 and 7/12
    for #2 (roulette wheel), the final population of hawks and doves for several trials of different population sizes
    for #3 (stochastic universal sampling), for several trials of different population sizes, that the population eventually converges to 5/12 and 7/12

For the math, I used a python library called numpy. For generating the drawings, I used a library called matplotlib.
