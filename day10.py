import re
import numpy as np
import math as m
import timeit

data = open("./data/day10.txt").readlines()
data = np.array([list(line.strip()) for line in data])      


class pointer:
    def __init__(self,row,col,symbol,direction):
        self.row=row
        self.col=col
        self.next_symbol=symbol
        self.current_direction=direction

    def read(self):

        self.next_symbol=data[self.row,self.col]

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
            self.col+=1
        elif self.current_direction=='L':
            self.col-=1
        elif self.current_direction=='U':
            self.row-=1
        elif self.current_direction=='D':
            self.row+=1   


# Take start and initialise pointers
Start = np.where(data=='S')

pointer1 = pointer(16,38,'-','R')
pointer1.move()

pointer2 = pointer(16,36,'F','D')
pointer2.move()

pipe=[(Start[0][0],Start[1][0])] # part 2

#print(data)
i=1
while abs(pointer1.row-pointer2.row) + abs(pointer1.col-pointer2.col)>1:
    pointer1.read()
    pointer1.move()
    pipe.append((pointer1.row,pointer1.col))

    pointer2.read()
    pointer2.move()
    pipe.append((pointer2.row,pointer2.col))
    i+=1
    if i>10000: break
    
print("done " + str(i+1))
#print(pipe)
# 2 #
# What's inside? 
# Well drawing a ray from any point to the outer edge - it must cross [0,2,4,6,8...] if it's OUTSIDE, and [1,3,5,7,9,...] if it's inside.
# So log the path points
# So draw the ray, count intersections with the path

pipe=set(pipe)
insides=0

for ROW in range(len(data)):
    for COL in range(len(data[0])):
        point = (ROW,COL)
        if point in pipe:
            continue
        # Maye a ray to the side
        rayE=[(point[0],cols) for cols in range(point[1])]
        # See how many times it crosses the pipe
        
        #rayE.reverse()
        crash=False # currenty in the pipe?
        crosses=0 # number of changes of <pipe to ¬pipe> or vice versa.

        for step in rayE:
            symbol=data[step[0],step[1]] 
            if step in pipe and symbol=='-':
                    pass
            if step in pipe and symbol!='-':
                    #if crash == False:
                    #    crash=True
                    crosses+=1
                    #if crash==True:
                    #    pass

            """ if step not in pipe:
                if crash==True:
                    crash=False
                    crosses+=1
                if crash==False:
                    pass """

        if crosses %2!=0:
            insides+=1

print(insides)
