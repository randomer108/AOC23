import re
import numpy as np
import math as m

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
        self.range_data.append(line)

    def clean_range_data(self):
        for R in self.range_data:
            source = range(R[1],R[1]+R[2])
            self.source_ranges.append(source)
            dest = range(R[0],R[0]+R[2])
            self.destination_ranges.append(dest)
        return self
        
    def process_seed(self,input_seed):
        for R in self.source_ranges:
            same=True
            if input_seed in R:
                correct_source_range =self.source_ranges.index(R)
                correct_source_index= R.index(input_seed)
                same = False
                break
            else:
                pass
            
        if same==True:
            self.output_seed=input_seed 
        else:  
            self.output_seed= self.destination_ranges[correct_source_range][correct_source_index]
        return self.output_seed


data = open("./AOC23/data/day5.txt").readlines()
data=[re.sub('\n','',x) for x in data]

# Get seeds from top row and delete top row with .pop()
seeds = str.split(re.sub('seeds: ','',data[0]),' ')
seeds=[int(x) for x in seeds]
data.pop(0);data.pop(0)


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

# distionary of cleaned maps, identified by their name.
Maps_dict = {Maps[i].name:Maps[i].clean_range_data() for i in range(len(Maps))}

def plant_seed(number):
    live_seed=number
    live_seed=Maps_dict['seed-to-soil map:'].process_seed(live_seed)
    live_seed=Maps_dict['soil-to-fertilizer map:'].process_seed(live_seed)
    live_seed=Maps_dict['fertilizer-to-water map:'].process_seed(live_seed)
    live_seed=Maps_dict['water-to-light map:'].process_seed(live_seed)
    live_seed=Maps_dict['light-to-temperature map:'].process_seed(live_seed)
    live_seed=Maps_dict['temperature-to-humidity map:'].process_seed(live_seed)
    live_seed=Maps_dict['humidity-to-location map:'].process_seed(live_seed)
    return(live_seed)


Answer=m.inf

for i in range(len(seeds)):
    x=plant_seed(seeds[i])
    if x<Answer:
        Answer=x

print('Minimum location is: ' +str(Answer))

# 2 # 

all_the_seed_ranges = [range(seeds[i*2],seeds[i*2]+seeds[i*2+1]) for i in range(10)] #<< manual
print(all_the_seed_ranges)


Answer2=m.inf

for seed_range in all_the_seed_ranges:
    for seed in seed_range:
        x=plant_seed(seed)
        if x<Answer2:
            Answer2=x

print('Minimum location for part 2 is: ' +str(Answer2))