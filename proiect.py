def generatePopulation(number, map):
    population = []
    initial_cromozom = [index for index in range(len(map[0]))]
    for chromosome_number in range(number):
        chromosome_number = []
        for i in 

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
    return [[0, 626, 349, 608, 994, 980, 307, 566, 1083, 528]
[626, 0, 360, 403, 531, 542, 320, 457, 593, 432],
[349, 360, 0, 612, 655, 623, 309, 573, 950, 167],
[608, 403, 612, 0, 861, 925, 302, 101, 542, 786],
[994, 531, 655, 861, 0, 213, 847, 918, 926, 595],
[980, 542, 623, 925, 213, 0, 841, 983, 1123, 477],
[307, 320, 309, 302, 847, 841, 0, 264, 781, 484],
[566, 457, 573, 101, 918, 983, 264, 0, 639, 746],
[1083, 593, 950, 542, 926, 1123, 781, 639, 0, 1071],
[528, 432, 167, 786, 595, 477, 484, 746, 1071, 0]]


distances = generateMap()

chromosomes_number = 100
population = generatePopulation(chromosomes_number, distances)

genes_number = 10