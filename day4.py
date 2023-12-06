import re
import numpy as np

class card:
    def __init__(self,row):
        temp= re.sub('Card\s+\d+:\s','',row)
        temp = re.sub('\n','',temp)
        temp=str.split(temp,'|')
        self.split_card=temp

        temp =str.split(self.split_card[0],' ')
        temp = [int(x) for x in temp if x!='']
        self.winning_numbers=temp

        temp =str.split(self.split_card[1],' ')
        temp = [int(x) for x in temp if x!='']
        self.numbers = temp
    
    def return_count(self):
        count=0
        for win in self.winning_numbers:
            if win in self.numbers:
                count +=1
        self.count=count
        return self.count 
    
    def return_score(self):
        count=self.return_count()

        if self.count >0:
            self.score=2**(self.count-1)
        else:
            self.score=0
        return self.score
    
data = open("./AOC23/data/day4.txt").readlines()
Scores= [card(data[i]).return_score() for i in range(len(data))]
print(sum(Scores))

# 2 #

Copies = np.repeat(1,len(data))

for row in range(len(data)):
    card_count = card(data[row]).return_count()
    cards_to_add = Copies[row]
    # print('Row: ' +str(row)+' add: '+str(cards_to_add)+' to next: '+str(card_count)+ ' rows.')
    for i in range(row,row+card_count):
        if card_count==0:
            pass
        else:
            Copies[i+1]+=cards_to_add
print(Copies)
print(sum(Copies))
