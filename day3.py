import re
import numpy as np
# identified unique 'symbols' with: print(set(str(data)))

data = list(open("./AOC23/data/day3.txt"))
data.append('.'*141); data.insert(0,'.'*141)
data=['.'+s+'.' for s in data]
data=[re.sub('\n','',s) for s in data]

def make_part_number_dictionary(row):
    digits = dict((m.start(), int(m.group())) for m in re.finditer(r'\d+', data[row])) # dictionary of numbers and their index, given a row.
    return digits

def analyse_part_number(match_index,row):
    digits=make_part_number_dictionary(row)
    n = digits[match_index]
    length=len(str(n))

    top = data[row-1][match_index-1:match_index+length+1]
    bottom =data[row+1][match_index-1:match_index+length+1]
    sides=data[row][match_index-1]+ data[row][match_index+length]
    borders= top+bottom+sides

    if bool(re.search('[\-&#*$%@=+/]',borders)):
        return digits[match_index]
    else:
        return 0

Valid_parts=[]
[[Valid_parts.append(analyse_part_number(match_index,row)) for match_index in make_part_number_dictionary(row)] for row in range(1,141)]


# 2 # 

class Gear:
    def __init__(self,index,row):
        self.index=index
        self.row=row
        self.neighbours = []

class Digit:
    def __init__(self,index,row,value):
        self.index=index
        self.row=row
        self.value=value
        self.length=len(str(self.value))

Gears = [[Gear(m.start(),row) for m in re.finditer('[*]', data[row])] for row in range(1,141)]
Gears = [item for sublist in Gears for item in sublist ]
Gears=[x for x in Gears if isinstance(x,Gear)==True]

Digits =[[Digit(m.start(),row, int(m.group())) for m in re.finditer(r'\d+', data[row])] for row in range(1,141)]
Digits =[ item for sublist in Digits for item in sublist]



Matches=[]
for G in Gears:
    for D in Digits:
        if abs(G.row-D.row)<=1 and (G.index-D.index in range(-1,D.length+1)):
            G.neighbours.append([D.index,D.row,D.value])
            Matches.append(G) if G not in Matches else Matches

#print(Matches[1].neighbours[1][2])
Matches= [m.neighbours[0][2]*m.neighbours[1][2] for m in Matches if len(m.neighbours)==2]

print(sum(Matches))
