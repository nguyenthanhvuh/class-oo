import random
import time


def initialize_population(pop_size, list_length):
    return [[random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8 , 9, -1, -2, -3, -4, -5, -6, -7, -8, -9]) 
             for _ in range(list_length)] for _ in range(pop_size)]

# def fitness(individual):
#     """
#     return the number of 0s
#     """
#     return individual.count(0)

#your task
#evolve a list whose sum is equal to target (target is 99)
def fitness(individual,target=99):
    return 100 - abs(target - sum(individual))


def select(population, fitnesses):
    tournament_size = 3
    selected = random.sample(list(zip(population, fitnesses)), tournament_size)
    return max(selected, key=lambda x: x[1])[0]

def crossover(parent1, parent2):
    if random.random() < 0.8:  # Crossover probability
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    else:
        return parent1, parent2

def mutate(individual, mutation_rate=0.01):
    new_individual = individual[:]
    for i in range(len(new_individual)):
        if random.random() < mutation_rate:
            if random.random() < 0.5:
                new_individual[i] = new_individual[i] + 1
            else:
                new_individual[i] = new_individual[i] - 1
    return new_individual

# Main Genetic Algorithm Loop
def genetic_algorithm(pop_size, list_length):
    
    population = initialize_population(pop_size, list_length)
    fitnesses = [fitness(ind) for ind in population]
    best_individual = max(population, key=fitness)
    
    while(fitness(best_individual) < list_length):
        fitnesses = [fitness(ind) for ind in population]
        new_population = []
        
        while len(new_population) < pop_size:
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.append(mutate(offspring1))
            if len(new_population) < pop_size:
                new_population.append(mutate(offspring2))
        
        population = new_population  # Replace the old population
        best_individual = max(population, key=fitness)
        print(f"Best = {best_individual}, fit = {fitness(best_individual)}, ")
        #time.sleep(0.1)
    return best_individual

# Parameters
population_size = 100
list_length = 15


# Run the GA
best = genetic_algorithm(population_size, list_length)
print(f"Best individual: {best}")
print(f"Best individual sum:", sum(best))
print(f"Best individual fitness:", fitness(best))

