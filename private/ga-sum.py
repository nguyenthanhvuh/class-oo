import random
import time

def gen_pop(pop_size, list_size, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(list_size)] 
            for _ in range(pop_size)]

def get_fitness(indiv, target):
    return 1. / (1 + abs(target - sum(indiv)))

def select(pop, fscores):
    tournament_size = 3
    selected = random.sample(list(zip(pop, fscores)), tournament_size)
    return max(selected, key=lambda x: x[1])[0]

def crossover(parent1, parent2, rate):
    if random.random() < rate: 
        pt = random.randint(1, len(parent1) - 1)
        return parent1[:pt] + parent2[pt:], parent2[:pt] + parent1[pt:]
    else:
        return parent1, parent2

def mutate(indiv, rate, min_val, max_val):
    new_indiv = indiv[:]
    for i in range(len(new_indiv)):
        if random.random() < rate:
            new_indiv[i] = random.randint(min_val, max_val)
    return new_indiv

def stopping_criteria(best_fit):
    return best_fit == 1.0

# Main Genetic Algorithm Loop

def genetic_algorithm(pop_size, list_size, xover_rate, mut_rate, min_val, max_val, target):

    pop = gen_pop(pop_size, list_size, min_val, max_val)
    fscores = [get_fitness(ind, target) for ind in pop]
    best_ind, best_fit = max(zip(pop, fscores), key=lambda x: x[1])
    gen = 0
    
    while not stopping_criteria(best_fit):
        gen = gen + 1
        new_pop = []
        while len(new_pop) < pop_size:
            parent1 = select(pop, fscores)
            parent2 = select(pop, fscores)
            offspring1, offspring2 = crossover(parent1, parent2, xover_rate)
            new_pop.append(mutate(offspring1, mut_rate, min_val, max_val))
            if len(new_pop) < pop_size:
                new_pop.append(mutate(offspring2, mut_rate, min_val, max_val))
        
        pop = new_pop  # Replace the old pop
        fscores = [get_fitness(ind, target) for ind in pop]
        best_ind, best_fit = max(zip(pop, fscores), key=lambda x: x[1])
        print(f"Gen = {gen}, best = {best_ind}, sum = {sum(best_ind)}, fit = {best_fit}")
        # time.sleep(0.1)
    return best_ind, best_fit


# Parameters
pop_size = 10
list_length = 20
target = 100
min_val = -10
max_val = 10
xover_rate = 0.8
mut_rate = 0.1
# Run the GA
stime = time.time()
best_ind, best_fit = genetic_algorithm(pop_size, list_length, xover_rate, mut_rate, min_val, max_val, target)
etime = time.time() - stime

print(f"RESULT: Best = {best_ind}, sum = {sum(best_ind)}, fit = {best_fit}, total time = {etime}s")



