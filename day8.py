import re
import numpy as np
import math as m
import timeit

data = open("./AOC23/data/day8.txt").readlines()
instructions = data[0:1]
instructions = [line for list in instructions for line in list]
instructions=list(filter(None,[re.sub('\\n','',instruction) for instruction in instructions]))
instructions = [0 if element == 'L' else 1 if element == 'R' else element for element in instructions]

data.pop(0);data.pop(0)
data=list(filter(None,[re.sub('\\n','',d) for d in data]))

data=[[d[0:3],d[7:10],d[12:15]] for d in data]

locations=[d[0]for d in data]
leftsRights=[[d[1],d[2]] for d in data]


# logic
""" node = 'AAA'
answer=0
i=0
while node !='ZZZ':
    i = i % len(instructions)
    instruction =  instructions[i]

    index=locations.index(node)
    node = leftsRights[index][instruction]
    i+=1
    answer+=1
    if answer>100000:
        print('This is taking too long')
        break

print(node)
print(answer) """

# 2 # 

def check_nodes(nodes):
    ends= [node[2] for node in nodes if node[2]=='Z']
    if len(ends) ==6:
        return True 
    else: return False

# set up

# logic
def part2():
    Nodes = [location for location in locations if location[2]=='A']
    finished=False
    answer2=0
    i=0

    while finished ==False:
        i = i % len(instructions)     # get instruction
        instruction =  instructions[i]   # if run out of instructions, start again

        for j in range(6):    # loop over nodes. Replace entry in Nodes with left/right
            node=Nodes[j]
            index=locations.index(node)
            node = leftsRights[index][instruction]
            Nodes[j]=node

        finished = check_nodes(Nodes)  # check if finished

        i+=1   # tick up index counter
        answer2+=1 # tick up answer
        """
        if answer2>100000:  # excape while
            print('This is taking too long')
            break """
    print(Nodes)
    print(answer2)

    
time=timeit.timeit(part2,number=1)
print(f"Execution time: {time:.6f} seconds")
