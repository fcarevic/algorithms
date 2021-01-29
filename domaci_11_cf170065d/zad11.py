#cf170065d
import random as rand
import matplotlib.pyplot as plt
import matplotlib as mlp


NUM = 10000;
LBOUND = -1
RBOUND =1
def f1(solution):
    return 2*solution[0]**2 + solution[1]**2;
def f2(solution):
    return -((solution[0]-solution[1])**2);

def plot_(points):
    mlp.rcParams['agg.path.chunksize'] = 10100
    plt.figure()
    bluepoints = list(filter(lambda x: x[2] == False, points))
    redpoints = list(filter(lambda x: x[2] == True, points))
    print(len(redpoints))
    print(len(bluepoints))
    plt.scatter([f1(bluepoints[i]) for i in range(len(bluepoints))],
                [f2(bluepoints[i]) for i in range(len(bluepoints))], c='b');
    plt.scatter([f1(redpoints[i]) for i in range(len(redpoints))], [f2(redpoints[i]) for i in range(len(redpoints))],
                c='r');
    plt.show()

def algo(points):
    for i in range(len(points)):
        if points[i][2] == False:
            continue
        for j in range(i, len(points)):
            f1i = f1(points[i])
            f1j = f1(points[j])
            f2i = f2(points[i])
            f2j = f2(points[j])
            if f1i < f1j and f2i <= f2j or f1i <= f1j and f2i < f2j:

                points[j][2] = False
            else:
                if f1j < f1i and f2j <= f2i or f1j <= f1i and f2j < f2i:
                    points[i][2] = False

points = [[rand.uniform(LBOUND, RBOUND), rand.uniform(LBOUND,RBOUND), True] for i in range(NUM)]
algo(points)
plot_(points)

points=[]
for i in range(NUM):
    x1 = rand.uniform(-1, 1)
    x2 = rand.uniform(-1, 1)
    while x1*x2 + 0.25 <0:
        x1 = rand.uniform(-1, 1)
        x2 = rand.uniform(-1, 1)
    points.append([x1,x2,True])

algo(points)
plot_(points)
