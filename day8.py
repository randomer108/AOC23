import re
import numpy as np
import math as m

data = open("./AOC23/data/day8.txt").readlines()
instructions = data[0:5]
instructions = [line for list in data for line in list]

data=list(filter(None,[re.sub('\\n','',d) for d in data]))

