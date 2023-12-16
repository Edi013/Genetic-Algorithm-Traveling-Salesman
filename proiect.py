import random
import numpy as np

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


def fitness(chromosome): 
    print(chromosome)
    route_cost = []
    for i in range(genes_number-1):
        route_cost.append(distances[i][i+1])
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
    
    printChromosome(chromosome_fitness_min)
    print(f"Distanta traseu = {min_fitness}")

    return fitnesses


def buildInitialChromosome():
    chromosome = [index for index in range(genes_number)]
    chromosome.pop(chromosome.index(start_city_index))
    return chromosome


def printChromosome(chromosome):
    for i in range(genes_number-2):
        city1 = cities.get(chromosome[i])
        city2 = cities.get(chromosome[i + 1])
        distance = distances[chromosome[i]][chromosome[i + 1]]
        print(f"{city1} -> {city2} = {distance}")

# Initialization
distances = getMap()
cities = getCities()

start_city_index = 1
chromosomes_number = 100
genes_number = len(distances[0]) # number of cities
initial_cromosome = buildInitialChromosome()
population = generatePopulation()


fitnesses = calculateFitnesses()
#print(fitnesses)
#print(min(fitnesses))

tournament_size = 5
#selectParents()
