import math as math
import numpy as np
import random as rand
import scipy.optimize as scopt
import copy as copy
S=[2.424595205726587e-01, 1.737226395065819e-01, 1.315612759386036e-01,
 1.022985539042393e-01, 7.905975891960761e-02, 5.717509542148174e-02,
 3.155886625106896e-02, -6.242228581847679e-03, -6.565183775481365e-02,
 -8.482380513926287e-02, -1.828677714588237e-02, 3.632382803076845e-02,
 7.654845872485493e-02, 1.152250132891757e-01, 1.631742367154961e-01,
 2.358469152696193e-01, 3.650430801728451e-01, 5.816044173713664e-01,
 5.827732223753571e-01, 3.686942505423780e-01];
R=15
N=20
F= 0.8
CR = 0.9
MAX_NUM_ITERATIONS= 10000
COORDINATES = [[R*math.cos(2*math.pi*i/N) ,R*math.sin(2*math.pi*i/N) ] for i in range(N)]

def cost_f(arr):
    if arr[0]* arr[0] + arr[1] * arr[1] >= R*R or arr[2]* arr[2] + arr[3] * arr[3] >= R*R:
        return 100
    else:
        return math.fsum([
                             (
        arr[4]/math.sqrt(
            (COORDINATES[i][0] - arr[0])**2+ (COORDINATES[i][1] - arr[1])**2 )
        +
        arr[5] / math.sqrt(
            (COORDINATES[i][0] - arr[2])**2 + (COORDINATES[i][1] - arr[3])**2)

        -S[i]
                             )**2

            for i in range(len(COORDINATES))
        ])

def selection(population):
    modified_population = []
    for i in range(len(population)):
        indexes = np.random.permutation(len(population))
        for j in range(3):
            if indexes[j] == i :
                indexes[j] = indexes[3]
                break
        sub  = np.subtract(population[indexes[1]], population[indexes[2]])
        new_individua=[]
        for ind in range(len(population[0])):
            new_individua.append(population[indexes[0]][ind] + F * sub[ind])

        modified_population.append(new_individua)
    return modified_population

def cross_over(current_population, modified_population):
    temp_population = copy.deepcopy(current_population)
    for  index_individua in range(len(temp_population)):
        individua = temp_population[index_individua]
        index = rand.randint(0,len(individua)-1)
        for i in range(len(individua)):
            if rand.random() < CR or i == index:
                individua[i] = modified_population[index_individua][i]
    return  temp_population

def solve_next_generation(current_population, modified_population):
    cost_f_current_population = [cost_f(individua) for individua in current_population]
    cost_f_modified_population = [cost_f(individua) for individua in modified_population]

    for i in range(len(current_population)):
        if cost_f_current_population[i] > cost_f_modified_population[i]:
            current_population[i] = modified_population[i]
    return current_population


def initialize():
    BOUND = 10
    i=0
    initial_population=[]

    while i<60:
        individua =  [ rand.uniform(-BOUND, BOUND), rand.uniform(-BOUND, BOUND),rand.uniform(-BOUND, BOUND) ,rand.uniform(-BOUND, BOUND)
                       ,rand.uniform(-BOUND, BOUND) ,rand.uniform(-BOUND, BOUND)]
        if(cost_f(individua) < 100):
            i = i + 1
            initial_population.append(individua)


    return  initial_population


def differential_evolution():
    current_popultaion = initialize()
    best = None
    min_cost = 100
    for i in range(MAX_NUM_ITERATIONS):
        modified_population = selection(current_popultaion)
        modified_population = cross_over(current_popultaion, modified_population)
        current_popultaion = solve_next_generation( current_popultaion, modified_population)
        current_popultaion.sort(reverse= False, key=cost_f)
        curr_min = cost_f(current_popultaion[0])
        if best == None or min_cost > curr_min :
            min_cost = curr_min
            best = current_popultaion[0].copy()
        if(cost_f(best) < 1e-14):
            break
    return best


def main():

    solution = differential_evolution()
    print("Cost value :" + str(cost_f(solution)))
    print("Array :"  + str(solution) )

def test():
    bounds = [(-15,15), (-15,15), (-15,15),(-15,15), (-15,15), (-15,15)]
    res = scopt.differential_evolution(cost_f, bounds)
    print(res)
#test()
main()





