import re
import numpy as np
import math as m
import timeit

data = open("./AOC23/data/day10.txt").readlines()
data = np.array([list(line.strip()) for line in data])      


class pointer:
    def __init__(self,y,x,symbol,direction):
        self.x=x
        self.y=y
        self.next_symbol=symbol
        self.current_direction=direction

    def read(self):

        self.next_symbol=data[self.y,self.x]

        if self.next_symbol=='-' and self.current_direction == 'R':
            self.current_direction == 'R'
        elif self.next_symbol=='-' and self.current_direction == 'L':
            self.current_direction == 'L'

        elif self.next_symbol=='|' and self.current_direction == 'U':
            self.current_direction == 'U'
        elif self.next_symbol=='|' and self.current_direction == 'D':
            self.current_direction == 'D'

        elif self.next_symbol=='7'and self.current_direction == 'U':
            self.current_direction='L'
        elif self.next_symbol=='7'and self.current_direction == 'R':
            self.current_direction='D'

        elif self.next_symbol=='L'and self.current_direction == 'D':
            self.current_direction='R'
        elif self.next_symbol=='L'and self.current_direction == 'L':
            self.current_direction='U'

        elif self.next_symbol=='J'and self.current_direction == 'R':
            self.current_direction='U'
        elif self.next_symbol=='J'and self.current_direction == 'D':
            self.current_direction='L'
            
        elif self.next_symbol=='F'and self.current_direction == 'U':
            self.current_direction='R'
        elif self.next_symbol=='F'and self.current_direction == 'L':
            self.current_direction='D'

        elif self.next_symbol=='S':
            print('Returned to start')
            return 

        elif self.next_symbol=='.':
            print('ERROR, RUN AGROUND')
            return 
        else:
            print('ERROR, WTF')
            return
    def move(self):
        if self.current_direction=='R':
            self.x+=1
        elif self.current_direction=='L':
            self.x-=1
        elif self.current_direction=='U':
            self.y-=1
        elif self.current_direction=='D':
            self.y+=1   


# Take start and initialise pointers
Start = np.where(data=='S')

pointer1 = pointer(16,38,'-','R')
pointer1.move()

pointer2 = pointer(16,36,'F','D')
pointer2.move()

pipe=[(Start[0][0],Start[1][0])] # part 2

print(data)
i=1
while abs(pointer1.x-pointer2.x) + abs(pointer1.y-pointer2.y)>1:
    pointer1.read()
    pointer1.move()
    pipe.append((pointer1.x,pointer1.y))

    pointer2.read()
    pointer2.move()
    pipe.append((pointer2.x,pointer2.y))
    i+=1
    if i>10000: break
    
print("done " + str(i+1))

# 2 #
# What's inside? 
# Well drawing a ray from any point to the outer edge - it must cross [0,2,4,6,8...] if it's OUTSIDE, and [1,3,5,7,9,...] if it's inside.
# So log the path points
# So draw the ray, count intersections with the path

pipe=set(pipe)
insides=0



for X in range(len(data)):
    for Y in range(len(data[0])):
        point = (X,Y)
        if point in pipe:
            continue

        # Maye a ray to the side
        rayE=[(x,point[1]) for x in range(point[0])]
        # See how many times it crosses the pipe

        rayE.reverse()

        crash=False # currenty in the pipe?
        crosses=0 # number of changes of <pipe to ¬pipe> or vice versa.

        for point in rayE:
            if point in pipe and point=='-':
                    continue
            if point in pipe and point!='-':
                    if crash == False:
                        crash=True
                        crosses+=1
                    if crash==True:
                        continue

            if point not in pipe:
                if crash==True:
                    crash=False
                    crosses+=1
                if crash==False:
                    continue

        if crosses %2!=0:
            insides+=1

print(insides)
