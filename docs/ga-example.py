import random
import time


def gen_pop(pop_size, list_size, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(list_size)] 
            for _ in range(pop_size)]

def fitness(individual):
    """
    return the number of 0s
    """
    return individual.count(0)

def select(population, fitnesses):
    tournament_size = 3
    selected = random.sample(list(zip(population, fitnesses)), tournament_size)
    return max(selected, key=lambda x: x[1])[0]

def crossover(parent1, parent2, rate):
    if random.random() < rate:  # Crossover probability
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    else:
        return parent1, parent2

def mutate(individual, rate, min_val, max_val):
    new_individual = individual[:]
    for i in range(len(new_individual)):
        if random.random() < rate:
            new_individual[i] = random.randint(min_val, max_val)
    return new_individual

# Main Genetic Algorithm Loop
def ga(pop_size, list_size, xover_rate, mut_rate, min_val, max_val):
    gen = 0
    population = gen_pop(pop_size, list_size, min_val, max_val)
    fitnesses = [fitness(ind) for ind in population]
    best_individual = max(population, key=fitness)
    
    while(fitness(best_individual) < list_size):
        gen += 1
        new_population = []
        
        while len(new_population) < pop_size:
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            offspring1, offspring2 = crossover(parent1, parent2, xover_rate)
            new_population.append(mutate(offspring1, mut_rate, min_val, max_val))
            if len(new_population) < pop_size:
                new_population.append(mutate(offspring2, mut_rate, min_val, max_val))
        
        population = new_population  # Replace the old population
        fitnesses = [fitness(ind) for ind in population]
        best_individual = max(population, key=fitness)
        print(f"Gen {gen}, best = {best_individual}, fit = {fitness(best_individual)}, ")
        #time.sleep(0.1)
    return best_individual


# Parameters
pop_size = 10
list_size = 100
min_val = -10
max_val = 10
xover_rate = 0.8
mut_rate = 0.01
# Run the GA
stime = time.time()
best = ga(pop_size, list_size, xover_rate, mut_rate, min_val, max_val)
etime = time.time() - stime

print(f"Best individual: {best}")
print(f"Best individual sum:", sum(best))
print(f"Best individual fitness:", fitness(best))
print(f"Total time: {etime} seconds")

