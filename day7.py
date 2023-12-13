import re
import numpy as np
import math as m

data = open("./AOC23/data/day7.txt").readlines()
data=list(filter(None,[re.sub('\\n','',d) for d in data]))


class hand:
    def __init__(self,inp,score):
        self.hand_raw=inp
        self.score= int(score)

        self.hand_counted={}
        self.hand_counted2={}

        self.type=str()
        self.type2=str()


    def count_cards(self):
        # Make dictionary with card labels, and total count in hand.
        cards = {}
        for card in enumerate(self.hand_raw):
            if card[1] in cards:
                cards[card[1]]+=1
            else:
                cards[card[1]]=1
        self.hand_counted = cards
        
        # I knpw aligning operators isn't PEP8 compliant but it makes it so much easier to see what's going on here.
        if   max(cards.values()) ==5:                    self.type='5ofaK'
        elif max(cards.values()) ==4:                    self.type='4ofaK'
        elif max(cards.values()) ==3 and len(cards)==2:  self.type='fullHouse'
        elif max(cards.values()) ==3 and len(cards)==3:  self.type='3ofaK'
        elif max(cards.values()) ==2 and len(cards)==3:  self.type='2pair'
        elif max(cards.values()) ==2 and len(cards)==4:  self.type='1pair'
        elif max(cards.values()) ==1:                    self.type='highCard'
        else: raise Exception('Hand type not recognised')
        return self
    
    def count_cards_2(self):
        # Expects card to already be counted by count_cards()

        # Count Jacks and separate them from hand
        try:
            wild = self.hand_counted['J']
        except:
            wild=0
        self.hand_counted2 = {card:value for card,value in self.hand_counted.items() if card != 'J'}
        

        cards = self.hand_counted2 # bt more terse
        # I knpw aligning operators isn't PEP8 compliant but it makes it so much easier to see what's going on here.
        if   self.hand_raw =='JJJJJ':                        self.type2='5ofaK'  # fixes up empty dictionary error case!
        elif max(cards.values()) ==5:                        self.type2='5ofaK'
        elif max(cards.values())+wild==5:                    self.type2='5ofaK'
 
        elif max(cards.values()) ==4:                        self.type2='4ofaK'
        elif max(cards.values())+wild ==4:                   self.type2='4ofaK'

        elif max(cards.values()) ==3 and len(cards) ==2:     self.type2='fullHouse'
        elif max(cards.values())+wild ==3 and len(cards) ==2:self.type2='fullHouse'

        elif max(cards.values()) ==3 and len(cards)==3:      self.type2='3ofaK'
        elif max(cards.values())+wild ==3 and len(cards)==3: self.type2='3ofaK'

        elif max(cards.values()) ==2 and len(cards)==3:      self.type2='2pair' # with 1 wild  - 2 pair is dominated by 3ofaK. With >2 J, 2 pair is obviously also dominated.

        elif max(cards.values()) ==2 and len(cards)==4:      self.type2='1pair'
        elif max(cards.values())+wild ==2 and len(cards)==4: self.type2='1pair'  

        elif max(cards.values()) ==1   and wild==0:          self.type2='highCard' # added condition of no wilds. If you have wilds, you should not get here! So shoud error instead!
        else: raise Exception('Hand type not recognised')

        self.hand_counted2 = cards # undo the terse thing
        return self


#  1  # 
# Generate Hands + set type based on cards in hand.
Hands=[hand(inp=d[:5], score=d[6:]).count_cards() for d in data] # data are strings with 5 characters, space, then the number (max 3 digits)

def custom_sort(instance):
    order_dict = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}
    return [order_dict[char] for char in instance.hand_raw]

# Sort the groups, startinig with highest scoring, and working down!
Hands_sorted = []
for handtype in ['5ofaK', '4ofaK', 'fullHouse', '3ofaK', '2pair', '1pair', 'highCard']:
    sorted_instances = sorted([H for H in Hands if H.type==handtype], key=custom_sort)
    Hands_sorted.append(sorted_instances)
Hands_sorted=[H for HH in Hands_sorted for H in HH] # flatten

# Calculate answer
Answer=0
i=len(Hands) # ranks are 1 for weakest hand...
for hand in Hands_sorted:
    Answer +=i*hand.score
    i-=1
print(Answer)


# 2 #
# Now jacks are low, but wild!
# So change soring order
# And a new processing function that take out the Jacks, and adds them to the 'max' operator?

# Recount the hands
Hands=[hand.count_cards_2() for hand in Hands]

# new sort - Jacks ay the end
def custom_sort_2(instance):
    order_dict = order_dict = {'A': 0, 'K': 1, 'Q': 2, 'T': 3, '9': 4, '8': 5, '7': 6, '6': 7, '5': 8, '4': 9, '3': 10, '2': 11, 'J': 12}
    return [order_dict[char] for char in instance.hand_raw]

# Sort the groups, startinig with highest scoring, and working down!
Hands_sorted2 = []
for handtype in ['5ofaK', '4ofaK', 'fullHouse', '3ofaK', '2pair', '1pair', 'highCard']:
    sorted_instances = sorted([H for H in Hands if H.type2==handtype], key=custom_sort_2)
    Hands_sorted2.append(sorted_instances)
Hands_sorted2=[H for HH in Hands_sorted2 for H in HH] # flatten

# Calculate answer2
Answer2=0
i=len(Hands) # ranks are 1 for weakest hand...
for hand in Hands_sorted2:
    Answer2 +=i*hand.score
    i-=1
print(Answer2)