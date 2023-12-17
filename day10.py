import re
import numpy as np
import math as m
import timeit

data = open("./AOC23/data/day10.txt").readlines()
data = np.array([list(line.strip()) for line in data])      

Start = np.where(data=='S')

print(data)
