import re
import numpy as np
import math as m
import timeit

data = open("./data/day18.txt").readlines()
data = [re.sub('\n','',d) for d in data]
data = [(d[0],int(d[2:4]), d[4:]) for d in data]
instructions=[[d[0],d[1]]for d in data]


Field = np.full((750,750),0)
point=[375,375]
for instruction in instructions:
    direction = instruction[0]
    length=instruction[1]

    if direction=='R':
        for step in range(0,length):
            Field[point[0],point[1]]=1
            point[1]+=1
    if direction=='L':
        for step in range(0,length):
            Field[point[0],point[1]]=1
            point[1]-=1
    if direction=='U':
        for step in range(0,length):
            Field[point[0],point[1]]=1
            point[0]-=1
    if direction=='D':
        for step in range(0,length):
            Field[point[0],point[1]]=1
            point[0]+=1


#print(Field)
#np.savetxt('my_array.txt', Field, fmt='%c')

Untested = [(0,0)]

# Fill OUTSIDE the shape
while Untested:
    point= Untested[0]
    Field[point[0],point[1]]=2
    for i in range(point[0] - 1, point[0] + 2):
        for j in range(point[1] - 1, point[1] + 2):
            if 0 <= i < len(Field) and 0 <= j < len(Field[0]):
                if Field[i,j] ==0 and (i,j) not in Untested:
                    Untested.append((i, j))
    Untested.pop(0)

answer= 750**2 -np.count_nonzero(Field==2)
print(answer)
