import random
from time import time
# import matplotlib.pyplot as plt


def create_population(siz):
    """
    An individual is a list of 100 elements
    A population is a list or set of individuals

    This function creates a population (of size `siz`)
    of randomly generated individuals
    """

    def create_individual():
        return [random.randint(-1000, 1000) for _ in range(100)]

    return [create_individual() for _ in range(siz)]


def get_fitness(ls):
    """
    give better fitness (closer to 0) to individuals
    having many similar elements
    """
    uniqs = set(ls)  # uniq vals
    max_cts = max(ls.count(v) for v in uniqs)  # get the max # of occurences
    return len(ls) - max_cts


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
            mutated[pos] = random.randint(-1000, 1000)
    return mutated


def genetic_algorithm(max_gen):
    """
    almost similar to the one in the book,
    has additional stuff to print out the best fit
    """

    start_time = time()
    # Generate and evaluate initial population
    generation = 0
    population = create_population(100)
    fitness = evaluate_population(population)
    best = min(fitness, key=lambda item: item[1])
    best_individual = best[0]
    best_fitness = best[1]
    print("Best fitness of initial population", (best_individual, best_fitness))

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
            if random.random() < 0.7:
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
        avg_fitness = sum(scores) / len(scores)
        avg_scores.append(avg_fitness)
        best_scores.append(best_fitness)

        if generation % 100 == 0:
            print(
                "Generation: {}, avg fit {}, best fit {}, individual {}".format(
                    generation, avg_fitness, best_fitness, best_individual
                )
            )

    print(
        "Found best individual: {}, fitness {} in {} generations, {}s".format(
            best_individual, best_fitness, generation, time() - start_time
        )
    )

    plt.xlabel("Iterations")
    plt.ylabel("Fitness (lower better)")
    plt.plot(best_scores, color="red")
    plt.plot(avg_scores, color="green")
    plt.show()


if __name__ == "__main__":
    genetic_algorithm(20000)
