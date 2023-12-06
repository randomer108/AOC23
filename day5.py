import re
import numpy as np

data = open("./AOC23/data/day5.txt").readlines()
data=[re.sub('\n','',x) for x in data]
# Get seeds from top row and delete top row with .pop()
seeds = str.split(re.sub('seeds: ','',data[0]),' ')
seeds=[int(x) for x in seeds]
data.pop(0);data.pop(0)



class map:
    def __init__(self,line):
        self.name=line
        self.range_data=[]

    def add_range_data(self,line):
        line=str.split(line,' ')
        line = [int(x) for x in line]
        #[source_start, destination_start, length]
        self.range_data.append(line)

# Read in the fucking maps! This was outragously difficult to get working.
current_map=None; Maps=[]

for line in data:
    if line =='':
        continue
    if bool(re.search('[A-z]',line)): # if it's got text, it's a new map!
        current_map=map(line=line) 
        Maps.append(current_map)
    else:
        current_map.add_range_data(line) # if it's not got text, it's data, so store it for use later.


# 
print(Maps[3].range_data[1][0])

#Headings = [bool(re.search('[A-z]',data[i])) for i in range(len(data))]
