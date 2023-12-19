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

print('# 1 #')
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

# by printing the answer at each iteration for 1000 cycles or so, I spotted cycling in the answers. So now I'll search for cycling!
# Track states of the board
States=[] 
flag=False

for i in range(1000000):
    data_out=cycle(data_out)
    for k in range(len(States)):
        if np.array_equal(States[k],data_out):
            flag=True
            First_repeat=i
            Repeated=k
            break 
    States.append(data_out.copy())
    if flag:
        break



correct_number_cycles=             Repeated +                           (1_000_000_000-First_repeat)%(First_repeat-Repeated)
#                     ^^ do these to hit start of cycling^^    ^^ do this many cycles to go far enough into the pattern to find the same state as state state 1_000_000_000

print('# 2 #')
print(f"The first repeat is {First_repeat} and it repeats state {Repeated}  so the loop length is {First_repeat-Repeated}")
print(f"We need to run it {Repeated} times to hit the start of the cycle. Then we run it {(1_000_000_000-First_repeat)%(First_repeat-Repeated)} times, which is 1_000_000_000 % cycle length")
# Now cycle the raw data that many times!
data_final = data_raw.copy()

for i in range(correct_number_cycles):
    data_final=cycle(data_final)

answer2=0
Height = len(data_final)
for i in range(len(data_final)):
    answer2+=len([x for x in data_final[i] if x=='O'])*(Height-i)

print(answer2)




