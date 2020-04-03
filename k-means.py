from pandas import DataFrame
import matplotlib.pyplot as plt
from random import randint
from random import random
import math  
import numpy

DataN = int(input("Podaj ilość próbek :"))
data = [[],[]]
for i in range(DataN):
    data[0].append(randint(0, 100))
    data[1].append(randint(0, 100))
print(data)

def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist 

N = int(input("Podaj k :"))
K = []
group = []

for i in range(N):
    K.append([i, randint(0, 100), randint(0, 100)])
    group.append([])
print(K)
    
for x in range(100):
    for i in range(len(data[0])):
        distance = []
        for j in range(N):
            distance.append(calculateDistance(data[0][i], data[1][i], K[j][1], K[j][2]))
        min = 1000
        mini = -1
        for k in range(len(distance)):
            if(distance[k]<min):
                min = distance[k]
                mini = k
        group[mini].append(i)

    for i in range(N):
        sumX=0
        sumY=0
        for j in range(len(group[i])):
            sumX += data[0][group[i][j]]
            sumY += data[1][group[i][j]]
        K[i][1] = sumX/(len(group[i])+0.001)
        K[i][2] = sumY/(len(group[i])+0.001)
        if(x<99):
            group[i] = []

print("grupy: ")
print(group)
print("środki: ")
print(K)

for i in range(N):
    tmpData = [[],[]]
    for j in range(len(group[i])):
        tmpData[0].append(data[0][group[i][j]])
        tmpData[1].append(data[1][group[i][j]])
    plt.plot(tmpData[0], tmpData[1], c=numpy.random.rand(3,), marker='o')    

plt.axis([0, 100, 0, 100])
for i in range(N):
    labelK = "K "+str(i)+" x: "+str(K[i][1])+" y: "+str(K[i][2])
    plt.plot(K[i][1], K[i][2], 'ro')

plt.show()
    
    