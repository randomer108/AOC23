import re
import numpy as np
import math as m
import timeit

data = open("./data/day15.txt")
data=[d.split(',') for d in data]
data=[d for dd in data for d in dd]

class lens:
    def __init__(self,label,value):
        self.lens_stuff ={label:value}


class instruction:
    def __init__(self,string):
        self.hash=int()
        self.string_raw=string
        
        self.box=int()

        if re.search('=',self.string_raw):
            self.label=re.sub('=.*','',string)
        else:
            self.label=re.sub('-','',string)

        match = re.search(r'\d+', string)
        if match:
            self.strength = int(match.group())
        else:
            self.strength = None
        
    def hashfun(self):
        x=0
        for i in self.string_raw:
            x+=ord(i)
            x=x*17
            x=x%256
        self.hash=x
        return self

    
    def process_instruction(self,lens_array):

        # get box
        x=0
        for i in self.label:
            x+=ord(i)
            x=x*17
            x=x%256
        self.box=int(x)

        box=lens_array[self.box]
        
        # process the instruction
        if re.search('-',self.string_raw):
            for dicts in box:
                if self.label in dicts:
                    box.remove(dicts)
                
        if re.search('=',self.string_raw):
            self.lens=lens(self.label,self.strength)
            found_lens=False
            if len(box)>0:
                count=0
                for dicts in box:
                    if self.label in dicts:
                        box[count]=self.lens.lens_stuff
                        found_lens=True
                    count+=1
            if not found_lens: 
                box.append(self.lens.lens_stuff)
               
        return lens_array



Hashed=[instruction(d).hashfun() for d in data]
print(sum([i.hash for i in Hashed]))
# 2 # 

lens_array=[[] for _ in range(256)]

for instruction in Hashed:
    instruction.process_instruction(lens_array=lens_array)

print(lens_array)

answer=0

for box_num in range(len(lens_array)):
    box=lens_array[box_num]
    for lens_num in range(len(box)):
        lens=box[lens_num]

        label=list(lens.keys())[0]

        answer+=(box_num+1)*(lens_num+1)*lens[label]

print(answer)