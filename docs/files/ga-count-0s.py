import random
import time

def gen_pop(pop_size, indv_size, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(indv_size)] 
            for _ in range(pop_size)]

def eval_fitness(indiv, indv_size):
    # code goes here
    pass    

def select(pop, fscores):
    # code goes here
    pass

def crossover(parent1, parent2, rate):
    # code goes here
    pass

def mutate(indiv, rate, min_val, max_val):
    new_indiv = indiv[:]
    for i in range(len(new_indiv)):
        if random.random() < rate:
            new_indiv[i] = random.randint(min_val, max_val)
    return new_indiv

def stopping_criteria(best_fit):
    return best_fit == 1.0

# Main Genetic Algorithm Loop
def ga(pop_size, indv_size, xover_rate, mut_rate, min_val, max_val):
    
    pop = gen_pop(pop_size, indv_size, min_val, max_val)
    fscores = [eval_fitness(ind, indv_size) for ind in pop]
    best, best_fit = max(zip(pop, fscores), key=lambda x: x[1])
    gen = 0
    while not stopping_criteria(best_fit):
        gen += 1
        new_pop = []
        while len(new_pop) < pop_size:
            parent1 = select(pop, fscores)
            parent2 = select(pop, fscores)
            offspring1, offspring2 = crossover(parent1, parent2, xover_rate)
            new_pop.append(mutate(offspring1, mut_rate, min_val, max_val))
            if len(new_pop) < pop_size:
                new_pop.append(mutate(offspring2, mut_rate, min_val, max_val))
        
        pop = new_pop  # Replace the old pop
        fscores = [eval_fitness(ind, indv_size) for ind in pop]
        best, best_fit = max(zip(pop, fscores), key=lambda x: x[1]) 
        print(f"Gen {gen}, best = {best}, fit = {best_fit}")

        time.sleep(0.05)
        
    return best, best_fit


# Parameters
pop_size = 5
indv_size = 50
min_val = -10
max_val = 10
xover_rate = 0.8
mut_rate = 0.01

# Run the GA
stime = time.time()
best, best_fit = ga(pop_size, indv_size, xover_rate, mut_rate, min_val, max_val)
etime = time.time() - stime

print(f"RESULT: Best = {best}, sum = {sum(best)}, fit = {best_fit}, total time = {etime}s")



# fitness :  returns 0 ... 1   (1 being the best, 0 being the worst)


#1. [0,1,4,10,-2]                  fit = 0.2

#2. [-1,-4,0,5,0]   better than 1   fit=.4
#3. [0,0, 1,0,-1]   better than 2   fit=.6

# => 
# [-1,-4,1,0,-1]      fit = .2 
# [0,0,0,5,0]         fit = .8

# [-1,-8,1,1,-1]    #  fit = 0 

# of 0's /  len(input)