import re
import numpy as np
import math as m

data = open("./AOC23/data/day7.txt").readlines()
data=list(filter(None,[re.sub('\\n','',d) for d in data]))
Hands = [d[:5] for d in data]
Bids = [d[6:9] for d in data]


class hand:
    def __init__(self,inp):
        self.hand_raw=inp
        self.hand_counted={}
        self.type=str()
    def count_cards(self):
        cards = {}
        for card in enumerate(self.hand_raw):
            if card[1] in cards:
                cards[card[1]]+=1
            else:
                cards[card[1]]=1
        self.hand_counted = cards
 
        if   max(cards.values()) ==5:                    self.type='5ofaK'
        elif max(cards.values()) ==4:                  self.type='4ofaK'
        elif max(cards.values()) ==3 and len(cards) ==2: self.type='fullHouse'
        elif max(cards.values()) ==3 and len(cards)==3: self.type='3ofaK'
        elif max(cards.values()) ==2 and len(cards)==3: self.type='2pair'
        elif max(cards.values()) ==2 and len(cards)==4: self.type='1pair'
        elif max(cards.values()) ==1:                  self.type='highCard'
        else: pass #raise Exception('Hand type not recognised')
        return self

        
        
    
""" x={'a':100,'b':20}
print(max(x.values()))
print(len(x)) """ 

for H in Hands:
    H= hand(H)
    H = H.count_cards()
    print(H.hand_counted)
    print(len(H.hand_counted))
    print(max(H.hand_counted.values()))
    print(H.type)

