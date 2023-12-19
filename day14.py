import re
import numpy as np
import math as m
import timeit

data_raw = open("./AOC23/data/day14.txt").readlines()
data_raw = [re.sub('\n','',d) for d in data_raw]
data_raw=[list(row) for row in data_raw]
data_raw=np.array(data_raw)


def north(data):
    for j in range(len(data[0])):
        col=data[:,j]
        sublists = [[]]
        for item in col:   # break each col at the '#'s
            if item == '#':
                sublists.append(['#'])
            else:
                sublists[-1].append(item)
        sublists = [sublist for sublist in sublists if sublist] # removes empty '[]'

        for sublist in sublists:
            sublist.sort(key=lambda x: x.count('O'), reverse=True) # put the 'O' to the left
            sublist.sort(key=lambda x: x.count('#'), reverse=True) # put the '#' back to the front

        col = [x for sublist in sublists for x in sublist] 

        data[:,j] =col
    return data

data1=data_raw.copy()


data1=north(data1)
answer=0
Height = len(data1)
for i in range(len(data1)):
    answer+=len([x for x in data1[i] if x=='O'])*(Height-i)

print(answer)





# 2 # 
    
def south(data):
    for j in range(len(data[0])):
        col=data[:,j]
        sublists = [[]]
        for item in col:   # break each col at the '#'s
            if item == '#':
                sublists.append(['#'])
            else:
                sublists[-1].append(item)
        sublists = [sublist for sublist in sublists if sublist] # removes empty '[]'

        for sublist in sublists:
            sublist.sort(key=lambda x: x.count('O')) # put the 'O' to the left
            sublist.sort(key=lambda x: x.count('#'), reverse=True) # put the '#' back to the front

        col = [x for sublist in sublists for x in sublist] 

        data[:,j] =col
    return data


def west(data):
    for i in range(len(data)):
        col=data[i]
        sublists = [[]]
        for item in col:   # break each col at the '#'s
            if item == '#':
                sublists.append(['#'])
            else:
                sublists[-1].append(item)
        sublists = [sublist for sublist in sublists if sublist] # removes empty '[]'

        for sublist in sublists:
            sublist.sort(key=lambda x: x.count('O'),reverse=True) # put the 'O' to the left
            sublist.sort(key=lambda x: x.count('#'), reverse=True) # put the '#' back to the front

        col = [x for sublist in sublists for x in sublist] 

        data[i] =col
    return data

def east(data):
    for i in range(len(data)):
        col=data[i]
        sublists = [[]]
        for item in col:   # break each col at the '#'s
            if item == '#':
                sublists.append(['#'])
            else:
                sublists[-1].append(item)
        sublists = [sublist for sublist in sublists if sublist] # removes empty '[]'

        for sublist in sublists:
            sublist.sort(key=lambda x: x.count('O')) # put the 'O' to the left
            sublist.sort(key=lambda x: x.count('#'), reverse=True) # put the '#' back to the front

        col = [x for sublist in sublists for x in sublist] 

        data[i] =col
    return data


def cycle(data):
    data=north(data)
    data=west(data)
    data=south(data)
    data=east(data)
    return data

data_out=data_raw.copy()


for i in range(1000000000):
    data_in = data_out.copy()
    data_out=cycle(data_out)
    if np.array_equal(data_in,data_out):
        break

# answer
answer=0
Height = len(data_out)
for i in range(len(data_out)):
    answer+=len([x for x in data_out[i] if x=='O'])*(Height-i) 

print(answer)
""" print(data_raw)
print(data_out)
print(np.array_equal(data_raw,data_out))
 """



