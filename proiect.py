import random
import numpy 

def generatePopulation():
    population = []
    for chromosome_number in range(chromosomes_number):
        chromosome = initial_cromosome.copy()
        random.shuffle(chromosome)
        population.append(chromosome)
    return population


def getMap():
# Barcelona, Madrid, Valencia, Bilbao, Seville, Malaga, Zaragoza, San Sebastian, A Coruna, Alicante :
# Barcelona         : 0, 626, 349, 608, 994, 980, 307, 566, 1083, 528
# Madrid            : 626, 0, 360, 403, 531, 542, 320, 457, 593, 432
# Valencia          : 349, 360, 0, 612, 655, 623, 309, 573, 950, 167
# Bilbao            : 608, 403, 612, 0, 861, 925, 302, 101, 542, 786
# Seville           : 994, 531, 655, 861, 0, 213, 847, 918, 926, 595
# Malaga            : 980, 542, 623, 925, 213, 0, 841, 983, 1123, 477
# Zaragoza          : 307, 320, 309, 302, 847, 841, 0, 264, 781, 484
# SanSeb.           : 566, 457, 573, 101, 918, 983, 264, 0, 639, 746
# A Coruna          : 1083, 593, 950, 542, 926, 1123, 781, 639, 0, 1071
# Alicante          : 528, 432, 167, 786, 595, 477, 484, 746, 1071, 0
    return [
        [0, 626, 349, 608, 994, 980, 307, 566, 1083, 528],
        [626, 0, 360, 403, 531, 542, 320, 457, 593, 432],
        [349, 360, 0, 612, 655, 623, 309, 573, 950, 167],
        [608, 403, 612, 0, 861, 925, 302, 101, 542, 786],
        [994, 531, 655, 861, 0, 213, 847, 918, 926, 595],
        [980, 542, 623, 925, 213, 0, 841, 983, 1123, 477],
        [307, 320, 309, 302, 847, 841, 0, 264, 781, 484],
        [566, 457, 573, 101, 918, 983, 264, 0, 639, 746],
        [1083, 593, 950, 542, 926, 1123, 781, 639, 0, 1071],
        [528, 432, 167, 786, 595, 477, 484, 746, 1071, 0]
    ]


def getCities():
    return {
        0: "Barcelona",
        1: "Madrid",
        2: "Valencia",
        3: "Bilbao",
        4: "Seville",
        5: "Malaga",
        6: "Zaragoza",
        7: "San Sebastian",
        8: "A Coruna",
        9: "Alicante"
    }


def buildInitialChromosome():
    chromosome = [index for index in range(len(cities))]
    chromosome.pop(chromosome.index(start_city_index))
    return chromosome


def fitness(chromosome): 
    route_cost = []
    for i in range(genes_number - 1): # genes_number = no. of cities - 1
        route_cost.append(distances[chromosome[i]][chromosome[i+1]])
        #print(distances[chromosome[i]][chromosome[i+1]])
    #print(f'route cost {sum(route_cost)} - {distances[start_city_index][chromosome[0]]} - {distances[chromosome[len(chromosome)-1]][start_city_index]}')
    return sum(route_cost) + distances[start_city_index][chromosome[0]] + distances[chromosome[len(chromosome)-1]][start_city_index]


def calculateFitnesses():
    fitnesses = []
    min_fitness = 10000000
    chromosome_fitness_min = []
    for i in range(chromosomes_number):
        current_chromosome = population[i]
        current_fitness = fitness(current_chromosome)
        fitnesses.append(current_fitness)
        if(min_fitness > current_fitness):
            min_fitness = current_fitness
            chromosome_fitness_min = current_chromosome.copy()
    return fitnesses, chromosome_fitness_min, min_fitness


def printChromosome(chromosome):
    print(f'Chromosome {chromosome} to analize : ')
    start_city = cities.get(start_city_index)
    print(f"{start_city} -> {cities.get(chromosome[0])} = {distances[start_city_index][chromosome[0]]}")
    for i in range(genes_number - 1):
        city1 = cities.get(chromosome[i])
        city2 = cities.get(chromosome[i + 1])
        distance = distances[chromosome[i]][chromosome[i + 1]]
        print(f"{city1} -> {city2} = {distance}")
    print(f"{cities.get(chromosome[genes_number - 1])} -> {start_city} = {distances[chromosome[genes_number-1]][start_city_index]}") 


def displayRouteOfChromosome(chromosome_fitness_min, fitness_min):
    printChromosome(chromosome_fitness_min)
    print(f"Distanta traseu = {fitness_min}")


def printMinimumPathForCurrentIteration(chromosome_fitness_min, fitness_min):
    print(f'Minimal fitness from fitnesses {fitness_min}')
    displayRouteOfChromosome(chromosome_fitness_min, fitness_min)


def selectParents():
    parents = []
    tournament_size = 5 # more higher = faster accurate answer

    if new_generation_size % 2 == 1:
        raise ValueError(f"Number of parents - chidren must be even. It is {new_generation_size} .")
    
    for iteration in range(new_generation_size):
        indexes_of_chosen_chromosomes = [random.randint(0, chromosomes_number-1) for x in range(tournament_size)]
        fitnesses_of_chosen_chromosomes = [fitnesses[indexes_of_chosen_chromosomes[i]] for i in range(tournament_size)]
        winner = population[
            indexes_of_chosen_chromosomes[
                fitnesses_of_chosen_chromosomes.index(
                    min(fitnesses_of_chosen_chromosomes))]]
        parents.append(winner)
    return parents


def generateCrossoverPoints():
    found = False
    points = []
    while (not found):
        points = []
        points.append(random.randint(1, genes_number-1))
        points.append(random.randint(1, genes_number-1))
        if( points[0] + 1 != points[1] and
            points[0]     != points[1] + 1 and
            points[0]     != points[1]):
            found = True
    points.sort()
    return points


def crossover(parent_1, parent_2):
    points = generateCrossoverPoints()
    # print("Puncte taiere")
    # print(points)

    # Step 1
    child_1 = [-1 for i in range(genes_number)] 
    child_2 = [-1 for i in range(genes_number)]
    child_1[points[0]:points[1]] = parent_1[points[0]:points[1]]
    child_2[points[0]:points[1]] = parent_2[points[0]:points[1]]
    children = [child_1, child_2]

    # print("Kids after step 1")
    # print(child_1)
    # print(child_2)

    # Step 2
    aux1 = parent_1[points[1]:] + parent_1[:points[1]]
    aux2 = parent_2[points[1]:] + parent_2[:points[1]]

    # print("Auxiliar chromosomes")
    # print(aux1)
    # print(aux2)

    # Step 3
    for iteration_number in range(genes_number):
        chromosome_1_index = points[1]
        chromosome_auxiliar_2_index = points[0]
        while -1 in children[0]:
            if aux2[chromosome_auxiliar_2_index] in children[0] :
                chromosome_auxiliar_2_index += 1
                if chromosome_auxiliar_2_index == genes_number:
                    chromosome_auxiliar_2_index = 0
            else:
                children[0][chromosome_1_index] = aux2[chromosome_auxiliar_2_index]
                chromosome_1_index += 1
                if chromosome_1_index == genes_number:
                    chromosome_1_index = 0

    for iteration_number in range(genes_number):
        chromosome_2_index = points[1]
        chromosome_auxiliar_1_index = points[0]
        while -1 in children[1]:
            if aux1[chromosome_auxiliar_1_index] in children[1] :
                chromosome_auxiliar_1_index += 1
                if chromosome_auxiliar_1_index == genes_number:
                    chromosome_auxiliar_1_index = 0
            else:
                children[1][chromosome_2_index] = aux1[chromosome_auxiliar_1_index]
                chromosome_2_index += 1
                if chromosome_2_index == genes_number:
                    chromosome_2_index = 0
    # print("Parents, auxiliars and kids:")
    # print(p1)
    # print(p2)
    # print(aux1)
    # print(aux2)
    # print(children[0])
    # print(children[1])
    return children


def crossoverParents(parents):
    i = 0
    kids = []
    while (i <= new_generation_size-1):
        result = crossover(parents[i], parents[i+1])
        i += 2
        kids.append(result[0])
        kids.append(result[1])
    return kids


def startMutation(children):
    def generateRandomValue():
        return numpy.random.rand()

    def mutation(kids):
        for i in range(new_generation_size):
            if random_values[i] <= mutation_probability:
                # print(f"Chromosome {i} :")
                # print(kids[i])
                while(True):
                    gene_1_index = random.randint(0, genes_number-1)
                    gene_2_index = random.randint(0, genes_number-1)
                    if(gene_1_index != gene_2_index):
                        break
                chosen_genes = [gene_1_index, gene_2_index]
                chosen_genes.sort()
                #print(f"Have been chosen genes {chosen_genes[0]} and {chosen_genes[1]}, 0 based index")

                kids[i][gene_1_index], kids[i][gene_2_index] = kids[i][gene_2_index], kids[i][gene_1_index]
                # print("Result")
                # print(population[i])
                # print()

    mutation_probability = 0.2

    random_values = []
    for i in range(new_generation_size):
        random_values.append(generateRandomValue())

    mutation(children)


def generateSizeOfNewGeneration():
    percent_of_population_size = 0.05
    result = int(chromosomes_number * percent_of_population_size) 
    result = result if result % 2 == 0 else result + 1
    return  2 if result <= 1 else result


def introduceNewGenerationIntoPopulation(population, children, new_generation_size):
    for i in range (new_generation_size):
        population.append(children[i]) 


def removeWeakChromosomesFromPopulation(population):
    #print(population)
    #print(len(population))
    while (len(population) != chromosomes_number):
        fitnesses, chromosome_fitness_min, fitness_min = calculateFitnesses()
        population.remove(chromosome_fitness_min)
    #print(population)
    #print(len(population))
        

def store_average_fitness_current_population(average_fitness):
    average_fitness.append(average_fitness())


def average_fitness(fitnesses):
    return sum(fitnesses) / len(fitnesses)



# Initialization
distances = getMap()
cities = getCities()

genes_number = len(cities) - 1 # '-1' for the starting city
start_city_index = 1
initial_cromosome = buildInitialChromosome()

chromosomes_number = 100
population = generatePopulation()

fitnesses = calculateFitnesses()
average_fitness = []
store_average_fitness_current_population(average_fitness)

new_generation_size = generateSizeOfNewGeneration()

new_generations_number = 10
contor = 1
while(contor <= new_generations_number):    
    # Selecting parents
    parents = selectParents()

    # Create new chromosomes
    children = crossoverParents(parents)

    # mutation of newborns
    startMutation(children)

    # append kids to popullation
    introduceNewGenerationIntoPopulation(population, children, new_generation_size)

    # remove weak chromosomes from pop
    removeWeakChromosomesFromPopulation(population)

    # Create fitnesses for new popullation
    fitnesses, chromosome_fitness_min, fitness_min = calculateFitnesses()

    # Store average fitness of new population
    store_average_fitness_current_population(average_fitness)

    # end of loop
    contor += 1

printMinimumPathForCurrentIteration(chromosome_fitness_min, fitness_min)

# display grafic convergence
