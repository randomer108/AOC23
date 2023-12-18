import re
import numpy as np
import math as m
import timeit

data = open("./AOC23/data/day10.txt").readlines()
data = np.array([list(line.strip()) for line in data])      

Start = np.where(data=='S')
print(Start[0],Start[1])
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
 
pointer1 = pointer(16,38,'-','R')
pointer1.move()
#print(' I am: '+pointer1.next_symbol+'  heading: '+pointer1.current_direction)

pointer2 = pointer(16,36,'F','D')
pointer2.move()
#print(' I am: '+pointer2.next_symbol+'  heading: '+pointer2.current_direction)

print(data)
i=1
while abs(pointer1.x-pointer2.x) + abs(pointer1.y-pointer2.y)>1:
    pointer1.read()
    #print(' I am: '+pointer1.next_symbol+'  heading: '+pointer1.current_direction)
    pointer1.move()
    
    pointer2.read()
    #print(' I am: '+pointer2.next_symbol+'  heading: '+pointer2.current_direction)
    pointer2.move()
    i+=1
    if i>10000: break
    
print("done " + str(i+1))





