import re
import numpy as np
import math as m
import timeit

data = open("./AOC23/data/day9.txt").readlines()
data = [list.split(' ') for list in data]
for i, row in enumerate(data):
    for j, num in enumerate(row):
        data[i][j] = int(re.sub('\\n', '', num))

# function to take differences of 
def diffs(list):
    diff= [list[i+1]-list[i] for i in range(len(list)-1)]
    #print(diff)
    return diff


# 1 #
RESULTS=[]

for row in data:
    row_results=[row[-1]]

    while len(set(row))>1:
        row=diffs(row)
        row_results.append(row[-1])

    RESULTS.append(sum(row_results))

print(sum(RESULTS))

# 2 #

def backout(list):
    list.reverse()
    back=[0]
    for i in range(len(list)):
        back.append(list[i]-back[i])
    return back


RESULTS=[]

for row in data:
    row_results=[row[0]]

    while len(set(row))>1:
        row=diffs(row)
        row_results.append(row[0])

    row_results=backout(row_results)
    RESULTS.append(row_results[-1])

print(sum(RESULTS))
