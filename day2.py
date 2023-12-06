import re

# structure data into draws in rounds in games
data = list(open("./AOC23/data/day2.txt"))
data=[game.split(';') for game in data]
data=[[re.sub('Game [0-9]*:','',round) for round in game] for game in data]
data=[[re.sub('\n','',round) for round in game] for game in data]
data=[[round.split(',') for round in game] for game in data]

# Limits for each colour in each game from challenge
RED=12; GREEN=13; BLUE=14
games_nani =[]

def fail():
     games_nani.append(data.index(game)+1)
     GAME=False

def scan(inp):
    if inp.find('green')>=0 and int(re.sub('[a-zA-Z ]*','',inp)) > GREEN:
        fail()
    if inp.find('blue')>=0 and int(re.sub('[a-zA-Z ]*','',inp)) > BLUE:
        fail()
    if inp.find('red')>=0 and int(re.sub('[a-zA-Z ]*','',inp)) > RED:
        fail()



for game in data:
    GAME=True
    while GAME==True:
        for round in game:
                for draw in round:
                    if data.index(game)+1 not in games_nani:
                        scan(draw)
        GAME=False

print(sum(range(1,101))-sum(games_nani)) # Hacky - sum 1:101 is the sum of all game indices. I subtracted the sum of invalid games. 

# Star 2 #

games_power =[]

def get_cube_num(inp):
    return(int(re.sub('[a-zA-Z ]*','',inp)))

def parse(inp):
    if inp.find('green')>=0 and get_cube_num(inp) > GREEN2:
        globals()['GREEN2']=get_cube_num(inp)
        return
    if inp.find('blue')>=0 and get_cube_num(inp) > BLUE2:
        globals()['BLUE2']=get_cube_num(inp)
        return
    if inp.find('red')>=0 and get_cube_num(inp) > RED2:
        globals()['RED2']=get_cube_num(inp)
        return

for game in data:
    RED2=0; GREEN2=0; BLUE2=0
    for round in game:
        for draw in round:
            parse(draw)
    games_power.append(RED2*GREEN2*BLUE2)

print(sum(games_power))