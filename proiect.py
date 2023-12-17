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
    if new_generation_size % 2 == 1:
        raise ValueError(f"Number of parents - chidren must be even. It is {new_generation_size} .")
    parents = []
    for iteration in range(new_generation_size):
        indexes_of_chosen_chromosomes = [random.randint(0, chromosomes_number-1) for x in range(tournament_size)]
        fitnesses_of_chosen_chromosomes = [fitnesses[indexes_of_chosen_chromosomes[i]] for i in range(tournament_size)]
        winner = population[
            indexes_of_chosen_chromosomes[
                fitnesses_of_chosen_chromosomes.index(
                    min(fitnesses_of_chosen_chromosomes))]]
        parents.append(winner)
    return parents

def generarePuncteTaiere():
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

def crossover(p1, p2):
    cutPoints = generarePuncteTaiere()
    print("Puncte taiere")
    print(cutPoints)

    # Pasul 1
    copil1 = numpy.full(numarGene, -1)
    copil2 = numpy.full(numarGene, -1)
    copil1[cutPoints[0]:cutPoints[1]] = p1[cutPoints[0]:cutPoints[1]]
    copil2[cutPoints[0]:cutPoints[1]] = p2[cutPoints[0]:cutPoints[1]]
    copii = [copil1, copil2]

    print("Copii dupa pasul 1")
    print(copil1)
    print(copil2)

    # Pasul 2
    aux1 = p1[cutPoints[1]:] + p1[:cutPoints[1]]
    aux2 = p2[cutPoints[1]:] + p2[:cutPoints[1]]

    print("Cromozomi auxiliari")
    print(aux1)
    print(aux2)

    # Pasul 3
    for indexCopil in range(len(copii)):
        indexCromozom = cutPoints[1]
        indexCromozomAuxiliar = cutPoints[1]
        while -1 in copii[0]:
            if aux2[indexCromozomAuxiliar] in copii[0] :
                indexCromozomAuxiliar += 1
                if indexCromozomAuxiliar == numarGene  :
                    indexCromozomAuxiliar = 0
            else:
                copii[0][indexCromozom] = aux2[indexCromozomAuxiliar]
                indexCromozom += 1
                if indexCromozom == numarGene:
                    indexCromozom = 0

    for indexCopil in range(len(copii)):
        indexCromozom = cutPoints[1]
        indexCromozomAuxiliar = cutPoints[1]
        while -1 in copii[1]:
            if aux1[indexCromozomAuxiliar] in copii[1] :
                indexCromozomAuxiliar += 1
                if indexCromozomAuxiliar == numarGene  :
                    indexCromozomAuxiliar = 0
            else:
                copii[1][indexCromozom] = aux1[indexCromozomAuxiliar]
                indexCromozom += 1
                if indexCromozom == numarGene:
                    indexCromozom = 0

    print(copii[0])
    print(copii[1])


def generateKids(parents):
    i = 0
    kids = []
    while (i <= new_generation_size):
        result = crossover(parents[i], parents[i+1])
        i += 2
        kids.append(result[0])
        kids.append(result[1])

# Initialization
distances = getMap()
cities = getCities()

genes_number = len(cities) - 1 # '-1' for the starting city
start_city_index = 1 
initial_cromosome = buildInitialChromosome()

chromosomes_number = 100
population = generatePopulation()

# Create fitnesses for popullation
fitnesses, chromosome_fitness_min, fitness_min = calculateFitnesses()
#print(fitnesses)

# to save the average fitness of the population for displaying it's progression
#printMinimumPathForCurrentIteration(chromosome_fitness_min, fitness_min)
# --- not done

# selecting parents
tournament_size = 5 # more higher = faster accurate answer
new_generation_size = int(chromosomes_number * 0.1) # must be even
if(new_generation_size % 2 == 1):
    new_generation_size+=1
parents = selectParents()

# create new chromosomes
children = generateKids(parents)

# mutation of newborns

# appends kids to popullation

# remove weak chromosomes from pop

# end of loop
