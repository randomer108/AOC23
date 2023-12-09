import re
import numpy as np
import math as m

data = open("./AOC23/data/day6.txt").readlines()
data = [str.split(d,'  ') for d in data]
Times = list(filter(None,[re.sub('([A-z]*:|\\n|\s)','',d) for d in data[0]]))
Distances = list(filter(None,[re.sub('([A-z]*:|\\n|\s)','',d) for d in data[1]]))

Results={}

for Race in range(len(Times)):
    T=int(Times[Race])
    D=int(Distances[Race])

    Threshold=0 # First button-holding strategy that wins.
    for t in range(1,m.ceil(T/2)):
        if t*(T-t)<=D: # math: note symmetry, so only trying to T/2 rounded up.
            pass
        else:
            Threshold=t
            Results[str('Race: '+str(Race))]=T-1-(Threshold-1)*2 
            # Say: T ways to win (1,2,3...T) >> but t=T loses, so -1 >> Everything <threshold or >(T-threshold) loses, so -(Threshold-1)*2 
            break

# Answer is all the race results multipled together
Answer=1
for i in Results:
    Answer = Answer*Results[i]

print(Results)
print(Answer)

# 2 # 
 # Concatonate times and distances into single TIME and DISTANCE
TIME=str(); DISTANCE=str()

for i in range(len(Times)):
    TIME = TIME+str(Times[i])
    DISTANCE=DISTANCE+str(Distances[i])

TIME=int(TIME);DISTANCE=int(DISTANCE)

# Same logic as before but storing results for multiple races is unecessary :)
THRESHOLD=0
for t in range(1,m.ceil(TIME/2)):
    if t*(TIME-t)<=DISTANCE:
        pass
    else:
        THRESHOLD=t
        RESULT = TIME-1-(THRESHOLD-1)*2 
        # TIME ways to win (1,2,3...T) >> but t=TIME loses, so -1 >> Everything <t or >(TTIME-t) loses, so -(Threshold-1)*2 
        break

print(RESULT)