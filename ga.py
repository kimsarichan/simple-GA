"""
Finding x,y for minimation function F(x,y) = 3x^2 + 2y^2 - 4x + y/2 using Genetic Algorithm
wrismawan, E101
"""
from random import randint
import collections

Individu = collections.namedtuple('Individu', 'ind fitness')

class GA(object):
    def __init__(self, jum_pop=10, mut_rate=.3):
        self.jum_pop = jum_pop
        self.mut_rate = mut_rate

    def solve(self, fitness, initial_population, generation=10):
        """
        Main function of GA
        """
        current_generation = [Individu(ind, fitness(ind)) for ind in initial_population]
        print current_generation

    def _crossover(self, u, v):
        """
        Crossover function ..... coming soon
        """

    def _mutation(self, ind):
        """
        Mutation function ..... coming soon
        """     

    def _selection(self, pop):
        """
        Selection function ..... coming soon
        """     
    
if __name__ == "__main__":
    def decode(ind):
        """
        Decode string individual into integer x,y (as function parameter)
        """
        mid = len(ind)/2
        x = int(ind[:mid],2)
        y = int(ind[mid:],2)
        return [x , y]

    def encode(x,y):
        """
        Encode two integers x,y into string as individual
        """
        bin_x = '{0:04b}'.format(x)
        bin_y = '{0:04b}'.format(y)
        return bin_x+bin_y

    def calculate_fitness(ind):
        """
        Calculate fitness of individual
        F(x,y) = 3x^2 + 2y^2 - 4x + y/2
        """
        val = decode(ind)
        x = val[0]
        y = val[1]
        f = 3*(x**2) + 2*(y**2) - (4*x) + (y*1.0/2)
        return 1 * 1.0 / f + .1

    ga = GA()

    #init population
    pop = ["".join([str(randint(0,1)) for _ in range(8)]) for _ in range(ga.jum_pop)]

    ga.solve(calculate_fitness, pop, generation=10)


