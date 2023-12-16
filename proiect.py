import random

def generatePopulation():
    population = []
    initial_cromosome = [index for index in range(number_of_cities)]
    initial_cromosome.pop(initial_cromosome.index(start_city_index))
    for chromosome_number in range(chromosomes_number):
        chromosome = initial_cromosome.copy()
        random.shuffle(chromosome)

        chromosome.insert(0, start_city_index)
        chromosome.insert(len(chromosome), start_city_index)
        print(chromosome)

        population.append(chromosome)

# def generarePopulatie():
#     for i in range(dimensiunePopulatie):
#         valoriUniceAleUnuiIndivid = [i for i in range(numarGene)]
#         individ = valoriUniceAleUnuiIndivid.copy()
#         random.shuffle(individ)
#         populatie.append(individ)
        
def generateMap():
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
    return [[0, 626, 349, 608, 994, 980, 307, 566, 1083, 528],
[626, 0, 360, 403, 531, 542, 320, 457, 593, 432],
[349, 360, 0, 612, 655, 623, 309, 573, 950, 167],
[608, 403, 612, 0, 861, 925, 302, 101, 542, 786],
[994, 531, 655, 861, 0, 213, 847, 918, 926, 595],
[980, 542, 623, 925, 213, 0, 841, 983, 1123, 477],
[307, 320, 309, 302, 847, 841, 0, 264, 781, 484],
[566, 457, 573, 101, 918, 983, 264, 0, 639, 746],
[1083, 593, 950, 542, 926, 1123, 781, 639, 0, 1071],
[528, 432, 167, 786, 595, 477, 484, 746, 1071, 0]]

def functieDeCost(): # echivalent cu aia de ne trb la selectie


distances = generateMap()
number_of_cities = len(distances[0])
start_city_index = 1

chromosomes_number = 100
genes_number = 10
population = generatePopulation()
