import re
import numpy as np
import math as m
import timeit

data = open("./data/day15.txt")
data=[d.split(',') for d in data]
data=[d for dd in data for d in dd]

class instruction:
    def __init__(self,string):
        self.hash=int()
        self.string_raw=string
        self.label=re.sub('=.*|-','',string)

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

    
    def process_instruction(self):

        box=lens_array[self.hash]

        if re.search('-',self.string_raw):
            if self.label in box:
                box.remove(self.label)
                lens_array[self.hash]= box

        if re.search('=',self.string_raw):
            lens=lens(self.label,self.strength)





class lens:
    def __init__(self,label,value):
        self.properties ={label:value}





Hashed=[instruction(d).hashfun() for d in data]
print(sum([i.hash for i in Hashed]))

# 2 # 

lens_array=[[] for _ in range(256)]

print([i.strength for i in Hashed])