import re
import numpy as np
import math as m
import timeit

data_raw = open("./AOC23/data/day11.txt").readlines()
data_raw = [re.sub('\n','',d) for d in data_raw]
data_raw=[list(row) for row in data_raw]
data_raw=np.array(data_raw)


# 1 #

data=data_raw
# Expand space!
    # Expanding a row, doesn't affect if a column is expandable. Adding some extra '.' doesn't change if there are any ¬'.' chracters.
#rows
nrow, ncol = data.shape
hubble=0
for n in range(nrow):
    row = data[n+hubble]
    if len([x for x in row if x!='.']) ==0:
        data = np.insert(data, n+hubble, row, axis=0)
        hubble +=1

#cols 
nrow, ncol = data.shape
hubble=0
for n in range(ncol):
    col = data[:,n+hubble]
    if len([x for x in col if x!='.']) ==0:
        data = np.insert(data, n+hubble, col, axis=1)
        hubble +=1

# count galaxies
nrow, ncol = data.shape
class galaxy:
    def __init__(self,x,y):
        self.x = x
        self.y =y

local_group =[]

for i in range(nrow):
    for j in range(ncol):
         if data[i][j]=='#':
             local_group.append(galaxy(j,i))
# count distances
answer=0
for galaxy in local_group:
    for neighbour in local_group:
        dist=abs(galaxy.x-neighbour.x)+abs(galaxy.y-neighbour.y)
        answer+=dist
print(answer)

# 2 # 
data=data_raw

# Expand Space
    # This time, add a symbol 'x' if a row/col is empty. Then we'll count x's and multiple through by 10^6 
xrow = ['x' for d in data[0]]
xcol = ['x' for d in data[:,0]]
nrow, ncol = data.shape

for n in range(nrow):
    row = data[n]
    if len([x for x in row if x=='#']) ==0:
        data[n] = xrow
for n in range(ncol):
    col = data[:,n]
    if len([x for x in col if x=='#']) ==0:
        data[:,n] = xcol

super_cluster =[]
class galaxy:
    def __init__(self,x,y):
        self.x = x
        self.y =y

for i in range(nrow):
    for j in range(ncol):
         if data[i][j]=='#':
             super_cluster.append(galaxy(j,i))


answer=0

for galaxy in super_cluster:
    for neighbour in super_cluster:
        # get the symbols between galaxy, and neighbour on the row/col of galaxy. 
        # This will include the correct number of Xs, thoug the mix of '.' and '#' will be wrong
        across=data[galaxy.y,range(min(galaxy.x,neighbour.x),max(galaxy.x,neighbour.x))]
        vert=data[range(min(galaxy.y,neighbour.y),max(galaxy.y,neighbour.y)),galaxy.x,]
        
        dist=abs(galaxy.x-neighbour.x)+abs(galaxy.y-neighbour.y) # pure distance
        answer+=dist
        answer+=999999*len([star for star in across if star=='x']) # add extra distance for 'x' rows 
        answer+=999999*len([star for star in vert if star=='x']) # add extra distance for 'x' rows 

print(answer/2)