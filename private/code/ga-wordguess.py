import random
from time import time, sleep
import pdb
# import matplotlib.pyplot as plt
DBG = pdb.set_trace

#############################################################################################
TARGET = '''
The 2012 Aston Martin Vanquish was the second generation of the Vanquish, a grand touring car. It was produced between 2012 and 2018 by the British carmaker Aston Martin. It succeeded the DBS, resurrected the name of the 2001–2007 model, and was available as both a coupe and a convertible, the latter known as the Volante. The Vanquish, which is based upon the DB9's architecture, extensively incorporates aluminium throughout its construction. The Vanquish was designed by Marek Reichman and showcased at several events in 2012. It was produced in Gaydon, a village in Warwickshire, England. Aston Martin unveiled the Vanquish Volante in August 2013 and began deliveries late that year. In 2014, they implemented minor modifications to the Vanquish's engine performance. A significantly modified version, the Vanquish S, was launched in 2016; its Volante version was released the following year. The Vanquish S introduced such updates as increased horsepower and torque, and a new body kit. 
'''

len_target = len(TARGET)

def get_fitness(ls):
    """
    """
    return len([i for i in range(len(ls)) if ls[i] != TARGET[i]])


################################################################################################


CHOICES = '''abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890<>^+`, .-;:_!'"#%&/()=?@${[]}'''


def to_str(chrome):
    return ''.join(chrome)


def create_population(chrome_siz, pop_siz):
    """
    An individual is a list of 100 elements
    A population is a list or set of individuals

    This function creates a population (of size `siz`)
    of randomly generated individuals
    """

    def create_individual():
        return [random.choice(CHOICES) for _ in range(chrome_siz)]

    return [create_individual() for _ in range(pop_siz)]





def evaluate_population(population):
    # similar to the one in the book
    fitness = [get_fitness(x) for x in population]
    return list(zip(population, fitness))


def selection(evaluated_population, tournament_size):
    # similar to the one in the book
    competition = random.sample(evaluated_population, tournament_size)
    winner = min(competition, key=lambda individual: individual[1])[0]

    # Return a copy of the selected individual
    return winner[:]


def crossover(parent1, parent2):
    # similar to the one in the book
    pos = random.randint(1, len(parent1))

    offspring1 = parent1[:pos] + parent2[pos:]
    offspring2 = parent2[:pos] + parent1[pos:]

    return (offspring1, offspring2)


def mutate(chromosome):
    # almost similar to the one in the book, but replace element with random val

    mutated = chromosome[:]
    P = 1.0 / len(mutated)

    for pos in range(len(mutated)):
        if random.random() < P:
            mutated[pos] = random.choice(CHOICES)
    return mutated


def genetic_algorithm(chrome_siz, pop_siz, max_gen):
    """
    almost similar to the one in the book,
    has additional stuff to print out the best fit
    """

    start_time = time()

    xover_rate = 0.7
    mut_rate = 1.0 - xover_rate
    cur_xover_rate = xover_rate
    cur_mut_rate = mut_rate

    # Generate and evaluate initial population
    generation = 0
    population = create_population(chrome_siz, pop_siz)

    fitness = evaluate_population(population)
    best = min(fitness, key=lambda item: item[1])
    best_individual = best[0]
    best_fitness = best[1]
    print("Best fitness of initial population",
          (to_str(best_individual), best_fitness))

    best_scores = []
    avg_scores = []

    # Stop when optimum found, or we run out of patience
    while best_fitness > 0 and generation < max_gen:

        # The next generation will have the same size as the current one
        new_population = []
        while len(new_population) < len(population):
            # Selection
            offspring1 = selection(fitness, 10)
            offspring2 = selection(fitness, 10)

            # Crossover
            if random.random() < cur_xover_rate:
                (offspring1, offspring2) = crossover(offspring1, offspring2)

            # Mutation
            offspring1 = mutate(offspring1)
            offspring2 = mutate(offspring2)

            new_population.append(offspring1)
            new_population.append(offspring2)

        # Once full, the new population replaces the old one
        generation += 1
        population = new_population
        fitness = evaluate_population(population)

        best = min(fitness, key=lambda item: item[1])
        best_individual = best[0]
        best_fitness = best[1]

        # new stuff to keep track of progress
        scores = [fit[1] for fit in fitness]
        avg_fitness = sum(scores)/len(scores)
        avg_scores.append(avg_fitness)
        best_scores.append(best_fitness)

        if generation % 2 == 0:
            print(f"\n*** Generation: {generation}, "
                  f"avg fit {avg_fitness}, best fit {best_fitness}\n",
                  to_str(best_individual))

        # sleep(0.5)

    etime = time() - start_time
    print(f"\nBest individual: fit {best_fitness} in {generation} gens, {etime}s\n",
          to_str(best_individual))

    # plt.xlabel("Iterations")
    # plt.ylabel("Fitness (lower better)")
    # plt.plot(best_scores, color="red")
    # plt.plot(avg_scores, color="green")
    # plt.show()


if __name__ == '__main__':
    genetic_algorithm(len_target, 100, 30000)
