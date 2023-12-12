import re
import numpy as np
import math as m

data = open("./AOC23/data/day7.txt").readlines()
data=list(filter(None,[re.sub('\\n','',d) for d in data]))



class hand:
    def __init__(self,inp,score):
        self.hand_raw=inp
        self.hand_counted={}
        self.type=str()
        self.score= int(score)


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
        else: raise Exception('Hand type not recognised')
        return self


# sorting
def custom_sort(instance):
    order_dict = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}
    return [order_dict[char] for char in instance.hand_raw]

   
# Generate Hands + set type based on cards in hand.
Hands=[hand(inp=d[:5], score=d[6:9]).count_cards() for d in data] # data are strings with 5 characters, space, then the number (max 3 digits)

# Sort the groups, syartinig with highest scoring, and working down!
Hands_sorted = []
for handtype in ['5ofaK', '4ofaK', 'fullHouse', '3ofaK', '2pair', '1pair', 'highCard']:
    sorted_instances = sorted([H for H in Hands if H.type==handtype], key=custom_sort)
    Hands_sorted.append(sorted_instances)

Hands_sorted=[H for HH in Hands_sorted for H in HH] # flatten


# Calculate answer
Answer=0
i=len(Hands) # ranks are 1 for weakest hand...
for hand in Hands_sorted:
    print(i)
    Answer +=i*hand.score
    i-=1

print(Answer)