import re
d = list(open("./AOC23/data/day1.txt"))
dd=[re.sub('[a-zA-Z]*','',i)for i in d]
dd=[re.sub('\n','',i) for i in dd]
dd=[int(s[0] +s[-1]) for s in dd]
print(sum(dd))

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

starts=[]
for string in d:
    index=99999
    number=-2
    for num in range(len(digits)):
        i=string.find(digits[num])
        if i!=-1 and i<index:
            index=i
            number=num+1      

    for dig in range(1,10):
        j=string.find(str(dig))
        if j!=-1 and j<index:
            index=j
            number=dig  

    starts.append([index,number])

ends=[]
for string in d:
    index=-99999
    number=-2
    for num in range(len(digits)):
        i=string.rfind(digits[num])
        if i!=-1 and i>index:
            index=i
            number=num+1      

    for dig in range(1,10):
        j=string.rfind(str(dig))
        if j!=-1 and j>index:
            index=j
            number=dig  

    ends.append([index,number])

startend = [int(str(starts[i][1])+str(ends[i][1])) for i in range(1000)]
print(sum(startend))



#print(sum([end[1] for end in ends]+[start[1] for start in starts]))



