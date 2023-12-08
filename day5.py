import re
import numpy as np

data = open("./AOC23/data/day5.txt").readlines()
data=[re.sub('\n','',x) for x in data]
# Get seeds from top row and delete top row with .pop()
seeds = str.split(re.sub('seeds: ','',data[0]),' ')
seeds=[int(x) for x in seeds]
data.pop(0);data.pop(0)

class seed:
    def __init__(self,number):
        self.value=number
        self.type='seed'
        self.soil=int()
        self.fertilizer=int()
        self.water=int()
        self.light=int()
        self.temperature=int()
        self.humidity=int()
        self.location=int()


class map:
    def __init__(self,line):
        self.name=line
        self.range_data=[]
        self.source_ranges = []
        self.destination_ranges = []
        self.output_seed=int()

    def add_range_data(self,line):
        line=str.split(line,' ')
        line = [int(x) for x in line]
        #[source_start, destination_start, length]
        self.range_data.append(line)

    def clean_range_data(self):
        for R in self.range_data:
            source = range(R[0],R[0]+R[2]+1)
            self.source_ranges.append(source)
            dest = range(R[1],R[1]+R[2]+1)
            self.destination_ranges.append(dest)
        return self
        
    def process_seed(self,input_seed):
        for R in self.source_ranges:
            if input_seed in R:
                correct_source_range =self.source_ranges.index(R)
                correct_source_index= R.index(input_seed)
                break
            else:
                pass
        self.output_seed= self.destination_ranges[correct_source_range][correct_source_index]
        return self

    #def scan_range_data(self,seed)

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
print(Maps[3].range_data)
x=Maps[3].clean_range_data()
print(x.destination_ranges)
x=x.process_seed(1)
print(x.output_seed)



